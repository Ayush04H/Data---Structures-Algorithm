import time
from multiprocessing import Process,freeze_support
def do_something():
    print("I'm going to sleep")
    time.sleep(10)
    print("I'm waking up") 

# Create new child process

process_1 = Process(target=do_something)
#process_2 = Process(target=do_something)

# Starts both processes
if __name__ == "__main__":
    # Starts both processes
    freeze_support()
    print("Starting the process\n")
    process_1.start()
    #do_something()
    print("I'm awake") 
    #process_2.start()