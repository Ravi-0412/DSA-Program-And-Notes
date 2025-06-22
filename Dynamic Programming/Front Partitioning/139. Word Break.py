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
# Method 2: 
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

# Java Code 
"""
import java.util.*;

class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);  // to check any substring present or not in O(1)
        int n = s.length();
        boolean[] dp = new boolean[n + 1];
        dp[n] = true;  // Base case: if ind == n

        for (int ind = n - 1; ind >= 0; ind--) {
            for (int k = ind + 1; k <= n; k++) {  // 'k' should go till 'n'
                if (wordSet.contains(s.substring(ind, k)) && dp[k]) {
                    dp[ind] = true;
                    break;  // No need to check further once we know it's breakable
                }
            }
        }

        return dp[0];
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <string>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());  // to check any substring present or not in O(1)
        int n = s.size();
        vector<bool> dp(n + 1, false);
        dp[n] = true;  // Base case: if ind == n

        for (int ind = n - 1; ind >= 0; --ind) {
            for (int k = ind + 1; k <= n; ++k) {  // 'k' should go till 'n'
                if (wordSet.count(s.substr(ind, k - ind)) && dp[k]) {
                    dp[ind] = true;
                    break;  // No need to check further once we know it's breakable
                }
            }
        }

        return dp[0];
    }
};
"""