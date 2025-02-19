class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(1, n):
            # Agar adjacent dono odd ya dono even h
            if (nums[i] % 2 == 1 and nums[i -1] % 2 == 1) or (nums[i] % 2 ==0 and nums[i -1] % 2 == 0):
                return False
        return True

# Better and concise way to write above code
# Logic: compare two consecutive element's parity, which we can do by taking their mods with 2.
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)) :
            if nums[i - 1] % 2 == nums[i] % 2 :
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
# Method 2: Using Bit Manipulation
# Logic: 
"""
By performing (element & 1), we can determine the parity of the number, 
we also know that bitwise xor of same numbers is 0 so 
we can simply return false if the xor of any two consecutive numbers' parity is 0.

"""

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)) :
            if (nums[i - 1] & 1) ^ (nums[i] & 1) == 0:
                return False

        return True

# Java
"""
class Solution {
    public boolean isArraySpecial(int[] nums) {
        for(int i = 1; i < nums.length; ++i) {
            if(((nums[i - 1] & 1) ^ (nums[i] & 1)) == 0) {
                return false;
            }
        }

        return true;
    }
}
"""
