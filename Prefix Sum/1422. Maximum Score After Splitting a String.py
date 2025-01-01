# Time = space = O(n)

class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        prefixZeroCount = [0]*(n + 1)  # prefixZeroCount[i]: Number of zero till index 'i-1' starting from index '0'.
        suffixOneCount = [0]*(n + 1)   # suffixOneCount[i] : Number of one till index 'i' starting from last.
        for i in range(n):
            if s[i] == "0":
                prefixZeroCount[i + 1] = prefixZeroCount[i] + 1
            else:
                prefixZeroCount[i + 1] = prefixZeroCount[i]
            if s[n - i -1] == "1":
                suffixOneCount[n-i-1] = suffixOneCount[n - i] + 1
            else:
                suffixOneCount[n-i- 1] = suffixOneCount[n - i]
        ans = 0
        for i in range(n - 1):
          # Number of 'zero' till 'i' and number of one till 'i+1'.
            ans = max(ans, prefixZeroCount[i + 1] + suffixOneCount[i + 1]) 
        return ans
            
# Method : Space optimised and in single pass
# time = O(n)
# Space = O(1)

# Logic:
"""
Logic behind this -
Result = Max of (ZerosOnLeft + OnesOnRight)
= Max of (ZerosOnLeft + (TotalOnes - OnesOnLeft))
= Max of (ZerosOnLeft - OnesOnLeft) + TotalOnes (as TotalOnes is constant)
"""

class Solution:
    def maxScore(self, s: str) -> int:
        zeros, ones, max_score = 0, 0, float('-inf')
    
        for i, char in enumerate(s):
            if char == '0':
                zeros += 1
            else:
                ones += 1
            if i != len(s) - 1:
                max_score = max(zeros - ones, max_score)
        
        return max_score + ones
