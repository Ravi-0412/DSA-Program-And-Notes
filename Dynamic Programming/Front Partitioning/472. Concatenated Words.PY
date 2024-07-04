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
                    return True
                if suffix in d and dfs(prefix):
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

# Try using trie
