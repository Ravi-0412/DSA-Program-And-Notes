
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# So we only need to check for duplicate in each row, each col and each sub-square.

# Brute Force:
# for each ele check if its duplicate is present in it's curr row or or curr col or curr sub-square.

# for square checking: 
# Ele at (r,c) will belong to sub-square no : (r//3, c//3).

#  there will be 9 sub-square from (0,0) to (2,2) 
# i.e (0, 0) : starting from cell (0, 0), 
# (0, 1)   : starting from cell (0, 3), 
# (0, 2)   : starting from cell (0, 6),
# (1, 0)   : starting from cell (3, 0),
# (1, 2)   : starting from cell (3, 3),
# (1, 3)   : starting from cell (3, 6),
# (2, 0)   : starting from cell (6, 0),
# (2, 1)   : starting from cell (6, 3),
# (2, 2)   : starting from cell (6, 6)

# Time= Space= O(9^2)

from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows= defaultdict(set)  # will check duplicate in rows. [row_no : elements]
        cols= defaultdict(set)  # will check duplicate in cols
        squares= defaultdict(set)   # will check duplicate in square boxes.
        for r in range(9):
            for c in range(9):
                if board[r][c]!= '.':
                    # check if it's duplicate is present in it's curr row or curr col or curr sub-square boxes.
                    if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]:
                        return False
                    # if not then ,add this to rows,cols and squares set
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r//3, c//3)].add(board[r][c])
        # if none of above return False then it means sudoku is valid for current filled elements
        return True
