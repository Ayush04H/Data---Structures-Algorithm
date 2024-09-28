from collections import Counter
def minWindow(s: str, t: str) -> str:
        counter = Counter(t)
        overall = len(counter)

        i = 0
        j = 0

        res =""

        while j < len(s):
            if s[j] in counter:
                counter[s[j]] -= 1
                if counter[s[j]] == 0:
                    overall -= 1

            while overall == 0:
                if not res:
                    res = s[i:j+1]

                elif j-i+1 < len(res):
                    res = s[i:j+1]

                if s[i] in counter:
                    counter[s[i]] += 1
                    if counter[s[i]] > 0:
                        overall += 1

                i+=1

            j+=1

        return res


s = "ADOBECODEBANC"
t = "ABC"

print(minWindow(s,t))