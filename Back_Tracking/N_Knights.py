# by different methods than N_Queens
# here we taking no of knight that we have to place as parameter

# we are placing row wise in this also
def Knights(board, row, col, targets):
    if targets== 0:  # when no of knights available to place is '0'
                     # means all nights are placed safely
        Display(board)
        print()
        return 1

    # start placing the Knights in each row and each col
    # if col reaches the len(board[0]), start checking from next row
    if col== len(board[0]):   
        Knights(board,row+1,0,targets)
        return 
    
    if row== len(board):
        return 
    # if that position is safe, put the knight there and mark the position as 'True'
    if isSafe(board,row,col):
        board[row][col]= 'K'
        # after placing check whetehr we can place the next knight(targets) in the next col or not
        Knights(board,row,col+1,targets-1)
        board[row][col]= ' '  # after returning back restore the value

    # if that position is not safe check for next col in the same row with same no of knight
    Knights(board,row,col+1,targets)

def isValid(board,row,col):
    if row>=0 and row < len(board) and col>=0 and col<len(board[0]):
        return True
    
def isSafe(board,row,col):
    # there will be total 8 cases to check
    #  case 1: upper_left
    if isValid(board,row-2,col-1):
        if board[row-2][col-1]== 'K':
            return False

    # case 2: down_left
    if isValid(board,row+2,col-1):
        if board[row+2][col-1]== 'K':
            return False

    # case 3: left_up
    if isValid(board,row-1,col-2):
        if board[row-1][col-2]== 'K':
            return False

    # case 4: left_down
    if isValid(board,row+1,col-2):
        if board[row+1][col-2]== 'K':
            return False

    #  case 5: upper_right
    if isValid(board,row-2,col+1):
        if board[row-2][col+1]== 'K':
            return False

    # case 6: down_right
    if isValid(board,row+2,col+1):
        if board[row+2][col+1]== 'K':
            return False

    # case 7: right_up
    if isValid(board,row-1,col+2):
        if board[row-1][col+2]== 'K':
            return False

    # case 8: right_down
    if isValid(board,row+1,col+2):
        if board[row+1][col+2]== 'K':
            return False
            
    return True

def Display(board):
    # Now print the board
    for row in board:
        print(row)

# board= [[' ' for j in range(2)] for i in range(2)]
# board= [[' ' for j in range(3)] for i in range(3)]
# board= [[' ' for j in range(4)] for i in range(4)]
# print(Knights(board,0,0,5)) # last parameter means no of knights you want to place
# Knights(board,0,0,13)
# Knights(board,0,0,2)
board= [[' ' for j in range(3)] for i in range(4)]
Knights(board,0,0,6)
