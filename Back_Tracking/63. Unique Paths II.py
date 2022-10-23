# same as Q no '62'. only difference if it reaches the last row or last col 
# then whether to return '0' or '1' will depend on the pre cell of row and col respectively if obstacle is not present at that cell
# according to this we have to initialise in tabulation

# method 1: recursive way
# giving TLE but correct only
# better and concise one
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]== 1:   # if there is obstacle at destination
            return 0
        return self.helper(0,0,obstacleGrid)
    
    def helper(self,r,c,grid):
        if r>=len(grid) or c>=len(grid[0]): # if go out of grid dimension, simply return 0
            return 0
        if r== len(grid)-1 and c== len(grid[0])-1 :  #if reaches the end point 
            return 1
        if grid[r][c]== 1:  # if obstacle at that cell then simply return 
            return 0
        return self.helper(r+1,c,grid) + self.helper(r,c+1,grid)


# another way of writing the above code
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.Paths("", obstacleGrid, 0, 0)  # starting from 0,0 to reach the bottom most cell
    def Paths(self,ans, maze, row, col):
        count=0
        if row== len(maze)-1 and col== len(maze[0])-1:  # corner most will be only the base condition in this case
            if maze[row][col]== 1:  # means obstacles so simply return
                return 0
            else:
                print(ans)
                return 1
        if maze[row][col]== 1:  # means obstacles so simply return
            return 0
        if row< len(maze)-1:  # then only you can go down
            count+= Solution().Paths(ans+ 'D', maze, row+1, col)
        if col< len(maze[0])-1:  # then only you can go right
            count+= Solution().Paths(ans+ 'R', maze, row, col+1)
        return count


# method 2: memoization(method 1 )
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]== 1:   # if there is obstacle at destination
            return 0
        m,n= len(obstacleGrid), len(obstacleGrid[0])
        dp= [[-1 for j in range(n)] for i in range(m)]
        return self.helper(0,0,obstacleGrid,dp)
    
    def helper(self,r,c,grid,dp):
        if r>= len(grid) or c>= len(grid[0]):
            return 0
        if r== len(grid)-1 and c== len(grid[0])-1 :  #if reaches the end point 
            return 1
        if grid[r][c]== 1:  # if obstacle at that cell then simply return 
            return 0       
        if dp[r][c]!= -1:
            return dp[r][c]
        dp[r][c]= self.helper(r+1,c,grid,dp) + self.helper(r,c+1,grid,dp)
        return dp[r][c]

# tabulation 
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n= len(obstacleGrid), len(obstacleGrid[0])
        dp= [[0 for j in range(n)] for i in range(m)]
        # initialise with proper base cases
        
        # going from (m-1,n-1) to (0,0) so we have to check at (0,0)
        if obstacleGrid[0][0]!= 1:
            dp[0][0]= 1
        # initialisng the 1st row. after reaching the 1st row, paths will depend on the pre row cell( dp[0][i-1]) if no obstacle at that cell
        for i in range(1,n):
            if obstacleGrid[0][i]!= 1:
                dp[0][i]= dp[0][i-1]
        # initialisng the 1st col. after reaching the 1st col, paths will depend on the pre col cell( dp[i-1][0]) if no obstacle at that cell
        for i in range(1,m):
            if obstacleGrid[i][0]!= 1:
                dp[i][0]= dp[i-1][0]
           
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]!= 1:  # if not obstacle
                    dp[i][j]= dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]






