def characterReplacement(s: str, k: int) -> int:
        longest = 0
        i = 0 
        counts = [0] * 26 
        for j in range(len(s)):
            counts[ord(s[j]) - 65] += 1
            while j-i+1 - max(counts) > k:
                counts[ord(s[i]) - 65] -= 1
                i+=1
            longest = max(longest,j-i+1)
        return longest


s = "ABAB"
k = 2
print(characterReplacement(s,k))