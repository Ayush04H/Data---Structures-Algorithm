def lcs(x :str,y:str) ->int :
    m = len(x)
    n = len(y)

    t = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):

            if x[i-1] == y[j-1]:
                t[i][j] = 1 + t[i-1][j-1]

            else:
                t[i][j] = max(t[i-1][j] , t[i][j-1])

    return t[m][n]

S1 = "geek"
S2 = "eke"

print("Length of LCS is", lcs(S1, S2))