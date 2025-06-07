"""
Think value of matric = color
Logic: Just you have to make value of cells = given color if that cell is directly or indirectly connected to given cell and image_value of those cells are same.
i.e they are are forming a connected components with same value then make value of those cells = given color.
"""

"""

BFS CODE
PYTHON CODE

"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        src_color = image[sr][sc]
        q= deque([(sr,sc)])
        while q:
            for i in range(len(q)):
                r, c = q.popleft()  # clr= pixel at that (r,c)
                image[r][c]= color  # can update when we will see for 1st time also
                directions= [[-1,0],[1,0],[0,-1],[0,1]]  # up,down,left,right
                for dr,dc in directions:
                    row,col= r+ dr, c+ dc
                    # if in range and image_of_cur_cell = source image value and already not colored with given color(just working as visited)
                    if 0 <=row < len(image) and 0<= col < len(image[0]) and image[row][col] == src_color and image[row][col]!=color:
                        q.append((row, col))
        return image
    

"""

DFS CODE
PYTHON CODE

"""
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        src_color = image[sr][sc]
        if src_color == color:
            return image 
        def dfs(r, c):
            if (r < 0 or r >= len(image) or 
                c < 0 or c >= len(image[0]) or 
                image[r][c] != src_color):
                return
            image[r][c] = color
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        dfs(sr, sc)
        return image

# Can do by single source bfs and dfs also.
# better do by this only. 
