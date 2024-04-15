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
