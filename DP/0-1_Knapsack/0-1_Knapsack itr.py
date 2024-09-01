def knapsack(W: int, val: list[int], weight: list[int], n: int) -> int:
    # Step 1: Initialize the matrix with 0
    t = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Step 2: Fill the table
    for i in range(1, n + 1):
        for w in range(1,W + 1):
            if weight[i - 1] <= w:
                # If the current item's weight is less than or equal to the current capacity,
                # take the maximum of including or not including the item
                t[i][w] = max(val[i - 1] + t[i - 1][w - weight[i - 1]], t[i - 1][w])
            else:
                # Otherwise, we can't include this item
                t[i][w] = t[i - 1][w]

    # The answer is in t[n][W], i.e., considering all items and the full capacity
    return t[n][W]

def main():
    # Example values for the knapsack problem
    W = 7  # Maximum weight capacity of the knapsack
    val = [1, 4, 5, 7]  # Values of the items
    weight = [1, 3, 4, 5]  # Weights of the items
    n = len(val)  # Number of items

    # Call the knapsack function
    result = knapsack(W, val, weight, n)
    
    # Print the result
    print("Maximum value that can be obtained:", result)

if __name__ == "__main__":
    main()
