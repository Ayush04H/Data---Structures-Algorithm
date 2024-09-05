def lcs(x:str,y:str) ->int:
    m=len(x)
    n=len(y)

    t = [[-1 for i in range(n+1)] for _ in range(m+1)]

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

def pallindrome_subsequence(s:str) ->int:
    rev_s = s[::-1]
    return lcs(s,rev_s)

# Example usage
S = "bbbab"
lps_length = pallindrome_subsequence(S)
print(f"Length of Longest Palindromic Subsequence is {lps_length}")