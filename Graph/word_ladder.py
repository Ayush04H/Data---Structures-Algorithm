from collections import deque
import string
def ladderLength(beginWord,endWord,wordList):
    if endWord not in wordList:
        return 0 
    
    wordset = set(wordList)
    q = deque()
    s = beginWord
    visited = set()
    visited.add(s)
    q.append((s,1))

    while q:
        word , step = q.popleft()
        if word == endWord:
            return step
        
        for i in range(len(word)):
            for c in string.ascii_lowercase:
                newword = word[:i] + c + word[i+1:]

                if newword in wordset and newword not in visited:
                    q.append((newword,step+1))
                    visited.add(newword)


    return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(ladderLength(beginWord,endWord,wordList))
    