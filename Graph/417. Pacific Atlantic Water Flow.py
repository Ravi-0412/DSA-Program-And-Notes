# Q meaning: you have to return all that grid in a 2D matrix from which water can flow to both pacific and atlantic ocean
# we are going reverse i.e from ocean to the cells
# so curr height of cell should be gretaer than the preHeight of the cell
# logic: find the cell that can reach the pacific and atlantic respectively and 
# at last find the cell that can reach both and add them into the ans

# very better logic as we are going from ocean to the cell then for next adjacent node, 
# we will have to check with height of preCell only, if height greater than preCell then the curr cell and also reach the respective ocean
# exactly  same as "No of island", only change in height checking condition

# time: O(m*n), space: O(m*n)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col= len(heights), len(heights[0])
        pac, atl= set(),set()
        ans= []
        
        def DFS(r,c,visited,preHeight):
            if r<0 or r>=row or c<0 or c>=col or (r,c) in visited or heights[r][c] < preHeight:
                return
            # now means this cell can reach the ocean so add in the visited 
            visited.add((r,c))
            directions= [[-1,0],[1,0],[0,-1],[0,1]]    # up,down,left,right
            for dr,dc in directions:
                r1,c1= r+dr, c+dc
                DFS(r1,c1,visited,heights[r][c])
        
        # code starts from here
        # cells that are in the 1st and last row can reach the pacific and atlantic respectively
        for c in range(col):
            DFS(0, c, pac, heights[0][c])  # 1st row. since equal distance is also allowed so passed the height of 1st cell as preHeight
            DFS(row-1, c, atl,heights[row-1][c])  # last row
            
        # cells that are in the 1st  and last col can reach the pacific and atlantic respectively   
        for r in range(row):
            DFS(r, 0, pac, heights[r][0])           # 1st column
            DFS(r, col-1, atl, heights[r][col-1])   # last column
  
        # now find out the cells that are present in both pacific and atlantic cell and them into ans
        for i in range(row):
            for j in range(col):
                if (i,j) in pac and (i,j) in atl:
                    ans.append([i,j])
        return ans


# method 2: By Bfs using same logic as we did in case of "No of island"

# method: Try to do by DP(neetocde was not able to do by DP).. i also tried but not able to do
# But seeming a Q of dp:  Ask someone