# method1: correct only but since brute force so will give
# time exceeded for larger inputs
# page: 17
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.Paths("", obstacleGrid, 0, 0)  # starting from 0,0 to reach the bottom most cell
    def Paths(self,ans, maze, row, col):
        count=0
        if row== len(maze)-1 and col== len(maze[0])-1:  # corner most will be only the base condition in this case
            if maze[row][col]== 1: # you have to check inside also for obstacles
                                   # as the destination can also have obstacles so no path will be possible there
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

# memoization
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
            
        if r<= len(grid)-1 and c<= len(grid[0])-1 and dp[r][c]!= -1:
            return dp[r][c]
        down,right= 0,0
        if r<= len(grid)-1:
            down+= self.helper(r+1,c,grid,dp)
        if c<= len(grid[0])-1:
            right+= self.helper(r,c+1,grid,dp)
        dp[r][c]= down + right
        return dp[r][c]
        

# other way of writing memoization
# Note:write always like this only(False condition + out of bound cases all together and bases cases first)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]== 1:   # if there is obstacle at destination
            return 0
        m,n= len(obstacleGrid), len(obstacleGrid[0])
        dp= [[-1 for j in range(n)] for i in range(m)]
        return self.helper(0,0,obstacleGrid,dp)
    
    def helper(self,r,c,grid,dp):
        if r>= len(grid) or c>= len(grid[0]) or grid[r][c]==1:  # write all the false cases together like we used to do in graph
                                                                # this help you to avoid a lot of checking condition further
            return 0
        if r== len(grid)-1 and c== len(grid[0])-1 :  #if reaches the end point 
            return 1
        if dp[r][c]!= -1:
            return dp[r][c]
        dp[r][c]= self.helper(r+1,c,grid,dp) + self.helper(r,c+1,grid,dp)
        return dp[r][c]

# tabulation: Bottom up
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n= len(obstacleGrid), len(obstacleGrid[0])
        dp= [[0 for j in range(n)] for i in range(m)]
        # initialise with proper base cases
        # first we have to check at (0,0) then only we can initialise the base case further
        if obstacleGrid[0][0]!= 1:
            dp[0][0]= 1
        # initialisng the 1st row. after reaching the 1st row, paths will depend on the value of curr row(0th) and pre col val ( dp[0][i-1]) if no obstacle at that cell
        for i in range(1,n):
            if obstacleGrid[0][i]!= 1:
                dp[0][i]= dp[0][i-1]
        # initialisng the 1st col. after reaching the 1st col, paths will depend on the curr col(0th) and pre row val( dp[i-1][0]) if no obstacle at that cell
        for i in range(1,m):
            if obstacleGrid[i][0]!= 1:
                dp[i][0]= dp[i-1][0]
           
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]!= 1:  # if not obstacle
                    dp[i][j]= dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


# optimising space complexity to O(n)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n= len(obstacleGrid), len(obstacleGrid[0])
        pre= [0 for i in range(n)]
        # initialise with proper base cases
        # first we have to check at (0,0) then only we can initialise the base case further
        if obstacleGrid[0][0]!= 1:
            pre[0]= 1
            
        # initialisng the 1st row. after reaching the 1st row, paths will depend on the value of curr row(0th) and pre col val ( dp[0][i-1]) if no obstacle at that cell
        for i in range(1,n):
            if obstacleGrid[0][i]!= 1:
                pre[i]= [i-1]
        
        # calculate the value of remaining row one by one
        for i in range(1,m):
            curr= [0 for i in range(n)]
            for j in range(n):
                if obstacleGrid[i][j]!= 1:  # if not obstacle
                    curr[j]= pre[j] + curr[j-1]  if j>=1 else pre[j]
            pre= curr.copy()
        return pre[n-1]