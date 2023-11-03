# Method 1: Brute force
# For each pair of row and col, check all elements.

# Time: O(n^3)


# Method 2: 

# time: O(n^2)
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        sameRowCount = collections.defaultdict(int)
        for r in range(n):
            sameRowCount[tuple(grid[r])] += 1
        # now check each col, how many times it is present as row.
        # that much pair we can form with this col with all those rows.
        ans = 0
        for c in range(n):
            col = []
            for r in range(n):
                col.append(grid[r][c])
            ans += sameRowCount[tuple(col)]
        return ans

