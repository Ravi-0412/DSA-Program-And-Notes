# method 1: Brute Force
# take another 2D array for ans and keep checking the ele from original matrix and keep updating the res in 'ans' matrix.
# time= Space= O(n)

# method 2: 
# just store the rows and cols for which we have to make all ele zero.
# time: O(n), space= O(m+n)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n= len(matrix), len(matrix[0])
        zeroRow= [False]*m  # zeroRow[r] means all ele of row 'r' must be set to zero.
        zeroCol= [False]*n  # zeroCol[c] means all ele of col 'c' must be set to zero.
        # first find the rows and col for which we have to make ele zero
        for r in range(m):
            for c in range(n):
                if matrix[r][c]== 0:
                    zeroRow[r], zeroCol[c]= True, True
        
        #now make all ele of those rows and col to zero.
        for r in range(m):
            for c in range(n):
                if zeroRow[r] or zeroCol[c]:
                    matrix[r][c]= 0


# method 3:
# instead of taking rows and cols array separately to mark.
# we can do that inplace like we can use the 1st row and col of given matrix only to mark that.
# whenver we we will find any ele 'zero' we will mark the 1st ele of that row and col as zero denoting,
#  we have to make all ele of this row and col to 'zero'.

# but we will start updatig from (1,1) instead of (0,0) since we will updating also and 
# then after updating our first row and col can become zero leading to wrong ans.

# for updating frst row and col , we will keep one variable and will update first row and col at last.
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n= len(matrix), len(matrix[0])
        rowZero= False  # will tell whether we have to make ele of row= 0 equal to zero or not.
        # first find the rows and col for which we have to make ele zero
        for r in range(m):
            for c in range(n):
                if matrix[r][c]== 0:
                    matrix[0][c]= 0  # marking the columns
                    if r== 0:  # if any ele in row zero is '0'.
                        rowZero= True
                    else:  
                        matrix[r][0]= 0  # marking the rows 

        #now make all ele of those rows and col to zero.
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c]== 0:  # if first ele of either row or col of this ele is zero then make that cell= 0
                    matrix[r][c]= 0

        # marking the 1st row and col
        # for marking 1st col
        if matrix[0][0]== 0:
            for r in range(m):
                matrix[r][0]= 0
        
        # for marking 1st row.
        if rowZero:
            for c in range(n):
                matrix[0][c]= 0

