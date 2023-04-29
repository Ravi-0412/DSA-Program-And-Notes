# if we make a matrix and make the value at coordinates of matrix= 1 then our Q reduces to " find the max prefix sum of rectangle of size x*y".

# i tried to do by same way but able to traverse the matrix of size x*y to find the ans.

# But this will only work if there is no point on right edge and lower edge of rectangle.
# in Q it is given points can be on the edge also.

# have to ask someone the approach for both cases

# note: in matrix row->x_coordinate, col->y_coordinate

def maximumPoints(points, x, y):
    # create a 2d matrix with no_row= max(x_coordiante) +  and no_col= max(y_coordinate ) + 1. "1" for 1-based indexing since points is given in 1-based
    # finding max value of x and y y_coordinate and storing them into row and col.
    row, col= 1, 1  # minimum no of row and col can be '1'
    for point in points:
        x1, y1= point
        row= max(row, x1)
        col= max(col, y2)
    # make 2d matrix 
    mat= [[0 for j in range(col +1)] for i in range(row + 1)]
    # make mat value= 1 where point is present
    for point in points:
        x1, y1= point
        mat[x1][y1]= 1
    
    # now find the prefix sum of rectangle from (0,0) to (i, j). we can store in same matrix
    for i in range(1, row +1):
        prefixSum= 0
        for j in range(1, col + 1):
            prefixSum+= matrix[i][j]
            above= mat[i-1][j]
            mat[i][j]= prefixSum + above
    
    # Now go through all rectangle of dimension x*y starting from (0,0) and find the ans
    for i in range(col- y):  # this much time you have to go below for sub-boxes
        for j in range(col -x):   # this much time you have to go right for sub-boxes
            row1, col1, row2, col2= i, i, i, 
            