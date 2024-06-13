# Logic: Just apply binary search in range [1, max(nums)] and check 
# if it is possible to divide 'nums' having maximum value as 'num' in 'maxOperations' ?

# How to check this?
# if 'nums[i]' is > 'num' then means we have to divide 'nums[i]' 
# and no of operations required to divide will be equal to : ceil(nums[i] / num) - 1
# '-1' because for getting 'n+1' numbers from a single number we need 'n' operations.

# Time : O(n *log(max(nums)))

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        # is it possible to divide 'nums' having maximum value as 'num' in 'maxOperations' ?
        def isPossible(num):
            operation = 0
            for i in range(len(nums)):
                if nums[i] > num:
                    operation += ceil(nums[i] / num) - 1
            return operation <= maxOperations

        start , end = 1, max(nums)   # maximum value we can get = max(nums)
        while start < end:
            mid = start + (end - start) // 2
            if isPossible(mid):
                end  = mid
            else:
                start = mid + 1
        return start