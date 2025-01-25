import csv
import os
from docx import Document

def extract_text_from_docx(file_path):
    """
    Extracts all the text from a .docx file and formats it using specific tags.
    """
    document = Document(file_path)
    text = []
    
    for paragraph in document.paragraphs:
        if paragraph.text.strip():  # Avoid empty lines
            # Wrap the paragraph with the required tags
            formatted_paragraph = f"<s> [INST] <<SYS>> You are a helpful, respectful, and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information. <</SYS>> {paragraph.text} [/INST] </s>"
            text.append(formatted_paragraph)
    
    return "\n".join(text)  # Combine all paragraphs into a single string, each separated by a newline

def preprocess_and_save_as_csv(input_file, output_file):
    """
    Preprocess text and append it as a single-column CSV with formatted tags.
    """
    # Extract and format the text from the .docx file
    text = extract_text_from_docx(input_file)
    
    # Check if the file already exists
    file_exists = os.path.isfile(output_file)

    # Open the CSV file in append mode
    with open(output_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # If the file doesn't exist, write the header
        if not file_exists:
            writer.writerow(['Text'])  # Adding column name

        # Append the extracted text as a new row
        writer.writerow([text])   

    print(f"Processed and formatted text saved to {output_file}")

# File paths
input_file_path = "Ut1.docx"  # Replace with your .docx file path
output_csv_path = "output_file.csv"  # Replace with your desired CSV file path

# Execute the function
preprocess_and_save_as_csv(input_file_path, output_csv_path)
