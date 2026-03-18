# Exact code for 1st part with one count variable for ans

class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        all_board= []  # to store the result. 
        board= [['.' for j in range(n)] for i in range(n)]   # created inputs board
        return self.helper(all_board,board,0)  # we will put col wise
                                        # starting from zero(row will always start from zero)

    def helper(self,all_board,board,col):
        if col== len(board):
            # Add 'baord' into ans 'all_board'
            self.saveBoard(all_board, board)
            return 1
        
        count = 0
        
        for row in range(len(board)):
            if self.isSafe(board,row,col):
                board[row][col]= 'Q'
                count += self.helper(all_board,board,col+1)
                board[row][col]= '.'
        return count

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
