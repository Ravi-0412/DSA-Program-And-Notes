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

# java
# Method 2:
"""
import java.util.*;

public class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> allBoards = new ArrayList<>();
        char[][] board = new char[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = '.';
            }
        }
        helper(allBoards, board, 0);
        return allBoards;
    }

    private void helper(List<List<String>> allBoards, char[][] board, int col) {
        if (col == board.length) {
            saveBoard(allBoards, board);
            return;
        }
        for (int row = 0; row < board.length; row++) {
            if (isSafe(board, row, col)) {
                board[row][col] = 'Q';
                helper(allBoards, board, col + 1);
                board[row][col] = '.';
            }
        }
    }
     private void saveBoard(List<List<String>> allBoards, char[][] board) {
        List<String> newBoard = new ArrayList<>();
        for (int i = 0; i < board.length; i++) {
            newBoard.add(new String(board[i]));
        }
        allBoards.add(newBoard);
    }

    private boolean isSafe(char[][] board, int row, int col) {
        for (int i = 0; i < board.length; i++) {
            if (board[row][i] == 'Q') {
                return false;
            }
        }
        int r = row, c = col;
        while (r >= 0 && c >= 0) {
            if (board[r][c] == 'Q') {
                return false;
            }
            r--;
            c--;
        }
        r = row;
        c = col;
        while (r < board.length && c >= 0) {
            if (board[r][c] == 'Q') {
                return false;
            }
            r++;
            c--;
        }
        return true;
    }
}

"""