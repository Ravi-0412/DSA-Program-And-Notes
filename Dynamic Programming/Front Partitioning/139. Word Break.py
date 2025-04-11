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

# memoization
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
    
# Java
"""
import java.util.*;

public class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);
        int n = s.length();
        Boolean[] dp = new Boolean[n + 1];
        return helper(0, n, s, wordSet, dp);
    }

    private boolean helper(int index, int n, String s, Set<String> wordSet, Boolean[] dp) {
        if (index == n) {
            return true;
        }
        if (dp[index] != null) {
            return dp[index];
        }
        for (int k = index + 1; k <= n; k++) {
            if (wordSet.contains(s.substring(index, k)) && helper(k, n, s, wordSet, dp)) {
                dp[index] = true;
                return true;
            }
        }
        dp[index] = false;
        return false;
    }
}
"""


# Note vvi: 
# Same method but when doing by taking actual string giving TLE.
# Have to analyse this properly and discuss with someone.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(s):
            if not s:
                return True
            if s in cache:
                return cache[s]
            for i in range(len(s)):
                if s[: i+1] in wordDict and self.wordBreak(s[i+1 :], wordDict):
                    cache[s] = True
                    return True
            cache[s] = False
            return False
        cache = {}
        return dfs(s)
