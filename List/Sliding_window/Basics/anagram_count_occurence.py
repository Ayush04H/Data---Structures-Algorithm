from collections import Counter
string = "aabaabaa"
ptr = "aaba"
n = len(string)
k = len(ptr)
'''d = {}
for i in ptr:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1'''
d = Counter(ptr)
i = 0
j = 0
count = len(d)

ans = 0

while j < n:
    if string[j] in d:
        d[string[j]] -= 1
        if d[string[j]] == 0:
            count -= 1

    if (j-i+1) < k:
        j+=1

    elif (j-i+1) == k:
        if count == 0:
            ans += 1

        if string[i] in d:
            d[string[i]] += 1
            if d[string[i]] == 1:
                count +=1


        j+=1
        i+=1

print(ans)



    