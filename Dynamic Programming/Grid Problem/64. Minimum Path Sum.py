# method 1: Recursion
# just same as Q n: '62' 
# just add the value of the cell you are currently present while calling for the next function
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n= len(grid), len(grid[0])
        return self.helper(m-1,n-1,grid)  # going from 'm-1,n-1' to '0,0'
    
    def helper(self,row,col,grid):
        # when you have reached the 0th row, then you have only one choice i.e from curr col move to 0th col by adding all the ele bw that
        if row==0:
            path_sum= 0
            for i in range(col,-1,-1):
                path_sum+= grid[0][i]
            print(path_sum)
            return path_sum
        # same logic as row
        if col==0:
            path_sum= 0
            for i in range(row,-1,-1):
                path_sum+= grid[i][0]
            print(path_sum)
            return path_sum
        left,up= 0,0
        up+=   grid[row][col] +   self.helper(row-1,col,grid)
        left+= grid[row][col] +   self.helper(row,col-1,grid)
        return min(left,up)

# memoization
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n= len(grid), len(grid[0])
        dp= [[-1 for j in range(n)]for i in range(m)]
        return self.helper(m-1,n-1,grid,dp)
    
    
    def helper(self,row,col,grid,dp):
        if row==0:
            path_sum= 0
            for i in range(col,-1,-1):
                path_sum+= grid[0][i]
            dp[row][col]= path_sum
            return dp[row][col]
        if col==0:
            path_sum= 0
            for i in range(row,-1,-1):
                path_sum+= grid[i][0]
            dp[row][col]= path_sum
            return dp[row][col]
        if dp[row][col]!= -1:
            return dp[row][col]
        left,up= 0,0
        up+=   grid[row][col] +   self.helper(row-1,col,grid,dp)
        left+= grid[row][col] +   self.helper(row,col-1,grid,dp)
        dp[row][col]= min(left,up)
        return dp[row][col]

# same way we you can optimise space like pre Q: 62,63
