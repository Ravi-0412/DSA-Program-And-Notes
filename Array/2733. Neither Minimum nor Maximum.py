# Note: All numbers are distinct that's why this all methods are working.

# logic: just sort and return the 2nd ele i.e nums[1]
# time: O(n*logn)
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <=2:
            return -1
        nums.sort()
        return nums[1]

# Method 2: 
# logic: No need to sort all, we only need to sort first three and return 2nd one i.e nums[1]
# time: O(3*log3)
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <=2:
            return -1
        return sorted(nums[: 3])[1]
    

# method 3:
# logic: find min and max and traverse array and if that is neither max or minimum.
# Note: this will work in case of duplicates also.

# time: O(n)
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <=2:
            return -1
        mn, mx= min(nums), max(nums)
        for num in nums:
            if num != mn and num != mx:
                return num

# method 4: optimising method '3'.
# we only need to do the above for 1st three ele.

# time: O(3)
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <=2:
            return -1
        mn, mx= min(nums[:3]), max(nums[:3])
        for num in nums[:3]:
            if num != mn and num != mx:
                return num
    