from collections import Counter
def countanagrams(string,ptr):
    i = j = 0
    n = len(string)
    k = len(ptr)

    d = Counter(ptr)
    count = len(d)
    ans = []
    while j < n:
        if string[j] in d:
            d[string[j]] -=1
            if d[string[j]] == 0:
                count-=1

        if j-i+1 < k:
            j+=1

        elif j - i + 1 == k:
            if count == 0:
                ans.append(string[i:j+1])

            if string[i] in d:
                d[string[i]] += 1
                if d[string[i]] == 1:
                    count+=1


            j+=1
            i+=1

    print(ans)

string = "aabaabaa"
ptr = "aaba"

countanagrams(string,ptr)
