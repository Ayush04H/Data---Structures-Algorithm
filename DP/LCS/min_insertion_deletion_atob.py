def lcs(x:str,y:str) ->int:
    m = len(x)
    n = len(y)

    t = [[-1 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        t[i][0] = 0
    for i in range(n+1):
        t[0][i] = 0

    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1] == y[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j],t[i][j-1])

    return t[m][n]


def min_ins_del(x:str,y:str) ->tuple:
    lcs_res = lcs(x,y)

    insertion = len(y) - lcs_res
    deletion = len(x) - lcs_res

    return insertion , deletion

A = "heap"
B = "pea"

insertions, deletions = min_ins_del(A, B)
print(f"Minimum number of insertions: {insertions}")
print(f"Minimum number of deletions: {deletions}")
