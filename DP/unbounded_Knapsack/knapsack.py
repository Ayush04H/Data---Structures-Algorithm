# Let's define the knapsack function first and then write a main function to call it with an example input.

def knapsack(val, arr, W):
    n = len(arr)
    t = [[0 for i in range(W + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for s in range(1, W + 1):
            if arr[i - 1] <= s:
                t[i][s] = max(val[i - 1] + t[i][s - arr[i - 1]], t[i - 1][s])
            else:
                t[i][s] = t[i - 1][s]

    return t[n][W]

# Now, let's write the main function to call the knapsack function with an example.

def main():
    val = [10, 40, 50, 70]  # Example values of the items
    arr = [1, 3, 4, 5]  # Example weights of the items
    W = 8  # Example capacity of the knapsack

    max_val = knapsack(val, arr, W)
    print(f"The maximum value for the unbounded knapsack problem is: {max_val}")

# Call the main function
main()
