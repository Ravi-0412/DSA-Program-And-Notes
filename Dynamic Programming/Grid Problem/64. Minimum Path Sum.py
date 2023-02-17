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
            return path_sum
        if col==0:
            path_sum= 0
            for i in range(row,-1,-1):
                path_sum+= grid[i][0]
            return path_sum
        return grid[row][col] +  min(self.helper(row-1,col,grid), self.helper(row,col-1,grid))

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
                path_sum+= grid[0][i]   # sum of all values from curr col to col '0'.
            dp[row][col]= path_sum     # indirectly grid value  + pre_col dp value i.e dp[0][col]= grid[0][i] + dp[0][col-1]
            return dp[row][col]
        if col==0:   
            path_sum= 0
            for i in range(row,-1,-1):  # sum of all values from curr row to row '0'.
                path_sum+= grid[i][0]
            dp[row][col]= path_sum       # indirectly dp[i][0]= grid[i][0] + dp[i-1][0]
            return dp[row][col]

        if dp[row][col]!= -1:
            return dp[row][col]

        dp[row][col]= grid[row][col] +  min(self.helper(row-1,col,grid), self.helper(row,col-1,grid))
        return dp[row][col]

# Tabulation:


# writing the above recursive equation.
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n= len(grid), len(grid[0])
        return self.helper(m-1,n-1,grid)  # going from 'm-1,n-1' to '0,0'
    
    def helper(self,row,col,grid):
        # when you have reached the 0th row, then you have only one choice i.e from curr col move to 0th col by adding all the ele bw that
        if row==0 and col== 0:
            return grid[row][col]
        if col== 0: # we can only move vertically up
            return grid[row][col] +  self.helper(row-1, col, grid)
        if row == 0:
            return grid[row][col] +  self.helper(row, col-1, grid)
        return grid[row][col] +  min(self.helper(row-1,col,grid), self.helper(row,col-1,grid))
    


# my mistakes VVI:
# if row and col will go out of bound then left or right will be '0' then it will return '0' since we are returning minimum value.
# so we have to stop before reaching the invalid case.
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n= len(grid), len(grid[0])
        return self.helper(m-1,n-1,grid)
    
    
    def helper(self,row,col,grid):
        if row==0 and col== 0:
            return grid[row][col]

        left,up= 0,0
        if row >= 0 :
            up+=   grid[row][col] +   self.helper(row-1,col,grid)
        if col >= 0:
            left+= grid[row][col] +   self.helper(row,col-1,grid)
        return min(left,up)