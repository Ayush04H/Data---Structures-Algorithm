def lcs(x: str, y: str) -> int:
    m = len(x)
    n = len(y)
    t = [[-1 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        t[i][0] = 0
    for j in range(n+1):
        t[0][j] = 0
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])

    return t[m][n]



def minimum_deletions_to_make_palindrome(s: str) -> int:
    # The LPS of a string is the LCS of the string and its reverse
    reverse_s = s[::-1]
    lps_length = lcs(s, reverse_s)
    
    # The minimum number of deletions to make the string a palindrome
    return len(s) - lps_length

# Example usage
S = "agbcba"
min_deletions = minimum_deletions_to_make_palindrome(S)
print(f"Minimum number of deletions to make '{S}' a palindrome is {min_deletions}")