def lcs(x: str, y: str) -> int:
    m = len(x)
    n = len(y)
    t = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            # Check if characters match and indices are different
            if x[i-1] == y[j-1] and i != j:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])

    return t[m][n]

def longest_repeating_subsequence(s: str) -> int:
    # The LRS is the LCS of the string with itself, but with a condition on indices
    return lcs(s, s)

# Example usage
S = "AABEBCDD"
lrs_length = longest_repeating_subsequence(S)
print(f"Length of Longest Repeating Subsequence is {lrs_length}")
