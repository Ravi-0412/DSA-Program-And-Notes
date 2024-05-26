
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


# Java
"""
public class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, Set<Character>> rows = new HashMap<>();
        Map<Integer, Set<Character>> cols = new HashMap<>();
        Map<String, Set<Character>> squares = new HashMap<>(); // Using a string key for squares

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char currentChar = board[r][c];
                if (currentChar != '.') {
                    // Check if it's a duplicate in its current row, column, or sub-grid.
                    if (rows.containsKey(r) && rows.get(r).contains(currentChar) ||
                            cols.containsKey(c) && cols.get(c).contains(currentChar) ||
                            squares.containsKey((r / 3) + "-" + (c / 3)) && squares.get((r / 3) + "-" + (c / 3)).contains(currentChar)) {
                        return false;
                    }
                    // If not a duplicate, add it to rows, cols, and squares sets.
                    rows.computeIfAbsent(r, k -> new HashSet<>()).add(currentChar);
                    cols.computeIfAbsent(c, k -> new HashSet<>()).add(currentChar);
                    squares.computeIfAbsent((r / 3) + "-" + (c / 3), k -> new HashSet<>()).add(currentChar);
                }
            }
        }
        // If none of the checks above return false, the Sudoku board is valid for the current filled elements.
        return true;
    }
}
"""