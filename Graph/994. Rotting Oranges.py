# didn't understand the Q properly. this is happening a lot 
# i understood only that orange will get rotten that will be surrounded by all four side 

# later:  i thought in totally correct way only ,how to do and what to apply like: DFS you can't apply here 
# and bfs you will have to store all the rotten oranges at once in the queue, next all adjacent rotten oranges at once and so on 
# and also you need to call BFS only once time as all the oranges that can got rotten(connected one) will be become rotten as we are pushing all the rotten oranges at once that time
# simple way: just find the oranges that can got rotten in time=1 , time=2 and so on

# here better to do in same function rather than making separate function for BFS as we have to run the function only one time

# also you can think like that : fresh oranges that are at level 1 from any of the rotten oranges will got rotten in one unit of time, 
# and oranges at level 2 will got rotten in two unit of time and so on 
# so for this bfs is better as we only have to visit each cell once if we start from all rotten oranges at once

# time: O(m*n)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col= len(grid), len(grid[0])
        q= collections.deque()
        time, fresh= 0, 0
        
        for r in range(row):
            for c in range(col):
                if grid[r][c]== 2:
                    q.append((r,c))
                if grid[r][c]== 1:
                    fresh+= 1
                   
        while q and fresh:
            time+= 1 
            # oranges that will get rotten in one unit time will depend on the no of adjacent oranges with the ele present in the Queue 
            for i in range(len(q)):  # we are poping and pushing but it this loop will run till the pre length only
                # pop one ele and make all the oranges adjacent to this ele as rotten and append that in Q for next cycle
                r1,c1= q.popleft()
                # writing all possible allowed directions i.e up,down,left,right in form of matrix
                directions= [[-1,0],[1,0],[0,-1],[0,1]]
                for dr,dc in directions:
                    r,c= r1+dr, c1+dc
                    if 0<=r<row and 0<=c<col and  grid[r][c]==1:
                        grid[r][c]= 2
                        fresh-= 1
                        q.append((r,c))

        return time if fresh==0 else -1  # if no fresh oranges is left

