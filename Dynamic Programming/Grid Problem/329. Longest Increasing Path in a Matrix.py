# mistakes: was doing correct only but was missing out of order cases of row and col(<0)

# here no need to mark cell visited as it will only take the increasing one only,
# so no chance of loop or viisting the same call again insam efunction call.
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ans= 1  # each grid will contibute so automatically it will be '1'.
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                ans= max(ans, self.dfs(r, c,-1, matrix))
        return ans

    def dfs(self, r, c, pre, mat):
        count, ans= 0, 1
        directions= [[-1, 0], [1, 0], [0, -1], [0, 1]]  # up, down, left, right
        for dr, dc in directions:
            row, col= r + dr, c+ dc
            # if out of order then simply skip.
            if row< 0 or row>= len(mat) or col< 0 or col >= len(mat[0]) or mat[row][col] <= mat[r][c]:  
                continue        
            # count+= 1 + self.dfs(row, col, mat[row][col], mat)   # it adding the pre count values also that wh getting error
            count= 1 + self.dfs(row, col, mat[row][col], mat)     # incr count by 1 and call the valid function
            ans= max(ans, count)
        return ans

# memoisation
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ans= 1  # each grid will contibute so automatically it will be '1'.
        dp= [[-1 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                ans= max(ans, self.dfs(r, c,-1, matrix, dp))
        return ans

    def dfs(self, r, c, pre, mat, dp):
        if dp[r][c]!= -1:
            return dp[r][c]
        count, ans= 0, 1
        directions= [[-1, 0], [1, 0], [0, -1], [0, 1]]  # up, down, left, right
        for dr, dc in directions:
            row, col= r + dr, c+ dc
            # if out of order then simply skip.
            if row< 0 or row>= len(mat) or col< 0 or col >= len(mat[0]) or mat[row][col] <= mat[r][c]:  
                continue        
            count= 1 + self.dfs(row, col, mat[row][col], mat, dp)
            ans= max(ans, count)
        dp[r][c]= ans
        return dp[r][c]


# we can also use bfs.

# top down approach will be very tough.