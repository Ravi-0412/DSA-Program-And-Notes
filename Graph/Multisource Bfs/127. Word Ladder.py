
# At any time you see, find the shortest steps/path you should immediately think Breadth-First-Search or dijkastra.
# logic: beginword will be at level '0' and now just keep all the words which can be formed by changing one char at level 1 ,
#  word which can be formed by changing two char at level 2 and so on.
# for this type of Q we always use multisource BFS.

# Method 1: Simplest solution
# Logic: word which will differ by single character all those words will come adjacent to each other.
# So 1st make adjacency list by checking the difference and then apply mutisource bfs.

# from two constraints: 
# 1) endWord.length == beginWord.length
# 2) wordList[i].length == beginWord.length
# it is clear that beginWord and all words in wordList are of same length.

# First time when we will see the 'endWOrd' that will be the ans only.

# Time: O(n^2 * m). n= len(wordList) , m = len(each word) => more than 10**8 so TLE

class Solution(object):
    def ladderLength(self, beginWord, endWord, words):
        if endWord not in words:
            return 0
        words.append(beginWord)
        n = len(words)
        adj = collections.defaultdict(list)   # [word: adjacent_words]
        for i in range(n):
            word1 = words[i]
            for j in range(i + 1, n):
                word2 = words[j]
                k = 0
                cnt = 0
                while k < len(word1):
                    if word1[k] != word2[k]:
                        cnt += 1
                    k += 1
                if cnt == 1:
                    adj[word1].append(word2)
                    adj[word2].append(word1)
        q= deque()
        q.append((1, beginWord))
        visited = set()
        visited.add(beginWord)
        while q:
            for i in range(len(q)):
                step, word = q.popleft()
                for nei in adj[word]:
                    if nei ==  endWord:
                        return step + 1
                    if nei not in visited:
                        q.append((step + 1, nei))
                        visited.add(nei)
        return 0
    

# optimising the above solution:
# Logic: Instead of checking character difference between each pair of word
# check what all possible words we can get which is in 'wordList' by changing an character of a word.


# Time Complexity :- BigO(M^2 * N), where M is size of dequeued word & N is size of our word list
# Space Complexity :- BigO(M * N) where M is no. of character that we had in our string & N is the size of our wordList.

# Can do using normal bfs also taking extra variable by herew multisource bfs is making more sense.

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:   # corner case
            return 0
        dic= collections.defaultdict(list)
        # append the 'beginword' into the 'wordlist'
        wordList.append(beginWord)
        # now store the word w.r.t to the pattern they can make by changing one one charater into the dictionary
        for word in wordList:
            for i in range(len(beginWord)):
                # if we change the char at 'i'th index in 'word' then what all words it can form.
                # so skip the character at 'ith' index from 'word' with any special character.
                pattern= word[:i] + "*" + word[i+1:]
                dic[pattern].append(word)  # all words from which we can find this pattern will be at one distance only.
                
        # now do bfs from beginWord and store all the words that can be formed by changing one character in the 'beginWord'
        # all those words will be at level 1 from the "beginWord" and so on do for level word till 'Q' becomes empty
        visited= set()  # have to use this since one word can be added many times in the 'Q' 
        Q= collections.deque()
        Q.append((beginWord)) 
        visited.add(beginWord)
        level = 1
        while Q:
            for i in range(len(Q)): 
                word= Q.popleft()
                # now find the pattern that the curr 'word' can make and append those words that can make that pattern
                for i in range(len(word)):
                    pattern= word[:i] + "*" + word[i+1:]
                    # add all the nei(adjacent) to this word, for this find out the word which is present in the dic w.r.t to all the pattern that this word can generate
                    # that all will have one character diff from 'cur' word i.e one level ahead
                    for nei in dic[pattern]:
                        if nei not in visited:
                            if nei == endWord:
                                return level + 1
                            Q.append((nei))
                            visited.add(nei)
            level += 1
                            
        return 0   # return default if there is no any sequence is present

# method 2: Better one. Do by this only
# logic: Try to replace each char of each word from 'a' to 'z'.
# and check if the new_word formed by replacing exist in wordlist or not.

# Did using normal bfs can do by mutisource bfs also

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:   # corner case
            return 0
    
        wordSet= set(wordList)   # to check in O(1) after changing each char whether that word exist or not.
        # now do bfs from beginWord and store all the words that can be formed by changing one character in the 'beginWord'
        # all those words will be at level 1 from the "beginWord" and so on do for level word till 'Q' becomes empty .
        visited= set()  # have to use this since one word can be added many times in the 'Q' 
        Q= collections.deque()
        Q.append(beginWord)   # 2nd para: storing no of steps.
        visited.add(beginWord)
        shortest_path = 1
        while Q:
            for i in range(len(Q)):
                word = Q.popleft()
                # now find all worss that we can get by changing single char of this word which is present in 'wordList'.
                for j in range(len(word)):
                    for k in range(97, 123):  # replacing each char from 'a' to 'z' and checking if it exist in the words set
                        # word= word[: i] + chr(j) + word[i+1: ]   # my mistake(letter chenged will reflect permanently)
                        nextWord= word[: j] + chr(k) + word[j+1: ]
                        if nextWord in wordSet and nextWord not in visited:
                            if nextWord == endWord:
                                return shortest_path + 1
                            Q.append(nextWord)
                            visited.add(nextWord)
            shortest_path += 1                
        return 0   # return default if there is no any sequence is present