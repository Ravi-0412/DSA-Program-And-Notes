# Note vvi: What actually we need to find?
# Ans: Minimum number (when subsequence is combined as a single number) of length 'k'. 

# And minimum number we will get when number will be in increasing order if number of ele from minimum ele >= k.

# logic: Suppose min ele of num is at index 'i' and there is >= k there from index 'i'.
# then we simply need to return all ele from 'i' to 'n-1'.

# Generalising the above logic:
# if we start from minimum ele then search for just next greater than this then next greater than previously added & so on.
# Then we will get our ans because we have to find the minimum number of len 'k'.

# vvvi: This means we need to maintain a incraesing order stack.

# Note: But in doing this process we might left with ele < k at last.
# So we will only pop if we will if "sum of ele after poping + remaining ele left to traverse including the current one" >= k.

# But we will only add ele in stack if len(stack) will be < k.

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for i, num in enumerate(nums):
            # if cur ele is greater than the last ele of stack then we need to pop to make the number smaller 
            # But before poping we need to check if "sum of ele after poping + remaining ele left to traverse including the current one" >= k.
            while stack and stack[-1] > num and (len(stack) -1 ) + (len(nums) - i) >= k:
                stack.pop()
            # only add ele in stack if len(stack) will be < k.
            if len(stack) < k:
                stack.append(num)
        return stack

# Method 2:
# Can do by other method as we did in "402. Remove K Digits".
