# just same logic as number of island 

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col= len(grid), len(grid[0])
        visited= set()
        island= 0
        maxArea= [0]  # since variable we can't change in insider function so storing in list
        
        # if you write function inside a function then you can't acess the immutable objects, you can only acess the mutable objects of the main function
        def BFS(r,c):
            Q= collections.deque()
            Q.append((r,c))
            count= 0
            while Q:
                r1,c1= Q.popleft()
                count+= 1
                maxArea[0]= max(maxArea[0],count)
                # writing all possible allowed directions i.e up,down,left,right in form of matrix
                directions= [[-1,0],[1,0],[0,-1],[0,1]]
                for dr,dc in directions:
                    r,c= r1+dr, c1+dc
                    if 0<=r<row and 0<=c<col and  grid[r][c]==1 and (r,c) not in visited:
                        visited.add((r,c))
                        Q.append((r,c))
                        
        # code starts from here
        for r in range(row):
            for c in range(col):
                if grid[r][c]== 1 and (r,c) not in visited:
                    island+= 1
                    visited.add((r,c))
                    BFS(r,c)
        return maxArea[0]