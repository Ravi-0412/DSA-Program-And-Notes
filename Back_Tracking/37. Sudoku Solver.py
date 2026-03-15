# method 1: 

# easy solution only.
# just write the logic into code.
# The time complexity should be 9 ^ m (m represents the number of blanks to be filled in), since each blank can have 9 choices.
# TLE after latest test case

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
                                # OR , start_row = (row // 3) * 3 (find find the box number then multily by 3)
        start_col= col- col%3   # OR , column_row = (row // 3) * 3
        for r in range(start_row, start_row+3):  # size of subboxes is three
            for c in range(start_col, start_col+3):
                if board[r][c]== num:
                    return False
        
        # if none of the above return False means we can place that number in that empty cell
        return True


# Trying to optimise using BitMasking
"""
Q) How 'flip_state(r, c, mask)' works ?
Ans : you constantly do two opposite actions:
i) Place a number (Mark it as "used").
ii) Remove a number (Mark it as "available" again) during backtracking.

How it works ?
Each integer in rows, cols, and boxes is a sequence of bits (0s and 1s). Let’s say we are looking at the number 3. Its mask is 1 << (3-1), which is 100 in binary.
1. Marking as "Used" (0 to 1)
If the number 3 is not in the row yet, the 3rd bit of rows[r] is 0.
    0 ^ 1 = 1
Now the bit is 1. The number is officially "used."
2. Unmarking / Backtracking (1 to 0)
If you decide to remove the number 3, that bit is currently 1. You call flip_state again with the same mask.
    1 ^ 1 = 0
Now the bit is 0. The number is "available" again for other attempts.

Time Complexity : O(81* m^n)  = O(81 * 9 ^81)  since m ≤ 9 and n ≤ 81,
where m is the branching factor (average number of choices per cell) and n is the number of empty cells.
"""

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        # State trackers: Integers where the i-th bit represents if number (i+1) is used
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9 # Flattened 3x3 grid tracker (0 to 8)

        def get_box_index(r, c):
            """Helper to map 2D coordinates to one of the 9 sub-boxes."""
            return (r // 3) * 3 + (c // 3)

        def isSafe(r, c, mask):
            """
            Check if the number (represented by mask) exists in 
            the current row, column, or sub-box.
            """
            box_idx = get_box_index(r, c)
            # If the bit is already 1 in any mask, it returns True (Not Safe)
            return not (rows[r] & mask or cols[c] & mask or boxes[box_idx] & mask)

        def flip_state(r, c, mask):
            """Toggles the bit for a number in the row, column, and box masks."""
            box_idx = get_box_index(r, c)
            rows[r] ^= mask
            cols[c] ^= mask
            boxes[box_idx] ^= mask

        # 1. Initialize the board state
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = int(board[r][c])
                    mask = 1 << (num - 1)
                    flip_state(r, c, mask)

        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for num in range(1, 10):
                            mask = 1 << (num - 1)
                            
                            if isSafe(r, c, mask):
                                # 2. Place number and update bitmasks
                                board[r][c] = str(num)
                                flip_state(r, c, mask)
                                
                                if solve():
                                    return True
                                
                                # 3. Backtrack: Remove number and flip bits back to 0
                                board[r][c] = '.'
                                flip_state(r, c, mask)
                                
                        return False # Trigger backtracking
            return True # Sudoku complete

        solve()


"""
Most optimsied one. 
In above one, we are running for loop on whole sudoku.
So checking every cell better check and try to fill the empty cells only.

Optimisation:
1. Reduced Search Space: Instead of 9×9=81 checks per call, we jump directly to the next (r, c) using cell_idx.
2. Recursive Efficiency: We avoid the O(81) double-loop inside the solve function.
"""

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        # Bitmasks for rows, columns, and 3x3 boxes
        rows, cols, boxes = [0] * 9, [0] * 9, [0] * 9
        empty_cells = []

        def get_box_idx(r, c): return (r // 3) * 3 + (c // 3)

        def flip_state(r, c, mask):
            rows[r] ^= mask
            cols[c] ^= mask
            boxes[get_box_idx(r, c)] ^= mask

        # 1. Initial scan: Record masks and locate empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty_cells.append((r, c))
                else:
                    num = int(board[r][c])
                    flip_state(r, c, 1 << (num - 1))

        def solve(cell_idx):
            # Base Case: All empty cells have been processed
            if cell_idx == len(empty_cells):
                return True
            
            # Optimization: You could sort empty_cells here to pick 
            # the one with fewest options, but simply indexing 
            # usually passes LeetCode's TLE.
            r, c = empty_cells[cell_idx]
            
            for num in range(1, 10):
                mask = 1 << (num - 1)
                
                # O(1) Safety Check
                if not (rows[r] & mask or cols[c] & mask or boxes[get_box_idx(r, c)] & mask):
                    board[r][c] = str(num)
                    flip_state(r, c, mask)
                    
                    if solve(cell_idx + 1): # Move to the next pre-stored empty cell
                        return True
                    
                    # Backtrack
                    flip_state(r, c, mask)
                    board[r][c] = '.'
            
            return False

        solve(0)

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


