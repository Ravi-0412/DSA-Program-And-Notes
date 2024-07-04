# Similar to : "139. Word Break".
# Diff: Here susbtring present may be discontinuous.
# To get the substring we may have to skip some characters.
# Ans our ans will be 'How many char we need to skip'.


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words= set()
        # store all words of dictionary into set to check whether substr in dictionary in O(1).
        for word in dictionary:
            words.add(word)
        n= len(s)
        
        @lru_cache(None)
        def solve(ind):
            if ind >= n:
                return 0
            res= float('inf')   # Have to take minimum of all possibility.
            # check for each substring that can form from the remaining index.
            for j in range(ind, len(s)):
                substr= s[ind: j+1]
                if substr in words:
                    # if present then no need to leave any char
                    # is function call pe kitna leave kiye + next upcoming function call.
                    res= min(res, 0 + solve(j + 1))  
                else: # we will leave (j - ind + 1) no of char
                    res= min(res, (j - ind + 1) + solve(j + 1))
            return res

        return solve(0)
    

# Method 2:
# count the max length we can form from the dictionary.
# then our ans = len(s) - maxLength

# Just similar to above method, here we have to take maximum.

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)

        @lru_cache(None)
        def solve(i):
            if i == n:
                return 0
            maxLength = 0
            for j in range(i, n):
                # is function call itna length contribute kar rha + next function call kitna karega . Then take max of all.
                if s[i: j+ 1] in dictionary:
                    maxLength = max(maxLength, j - i + 1 + solve(j + 1))
                else:
                    maxLength = max(maxLength, 0 + solve(j + 1))
            return maxLength

        maxLength = solve(0)
        return n - maxLength


# My mistake in method 2:
# 1)  not taking max in when substring is in dictionary i.e 
# maxLength = j - i + 1 + solve(j + 1) 
# if we do like this then it will not take max of other function calls.

# 2) maxLength += j - i + 1 + solve(j + 1) 
# This will add all possible length but here we have to take maximum of all possibility. Not to add all.

# Hmlog jb 'j - i + 1 + solve(j + 1) ' like rhe to next function call ka value add kar rhe already.


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        
        @lru_cache(None)
        def solve(i):
            if i == n:
                return 0
            maxLength = 0
            for j in range(i, n):
                if s[i: j+ 1] in dictionary:
                    maxLength += j - i + 1 + solve(j + 1)    
                else:
                    maxLength = max(maxLength, 0 + solve(j + 1))
            return maxLength


        
        maxLength = solve(0)
        return n - maxLength