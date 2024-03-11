# Logic: Given both ararys sorted in increasing order.
# So apply two pointer and if equal then return ans because that will be the smallest one only.
# else incr pointer of array whose value is small to find more bigger element for comparison.

# Time: O(m+ n)

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i , j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            if nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return -1
        