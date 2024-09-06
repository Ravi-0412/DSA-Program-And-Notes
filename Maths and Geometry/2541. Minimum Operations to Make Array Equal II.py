# logic:
"""
1) if k == 0 then both array must be equal i.e element at corresponding index must be same.
2) sum(nums1) = sum(nums2) because then only we can redistribute(incremement/decrement) element.
If these two condition are verified then it is sure that we can make both arrays equal.

3) Now to make each corresponding element equal , abs(abs(nums1[i] - nums2[i]) % k) == 0 
because only then we can make them equal by adding/subtracting 'k'.
Note: No of times we need to increment by 'k' must be equal to decrement operation also.
So just count ans of either increment/decrement to get the actual ans.
"""

# Note: Here we only counting answer for increment operation and directly returning at last 
# because we have checked 'sum(nums1) == sum(nums2)' so it confirms that there is possible way.

# if we won't check 'sum(nums1) == sum(nums2)' then we need to count both increment and decrement 
# operation and both these operations must be equal. we need to check this at last.
# see method 2.

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0 :
            return -1 if nums1 != nums2 else 0
        if sum(nums1) != sum(nums2):
            return -1
        n = len(nums1)
        ans = 0
        for i in range(n):
            if abs(nums1[i] - nums2[i]) % k != 0:
                return -1
            if nums2[i] >= nums1[i]:
                # counting ans for increment 
                ans += (nums2[i] - nums1[i]) // k
        return ans

# java
"""
class Solution {
    public long minOperations(int[] nums1, int[] nums2, int k) {
        if (k == 0) {
            for (int i = 0; i < nums1.length; i++) {
                if (nums1[i] != nums2[i]) {
                    return -1;
                }
            }
            return 0;
        }
        
        long sum1 = 0, sum2 = 0;
        for (int i = 0; i < nums1.length; i++) {
            sum1 += nums1[i];
            sum2 += nums2[i];
        }
        if (sum1 != sum2) {
            return -1;
        }
        
        long ans = 0;
        int n = nums1.length;
        for (int i = 0; i < n; i++) {
            if (Math.abs(nums1[i] - nums2[i]) % k != 0) {
                return -1;
            }
            if (nums2[i] >= nums1[i]) {
                ans += (nums2[i] - nums1[i]) / k;
            }
        }
        
        return ans;
    }
}
"""

# Method 2:
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:  # if k is 0, we can't perform any operations
            return 0 if nums1 == nums2 else -1  # if nums1 equals nums2, return 0; otherwise, return -1

        p_diff = 0  # stores the positive difference between nums1[i] and nums2[i]
        n_diff = 0  # stores the negative difference between nums1[i] and nums2[i]

        for i in range(len(nums1)):
            if nums1[i] >= nums2[i]:
                # check if the difference is divisible by k
                if (nums1[i] - nums2[i]) % k == 0:
                    p_diff += (nums1[i] - nums2[i]) // k
                else:
                    return -1
            else:
                # check if the difference is divisible by k
                if (nums2[i] - nums1[i]) % k == 0:
                    n_diff += (nums2[i] - nums1[i]) // k
                else:
                    return -1

        # if both positive and negative differences are equal, we can make nums1 equal to nums2
        return p_diff if p_diff == n_diff else -1
