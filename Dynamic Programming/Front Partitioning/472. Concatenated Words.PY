# Method 1: 
# Brute force
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        longest_word = max(words, key = len)
        maxLength = len(longest_word)
        wordsSet = set(words)

        def solve(s , no_word):
            if no_word >= 2 and s in wordsSet:
                ans.append(s)
            if len(s) >= maxLength :
                return
            for i in range(len(words)):
                solve(s + words[i] , no_word + 1)

        ans = []
        solve("", 0)
        return ans

# Java Code 
"""
import java.util.*;

class Solution {
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        String longestWord = "";
        for (String w : words)
            if (w.length() > longestWord.length())
                longestWord = w;
        int maxLength = longestWord.length();

        Set<String> wordsSet = new HashSet<>(Arrays.asList(words));
        List<String> ans = new ArrayList<>();
        solve("", 0, words, wordsSet, maxLength, ans);
        return ans;
    }

    void solve(String s, int noWord, String[] words, Set<String> wordsSet, int maxLength, List<String> ans) {
        if (noWord >= 2 && wordsSet.contains(s)) {
            ans.add(s);
        }
        if (s.length() >= maxLength)
            return;

        for (String word : words) {
            solve(s + word, noWord + 1, words, wordsSet, maxLength, ans);
        }
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <string>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        string longestWord = "";
        for (const string& word : words)
            if (word.length() > longestWord.length())
                longestWord = word;
        int maxLength = longestWord.length();

        unordered_set<string> wordsSet(words.begin(), words.end());
        vector<string> ans;
        solve("", 0, words, wordsSet, maxLength, ans);
        return ans;
    }

    void solve(string s, int noWord, vector<string>& words, unordered_set<string>& wordsSet, int maxLength, vector<string>& ans) {
        if (noWord >= 2 && wordsSet.count(s)) {
            ans.push_back(s);
        }
        if ((int)s.length() >= maxLength)
            return;

        for (const string& word : words) {
            solve(s + word, noWord + 1, words, wordsSet, maxLength, ans);
        }
    }
};
"""

# method 2:
# Logic: Check each word whether we can form this or not.
# for this any of the prefix must be in words and suffix must be also in words.
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        d = set(words)
        
        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in d and suffix in d:
                    return True
                if prefix in d and dfs(suffix):
                # agar prefix present h but suffix present nhi h then, suffix ke liye alag se call karo.
                    return True
                if suffix in d and dfs(prefix):
                # agar suffix present h but prefix present nhi h then, prefix ke liye alag se call karo.
                    return True
            
            return False
        
        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        
        return res


# Java Code 
"""
import java.util.*;

class Solution {
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        Set<String> d = new HashSet<>(Arrays.asList(words));
        List<String> res = new ArrayList<>();

        for (String word : words) {
            if (dfs(word, d)) {
                res.add(word);
            }
        }

        return res;
    }

    private boolean dfs(String word, Set<String> d) {
        for (int i = 1; i < word.length(); i++) {
            String prefix = word.substring(0, i);
            String suffix = word.substring(i);

            if (d.contains(prefix) && d.contains(suffix)) {
                return true;
            }
            if (d.contains(prefix) && dfs(suffix, d)) {
                // agar prefix present h but suffix present nhi h then, suffix ke liye alag se call karo.
                return true;
            }
            if (d.contains(suffix) && dfs(prefix, d)) {
                // agar suffix present h but prefix present nhi h then, prefix ke liye alag se call karo.
                return true;
            }
        }

        return false;
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
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        unordered_set<string> d(words.begin(), words.end());
        vector<string> res;

        for (const string& word : words) {
            if (dfs(word, d)) {
                res.push_back(word);
            }
        }

        return res;
    }

private:
    bool dfs(const string& word, const unordered_set<string>& d) {
        for (int i = 1; i < word.size(); ++i) {
            string prefix = word.substr(0, i);
            string suffix = word.substr(i);

            if (d.count(prefix) && d.count(suffix)) {
                return true;
            }
            if (d.count(prefix) && dfs(suffix, d)) {
                // agar prefix present h but suffix present nhi h then, suffix ke liye alag se call karo.
                return true;
            }
            if (d.count(suffix) && dfs(prefix, d)) {
                // agar suffix present h but prefix present nhi h then, prefix ke liye alag se call karo.
                return true;
            }
        }

        return false;
    }
};
"""       
# Method 3: 
# Optimsing above solution using memoisation
# Also no need to dfs(prefix)

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordsSet = set(words)

        def dfs(word):
            if word in dp:
                return dp[word]
            dp[word] = False
            for i in range(1, len(word)):
                prefix = word[: i]
                suffix = word[i :]
                if prefix in wordsSet and suffix in wordsSet:
                    dp[word] = True
                    return True
                if prefix in wordsSet and dfs(suffix):
                    dp[word] = True
                    return True
                # if suffix in wordsSet and dfs(prefix):
                #     dp[word] = True
                #     return True
            return dp[word]

        dp = {}
        ans = []
        for word in words:
            if dfs(word):
                ans.append(word)
        return ans

# Java Code 
"""
import java.util.*;

class Solution {
    Set<String> wordsSet;
    Map<String, Boolean> dp;

    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        wordsSet = new HashSet<>(Arrays.asList(words));
        dp = new HashMap<>();
        List<String> ans = new ArrayList<>();

        for (String word : words) {
            if (dfs(word)) {
                ans.add(word);
            }
        }

        return ans;
    }

    private boolean dfs(String word) {
        if (dp.containsKey(word))
            return dp.get(word);
        dp.put(word, false);
        for (int i = 1; i < word.length(); i++) {
            String prefix = word.substring(0, i);
            String suffix = word.substring(i);

            if (wordsSet.contains(prefix) && wordsSet.contains(suffix)) {
                dp.put(word, true);
                return true;
            }

            if (wordsSet.contains(prefix) && dfs(suffix)) {
                dp.put(word, true);
                return true;
            }

            // if (wordsSet.contains(suffix) && dfs(prefix)) {
            //     dp.put(word, true);
            //     return true;
            // }
        }

        return dp.get(word);
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>
using namespace std;

class Solution {
    unordered_set<string> wordsSet;
    unordered_map<string, bool> dp;

public:
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        for (const string& word : words)
            wordsSet.insert(word);
        vector<string> ans;

        for (const string& word : words) {
            if (dfs(word))
                ans.push_back(word);
        }

        return ans;
    }

    bool dfs(const string& word) {
        if (dp.count(word))
            return dp[word];
        dp[word] = false;

        for (int i = 1; i < word.length(); ++i) {
            string prefix = word.substr(0, i);
            string suffix = word.substr(i);

            if (wordsSet.count(prefix) && wordsSet.count(suffix)) {
                dp[word] = true;
                return true;
            }

            if (wordsSet.count(prefix) && dfs(suffix)) {
                dp[word] = true;
                return true;
            }

            // if (wordsSet.count(suffix) && dfs(prefix)) {
            //     dp[word] = true;
            //     return true;
            // }
        }

        return dp[word];
    }
};
"""

