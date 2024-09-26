def toy_pick(s):
    i = 0
    toy_count = {}
    n = len(s)
    maxi = 0

    for j in range(n):
        if s[j] in toy_count:
            toy_count[s[j]] += 1

        else:
            toy_count[s[j]] = 1

        while len(toy_count) > 2:
            toy_count[s[i]] -= 1
            if toy_count[s[i]] == 0:
                del toy_count[s[i]]

            i+=1
        
        maxi = max(maxi,j-i+1)

    return maxi 


s = "abacceaaab"
result = toy_pick(s)
print(f"Maximum number of toys that can be picked: {result}")