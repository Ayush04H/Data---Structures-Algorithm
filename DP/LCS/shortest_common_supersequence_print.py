def scs(x: str, y: str) -> str:
    m = len(x)
    n = len(y)
    t = [[-1 for _ in range(n+1)] for _ in range(m+1)]

    # Initialize the table with LCS length computation
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

    # Construct the SCS by backtracking through the table
    scs_str = []
    i, j = m, n

    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            scs_str.append(x[i-1])
            i -= 1
            j -= 1
        elif t[i-1][j] > t[i][j-1]:
            scs_str.append(x[i-1])
            i -= 1
        else:
            scs_str.append(y[j-1])
            j -= 1

    # If any characters are left in x or y, add them
    while i > 0:
        scs_str.append(x[i-1])
        i -= 1
    while j > 0:
        scs_str.append(y[j-1])
        j -= 1

    # The SCS is constructed backwards, so reverse the list
    scs_str.reverse()

    # Convert the list to a string and return
    return ''.join(scs_str)

S1 = "abac"
S2 = "cab"

print("SCS of", S1, "and", S2, "is", scs(S1, S2))
