def longest(s):
    n = len(s)
    if n == 0:
        return 0
    maxi = 0
    i = 0
    char_count = {}

    for j in range(n):
        if s[j] in char_count and char_count[s[j]] >= i:
            i = char_count[s[j]] + 1

        char_count[s[j]] = j

        maxi = max(maxi,j-i+1)


    return maxi


s = "aabacbebebe"

result = longest(s)
print(f"Length of the longest substring without repeating characters: {result}")