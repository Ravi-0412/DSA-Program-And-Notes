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
# instead of taking rows and cols array separately to mark ,we can do marking inplace .
# whenver we we will find any ele 'zero' we will mark the 1st ele of that row and col as zero denoting,
#  we have to make all ele of this row and col to 'zero' later.

# In this way our whole 1st row ans 1st column will tell what all rows and column we have to make zero.
# Here for marking it's also taking O(m + n) space but it is inplace.

# Note: we will start updating from (1,1) because 0th row and 0th col we have used for marking.
# So if we start marking from '0'th row and '0'th col then it may unnecessarily make 0th row and 0th column zero.

# So we will handle whether we have to mark '0'th row and '0'th column separately.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n= len(matrix), len(matrix[0])
        rowZero, colZero= False, False # will tell whether we have to make ele of row= 0 and col = 0 equal to zero or not.                   
        # first find the rows and col for which we have to make ele zero
        for r in range(m):
            for c in range(n):
                if matrix[r][c]== 0:
                    matrix[0][c]= 0  # marking the columns
                    matrix[r][0]= 0  # marking the rows 
                    if r == 0:  # if any ele in row zero is '0'.
                        rowZero= True
                    if c == 0:
                        colZero = True
                        
        #now make all ele of those rows and col to zero starting from (1, 1).
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c]== 0:  # if first ele of either row or col of this ele is zero then make that cell= 0
                    matrix[r][c]= 0

        # marking the 1st row and col
        # for marking 1st col
        if colZero:
            for r in range(m):
                matrix[r][0]= 0
        
        # for marking 1st row.
        if rowZero:
            for c in range(n):
                matrix[0][c]= 0


# Java
"""
// Method 2:
class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        boolean[] zeroRow = new boolean[m];  // zeroRow[r] means all elements of row 'r' must be set to zero.
        boolean[] zeroCol = new boolean[n];  // zeroCol[c] means all elements of col 'c' must be set to zero.

        // First, find the rows and columns that need to be zeroed
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (matrix[r][c] == 0) {
                    zeroRow[r] = true;
                    zeroCol[c] = true;
                }
            }
        }

        // Now, set the elements of those rows and columns to zero
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (zeroRow[r] || zeroCol[c]) {
                    matrix[r][c] = 0;
                }
            }
        }
    }
}


// Method 3:
class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        boolean rowZero = false;
        boolean colZero = false;

        // Identify the rows and columns that need to be zeroed
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (matrix[r][c] == 0) {
                    matrix[0][c] = 0;  // Mark the column
                    matrix[r][0] = 0;  // Mark the row
                    if (r == 0) {
                        rowZero = true;  // First row has a zero
                    }
                    if (c == 0) {
                        colZero = true;  // First column has a zero
                    }
                }
            }
        }

        // Set matrix elements to zero based on the markers in the first row and column
        for (int r = 1; r < m; r++) {
            for (int c = 1; c < n; c++) {
                if (matrix[r][0] == 0 || matrix[0][c] == 0) {
                    matrix[r][c] = 0;
                }
            }
        }

        // Handle the first column if it needs to be zeroed
        if (colZero) {
            for (int r = 0; r < m; r++) {
                matrix[r][0] = 0;
            }
        }

        // Handle the first row if it needs to be zeroed
        if (rowZero) {
            for (int c = 0; c < n; c++) {
                matrix[0][c] = 0;
            }
        }
    }
}

"""