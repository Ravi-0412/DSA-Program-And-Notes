# we have to do in O(1) space complexity except ans array.
# logic:just calculate the prefix and postfix multiplication for each ele nd multiply both to get the ans at that index.
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