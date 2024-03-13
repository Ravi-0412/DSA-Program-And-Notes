# easy solution only.
# just write the logic into code.
# The time complexity should be 9 ^ m (m represents the number of blanks to be filled in), since each blank can have 9 choices.

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # first find the empty space
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]== '.':   # means there some empty space to fill
                    # Try all possible number from '1' to '9' to fill this empty cell.
                    for num in range(1, 10):
                        if self.isSafe(board, r, c, str(num)):  # then fill the board at (r,c) with this num
                            board[r][c]= str(num)
                            # Again check after filling this curr empty cell with this 'num', if we are able to make a valid sudoku
                            if self.solveSudoku(board):
                                return True
                            # if filling with this num at curr empty cell doesn't lead to a valid sudoku, reset the changes made.
                            board[r][c]= '.'
                    # if we are not able to fill this place with any of the num from '1' to '9', then return False
                    # Now it will backtrack and will try to change the num at empty places after which this function was called
                    return False
        # If there is no empty space left i.e sudoku is fully filled 
        return True
    
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


# 



