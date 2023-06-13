# Brute Force (TLE)
class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n , q = len(nums1), len(queries)
        ans = [-1] * q
        for j, (x, y) in enumerate(queries):
            cur_max = -1
            for i in range(n):
                if nums1[i] >= x and nums2[i] >= y:
                    cur_max = max(cur_max, nums1[i] + nums2[i])
            ans[j] = cur_max
        return ans
