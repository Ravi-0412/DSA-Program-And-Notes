# Logic: 
"""
Answer will be equal to make all element in strictly increasing order.
for this sort the array & try to make next element = prev + 1.
we need moves = (pre - nums[i]) + 1 to make current(nums[i]) one greater than prev.
"""
# 

# Time: O(n*logn)

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        pre = nums[0]
        ans = 0
        for i in range(1, len(nums)):
            moves = 0
            if nums[i] <= pre:
                moves = (pre - nums[i]) + 1
                ans +=  moves
            pre = nums[i] + moves
        return ans
    
# Note: Later try by other approaches in sheet.