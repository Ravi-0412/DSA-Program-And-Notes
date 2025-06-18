# Methdd 1: 

"""
we are allowed to go in all four directions.

logic: from every cell, we are checking can be get our desired word starting from that cell?

Note: we are not marking visited when we see any cell for 1st time because that cell can be used later for forming another
letter of the word.
so mark only visited when you are going to see all its neighbour like Diskastra Algo.

Here blindly calling dfs so we have to check for invalid cases just after base case.
Good approach. Do like this only.

time: O(m*n.4^(m*n))
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col= len(board), len(board[0])
        path = set()  # will be only empty after each function call.
             # will tell whether we have visited that cell in current cycle or not. just like we are passing this empty path in each call.
        
        def dfs(r,c,word):
            if not word:
                return True
            # if we can;t get ans by curent cell then simply return False
            if r<0 or r>=row or c<0 or c>= col or board[r][c]!= word[0] or (r,c) in path:
                return False   # return    . this will also work since everywhere we are cheking for True not False.
            # it means we have found the matching char at (r,c)
            path.add((r,c))  # added in path so that this cell char doesn't repeat in same cycle
            directions= [[r,c-1], [r, c+1], [r-1, c], [r+1, c]]
            for nr, nc in directions:
                if dfs(nr, nc, word[1: ]):
                    return True
            # now backtrack if we don't ans by adding the char at (r,c)
            # so that this cell can be used in next cycle.
            path.remove((r,c))
            return False
        
        for r in range(row):
            for c in range(col):
                if dfs(r,c,word):
                    return True
        return False


# Method 2: 
# if we don't want to use the path set for visited then do like this.
# just mark grid value by any char.
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col= len(board), len(board[0])
        
        def dfs(r,c,word):
            if not word:
                return True
            if r < 0 or r >= row or c < 0 or c>= col or board[r][c] == "#" or board[r][c] != word[0]:
                return False
            temp = board[r][c]
            board[r][c]= "#"
            directions= [[r,c-1], [r, c+1], [r-1, c], [r+1, c]]
            for nr, nc in directions:
                if dfs(nr, nc, word[1: ]):
                    return True
            # now backtrack if we don't ans by adding the char at (r,c)
            board[r][c]= temp
            return False
        
        for r in range(row):
            for c in range(col):
                if dfs(r,c,word):
                    return True
        return False


# method 3: Another way of doing .
# just same logic only
# Here we are not calling blindly so need to check invalid cases.
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col= len(board), len(board[0])
        
        def dfs(r,c,word):
            if not word:
                return True
            # if board[r][c]== "#":  # duplicate. No need of this because we are only calling dfs if that cell is not visited.
            #     return
            temp= board[r][c]
            board[r][c]= "#"  # marking visited
            directions= [[r,c-1], [r, c+1], [r-1, c], [r+1, c]]
            for nr, nc in directions:
                if 0<=nr < row and 0<= nc < col and board[nr][nc]!= "#" and board[nr][nc]== word[0]: 
                    if dfs(nr, nc, word[1: ]):
                        return True
            # now backtrack if we don't ans by adding the char at (r,c)
            board[r][c]= temp
            return False
        
        for r in range(row):
            for c in range(col):
                if board[r][c]== word[0] and dfs(r,c,word[1:]):  # checking if we can get and from current cell
                    return True
        return False


