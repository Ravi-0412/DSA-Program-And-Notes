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
