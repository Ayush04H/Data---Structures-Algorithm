import os
import pandas as pd
import csv
import codecs
import uuid
from multiprocessing import Process, freeze_support
from fastapi import FastAPI, File, UploadFile, BackgroundTasks, HTTPException, Response
from fastapi.responses import FileResponse
import uvicorn
from benchmarking_for_models.main_script import PromptGenerator
import dataset_for_benchmarking.configurations as config
from benchmarking_for_models.query_llm import QueryLLM
from benchmarking_for_models.Cosine_Eval import CosineEvaluator
from cognitive_framework_commons.common_operations.common_operations import CommonOperations
from new_dtect_logging.logger import DtectLogging

# Setup logger
if __name__ == "__main__":
    freeze_support()  # Required for multiprocessing on Windows
    log_file_name = __file__.split(os.sep)[-2] + "_" + __file__.split(os.sep)[-1].split(".")[0]
    lobj_dtect_logger = DtectLogging(log_file_name)
else:
    lobj_dtect_logger = DtectLogging()

# Create FastAPI app
app = FastAPI()

# Define directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "API")
OUTPUT_DIR = config.OUTPUT_DIR

# Dictionary to store context keys and their corresponding file paths
context_key_to_file_map = {}

@app.get("/")
def read_root():
    """Root endpoint to verify the API is running."""
    return {"Hello": "FastAPI"}

def process_csv_file(file_path: str, context_key: str):
    """Process the uploaded CSV file and generate the output."""
    try:
        # Generate prompts
        lobj_prompt_generator = PromptGenerator()
        lobj_prompt_generator.generate_prompts(file_path)

        # Process dataset
        lobj_query_llm = QueryLLM()
        lobj_query_llm.process_dataset()

        # Set the output filename to {context_key}.csv and store it in the Intermediate folder
        output_filename = f"{context_key}.csv"
        output_file_path = os.path.join(os.path.dirname(file_path), output_filename)

        # Calculate cosine similarities
        lobj_cosine_eval = CosineEvaluator()
        lobj_cosine_eval.process_data(output_file_path)

        return output_file_path
    except Exception as e:
        lobj_dtect_logger.logger.error(f"Error processing CSV file in subprocess: {e}")
        raise

def start_processing(file_path: str, context_key: str):
    """Start the CSV file processing in a separate process."""
    try:
        print("File under processing. Please check API endpoint /check_status for knowing the status.")

        # Process the CSV file
        output_file_path = process_csv_file(file_path, context_key)
        context_key_to_file_map[context_key] = output_file_path
        print(output_file_path)
        print(context_key_to_file_map[context_key])
    except Exception as e:
        lobj_dtect_logger.logger.error(f"Error starting processing: {e}")

@app.post("/file/upload/csv")
def upload_csv_file(background_tasks: BackgroundTasks, file: UploadFile = File(...), context_key: str = None):
    """Upload CSV file endpoint."""
    try:
        # Check if uploaded file is a CSV
        if file.content_type != "text/csv":
            lobj_dtect_logger.logger.error("Invalid document type")
            raise HTTPException(status_code=400, detail="Invalid document type")

        # Read the uploaded CSV file
        csv_reader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
        data = list(csv_reader)

        # Validate or generate context key
        if context_key:
            try:
                uuid.UUID(context_key)  # Validate the UUID format
            except ValueError:
                raise HTTPException(status_code=400, detail="Invalid UUID format")
        else:
            context_key = str(uuid.uuid4())

        # Create a folder named after the context key
        context_folder = os.path.join(OUTPUT_DIR, context_key)
        if os.path.exists(context_folder):
            return {"message": "Context key is duplicate, please enter a new context key and send the request again"}
        else:
            # Create necessary directories
            os.makedirs(context_folder, exist_ok=True)
            os.makedirs(os.path.join(context_folder, "intermediate"), exist_ok=True)
            os.makedirs(os.path.join(context_folder, "temporary"), exist_ok=True)
            lobj_dtect_logger.logger.info("Path does not exist, creating folders")

        # Store data and save the CSV file
        ldict_data = {"context_key": context_key, "data": data}
        ldf_dataset = pd.DataFrame(data)
        lstr_input_file_path = os.path.join(context_folder, "intermediate", file.filename)
        ldf_dataset.to_csv(lstr_input_file_path, index=False)

        # Start processing in a separate process
        process_1 = Process(target=start_processing, args=(lstr_input_file_path, context_key))
        process_1.start()

        background_tasks.add_task(file.file.close)
        lobj_dtect_logger.logger.info("API Init. Successful")
        return {"context_key": context_key, "description": "File is under processing, please use /check_status to know about the status"}

    except Exception as e:
        lobj_dtect_logger.logger.error(f"Error processing CSV file: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/download/{context_key}/{filename}")
async def download_file(context_key: str, filename: str):
    """Endpoint to download the processed file."""
    if context_key not in context_key_to_file_map:
        raise HTTPException(status_code=422, detail="Conflict with Context key")

    context_folder = os.path.join(OUTPUT_DIR, context_key)
    file_path = os.path.join(context_folder, "intermediate", filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(file_path, media_type='application/octet-stream', filename=filename)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
