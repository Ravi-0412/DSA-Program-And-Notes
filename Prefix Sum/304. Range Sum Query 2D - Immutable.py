# method 1: 
# we can just find the prefixSum of rows from 'row1' to 'row2' , indices in range from 'col1' to col2'.

# time: O(row2- row1)= O(200). for finding sum of  region each time

class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        self.mat= matrix
        self.r= len(self.mat)   # no of row
        self.c= len(self.mat[0])  # no of column
        self.prefixSum= [[0]*self.c for i in range(self.r)]   # 2d array to store prefixSum of each row.
        for i in range(self.r):
            self.prefixSum[i][0]= self.mat[i][0]
            for j in range(1, self.c):
                self.prefixSum[i][j]= self.mat[i][j] + self.prefixSum[i][j-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum= 0
        for i in range(row1, row2 + 1):
            if col1 >=1:
                sum+= self.prefixSum[i][col2] - self.prefixSum[i][col1-1]
            else:
                sum+= self.prefixSum[i][col2]
        return sum


# method 2: 
# soo nicee logic.
# sumMat[i][j]= sum of rectangular matrix elements from (0,0) to (i, j)..   (don't all ele when we will traverse each row from row1 to row till col2 in row2).
# It is prefix sum of enclosed rectangle joining end points (0,0) to (i, j). Make rectangle on paper joining 1st coordinate as leftmost_uppermost point and 
# 2nd coordinate as rightmost_lowest point. joining both points will form diagonal of that rectangular area.

# for calculating sumMat[i][j], we can add the prefix of current row(i) till col(j)  with the sumMat value of just above row having same col i.e:
# sumMat[i][j]= prefix + sumMat[i-1][j]


# And to get ans in range: we will use the inclusion and exclusion principle
# see the link in diagram 

# Draw diagram then you will get the proper visualisation.
# time: O(1) to get the sum of region each time.
class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        row, col= len(matrix), len(matrix[0])
        self.sumMat= [[0]* (col +1) for i in range(row + 1)]   # using 1 based indexing for "sumMat" to handle the corner cases 
                                            # when either row1= 0 or col1= 0 while subtraction (row above and column left) and also to find the prefix sum of row '0' and col '0'.
        for i in range(row ):
            prefixSum= 0    # will store the preSum of each row.
            for j in range(col):
                prefixSum+= matrix[i][j]
                above= self.sumMat[i][j + 1]
                self.sumMat[i + 1][j + 1]= prefixSum + above
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sumMat[row2 + 1][col2 + 1] - self.sumMat[row2 + 1][col1] - self.sumMat[row1][col2 + 1] + self.sumMat[row1][col1]
    
# Java Code
"""
//Method 1
class NumMatrix {
    private int[][] prefixSum;
    private int r, c;

    public NumMatrix(int[][] matrix) {
        r = matrix.length;
        c = matrix[0].length;
        prefixSum = new int[r][c];

        // Compute prefix sum for each row
        for (int i = 0; i < r; i++) {
            prefixSum[i][0] = matrix[i][0];
            for (int j = 1; j < c; j++) {
                prefixSum[i][j] = matrix[i][j] + prefixSum[i][j - 1];
            }
        }
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        int sum = 0;
        for (int i = row1; i <= row2; i++) {
            if (col1 >= 1) {
                sum += prefixSum[i][col2] - prefixSum[i][col1 - 1];
            } else {
                sum += prefixSum[i][col2];
            }
        }
        return sum;
    }
}
//Method 2
class NumMatrix {
    private int[][] sumMat;

    public NumMatrix(int[][] matrix) {
        int row = matrix.length, col = matrix[0].length;
        sumMat = new int[row + 1][col + 1]; // Using 1-based indexing

        for (int i = 0; i < row; i++) {
            int prefixSum = 0; // Will store the prefix sum of each row
            for (int j = 0; j < col; j++) {
                prefixSum += matrix[i][j];
                int above = sumMat[i][j + 1];
                sumMat[i + 1][j + 1] = prefixSum + above;
            }
        }
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        return sumMat[row2 + 1][col2 + 1] - sumMat[row2 + 1][col1] - sumMat[row1][col2 + 1] + sumMat[row1][col1];
    }
}
"""

# C++ Code 
"""
//Method 1
#include <vector>

using namespace std;

class NumMatrix {
public:
    vector<vector<int>> prefixSum;
    int r, c;

    NumMatrix(vector<vector<int>>& matrix) {
        r = matrix.size();
        c = matrix[0].size();
        prefixSum.assign(r, vector<int>(c, 0));

        // Compute prefix sum for each row
        for (int i = 0; i < r; i++) {
            prefixSum[i][0] = matrix[i][0];
            for (int j = 1; j < c; j++) {
                prefixSum[i][j] = matrix[i][j] + prefixSum[i][j - 1];
            }
        }
    }

    int sumRegion(int row1, int col1, int row2, int col2) {
        int sum = 0;
        for (int i = row1; i <= row2; i++) {
            if (col1 >= 1) {
                sum += prefixSum[i][col2] - prefixSum[i][col1 - 1];
            } else {
                sum += prefixSum[i][col2];
            }
        }
        return sum;
    }
};
//Method 2
class NumMatrix {
public:
    vector<vector<int>> sumMat;

    NumMatrix(vector<vector<int>>& matrix) {
        int row = matrix.size(), col = matrix[0].size();
        sumMat.assign(row + 1, vector<int>(col + 1, 0)); // Using 1-based indexing

        for (int i = 0; i < row; i++) {
            int prefixSum = 0; // Will store the prefix sum of each row
            for (int j = 0; j < col; j++) {
                prefixSum += matrix[i][j];
                int above = sumMat[i][j + 1];
                sumMat[i + 1][j + 1] = prefixSum + above;
            }
        }
    }

    int sumRegion(int row1, int col1, int row2, int col2) {
        return sumMat[row2 + 1][col2 + 1] - sumMat[row2 + 1][col1] - sumMat[row1][col2 + 1] + sumMat[row1][col1];
    }
};
"""
