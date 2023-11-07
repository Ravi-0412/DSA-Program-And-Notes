# Brute force:
# Just calculate the 'prefix' and 'suffix' multiplication then, 
# ans[i] = prefix[i - 1] * suffix[i + 1]

# Method 2: 
# Optimising space

# we have to do in O(1) space complexity except ans array.
# means we will have to store prefix and suffix into a variable instead of array.

# 1) Traverse from left to right and store the 'prefix' for each ele.
# 2) for 'suffix' traverse right to left.
# time: O(n),space: O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans= [1]*(len(nums))
        # first storing the prefix mutliply for each number in 'ans'
        prefix= 1
        for i in range(len(nums)):
            ans[i]= prefix
            prefix= prefix* nums[i]
        # now calculate the postfix and store the final ans in the 'ans'.
        postfix= 1
        for i in range(len(nums) -1, -1, -1):
            ans[i]= ans[i] * postfix   # ans[i] store the prefix for that index.
            postfix= postfix * nums[i]
        return ans


# observation:
# 1) if count of '0' will be = 1 then all elements will have value= 0 excecpt the '0'th ele.
# 2) if count of '0' >= 2 then value= 0 for all elements.