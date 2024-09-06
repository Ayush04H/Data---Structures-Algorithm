def lcs(x: str, y: str) -> int:
    m = len(x)
    n = len(y)
    t = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            # Check if characters match and indices are different
            if x[i-1] == y[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])

    return t[m][n]


def sequence(a:str , b:str) ->bool:
    lcs_len=lcs(a,b)
    return lcs_len == len(a)

# Example usage
A = "abzc"
B = "adbce"

if sequence(A, B):
    print(f"'{A}' is a subsequence of '{B}'")
else:
    print(f"'{A}' is not a subsequence of '{B}'")