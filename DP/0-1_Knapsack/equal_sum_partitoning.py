def knapsack(arr :list[int] , Sum):
    n = len(arr)
    t= [[False for _ in range(Sum+1)] for _ in range(n+1)]
    for i in range(n+1):
        t[i][0] = True 
    
    for i in range(1,n+1):
        for s in range(1,Sum+1):
            if arr[i-1] <= s:
                t[i][s] = t[i-1][s-arr[i-1]] or t[i-1][s]
            else:
                t[i][s] = t[i-1][s]
    return t[n][Sum]

def equal_sum(arr):
    sum=0
    for i in arr:
        sum+=i

    if sum % 2 !=0:
        return False
    return knapsack(arr , sum //2)

def main():
    arr = [1,5,11,11]
    result = equal_sum(arr)
    print("Is there a Equal Partioning subset with the given arr?", result)

if __name__ == "__main__":
    main()
