class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(1, n):
            # Agar adjacent dono odd ya dono even h
            if (nums[i] % 2 == 1 and nums[i -1] % 2 == 1) or (nums[i] % 2 ==0 and nums[i -1] % 2 == 0):
                return False
        return True

# Java
"""
import java.util.List;

class Solution {
    public boolean isArraySpecial(List<Integer> nums) {
        int n = nums.size();
        for (int i = 1; i < n; i++) {
            // If two adjacent numbers are both odd or both even
            if ((nums.get(i) % 2 == 1 && nums.get(i - 1) % 2 == 1) || 
                (nums.get(i) % 2 == 0 && nums.get(i - 1) % 2 == 0)) {
                return false;
            }
        }
        return true;
    }
}

"""
