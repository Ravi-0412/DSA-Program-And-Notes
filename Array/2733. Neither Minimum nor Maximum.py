# Note: All numbers are distinct that's why this all methods are working.

# logic: just sort and return the 2nd ele i.e nums[1]. 
# Can return any no except minimum and maximum.
# time: O(n*logn)
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        nums.sort()
        return nums[1]


# method 2:
# logic: find min and max and traverse array and if that is neither max or minimum.
# Note: this will work in case of duplicates also.

# time: O(n)
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        mn, mx= min(nums), max(nums)
        for num in nums:
            if num != mn and num != mx:
                return num

# Method 3: Better one
# Logic: If we take any three number then out of that one will be our ans.
# But how to make sure which can be our ans?
# Ans: Middle ele will be our ans because other elements can be minimum or maximum.

# for getting middle ele , just sort any three ele and return nums[1].
# time: O(3*log3)
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        return sorted(nums[: 3])[1]

# java
"""
class Solution {
    public int findNonMinOrMax(int[] nums) {
        // Check if the array has fewer than 3 elements
        if (nums.length < 3) {
            return -1;
        }

        // Extract the first three elements
        int a = nums[0];
        int b = nums[1];
        int c = nums[2];

        // Find and return the middle value
        if ((a > b && a < c) || (a < b && a > c)) {
            return a;
        } else if ((b > a && b < c) || (b < a && b > c)) {
            return b;
        } else {
            return c;
        }
    }
}
"""
    
# method 4: optimising method '2' using logic of method '3'.
# we only need to do the above for 1st three ele.

# time: O(3)
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        mn, mx= min(nums[:3]), max(nums[:3])
        for num in nums[:3]:
            if num != mn and num != mx:
                return num

