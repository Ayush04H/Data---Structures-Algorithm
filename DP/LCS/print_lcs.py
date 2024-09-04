def lcs(x: str, y: str) -> str:
    m = len(x)
    n = len(y)

    # Initialize the table with zeros
    t = [[0 for _ in range(n+1)] for _ in range(m+1)]

    # Fill the table
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])

    # Initialize variables to trace back and construct the LCS string
    lcs_str = []
    i, j = m, n

    # Trace back from the bottom-right corner of the table
    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            lcs_str.append(x[i-1])
            i -= 1
            j -= 1
        elif t[i-1][j] > t[i][j-1]:
            i -= 1
        else:
            j -= 1

    # The LCS is constructed backwards, so reverse the list
    lcs_str.reverse()

    # Convert the list to a string and return
    return ''.join(lcs_str)

S1 = "geek"
S2 = "eke"

print("LCS of", S1, "and", S2, "is", lcs(S1, S2))
