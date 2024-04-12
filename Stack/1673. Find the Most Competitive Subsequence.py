# Note vvi: What actually we need to find?
# Ans: Minimum number (when subsequence is combined as a single number) of length 'k'. 

# And minimum number we will get when number will be in increasing order if number of ele from minimum ele >= k.

# logic: Suppose min ele of nums is at index 'i' and there is >= k no of element from index 'i'.
# then we simply need to return 'k' ele starting from 'i'.

# vvvi: for this we need to maintain a increasing order stack of len(k).

# VVi:if you see smaller number , keep on poping until you find find any ele <= num.
# Note: But in doing this process we might left with ele < k at last.
# So we will only pop if "sum of ele in stack + remaining ele left to traverse including the current one" > k.

# But we will only add ele in stack if len(stack) will be < k.

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for i, num in enumerate(nums):
            
            # But before poping we need to check if "sum of ele in stack + remaining ele left to traverse including the current one" > k
            while stack and stack[-1] > num and (len(stack)  + (len(nums) - i)) > k:
                stack.pop()
            # only add ele in stack if len(stack) will be < k.
            if len(stack) < k:
                stack.append(num)
        return stack

# Note vvi: When you have to find smallest / greatest ele i..e number in ascending or descending order use stack.
# use stack .

# Related Q:
# 1) 402. Remove K Digits



