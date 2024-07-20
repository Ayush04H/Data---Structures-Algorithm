import multiprocessing
import time as t

def addition(a, b):
    """Function to perform addition."""
    print(f"Addition of {a} and {b} is: {a + b}")
    t.sleep(5)

def subtraction(a, b):
    """Function to perform subtraction."""
    print(f"Subtraction of {a} and {b} is: {a - b}")
    t.sleep(5)

def multiplication(a, b):
    """Function to perform multiplication."""
    print(f"Multiplication of {a} and {b} is: {a * b}")
    t.sleep(5)
def division(a, b):
    """Function to perform division."""
    try:
        result = a / b
    except ZeroDivisionError:
        result = "undefined (division by zero)"
    print(f"Division of {a} and {b} is: {result}")
    t.sleep(5)

    
if __name__ == "__main__":
    # Define the numbers to be used in operations
    num1, num2 = 10, 5

    # Create a process for each mathematical operation
    p1 = multiprocessing.Process(target=addition, args=(num1, num2))
    p2 = multiprocessing.Process(target=subtraction, args=(num1, num2))
    p3 = multiprocessing.Process(target=multiplication, args=(num1, num2))
    p4 = multiprocessing.Process(target=division, args=(num1, num2))

    # Start each process
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    # Wait for all processes to finish
    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print("All operations completed.")
