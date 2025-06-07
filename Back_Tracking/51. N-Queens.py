# Q) find the no of possible ways to put the Queens
# page: 21
# in this we are placing row wise and once we got any safe place in a row, no need to check further col in that row.
# as two Queens can't be in the same row

# so we only need to check upper left diagonal, upper right diagonal and vertical up
# for whether Queen is safe orr not at that place

def NQueens(board,row):  # since we are checking from starting for each row, no need to write col
    if row== len(board):  # all queens are placed safely 
                        # means we have found a ways to place all Queens safely
                        # as we are checking each row one one after placing a Queen
        Display(board)
        print()
        return 1    # will count the no of ways
    
    count= 0  # will count the total no of ways to place all Queen safely

    # start placing the Queen at each col in the given row
    # repeat this for every row

    # after placing check whether that position is safe or not 
    # if safe mark that position as: 'True'

    for col in range(len(board)):   # checking for each col in that row
        if isSafe(board,row,col):  # means safe so place the Queen and mark that position as True
            board[row][col]= 'Q'
            # after placing(if not possible to place in given row) check for 
            # where we can place in further rows the next Queen
            count+= NQueens(board,row+1)  
            board[row][col]= 'X'     # while returning restore the changes made by that function call
                                # since it can affect the further recursive call if we don't remove 
                                # Also while finding for soultion it will create problem if we don't restore back
    return count

def isSafe(board,row,col):
    # checking the vertical line in the col where we want to place
    for i in range(len(board)):
        if board[i][col]=='Q':  # if any position is 'Q' means you cant place Queen  there
            return False

    # checking the horizontal line where we want to place
    # for i in range(len(board)):
    #     if board[row][i]=='Q':  # if any position is true means you cant place Queen is there
    #         return False
    
    # checking the upper left diagonal
    r,c= row,col
    while(r>=0 and c>=0):
        if board[r][c]== 'Q':  # if true 
            return False
        r,c= r-1,c-1

    # checking the lower left diagonal
    # r,c= row,col
    # while(r<len(board) and c>=0):
    #     if board[r][c]== 'Q':  # if true 
    #         return False
    #     r,c= r+1,c-1
        
    
    # checking the upper right diagonal
    r,c= row,col
    while(r>=0 and c<len(board)):
        if board[r][c]== 'Q':  # if true 
            return False
        r,c= r-1,c+1
    
    # checking the lower right diagonal
    # r,c= row,col
    # while(r<len(board) and c<len(board)):
    #     if board[r][c]== 'Q':  # if true 
    #         return False
    #     r,c= r+1,c+1
        
    
    
    # if any of these are false means you cant place Queen at that position
    # you are here means all are position is safe so simply return True
    return True

def Display(board):    
    # Now print the board
    for row in board:
        print(row)

# board= [['X' for j in range(4)] for i in range(4)]  # only create 2d array like this , never create by any other way(like a= [[0]*n]*n) due to this only i was getting wrong ans
board= [['X' for j in range(5)] for i in range(5)]
print(NQueens(board,0))
                


# submitted on leetcode
# in this we were placing col wise
# so we only need to check lower left diagonal, upper left diagonal and horizonatl
# for whether Queen is safe orr not at that place

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        all_board= []  # to store the result. 
        board= [['.' for j in range(n)] for i in range(n)]   # created inputs board
        self.helper(all_board,board,0)  # we will put col wise
                                        # starting from zero(row will always start from zero)
        return all_board
    
    def helper(self,all_board,board,col):
        if col== len(board):
            # Add 'baord' into ans 'all_board'
            self.saveBoard(all_board, board)
            return 
        
        for row in range(len(board)):
            if self.isSafe(board,row,col):
                board[row][col]= 'Q'
                self.helper(all_board,board,col+1)
                board[row][col]= '.'

    def saveBoard(self,all_board, board):
        new_board= []  # will contain all the ele of board row by row in single array
        for i in range(len(board)):
            new_board.append("".join(board[i]))
        all_board.append(new_board)

    def isSafe(self,board,row,col):    
        # checking the horizontal line where we want to place
        for i in range(len(board)):
            if board[row][i]=='Q':  # if any position is true means you cant place Queen is there
                return False
    
        # checking the upper left diagonal
        r,c= row,col
        while(r>=0 and c>=0):
            if board[r][c]== 'Q':  # if true 
                return False
            r,c= r-1,c-1
    
        # checking the lower left diagonal
        r,c= row,col
        while(r<len(board) and c>=0):
            if board[r][c]== 'Q':  # if true 
                return False
            r,c= r+1,c-1
                    
        # if any of these are false means you can't place Queen at that position
        # you are here means all are position is safe so simply return True
        return True


