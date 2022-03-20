    r,c= row,col
    while(r>=0 and c>=0):
        r,c= r-1,c-1
        if board[r][c]== 'Q':  # if true 
            return False