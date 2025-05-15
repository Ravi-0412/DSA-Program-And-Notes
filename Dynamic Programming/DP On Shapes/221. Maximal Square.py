# Logic: Just check how much side of square we can form from cur cell if cell value = 1.
# it will depend on side we can form from i.e min(left, up, upper_left_diagonal) + 1.

# Just same as : "1277. Count Square Submatrices with All Ones"

# Time : O(m *n)

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m , n = len(matrix) , len(matrix[0])
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    # find the min side of square formed by 
                    # its left, up, upper_left_diagonal
                    left = int(matrix[i][j - 1]) if j > 0 else 0
                    up =   int(matrix[i-1][j])   if i > 0 else 0
                    diagonal= int(matrix[i-1][j-1]) if i > 0 and j > 0 else 0
                    curSide = min(left , up, diagonal) + 1
                    maxArea = max(maxArea , curSide * curSide)
                    matrix[i][j] = str(curSide)
        return maxArea

# java
"""
class Solution {
    public int maximalSquare(char[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int maxArea = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == '1') {
                    int left = (j > 0) ? matrix[i][j - 1] - '0' : 0;
                    int up = (i > 0) ? matrix[i - 1][j] - '0' : 0;
                    int diagonal = (i > 0 && j > 0) ? matrix[i - 1][j - 1] - '0' : 0;

                    int curSide = Math.min(Math.min(left, up), diagonal) + 1;
                    matrix[i][j] = (char)(curSide + '0');

                    maxArea = Math.max(maxArea, curSide * curSide);
                }
            }
        }

        return maxArea;
    }
}
"""

# Method 2: If you don't want to modify the given matrix

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        max_side = 0
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1  # Edge cells can only form 1x1 squares
                    else:
                        dp[i][j] = min(
                            dp[i - 1][j],       # up
                            dp[i][j - 1],       # left
                            dp[i - 1][j - 1]    # diagonal
                        ) + 1
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side

# Java
"""
class Solution {
    public int maximalSquare(char[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }

        int m = matrix.length;
        int n = matrix[0].length;
        int maxSide = 0;

        // dp[i][j] will hold the side length of the largest square
        // whose bottom‑right corner is at (i, j)
        int[][] dp = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == '1') {
                    if (i == 0 || j == 0) {
                        // First row or first column can only form 1×1
                        dp[i][j] = 1;
                    } else {
                        // Extend the smaller square of the three neighbors
                        dp[i][j] = Math.min(
                            Math.min(dp[i - 1][j],     // up
                                     dp[i][j - 1]),    // left
                                     dp[i - 1][j - 1]  // diagonal
                        ) + 1;
                    }
                    // Track the largest side seen so far
                    maxSide = Math.max(maxSide, dp[i][j]);
                }
            }
        }

        // Area = side²
        return maxSide * maxSide;
    }
}
"""
