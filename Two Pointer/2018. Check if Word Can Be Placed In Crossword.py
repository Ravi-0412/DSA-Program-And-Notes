# Logic: 
"""
Once we find a valid starting space (an open cell or matching character to the beginning of our word), we can look to 
ensure it does not break rule 3/4 where the opposite of the direction we are going should be a wall ('#' or out of bounds). If rules 3/4 are not broken, we 
simply apply the typical two pointer approach moving the pointer in the word forward while simultaneously moving the row/col pointers forward in the 
appropriate direction (breaking early if we find an invalid cell or mismatching character). If we reach the end of the word and the row/col pointers are on 
a wall ('#' or out of bounds), we have found a valid place to place our word.
"""

# Time: O(m*n*max(m, n) * 4)  
class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

        # Helper function to check if the position (r, c) is within bounds of the board
        def in_bounds(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])

        # Iterate over each cell in the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                # Check if the starting cell is a valid space (either ' ' or the first character of word)
                if board[i][j] == ' ' or board[i][j] == word[0]:
                    # Try placing the word in each direction
                    for dir_r, dir_c in dirs:
                        r, c, idx = i, j, 0

                        # Check if the cell opposite to the direction is valid (should be a wall or out of bounds)
                        if in_bounds(r - dir_r, c - dir_c) and board[r - dir_r][c - dir_c] != '#':
                            continue

                        # Try to place the word by advancing in the current direction
                        while idx < len(word) and in_bounds(r, c):
                            if board[r][c] == '#' or (board[r][c] != ' ' and board[r][c] != word[idx]):
                                break
                            idx += 1
                            r += dir_r
                            c += dir_c

                        # If we placed the whole word and the next cell is out of bounds or a wall
                        if idx == len(word) and (not in_bounds(r, c) or board[r][c] == '#'):
                            return True
        return False
        
# java
"""
class Solution {
    // Directions: right, down, left, up
    private static final int[][] dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    public boolean placeWordInCrossword(char[][] board, String word) {
        int rows = board.length;
        int cols = board[0].length;

        // Iterate over each cell in the board
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                // Check if the starting cell is a valid space (either ' ' or the first character of word)
                if (board[i][j] == ' ' || board[i][j] == word.charAt(0)) {
                    // Try placing the word in each direction
                    for (int[] dir : dirs) {
                        int dir_r = dir[0], dir_c = dir[1];
                        int r = i, c = j, idx = 0;

                        // Check if the cell opposite to the direction is valid (should be a wall or out of bounds)
                        if (inBounds(r - dir_r, c - dir_c, rows, cols) && board[r - dir_r][c - dir_c] != '#') {
                            continue;
                        }

                        // Try to place the word by advancing in the current direction
                        while (idx < word.length() && inBounds(r, c, rows, cols)) {
                            if (board[r][c] == '#' || (board[r][c] != ' ' && board[r][c] != word.charAt(idx))) {
                                break;
                            }
                            idx++;
                            r += dir_r;
                            c += dir_c;
                        }

                        // If we placed the whole word and the next cell is out of bounds or a wall
                        if (idx == word.length() && (!inBounds(r, c, rows, cols) || board[r][c] == '#')) {
                            return true;
                        }
                    }
                }
            }
        }

        return false;
    }

    // Helper function to check if the position (r, c) is within bounds of the board
    private boolean inBounds(int r, int c, int rows, int cols) {
        return r >= 0 && r < rows && c >= 0 && c < cols;
    }
}

"""
