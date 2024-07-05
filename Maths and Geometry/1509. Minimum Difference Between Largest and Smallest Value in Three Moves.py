# Logic: If we can do 0 move, return max(A) - min(A)
# If we can do 1 move, return min(the second max(A) - min(A), the max(A) - second min(A)) & so on.

# So we need to consider all possibility like:
# i) remove 3 smallest number
# ii) 2 smallest and 1 largest
# iii) 1 smallest and 2 largest
# iv) 0 smallest and 3 largest

# Ans = min(all_four_possibility)

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:   # in case n == 4 make all element = any one ele so ans = 0
            return 0
        nums.sort()
        return min(nums[n -1] - nums[3], nums[n - 2] - nums[2], nums[n - 3] - nums[1], nums[n - 4] - nums[0])

# Java
"""
class Solution {
    public int minDifference(int[] nums) {
        int n = nums.length;
        if (n <= 4) {
            return 0;
        }
        Arrays.sort(nums);
        return Math.min(
            Math.min(nums[n - 1] - nums[3], nums[n - 2] - nums[2]),
            Math.min(nums[n - 3] - nums[1], nums[n - 4] - nums[0])
        );
    }
}
"""