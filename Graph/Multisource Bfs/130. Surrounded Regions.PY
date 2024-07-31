# Soo nicee Question
# logic: just same as we did in "pacific Atlantic Ocean work flow" i.e in reverse way thinking
# change the q from "capture surrounded regions " to "capture everything except surrounded regions": both have same meaning only

#  all those cell will come under unsurrounded that will be connected to any of the "O" at the boundary
# so run the dfs at the boundary only and mark all the connected "O" by some special symbol say "V"
# after doing this you will get all unsurrounded "O" marked by "V" and all surrounded "O" will remain as it is

# now for getting the ans, just change the surrounded "O" by "X" and unsurrounded "O"(which is "V") now by "O" 

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row,col= len(board), len(board[0])
        
        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>= col or board[r][c]!= "O":
                return 
            board[r][c]= "V"     # any special symbol
            directions= [[-1,0],[1,0],[0,-1],[0,1]]    # up,down,left,right
            for dr,dc in directions:
                r1,c1= r+dr, c+dc
                dfs(r1,c1)
        
        # code starts from here
        for r in range(row):
            for c in range(col):
                # we only have to call the dfs at the edges like at 1st row,last row,1st col, last col
                if board[r][c]== "O" and (r==0 or r==row-1 or c==0 or c==col-1): 
                    dfs(r,c)
        
        for r in range(row):
            for c in range(col):
                if board[r][c]== "O":
                    board[r][c]="X"
                if board[r][c]== "V":
                    board[r][c]="O"
        return board


# Can do by multisource bfs. Append all the boundary 'O' into queue and go on.


# java
""""
class Solution {
    private int row, col;
    private char[][] board;
    
    public void solve(char[][] board) {
        this.row = board.length;
        if (row == 0) return;
        this.col = board[0].length;
        this.board = board;

        // Code starts from here
        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                // We only have to call dfs at the edges (1st row, last row, 1st col, last col)
                if (board[r][c] == 'O' && (r == 0 || r == row - 1 || c == 0 || c == col - 1)) {
                    dfs(r, c);
                }
            }
        }
        
        // Flip all 'O' to 'X' and 'V' (visited) back to 'O'
        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                if (board[r][c] == 'O') {
                    board[r][c] = 'X';
                }
                if (board[r][c] == 'V') {
                    board[r][c] = 'O';
                }
            }
        }
    }
    
    // Helper function to perform DFS
    private void dfs(int r, int c) {
        if (r < 0 || r >= row || c < 0 || c >= col || board[r][c] != 'O') {
            return;
        }
        board[r][c] = 'V'; // Mark as visited with a special symbol
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // Up, down, left, right
        for (int[] direction : directions) {
            dfs(r + direction[0], c + direction[1]);
        }
    }
}

"""