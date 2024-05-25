# logic: just check which substring starting from start is present in 'dict, 
# if it is present in dict then check for remaining string recursively and keep adding that to ans.

# Time Complexity: O(2^n). Because there are 2^n combinations in worst case i.e when every char is present in the dictionary
# in this case for every char we will have two options either to chose that char or not
# space: O(n) recursive depth + O(n) for storing ans= O(n)

# Cross Q / follow up 
# NOte vvvi: "the same word in the dictionary may be reused multiple times in the segmentation.".
# Due to this only we are able to check if cur substring of 's[i: j+ 1]' matches with any word in 'dict'.
# If same word of dict is not allowed mutiple times then, we will have to take visited set for dict words(index will work)
# to check whether the word at that index is already used or not.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        dictSet = set(wordDict)
        ans = []

        def backtrack(i, sent):
            if i == n:
                ans.append(" ".join(sent))
                return
            for j in range(i, n):
                if s[i: j + 1] in dictSet:
                    backtrack(j + 1, sent + [s[i: j + 1]])
        backtrack(0, [])
        return ans

# Similar Questions:
# 1) "139. Word Break"

