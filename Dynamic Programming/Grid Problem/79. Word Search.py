# Brute force by backtracking. Q was on this only. we can see from matrix dimension
# instead of visited set just marked the cell by special symbol
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col= len(board), len(board[0])
        # from each cell we are checking    
        for r in range(row):
            for c in range(col):
                if self.dfs(r,c,word, board):
                    return True
        return False
        
    def dfs(self, r,c,word, board):
        if not word: # all the characters are found
            return True
        if r<0 or r>=len(board) or c<0 or c>= len(board[0]) or board[r][c]!= word[0] :
            return False
        # it means we have found the matching char at (r,c), now check for remaining
        tmp = board[r][c]
        board[r][c] = "#"  # marking visites to avoid visiting again
        res= self.dfs(r,c-1,word[1:], board)  or self.dfs(r,c+1,word[1:], board) or self.dfs(r-1,c,word[1:], board) or self.dfs(r+1,c,word[1:], board)    # left,right,up,down
        # now backtrack if we don't ans by adding the char at (r,c)
        board[r][c]= tmp
        return res

