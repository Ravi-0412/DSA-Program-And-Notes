# Q:

# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Brute Force:
# for each ele check if its duplicate is present in it's curr row or or curr col or curr sub-square.

# for square checking: (r,c)
# it will belong to sub-square no : (r//3, c//3). there will be 9 sub-square from (0,0) to (2,2)
# Time= Space= O(9^2)
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows= defaultdict(set)  # will check duplicate in rows
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
