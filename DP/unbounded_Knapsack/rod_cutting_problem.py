def knapsack(price :list[int] , W) -> int:
    arr = [(i+1) for i in range(W)]
    n=len(arr)
    t =[[0 for _ in range(W+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        for s in range(1,n+1):
            if arr[i-1] <= s:
                t[i][s] = max(price[i - 1] + t[i][s - arr[i - 1]], t[i - 1][s])
            else:
                t[i][s] = t[i - 1][s]

    return t[n][W]


def main():
    # Lengths of rod pieces (now includes length 5)
    val = [1 , 5, 8, 9, 10, 17 , 17 , 20]  # Example prices for each piece length
    W = len(val)  # Length of the rod

    max_val = knapsack(val,W)
    print(f"The maximum value obtainable from cutting the rod is: {max_val}")

# Call the main function
main()
                