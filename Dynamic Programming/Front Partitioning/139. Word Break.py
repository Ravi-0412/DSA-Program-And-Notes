# Method 1: 
# just same logic what we did in Q: 140. Word Break II

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)  # to check any substring present or not in O(1)
        n= len(s)
        return self.helper(0, n, s, wordSet) 
    
    def helper(self, ind, n, s, wordSet):
        if ind== n:
            return True
        for k in range(ind +1, n+1): # 'k ' should go till 'n'
            if s[ind: k] in wordSet and self.helper(k, n, s, wordSet):
                return True
        return False



# Method 2: 
# Memoization
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet= set(wordDict)  # to check any substring present or not in O(1)
        n= len(s)
        dp= [-1 for i in range(n+1)]  # dp[i]: denotes whether we can partition s[: i+1] into words given in wordDict or not.
        return self.helper(0, n, s, wordSet, dp) 
    
    def helper(self, ind, n, s, wordSet, dp):
        if ind== n:
            return True
        if dp[ind]!= -1:
            return dp[ind]
        for k in range(ind +1, n+1): # 'k ' should go till 'n'
            if s[ind: k] in wordSet and self.helper(k, n, s, wordSet, dp):
                dp[ind]= True
                return True
        dp[ind]= False
        return False


# Method 3:
# Tabulation
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)  # to check any substring present or not in O(1)
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True  # Base case: if ind == n
        
        for ind in range(n - 1, -1, -1):
            for k in range(ind + 1, n + 1):  # 'k' should go till 'n'
                if s[ind:k] in wordSet and dp[k]:
                    dp[ind] = True
                    break  # No need to check further once we know it's breakable
        
        return dp[0]


