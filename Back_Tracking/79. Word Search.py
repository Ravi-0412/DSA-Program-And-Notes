# we are allowed to go in all four directions.

# logic: from every cell, we are checking can be get our desired word starting from that cell?

# Note: we are not marking visited when we see any cell for 1st time because that cell can be used later for forming another
# letter of the word.
# so mark only visited when you are going to see all its neighbour like Diskastra Algo.

# time: O(m*n.4^(m*n))

# Here blindly calling dfs so we have to check for invalid cases just after base case.
# Good approach. Do like this only

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col= len(board), len(board[0])
        path= set()  # will be only empty after each function call.
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
            temp= board[r][c]
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


# method 2: Another way of doing .
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


# Java version

"""
// method 1: With optimised space for visited set.

class Solution {
    public boolean exist(char[][] board, String word) {
        int row = board.length;
        int col = board[0].length;
        
        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                if (dfs(board, word, r, c, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean dfs(char[][] board, String word, int r, int c, int index) {
        // If we have checked all characters in the word, return true
        if (index == word.length()) {
            return true;
        }

        // Boundary checks and character match check
        if (r < 0 || r >= board.length || c < 0 || c >= board[0].length || board[r][c] != word.charAt(index)) {
            return false;
        }

        // Save the current character and mark the cell as visited
        char temp = board[r][c];
        board[r][c] = '#';

        // Explore all possible directions: left, right, up, down
        int[][] directions = {{r, c - 1}, {r, c + 1}, {r - 1, c}, {r + 1, c}};
        for (int[] dir : directions) {
            int newRow = dir[0];
            int newCol = dir[1];
            if (dfs(board, word, newRow, newCol, index + 1)) {
                return true;
            }
        }

        // Backtrack: restore the character in the board
        board[r][c] = temp;
        return false;
    }

"""