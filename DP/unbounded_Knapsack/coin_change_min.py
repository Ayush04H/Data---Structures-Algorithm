def knapsack(arr , w):
    n = len(arr)
    t = [[float('inf') for _ in range(w +1)] for _ in range(n+1)]

    for i in range(n+1):
        t[i][0] = 0

    for i in range(1,n+1):
        for s in range(1,w+1):
            if arr[i-1] <= s:
                t[i][s] = min(1 + t[i][ s - arr[i-1]] , t[i-1][s])

            else:
                t[i][s] = t[i-1][s]
    
    return t[n][w] if t[n][w] != float('inf') else -1

def main():
    arr = [1, 2 , 3]  # Example coin denominations
    W = 5  # Example amount to make
    
    min_coins_required = knapsack(arr, W)
    print(f"The minimum number of coins required to make amount {W} is: {min_coins_required}")

# Call the main function
main()