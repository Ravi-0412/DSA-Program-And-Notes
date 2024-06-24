# Method using sortedList in python

from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        subArr = SortedList()
        i, j = 0, 0
        ans = 0
        while j < n:
            subArr.add(nums[j])
            while subArr[-1] - subArr[0] > limit:
                subArr.remove(nums[i])
                i += 1
            ans = max(ans, j - i + 1)
            j += 1
        return ans


# Method 2: Using Two heaps i.e minHeap and maxHeap.
# time: O(n* logk)
"""
from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        subArr = SortedList()
        i, j = 0, 0
        ans = 0
        while j < n:
            subArr.add(nums[j])
            while subArr[-1] - subArr[0] > limit:
                subArr.remove(nums[i])
                i += 1
            ans = max(ans, j - i + 1)
            j += 1
        return ans
"""


# Method 3: Try by Queue later
# Time: O(n)