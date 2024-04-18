# similar Q as word ladder.
# Differences from word ladder:
# 1) here we have to find the all the shortest path possible. so taking path also in Q.
# 2)VVI:  Here we will mark word as visited level by level i.e all nodes at same level at once.
# Not like one by one after visiting.
# Reason:if we mark visited at 1st tiem then we will not get all the answers.

# Take an example => in queue currently ["dog", "log"] is present and at 
# next level there is one word say "cog" .
# Now we will pop 1st word from 'queue' i.e 'dog' and now will visit its neighbour i.e 'cog'
# you mark 'cog' as visited . 
# Now you pop next word from 'queue' i.e 'log' and neighbour of 'log' is 'cog' but yiu have marked
# 'cog' visited in above step only. so you won't be able to add that but that will also path for one of our possible ans.

# That's why mark nodes visited level by level.

# Note vvi: In question "127.Word Ladder" they were asking only to find the shortest path so there was no need to add
# same node again and again to previous level nodes. But here we need to find all possible paths sowe have to add to all
# nodes to previous level.

# TLE

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:   # corner case
            return []
        wordSet= set(wordList) 
        visited = set()  # have to use this since one word can be added many times in the 'Q' 
        Q= collections.deque()
        Q.append((beginWord, [beginWord])) 
        visited.add(beginWord)
        ans = []
        while Q:
            level_visited = set()
            for i in range(len(Q)):
                word , path = Q.popleft()
                # now find all worss that we can get by changing single char of this word which is present in 'wordList'.
                for j in range(len(word)):
                    for k in range(97, 123): 
                        nextWord= word[: j] + chr(k) + word[j+1: ]
                        if nextWord in wordSet and nextWord not in visited:
                            if nextWord == endWord:
                                ans.append(path + [nextWord])
                            Q.append((nextWord, path + [nextWord]))
                            level_visited.add(nextWord)
            visited = visited.union(level_visited) 
        return ans


# Optimisation
# Think what repititive work we are doing in above one.

# repititive work: We are checking from whole wordList for each newWord.
# But we don't need to check words that we have seen till cur_level.

# So we have to removed words from wordList that we have seen at start of each level.
# For this best data structure is set for removing and adding in O(len(word)).

# So store words at each level in set and at each level remove the words that is in cur_level to avoid checking.

# But in set you can't take 'path' also because it won't maintain the order.
# For order add parents of all word in a list and then traverse back from 'endWord' to 'beginWord' to get all ans.

# Here no need to mark visited, if newWord in wordSet then it means they have not been visited till now.


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:   # corner case
            return []
        wordSet= set(wordList)
        parents = collections.defaultdict(list)
        cur_level = {beginWord}
        shortest_path = 1    # will give ans for 1st part "127.Word adder"
        while cur_level:
            # Remove all words from wordList which is inside cur_level
            # To avoid checking less no of  words later
            wordSet -= cur_level 
            next_level = set()  # to store words at next level
            for word in cur_level:
                for j in range(len(word)):
                    for k in range(97, 123): 
                        nextWord= word[: j] + chr(k) + word[j+1: ]
                        if nextWord in wordSet:
                            next_level.add(nextWord)
                            parents[nextWord].append(word)
            if endWord in next_level:
                break
            cur_level = next_level
            shortest_path += 1
        
        # Now backtrack from 'endWord' to 'beginWord' using dfs 
        ans = []

        def dfs(word, path):
            if word == beginWord:
                path.append(beginWord)
                ans.append(path[::-1])
                return
            for parent_word in parents[word]:
                dfs(parent_word, path + [word])
        dfs(endWord, [])
        return ans

