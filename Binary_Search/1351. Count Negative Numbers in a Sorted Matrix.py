# logic: "just we have to find the no of ele smaller than 0 in each row using binary search"

# time: O(m + n)

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans= 0
        m, n = len(grid), len(grid[0])
        j= n- 1
        for i in range(m):
            while j >= 0 and grid[i][j] < 0:
                j -= 1
            ans += n- 1 -j   # this much no of ele is < 0 in 'i'th row.
        return ans