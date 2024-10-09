def longest(s,k):
    maxi = 0
    n = len(s)

    if n==0 or k ==0:
        return 0
    
    counter = {}
    i = 0

    for j in range(n):
        if s[j] in counter:
            counter[s[j]] +=1
        else:
            counter[s[j]] = 1

        
        while len(counter) > k:
            counter[s[i]] -=1
            if counter[s[i]] == 0:
                del counter[s[i]]

            i+=1

        
        maxi = max(maxi,j-i+1)


    return maxi 


s = "aabacbebebe"
k = 3
result = longest(s, k)
print(f"Length of the longest substring with {k} unique characters: {result}")
