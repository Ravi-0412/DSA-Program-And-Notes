# method 1: Brute Force
# take another 2D array for ans and keep checking the ele from original matrix and keep updating the res in 'ans' matrix.
# time= Space= O(m*n)

class Solution(object):
    def setZeroes(self, matrix):
        if not matrix:
            return
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Create a copy of the original matrix
        matrix_copy = [row[:] for row in matrix]
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    # Set entire row to zero
                    for k in range(cols):
                        matrix_copy[i][k] = 0
                    # Set entire column to zero
                    for k in range(rows):
                        matrix_copy[k][j] = 0
        
        # Copy the modified matrix back to the original
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = matrix_copy[i][j]

# Java
"""
class Solution {
    public void setZeroes(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return;
        }
        
        int rows = matrix.length;
        int cols = matrix[0].length;
        
        int[][] matrixCopy = new int[rows][cols];
        
        // Create a copy of the original matrix
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                matrixCopy[i][j] = matrix[i][j];
            }
        }
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] == 0) {
                    // Set entire row to zero
                    for (int k = 0; k < cols; k++) {
                        matrixCopy[i][k] = 0;
                    }
                    // Set entire column to zero
                    for (int k = 0; k < rows; k++) {
                        matrixCopy[k][j] = 0;
                    }
                }
            }
        }
        
        // Copy the modified matrix back to the original
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                matrix[i][j] = matrixCopy[i][j];
            }
        }
    }
}
"""
# method 2: 
# just store the rows and cols for which we have to make all ele zero.
# time: O(m*n), space= O(m+n)
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
"""
instead of taking rows and cols array separately to mark ,we can do marking inplace .
whenver we we will find any ele 'zero' we will mark the 1st ele of that row and col as zero denoting,
 we have to make all ele of this row and col to 'zero' later.

In this way our whole 1st row ans 1st column will tell what all column and rows respectively, we have to make zero.
Here for marking it's also taking O(m + n) space but it is inplace.

Note: we will start updating from (1,1) because 0th row and 0th col we have used for marking.
So if we start marking from '0'th row and '0'th col then it may unnecessarily make a lot of rows and column zero because it will override the value.
So we will handle whether we have to mark '0'th row and '0'th column separately.

e.g: matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]
1) if we start from (1,1) then, When we find matrix[1][1] = 0, we mark the first row and first column:
matrix = [
    [1, 0, 3],   
    [0, 0, 6],
    [7, 8, 9]
]

2) If we start from (0,0) then ,matrix[0][1] = 0 and immediately start zeroing out the row and column, corrupting the markers and causing the wrong cells to be zeroed out.
matrix = [
    [0, 0, 0],   # Wrong! The first row is corrupted before we finish processing.
    [0, 0, 0],
    [7, 8, 9]
]

# best: take leetcode 2nd example and do on pen and paper.
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

"""

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
// Method 1:
class Solution {
    public void setZeroes(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return;
        }
        
        int rows = matrix.length;
        int cols = matrix[0].length;
        
        int[][] matrixCopy = new int[rows][cols];
        
        // Create a copy of the original matrix
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                matrixCopy[i][j] = matrix[i][j];
            }
        }
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] == 0) {
                    // Set entire row to zero
                    for (int k = 0; k < cols; k++) {
                        matrixCopy[i][k] = 0;
                    }
                    // Set entire column to zero
                    for (int k = 0; k < rows; k++) {
                        matrixCopy[k][j] = 0;
                    }
                }
            }
        }
        
        // Copy the modified matrix back to the original
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                matrix[i][j] = matrixCopy[i][j];
            }
        }
    }
}

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

# C++ Code 
"""
// Method 1:
#include <vector>
using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) {
            return;
        }
        
        int rows = matrix.size();
        int cols = matrix[0].size();
        
        vector<vector<int>> matrixCopy(rows, vector<int>(cols));
        
        // Create a copy of the original matrix
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                matrixCopy[i][j] = matrix[i][j];
            }
        }
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] == 0) {
                    // Set entire row to zero
                    for (int k = 0; k < cols; k++) {
                        matrixCopy[i][k] = 0;
                    }
                    // Set entire column to zero
                    for (int k = 0; k < rows; k++) {
                        matrixCopy[k][j] = 0;
                    }
                }
            }
        }
        
        // Copy the modified matrix back to the original
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                matrix[i][j] = matrixCopy[i][j];
            }
        }
    }
};

//Method 2
#include <vector>

using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<bool> zeroRow(m, false);  // zeroRow[r] means all elements of row 'r' must be set to zero.
        vector<bool> zeroCol(n, false);  // zeroCol[c] means all elements of col 'c' must be set to zero.

        // First, find the rows and columns for which we have to make elements zero.
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (matrix[r][c] == 0) {
                    zeroRow[r] = true;
                    zeroCol[c] = true;
                }
            }
        }

        // Now, make all elements of those rows and columns zero.
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (zeroRow[r] || zeroCol[c]) {
                    matrix[r][c] = 0;
                }
            }
        }
    }
};
//Method 3
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        bool rowZero = false, colZero = false;  // will tell whether we have to make elements of row 0 and col 0 equal to zero or not.

        // First, find the rows and columns for which we have to make elements zero.
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (matrix[r][c] == 0) {
                    matrix[0][c] = 0;  // marking the columns
                    matrix[r][0] = 0;  // marking the rows
                    if (r == 0) rowZero = true;
                    if (c == 0) colZero = true;
                }
            }
        }

        // Now, make all elements of those rows and columns zero starting from (1, 1).
        for (int r = 1; r < m; r++) {
            for (int c = 1; c < n; c++) {
                if (matrix[r][0] == 0 || matrix[0][c] == 0) {
                    matrix[r][c] = 0;
                }
            }
        }

        // Marking the first column.
        if (colZero) {
            for (int r = 0; r < m; r++) {
                matrix[r][0] = 0;
            }
        }

        // Marking the first row.
        if (rowZero) {
            for (int c = 0; c < n; c++) {
                matrix[0][c] = 0;
            }
        }
    }
};
"""