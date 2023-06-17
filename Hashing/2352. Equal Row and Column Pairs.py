# time: O(n^3)
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        sameRowCount = collections.defaultdict(int)
        for r in range(n):
            sameRowCount[tuple(grid[r])] += 1
        # now check each col, how many times it is present as row.
        # that much pair we can form with this col with all those rows.
        ans = 0
        for i in range(n):
            col = []
            for j in range(n):
                col.append(grid[j][i])
            ans += sameRowCount[tuple(col)]
        return ans


# Later try by other approaches(n^2) and tries
# https://leetcode.com/problems/equal-row-and-column-pairs/solutions/2781858/C++-oror-5-or-so-different-approaches-oror-fast-(54ms-100)/
# https://leetcode.com/problems/equal-row-and-column-pairs/solutions/2324688/cubic-432-vs-three-map-95-vs-trie-137/