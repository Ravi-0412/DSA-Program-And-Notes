# Method 1: Recursion + memoisation
# Time : O(n^4) = TLE

# Logic: for forming the target[0] (i.e 1st char in remaining target)
# we can use any of the char from all words from the next possible index(last index we used for target formation)

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(words[0])  # all of same length
        mod = 10**9 + 7

        @lru_cache(None)
        def solve(target , ind):
            if not target:
                return 1
            if ind >= n:
                return 0
            ans = 0
            for word in words:
                for k in range(ind, n):
                    if target[0] == word[k]:
                        ans += solve(target[1: ], k + 1)
            return ans % mod

        return solve(target , 0)  # [target, possibleIndexToChoose]
    

# How we can optimise this?
# Observe: "Once you use the kth character of the jth string of words, 
# you can no longer use the xth character of any string in words where x <= k. 
# In other words, all characters to the left of or at index k become unusuable for every string".

# From since we are not allowed to move backward ,why to move to same index in any of the other word?
# For each index 'i' in words, we can store the no of possible ways to get target[j].

# Note: length of 'target' can't be greater than len(words[0]).

# See the code for more.
# Time: O(n^2) , space : O(n^2) + O(m*26), m = len(words[0])

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        # storing the count of each char at each index including all words in dictionary.
        # for this we need a dictionary or 2d array for m(len(words[0])).
        m , n = len(words[0]), len(target)
        countCharAtIndex = [Counter() for i in range(m)] # will keep tarck of no of char 'c' at 'i'th index.
        # counter will directly give value = 0 if char is not present at that index considering all words.
        for word in words:
            for i, c in enumerate(word):
                countCharAtIndex[i][c] += 1  # At ith index count of 'c'.
        
        # Now for forming the target
        # we have 2 options:
        # 1) Don't include char of this index from any of the word so simply move to next function call (Not Take)
        # 2) Take the char at this index:
        # in this ans will depend on count of 'target[i]' i.e  say 'n' including all words then ans = n * next function call
        #  And last return sum of both

        mod = 10**9 + 7

        @lru_cache(None)
        def solve(i, j):
            if i == n:
                # found one of possible ways
                return 1
            if j == m:
                # Without getting target went out of array i.e no possible way
                return 0
            # choice 1: Not include char of cur index from any of the word
            ans = solve(i, j + 1)  # have to search from index 'i' only
            # choice 2: if we consider the char at cur index from any of the word.
            c = target[i]  # curChar
            ans += countCharAtIndex[j][c] * solve(i + 1 , j + 1)  # have to search from index 'i + 1' only
            return ans % mod
        
        return solve(0 , 0)  # [TargetIndex , wordIndex]


