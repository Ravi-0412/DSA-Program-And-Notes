# mistakes: was doing correct only but was missing out of order cases of row and col(<0)

# here no need to mark cell visited as it will only take the increasing one only,
# so no chance of loop or viisting the same call again insam efunction call.

# time: O(m * n * 4 ^ (m * n))
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ans= 1  # each grid will contibute so automatically it will be '1'.
        # checking ans from every cell.
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                ans= max(ans, self.dfs(r, c,-1, matrix))   # taking '-1' as pre: smaller value than all the possible values in the matrix
        return ans
    def dfs(self, r, c, pre, mat):
        # if out of order then simply return '0'.
        if r< 0 or r >= len(mat) or c< 0 or c >= len(mat[0]) or mat[r][c] <= pre:
            return 0
        count, ans= 0, 1
        directions= [[-1, 0], [1, 0], [0, -1], [0, 1]]  # up, down, left, right
        for dr, dc in directions:
            row, col= r + dr, c+ dc        
            # count+= 1 + self.dfs(row, col, mat[row][col], mat)   # it adding the pre count values also that why getting error
            count= 1 + self.dfs(row, col, mat[r][c], mat)     # incr count by 1 and call the next function.
            ans= max(ans, count)
        return ans

# memoisation
# time complexity = O(m * n)  (average)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ans= 1  # each grid will contibute so automatically it will be '1'.
        dp= [[-1 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        # checking ans from every cell.
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                ans= max(ans, self.dfs(r, c,-1, matrix, dp))   # taking '-1' as pre: smaller value than all the possible values in the matrix
        return ans
    def dfs(self, r, c, pre, mat, dp):
        # if out of order then simply return '0'.
        if r< 0 or r >= len(mat) or c< 0 or c >= len(mat[0]) or mat[r][c] <= pre:
            return 0
        if dp[r][c]!= -1:
            return dp[r][c]
        count, ans= 0, 1
        directions= [[-1, 0], [1, 0], [0, -1], [0, 1]]  # up, down, left, right
        for dr, dc in directions:
            row, col= r + dr, c+ dc        
            # count+= 1 + self.dfs(row, col, mat[row][col], mat)   # it adding the pre count values also that why getting error
            count= 1 + self.dfs(row, col, mat[r][c], mat, dp)     # incr count by 1 and call the next function.
            ans= max(ans, count)   # max of all four directions
        dp[r][c]= ans
        return dp[r][c]



# we can also use bfs.

# top down approach will be very tough.