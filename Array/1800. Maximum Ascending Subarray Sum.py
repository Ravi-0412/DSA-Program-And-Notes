# Time : O(n), space: O(1)

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr = ans = nums[0]
        for i in range(1, len(nums)):
            curr = curr + nums[i] if nums[i] > nums[i-1] else nums[i]
            ans = max(ans, curr)
        return ans

# Java
"""
class Solution {
    public int maxAscendingSum(int[] nums) {
        int curr = nums[0], ans = nums[0];
        for (int i = 1; i < nums.length; i++) {
            curr = nums[i] > nums[i - 1] ? curr + nums[i] : nums[i];
            ans = Math.max(ans, curr);
        }
        return ans;
    }
}
"""
