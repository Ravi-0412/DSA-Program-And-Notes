# The intuition behind the approach is to iterate over the arrays nums1 and nums2 simultaneously
# and track the lengths of the non-decreasing subsequences that can be formed by merging the 
# elements of the two arrays.

# Time : O(n) = space

class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        ans = 1
        pre1 , pre2 = 1 , 1
        for i in range(1, n):
            cur1, cur2 = 1, 1
            # we can take the cur number from nums1
            if nums1[i] >= nums1[i - 1]:
                cur1 = max(cur1 , pre1 + 1)
            if nums1[i] >= nums2[i - 1]:
                cur1= max(cur1, pre2 + 1)
            # we can take the cur number from nums2
            if nums2[i] >= nums2[i - 1]:
                cur2 = max(cur2, pre2 + 1)
            if nums2[i] >= nums1[i - 1]:
                cur2= max(cur2, pre1 + 1)
            ans = max(ans , max(cur1, cur2))
            pre1, pre2 = cur1, cur2
        return ans


# Method 2

# Note vvi: To get the actual array also (must do for cross Q).
# Understand in depth and do properly by this approach.
# https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/solutions/3738995/explained-sliding-window-very-simple-and-easy-to-understand-solution/

# Also ready rely by "codshashank_1" on comment by "cpcdevar" in above solution.