import random
import sys

def get_first_missing_number(bits):
    for i in range(len(bits)):
        if not bits[i]:
            return i
    return None

def main():
    random.seed(None)
    integers = 4000000000
    
    # Using a list to simulate bitset
    # Python list of booleans to act as the bitset
    bits = [False] * (integers + 1)

    for _ in range(integers + 1):
        r = random.randint(0, integers)
        bits[r] = True

    print(get_first_missing_number(bits))

if __name__ == "__main__":
    main()
