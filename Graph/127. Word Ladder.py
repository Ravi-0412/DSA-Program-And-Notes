# So, all this problem is asking us to do, is find a shortest path from our start word to end word using only word inside our list.
# Now any time you think, find the shortest sequence you should immediately think, always i need to use some shortest path algorithm like Breadth-First-Search or dijkastra
# logic: beginword will be at level '0' and now just keep all the words which can be formed by changing one char at level 1 ,
#  word which can be formed by changing two char at level 2 and so on.
# for this type of Q we always use multisource BFS(didi in many problem before)

# Time Complexity :- BigO(M^2 * N), where M is size of dequeued word & N is size of our word list
# Space Complexity :- BigO(M * N) where M is no. of character that we had in our string & N is the size of our wordList.

# detailed explanation in notes or below link(same way i have done)
# https://leetcode.com/problems/word-ladder/discuss/346920/Python3-Breadth-first-search

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:   # corner case
            return 0
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
        visited= set()  # have to use this since one word can be added many times in the 'Q' 
        Q= collections.deque()
        ans= 0
        Q.append(beginWord)
        visited.add(beginWord)
        while Q:
            ans+= 1
            for i in range(len(Q)):   # this i was missing.. we have to add all the neighbour at once .. just like multisource bfs
                word= Q.popleft()
                if word== endWord:
                    return ans     # if there will be any sequnce then it will return from here itself as we have already handled the corner case if 'endWord' is not present
                # now find the pattern that the curr 'word' can make and append those words that can make that pattern
                for i in range(len(word)):
                    pattern= word[:i] + "*" + word[i+1:]
                    # add all the nei(adjacent) to this word, for this find out the word which is present in the dic w.r.t to all the pattern that this word can generate
                    # that all will have one character diff from 'cur' word i.e one level ahead
                    for nei in dic[pattern]:
                        if nei not in visited:
                            Q.append(nei)
                            visited.add(nei)
                            
        return 0   # return default if there is no any sequence is present

        