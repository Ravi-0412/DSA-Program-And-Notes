# method 1: Recursion
# just same as Q n: '62' 
# cur cell ka value add  karo do iske adjacent ke minimum find karke.

# writing the above recursive equation. Can memoise this further.

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
# if row and col will go out of bound then left or up will be '0' then it will return '0' since we are returning minimum value.

# say you are at (0, 3) , from here you can go left and but can't go up.
# for from left , you will get : sum from index '3 to 0' in row '0'
# And from up you will get '0'.
# Now since it is returning minimum , it will return '0' instead of sum from index '3 to 0' in row '0'.

# That's why we have to stop before reaching the invalid case. SO did like above one
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n= len(grid), len(grid[0])
        return self.helper(m-1,n-1,grid)  # going from 'm-1,n-1' to '0,0'
    
    def helper(self,row,col,grid):
        # when you have reached the 0th row, then you have only one choice i.e from curr col move to 0th col by adding all the ele bw that
        if row==0 and col== 0:
            return grid[row][col]
        if row < 0 or col < 0:
            return 0
        return grid[row][col] +  min(self.helper(row-1,col,grid), self.helper(row,col-1,grid))