def mcm(arr,i,j):
    n =len(arr)
    
    if i>=j:
        return 0
    
    t = [[-1 for _ in range(n+1)] for _ in range(n+1)]

    if t[i][j] != -1:
        return t[i][j]

    min_cost = float('inf')

    for k in range(i,j):
        cost = (mcm(arr,i,k) +
                mcm(arr,k+1,j) +
                arr[i-1] * arr[k] * arr[j])

        if cost < min_cost:
            min_cost=cost

    t[i][j] = min_cost
    return t[i][j] 


arr = [10, 20, 30, 40, 50]
n=len(arr)
min_cost = mcm(arr , 1, n-1)
print(f"Minimum number of multiplications is {min_cost}")