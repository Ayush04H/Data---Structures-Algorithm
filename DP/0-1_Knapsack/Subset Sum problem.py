def subset_sum(arr: list[int], sum_val: int) -> bool:
    n = len(arr)
    
    # Step 1: Initialize the matrix with False values
    t = [[False for _ in range(sum_val + 1)] for _ in range(n + 1)]
    
    # Step 2: If sum is 0, then answer is True (by not including any items)
    for i in range(n + 1):
        t[i][0] = True
    
    # Step 3: Fill the table
    for i in range(1, n + 1):
        for s in range(1, sum_val + 1):
            if arr[i - 1] <= s:
                # Include the current item or don't include it
                t[i][s] = t[i - 1][s - arr[i - 1]] or t[i - 1][s]
            else:
                # Can't include the item
                t[i][s] = t[i - 1][s]
    
    # The answer is in t[n][sum_val], i.e., considering all items and the desired sum
    return t[n][sum_val]

def main():
    # Example values for the Subset Sum problem
    arr = [3, 34, 4, 12, 5, 2]  # Set of numbers
    sum_val = 37 # Desired sum
    
    # Call the subset_sum function
    result = subset_sum(arr, sum_val)
    
    # Print the result
    print("Is there a subset with the given sum?", result)

if __name__ == "__main__":
    main()