# Similar Question i.e based on checking 'isSafe()' for each possible number.

# 1) Placing n Knight in a 2d array such that they don't attack each other
# 2) 37. Sudoku Solver
# 3) M-Coloring Problem

# Java Code
# Method 2:
"""
class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> all_board = new ArrayList<>();  // to store the result.
        char[][] board = new char[n][n];
        
        // Initialize the board with '.'
        for (int i = 0; i < n; i++) {
            Arrays.fill(board[i], '.');
        }

        helper(all_board, board, 0);  // starting from column 0
        return all_board;
    }

    private void helper(List<List<String>> all_board, char[][] board, int col) {
        if (col == board.length) {
            saveBoard(all_board, board);
            return;
        }

        for (int row = 0; row < board.length; row++) {
            if (isSafe(board, row, col)) {
                board[row][col] = 'Q';
                helper(all_board, board, col + 1);
                board[row][col] = '.';
            }
        }
    }

    private void saveBoard(List<List<String>> all_board, char[][] board) {
        List<String> new_board = new ArrayList<>();
        for (int i = 0; i < board.length; i++) {
            new_board.add(new String(board[i]));
        }
        all_board.add(new_board);
    }

    private boolean isSafe(char[][] board, int row, int col) {
        // checking the horizontal row
        for (int i = 0; i < board.length; i++) {
            if (board[row][i] == 'Q') return false;
        }

        // checking the upper left diagonal
        for (int r = row, c = col; r >= 0 && c >= 0; r--, c--) {
            if (board[r][c] == 'Q') return false;
        }

        // checking the lower left diagonal
        for (int r = row, c = col; r < board.length && c >= 0; r++, c--) {
            if (board[r][c] == 'Q') return false;
        }

        return true;
    }
}


"""

# C++ Code 
"""
class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> all_board;  // to store the result
        vector<vector<char>> board(n, vector<char>(n, '.'));  // create empty board
        helper(all_board, board, 0);  // starting from column 0
        return all_board;
    }

    void helper(vector<vector<string>>& all_board, vector<vector<char>>& board, int col) {
        if (col == board.size()) {
            saveBoard(all_board, board);
            return;
        }

        for (int row = 0; row < board.size(); row++) {
            if (isSafe(board, row, col)) {
                board[row][col] = 'Q';
                helper(all_board, board, col + 1);
                board[row][col] = '.';
            }
        }
    }

    void saveBoard(vector<vector<string>>& all_board, vector<vector<char>>& board) {
        vector<string> new_board;
        for (int i = 0; i < board.size(); i++) {
            new_board.push_back(string(board[i].begin(), board[i].end()));
        }
        all_board.push_back(new_board);
    }

    bool isSafe(vector<vector<char>>& board, int row, int col) {
        // checking the horizontal row
        for (int i = 0; i < board.size(); i++) {
            if (board[row][i] == 'Q') return false;
        }

        // checking the upper left diagonal
        for (int r = row, c = col; r >= 0 && c >= 0; r--, c--) {
            if (board[r][c] == 'Q') return false;
        }

        // checking the lower left diagonal
        for (int r = row, c = col; r < board.size() && c >= 0; r++, c--) {
            if (board[r][c] == 'Q') return false;
        }

        return true;
    }
};

"""