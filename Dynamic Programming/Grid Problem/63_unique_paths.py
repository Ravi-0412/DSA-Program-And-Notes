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


# By memoization
# Don't know why it's not working
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n= len(obstacleGrid) -1, len(obstacleGrid[0]) -1
        dp= [[-1 for j in range(n)] for i in range(m)]
        dp[0][0]= 1 if obstacleGrid[0][0]== 0 else 0
        return self.Paths(obstacleGrid, m-1, n-1, dp)  # we are starting from bottom-right(m-1, n-1) and trying to reach the starting grid(0,0)
        
    def Paths(self, maze, m, n, dp):
        # if n==0 and m==0:  # since we are starting from m-1 and n-1 so this means we are in the destination row or destination col 
        #     if maze[m][n]==1:  # and there will be only one path to reach 0,0 after this either yougo left only or up on
        #         dp[m][n]
        











            ``
                        dp[i][j] += dp[i-1][j]
                    if j >0:
                        dp[i][j] += dp[i][j-1]
        return dp[-1][-1]

