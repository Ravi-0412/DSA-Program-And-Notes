# Method 1: 

# Q) find the no of possible ways to put the Queens
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
    
    # checking the upper left diagonal
    r,c= row,col
    while(r>=0 and c>=0):
        if board[r][c]== 'Q':  # if true 
            return False
        r,c= r-1,c-1
        
    
    # checking the upper right diagonal
    r,c= row,col
    while(r>=0 and c<len(board)):
        if board[r][c]== 'Q':  # if true 
            return False
        r,c= r-1,c+1

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
                

# Java Code 
"""
import java.util.*;

public class Solution {

    public int NQueens(char[][] board, int row) {  // since we are checking from starting for each row, no need to write col
        if (row == board.length) {  // all queens are placed safely
            // means we have found a way to place all Queens safely
            // as we are checking each row one by one after placing a Queen
            display(board);
            System.out.println();
            return 1;  // will count the number of ways
        }

        int count = 0;  // will count the total number of ways to place all Queens safely

        // start placing the Queen at each col in the given row
        // repeat this for every row

        for (int col = 0; col < board.length; col++) {  // checking for each col in that row
            if (isSafe(board, row, col)) {  // means safe so place the Queen
                board[row][col] = 'Q';
                count += NQueens(board, row + 1);  // check for next row
                board[row][col] = 'X';  // backtrack — restore the position
            }
        }
        return count;
    }

    public boolean isSafe(char[][] board, int row, int col) {
        // checking the vertical line in the col where we want to place
        for (int i = 0; i < board.length; i++) {
            if (board[i][col] == 'Q') return false;
        }

        // checking the upper left diagonal
        for (int r = row, c = col; r >= 0 && c >= 0; r--, c--) {
            if (board[r][c] == 'Q') return false;
        }

        // checking the upper right diagonal
        for (int r = row, c = col; r >= 0 && c < board.length; r--, c++) {
            if (board[r][c] == 'Q') return false;
        }

        // all checks passed — it's safe
        return true;
    }

    public void display(char[][] board) {
        for (char[] row : board) {
            System.out.println(Arrays.toString(row));
        }
    }

    // To call the solver:
    public static void main(String[] args) {
        int n = 5;
        char[][] board = new char[n][n];
        for (char[] row : board)
            Arrays.fill(row, 'X');

        Solution sol = new Solution();
        int ways = sol.NQueens(board, 0);
        System.out.println("Total ways: " + ways);
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int NQueens(vector<vector<char>>& board, int row) {  // since we are checking from starting for each row, no need to write col
        if (row == board.size()) {  // all queens are placed safely
            display(board);
            cout << endl;
            return 1;  // will count the number of ways
        }

        int count = 0;  // will count the total number of ways to place all Queens safely

        for (int col = 0; col < board.size(); ++col) {  // checking for each col in that row
            if (isSafe(board, row, col)) {  // means safe so place the Queen
                board[row][col] = 'Q';
                count += NQueens(board, row + 1);  // check for next row
                board[row][col] = 'X';  // backtrack — restore the position
            }
        }
        return count;
    }

    bool isSafe(vector<vector<char>>& board, int row, int col) {
        // checking the vertical line
        for (int i = 0; i < board.size(); ++i)
            if (board[i][col] == 'Q') return false;

        // upper-left diagonal
        for (int r = row, c = col; r >= 0 && c >= 0; --r, --c)
            if (board[r][c] == 'Q') return false;

        // upper-right diagonal
        for (int r = row, c = col; r >= 0 && c < board.size(); --r, ++c)
            if (board[r][c] == 'Q') return false;

        return true;
    }

    void display(vector<vector<char>>& board) {
        for (const auto& row : board) {
            for (char c : row)
                cout << c << " ";
            cout << endl;
        }
    }
};

int main() {
    int n = 5;
    vector<vector<char>> board(n, vector<char>(n, 'X'));
    Solution sol;
    int ways = sol.NQueens(board, 0);
    cout << "Total ways: " << ways << endl;
}
"""

# Method 2: 
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
                
# Java Code 
"""
import java.util.*;

public class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> allBoards = new ArrayList<>();  // to store the result
        char[][] board = new char[n][n];                   // created input board

        for (char[] row : board)
            Arrays.fill(row, '.');

        helper(allBoards, board, 0);  // we will put col wise, starting from zero
        return allBoards;
    }

    void helper(List<List<String>> allBoards, char[][] board, int col) {
        if (col == board.length) {
            // Add 'board' into ans 'allBoards'
            saveBoard(allBoards, board);
            return;
        }

        for (int row = 0; row < board.length; row++) {
            if (isSafe(board, row, col)) {
                board[row][col] = 'Q';
                helper(allBoards, board, col + 1);
                board[row][col] = '.';  // backtrack
            }
        }
    }

    void saveBoard(List<List<String>> allBoards, char[][] board) {
        List<String> newBoard = new ArrayList<>();  // will contain all rows in string form
        for (char[] row : board)
            newBoard.add(new String(row));
        allBoards.add(newBoard);
    }

    boolean isSafe(char[][] board, int row, int col) {
        // checking the horizontal line
        for (int i = 0; i < board.length; i++)
            if (board[row][i] == 'Q') return false;

        // checking the upper left diagonal
        for (int r = row, c = col; r >= 0 && c >= 0; r--, c--)
            if (board[r][c] == 'Q') return false;

        // checking the lower left diagonal
        for (int r = row, c = col; r < board.length && c >= 0; r++, c--)
            if (board[r][c] == 'Q') return false;

        // if all checks passed
        return true;
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> allBoards;  // to store the result
        vector<vector<char>> board(n, vector<char>(n, '.'));  // created input board
        helper(allBoards, board, 0);  // put col-wise, starting from zero
        return allBoards;
    }

    void helper(vector<vector<string>>& allBoards, vector<vector<char>>& board, int col) {
        if (col == board.size()) {
            saveBoard(allBoards, board);
            return;
        }

        for (int row = 0; row < board.size(); row++) {
            if (isSafe(board, row, col)) {
                board[row][col] = 'Q';
                helper(allBoards, board, col + 1);
                board[row][col] = '.';  // backtrack
            }
        }
    }

    void saveBoard(vector<vector<string>>& allBoards, vector<vector<char>>& board) {
        vector<string> newBoard;
        for (const auto& row : board)
            newBoard.push_back(string(row.begin(), row.end()));
        allBoards.push_back(newBoard);
    }

    bool isSafe(vector<vector<char>>& board, int row, int col) {
        // checking the horizontal line
        for (int i = 0; i < board.size(); ++i)
            if (board[row][i] == 'Q') return false;

        // checking the upper left diagonal
        for (int r = row, c = col; r >= 0 && c >= 0; --r, --c)
            if (board[r][c] == 'Q') return false;

        // checking the lower left diagonal
        for (int r = row, c = col; r < board.size() && c >= 0; ++r, --c)
            if (board[r][c] == 'Q') return false;

        return true;
    }
};
"""

# Similar Question i.e based on checking 'isSafe()' for each possible number.

# 1) Placing n Knight in a 2d array such that they don't attack each other
# 2) 37. Sudoku Solver
# 3) M-Coloring Problem

