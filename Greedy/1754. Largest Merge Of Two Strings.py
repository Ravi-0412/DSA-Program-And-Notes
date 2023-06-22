# What we actually we have to do?
# Note: Ans: we have to combine both the words into single word which must be greater than all words formed && 
# the relative order of the characters from the same word must be preserved.

# since we have to take care of relative order also and we have to include all the characters of both the words.
# So we will take the 1st char from word which is largest and so on.

# Logic: Just compare the string s1 and s2,
# if s1 >= s2, take from s1
# if s1 < s2, take from s2

# Time O(m^2+n^2)
# Space O(m^2+n^2)

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        if not word1 or not word2:
            return word1 + word2
        if word1[0] >= word2[0]:
            return word1[0] + self.largestMerge(word1[1 :], word2)
        return word2[0] + self.largestMerge(word1, word2[1: ])


# Iterative way:
class Solution:
    def largestMerge(self, word1, word2):
        ans = ''
        while word1 and word2:
            if word1>word2:
                ans += word1[0]
                word1 = word1[1:]
            else:
                ans += word2[0]
                word2 = word2[1:]
        ans += word1
        ans += word2
        return ans



# My mistake:
# Comparing only the 1st char will give wrong ans.
# E.g: word1 = "abcabc", word2 = "abdcaba"
# It will give output = "abcabcabdcaba" but expected is : "abdcabcabcaba"
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        print(word1, word2)
        if not word1 or not word2:
            return word1 + word2
        if word1[0] >= word2[0]:
            return word1[0] + self.largestMerge(word1[1 :], word2)
        return word2[0] + self.largestMerge(word1, word2[1: ])