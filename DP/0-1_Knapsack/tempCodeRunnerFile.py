n=len(arr)
    t = [[0 for _ in range(Sum + 1)] for _ in range(n+1)]
    for i in range(n+1):
        t[i][0]= 1