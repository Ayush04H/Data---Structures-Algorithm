from collections import Counter

def count_and_find_anagrams(string, ptr):
    n = len(string)
    k = len(ptr)
    d = Counter(ptr)
    i = 0
    j = 0
    count = len(d)
    ans = 0
    anagrams = []  # To store the anagrams

    while j < n:
        # Decrease the count of the current character in the map
        if string[j] in d:
            d[string[j]] -= 1
            if d[string[j]] == 0:
                count -= 1

        # Check if the window size is less than k
        if (j - i + 1) < k:
            j += 1

        # If the window size is equal to k
        elif (j - i + 1) == k:
            # If all characters match, it's an anagram
            if count == 0:
                ans += 1
                anagrams.append(string[i:j+1])  # Append the current anagram

            # Slide the window
            if string[i] in d:
                d[string[i]] += 1
                if d[string[i]] == 1:
                    count += 1

            j += 1
            i += 1

    return ans, anagrams


# Example Usage
string = "aabaabaa"
ptr = "aaba"
print(count_and_find_anagrams(string, ptr))
