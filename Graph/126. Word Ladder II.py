# similasr Q as word ladder.
# Differences from word ladder:
# 1) here we have to find the all the shortest path possible. so taking path also in Q.
# 2) Here we will mark word as visited only after each level at once.
#Reason: since that word can be next sequence for the word at same level leading to different sequences and we have to consider that also.

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:   # corner case
            return ""
        dic= collections.defaultdict(list)
        # append the 'beginword' into the 'wordlist'
        wordList.append(beginWord)
        # now store the word w.r.t to the pattern they can make by changing one one charater into the dictionary
        for word in wordList:
            for i in range(len(beginWord)):   # all the words will be of same size
                # you are putting the special char "*" at 'i'th index so you have to skip that char from the word
                pattern= word[:i] + "*" + word[i+1:]    # start is any special char, it tells the position we have changed the character
            
                dic[pattern].append(word)
                
        # now do bfs from beginWord and store all the words that can be formed by changing one character in the 'beginWord'
        # all those words will be at level 1 from the "beginWord" and so on do for level word till 'Q' becomes empty
        visited= set()  # here we will mark viisted only after each level not when we see at first only.

        Q= collections.deque()
        shortest_path= 0   # this will give the 'shortest path length'. Ans of Q: 'word ladder'.
        ans= []
        Q.append((beginWord, [beginWord], 0))  # storing the path also with level
        visited.add(beginWord)
        while Q:
            level_visited= set()   # to check at each level
            for i in range(len(Q)):   
                word, path, level= Q.popleft()
                if word== endWord:
                    ans.append(path)
                    shortest_path= level
                # now find the pattern that the curr 'word' can make and append those words that can make that pattern
                for i in range(len(word)):
                    pattern= word[:i] + "*" + word[i+1:]
                    for nei in dic[pattern]:
                        if nei not in visited:   # no matter if already locally visited. visited we have to mark only at the end of each level.
                            Q.append((nei, path + [nei], level +1))
                            level_visited.add(nei)    # only to mark  in level visited not in visited.
            visited= visited.union(level_visited)   # marking all the word that we have visited at curr level after each level.             
        return ans if len(ans) > 0 else ""


# later have to try the solution that doesn't give Tle.
# see the striver lecture no: 31 and solution in the link.
