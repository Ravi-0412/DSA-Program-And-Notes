# method 1: 

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


# Java Code 
"""
class Solution {
    public boolean solveSudoku(char[][] board) {
        // first find the empty space
        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board[0].length; c++) {
                if (board[r][c] == '.') {  // means there some empty space to fill
                    // Try all possible number from '1' to '9' to fill this empty cell.
                    for (char num = '1'; num <= '9'; num++) {
                        if (isSafe(board, r, c, num)) {  // then fill the board at (r,c) with this num
                            board[r][c] = num;
                            // Again check after filling this curr empty cell with this 'num', if we are able to make a valid sudoku
                            if (solveSudoku(board)) {
                                return true;
                            }
                            // if filling with this num at curr empty cell doesn't lead to a valid sudoku, reset the changes made.
                            board[r][c] = '.';
                        }
                    }
                    // if we are not able to fill this place with any of the num from '1' to '9', then return false
                    return false;
                }
            }
        }
        // If there is no empty space left i.e sudoku is fully filled 
        return true;
    }

    public boolean isSafe(char[][] board, int row, int col, char num) {
        // checking whether the number is present in the that row or not
        for (int i = 0; i < board[0].length; i++) {
            if (board[row][i] == num) return false;
        }
        // checking whether the number is present in the that col or not
        for (int i = 0; i < board.length; i++) {
            if (board[i][col] == num) return false;
        }
        // checking in the 3*3 subgrid
        // first find the starting row and starting col of the sub-boxes for the given row and col
        int start_row = row - row % 3;
        int start_col = col - col % 3;
        for (int r = start_row; r < start_row + 3; r++) {
            for (int c = start_col; c < start_col + 3; c++) {
                if (board[r][c] == num) return false;
            }
        }
        // if none of the above return false means we can place that number in that empty cell
        return true;
    }
}

"""

# C++ Code 
"""
class Solution {
public:
    bool solveSudoku(vector<vector<char>>& board) {
        // first find the empty space
        for (int r = 0; r < board.size(); r++) {
            for (int c = 0; c < board[0].size(); c++) {
                if (board[r][c] == '.') {  // means there some empty space to fill
                    // Try all possible number from '1' to '9' to fill this empty cell.
                    for (char num = '1'; num <= '9'; num++) {
                        if (isSafe(board, r, c, num)) {  // then fill the board at (r,c) with this num
                            board[r][c] = num;
                            // Again check after filling this curr empty cell with this 'num', if we are able to make a valid sudoku
                            if (solveSudoku(board)) {
                                return true;
                            }
                            // if filling with this num at curr empty cell doesn't lead to a valid sudoku, reset the changes made.
                            board[r][c] = '.';
                        }
                    }
                    // if we are not able to fill this place with any of the num from '1' to '9', then return false
                    return false;
                }
            }
        }
        // If there is no empty space left i.e sudoku is fully filled 
        return true;
    }

    bool isSafe(vector<vector<char>>& board, int row, int col, char num) {
        // checking whether the number is present in the that row or not
        for (int i = 0; i < board[0].size(); i++) {
            if (board[row][i] == num) return false;
        }
        // checking whether the number is present in the that col or not
        for (int i = 0; i < board.size(); i++) {
            if (board[i][col] == num) return false;
        }
        // checking in the 3*3 subgrid
        // first find the starting row and starting col of the sub-boxes for the given row and col
        int start_row = row - row % 3;
        int start_col = col - col % 3;
        for (int r = start_row; r < start_row + 3; r++) {
            for (int c = start_col; c < start_col + 3; c++) {
                if (board[r][c] == num) return false;
            }
        }
        // if none of the above return false means we can place that number in that empty cell
        return true;
    }
};

"""


