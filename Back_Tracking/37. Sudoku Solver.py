class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row,col= -1,-1
        emptyLeft= True  # will check whether any empty space is present or not
        # first find the empty cell
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]== '.':
                    row,col= i,j
                    emptyLeft= False
                    break
            if emptyLeft== False:  # means we have found one empty cell in any row
                break
        if emptyLeft== True:   # means no empty cell available i.e sudoku is already solved
            return True   
        
        for num in range(1,10):
            if self.isSafe(board,row,col,str(num)):
                board[row][col]= str(num)
                if self.solveSudoku(board):   # means sudoku is solved 
                    return True
                else:  #backtrack
                    board[row][col]= '.'  
        return False
    
    def isSafe(self,board,row,col,num):
        # checking whether the number is present in the that row or not
        for i in range(len(board[0])):
            if board[row][i]== num:
                return  False
        # checking whether the number is present in the that col or not
        for i in range(len(board)):
            if board[i][col]== num:
                return  False
        # checking in the 3*3 subgrid
        # first find the starting row and starting col of the sub-boxes for the given row and col
        start_row= row - row%3   # just remove the extra number. since it is in multiple of '3' so we can do like this
        start_col= col- col%3
        for r in range(start_row, start_row+3):  # size of subboxes is three
            for c in range(start_col, start_col+3):
                if board[r][c]== num:
                    return False
        
        # if none of the above return False means we can place that number in that empty cell
        return True
    
        