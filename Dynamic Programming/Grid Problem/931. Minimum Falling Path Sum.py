#Logic: we are going top-bottom.
# for any cell (i, j), ans = matrix[i][j] +  min(matrix[i - 1][j], matrix[i - 1][j + 1], matrix[i - 1][j - 1])
# Note: we have to handle the case for first row and last row

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if j == 0:
                    matrix[i][j] = matrix[i][j] + min(matrix[i - 1][j], matrix[i - 1][j + 1])
                elif j == len(matrix[0]) - 1:
                    matrix[i][j] = matrix[i][j] + min(matrix[i - 1][j],  matrix[i - 1][j - 1])
                # every other column will have three paths coming from above
                else:
                    matrix[i][j] = matrix[i][j] +  min(matrix[i - 1][j], matrix[i - 1][j + 1], matrix[i - 1][j - 1])
        
        # Now that minimum falling sums for each value at the bottom row have been computed
        # We can just take the min of the bottom row to get the smallest overall path sum
        return min(matrix[len(matrix) - 1])

# java
"""
class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;

        for (int i = 1; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (j == 0) {
                    matrix[i][j] += Math.min(matrix[i - 1][j], matrix[i - 1][j + 1]);
                } else if (j == cols - 1) {
                    matrix[i][j] += Math.min(matrix[i - 1][j], matrix[i - 1][j - 1]);
                } else {
                    matrix[i][j] += Math.min(matrix[i - 1][j], Math.min(matrix[i - 1][j + 1], matrix[i - 1][j - 1]));
                }
            }
        }

        // Now that minimum falling sums for each value at the bottom row have been computed
        // We can just take the min of the bottom row to get the smallest overall path sum
        int minSum = Integer.MAX_VALUE;
        for (int j = 0; j < cols; j++) {
            if (matrix[rows - 1][j] < minSum) {
                minSum = matrix[rows - 1][j];
            }
        }

        return minSum;
    }
}

"""