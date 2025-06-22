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

# Java Code 
"""
import java.util.*;

class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);  // to check any substring present or not in O(1)
        int n = s.length();
        return helper(0, n, s, wordSet);
    }

    // this function will return true if the substring from index 'ind' to end can be segmented
    private boolean helper(int ind, int n, String s, Set<String> wordSet) {
        if (ind == n)
            return true;
        for (int k = ind + 1; k <= n; k++) {  // 'k' should go till 'n'
            if (wordSet.contains(s.substring(ind, k)) && helper(k, n, s, wordSet))
                return true;
        }
        return false;
    }
}
"""
# C++ Code 
"""
#include <string>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());  // to check any substring present or not in O(1)
        int n = s.length();
        return helper(0, n, s, wordSet);
    }

    bool helper(int ind, int n, const string& s, unordered_set<string>& wordSet) {
        if (ind == n)
            return true;
        for (int k = ind + 1; k <= n; ++k) {  // 'k' should go till 'n'
            if (wordSet.count(s.substr(ind, k - ind)) && helper(k, n, s, wordSet))
                return true;
        }
        return false;
    }
};
"""

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
    

# Java Code 
"""
import java.util.*;

class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);  // to check any substring present or not in O(1)
        int n = s.length();
        int[] dp = new int[n + 1];  // dp[i]: denotes whether we can partition s[:i+1] into words given in wordDict or not.
        Arrays.fill(dp, -1);
        return helper(0, n, s, wordSet, dp);
    }

    private boolean helper(int ind, int n, String s, Set<String> wordSet, int[] dp) {
        if (ind == n)
            return true;
        if (dp[ind] != -1)
            return dp[ind] == 1;

        for (int k = ind + 1; k <= n; k++) {  // 'k' should go till 'n'
            if (wordSet.contains(s.substring(ind, k)) && helper(k, n, s, wordSet, dp)) {
                dp[ind] = 1;
                return true;
            }
        }

        dp[ind] = 0;
        return false;
    }
}
"""
# C++ Code 
"""
#include <string>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());  // to check any substring present or not in O(1)
        int n = s.length();
        vector<int> dp(n + 1, -1);  // dp[i]: denotes whether we can partition s[:i+1] into words given in wordDict or not.
        return helper(0, n, s, wordSet, dp);
    }

private:
    bool helper(int ind, int n, const string& s, unordered_set<string>& wordSet, vector<int>& dp) {
        if (ind == n)
            return true;
        if (dp[ind] != -1)
            return dp[ind] == 1;

        for (int k = ind + 1; k <= n; ++k) {  // 'k' should go till 'n'
            if (wordSet.count(s.substr(ind, k - ind)) && helper(k, n, s, wordSet, dp)) {
                dp[ind] = 1;
                return true;
            }
        }

        dp[ind] = 0;
        return false;
    }
};
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

# Java Code 
"""
import java.util.*;

class Solution {
    Map<String, Boolean> cache = new HashMap<>();

    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);
        return dfs(s, wordSet);
    }

    private boolean dfs(String s, Set<String> wordSet) {
        if (s.isEmpty())
            return true;
        if (cache.containsKey(s))
            return cache.get(s);

        for (int i = 0; i < s.length(); i++) {
            if (wordSet.contains(s.substring(0, i + 1)) && dfs(s.substring(i + 1), wordSet)) {
                cache.put(s, true);
                return true;
            }
        }

        cache.put(s, false);
        return false;
    }
}
"""
# C++ Code 
"""
#include <string>
#include <vector>
#include <unordered_set>
#include <unordered_map>
using namespace std;

class Solution {
    unordered_map<string, bool> cache;

public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());
        return dfs(s, wordSet);
    }

    bool dfs(const string& s, unordered_set<string>& wordSet) {
        if (s.empty())
            return true;
        if (cache.count(s))
            return cache[s];

        for (int i = 0; i < s.length(); ++i) {
            string prefix = s.substr(0, i + 1);
            if (wordSet.count(prefix) && dfs(s.substr(i + 1), wordSet)) {
                cache[s] = true;
                return true;
            }
        }

        cache[s] = false;
        return false;
    }
};
"""