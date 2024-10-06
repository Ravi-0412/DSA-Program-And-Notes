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

        

# Optimsing above solution using memoisation
# Also no need to dfs(prefix) => 3rd call

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

# Java: Dp
"""
import java.util.*;

public class Solution {
    // Set to store the words for quick lookup
    private Set<String> wordsSet;
    // Map to store already computed results for words
    private Map<String, Boolean> dp;

    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        // Initialize the set with all words
        wordsSet = new HashSet<>(Arrays.asList(words));
        // Initialize the dp map
        dp = new HashMap<>();
        // List to store the result of concatenated words
        List<String> ans = new ArrayList<>();

        // Iterate over each word
        for (String word : words) {
            if (dfs(word)) { // Call dfs to check if the word can be formed by concatenation
                ans.add(word); // If true, add the word to the result
            }
        }

        return ans;
    }

    // DFS function to check if a word can be formed by concatenating other words
    private boolean dfs(String word) {
        // If the word's result is already computed, return it
        if (dp.containsKey(word)) {
            return dp.get(word);
        }

        // Initialize the word in dp as false (assuming not concatenated)
        dp.put(word, false);

        // Try breaking the word at different points
        for (int i = 1; i < word.length(); i++) {
            String prefix = word.substring(0, i);
            String suffix = word.substring(i);

            // If both prefix and suffix are in the set, or prefix is in the set and suffix can be formed by concatenation
            if (wordsSet.contains(prefix) && (wordsSet.contains(suffix) || dfs(suffix))) {
                dp.put(word, true); // Mark the word as true (it can be concatenated)
                return true;
            }
        }

        return dp.get(word); // Return the result stored in dp
    }
}
"""

# Try using trie
