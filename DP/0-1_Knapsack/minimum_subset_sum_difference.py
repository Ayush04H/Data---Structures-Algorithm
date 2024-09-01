def minimum_sum_subset(arr:list[int]):
    n = len(arr)
    Sum = sum(arr)

    t = [[False for _ in range(Sum + 1)] for _ in range(n + 1)]

    for i in range(n+1):
        t[i][0] = True 

    for i in range(1,n+1):
        for s in range(1,Sum + 1):
            if arr[i-1] <= s:
                t[i][s] = t[i-1][s-arr[i-1]] or t[i-1][s]
            else:
                t[i][s] = t[i-1][s]

    min_diff = float('inf')
    for i in range(Sum //2 + 1):
        if t[n][i] :
            min_diff = min(min_diff , Sum - 2*i)

    return min_diff

def main():
    # Example array
    arr = [10, 20, 15, 5, 25]
    
    # Call the minimum_subset_sum_difference function
    result = minimum_sum_subset(arr)
    
    # Print the result
    print(f"The minimum subset sum difference is: {result}")

if __name__ == "__main__":
    main()