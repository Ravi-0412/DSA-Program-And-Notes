
# method 1: recursive.
# note: jyada dimag mat lagao recursion me , sb sahi logic socho or likh do.
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/solutions/441414/c-intuitive-solution-recursion-with-memoization/
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col= len(matrix), len(matrix[0])
        ans= 0
        for r in range(row):
            for c in range(col):
                if matrix[r][c]== 1:
                    ans+= self.dfs(matrix, r, c)
        return ans
    
    def dfs(self, matrix, r, c):
        if r<0 or r>= len(matrix) or c<0 or c>= len(matrix[0]) or matrix[r][c]!= 1:
            return 0
        return 1 + min(self.dfs(matrix, r+1, c), self.dfs(matrix, r, c+1), self.dfs(matrix, r+1, c+1))  # down, right, lower diagonal

# method 2: memoization
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col= len(matrix), len(matrix[0])
        dp= [[-1 for j in range(col +1)] for i in range(row +1)]
        ans= 0
        for r in range(row):
            for c in range(col):
                if matrix[r][c]== 1:
                    ans+= self.dfs(matrix, r, c, dp)
        return ans
    
    def dfs(self, matrix, r, c, dp):
        if r<0 or r>= len(matrix) or c<0 or c>= len(matrix[0]) or matrix[r][c]!= 1:
            return 0
        if dp[r][c]!= -1:
            return dp[r][c]
        dp[r][c]= 1 + min(self.dfs(matrix, r+1, c, dp), self.dfs(matrix, r, c+1, dp), self.dfs(matrix, r+1, c+1, dp))  # down, right, lower diagonal
        return dp[r][c]

# method 3: Tabulation (Bottom Up)
# in above approaches, we are just adding the ans of every cell to our final ans.
# and ans of any cell, we are calculating by seeing the three values (down, right and right diagonal).
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col= len(matrix), len(matrix[0])
        dp= [[0 for j in range(col +1)] for i in range(row +1)]  # got initialised with base case.
        ans= 0
        for r in range(row-1, -1, -1):
            for c in range(col-1, -1, -1):
                if matrix[r][c]== 1:
                    dp[r][c]= 1 + min(dp[r+1][c], dp[r][c+1], dp[r+1][c+1])
                    ans+= dp[r][c]
        return ans

# method 4: Tabulation (top Down)
# time: O(m*n)= space
# logic is totally same as above.

# logic: just find the no of matrix whose lower right corner is matrix[i][j].
# for 1st row and 1st col, ans will be matrix value only.

# why taking min of all three?
# since we are considering square so from all the three sides it should be a valid square then,adding the current ele will make valid square only.
# if we not take minimum of all three then it can't be a square, it can be a rectangle also.

# why counting the square ending with bottom right corner not starting with?
# because we only need to compare the three values but in later one we will have to find the no of square recursively.


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col= len(matrix), len(matrix[0])
        dp= [[0 for j in range(col)] for i in range(row)]
        ans= 0
        # initialising with base case
        for r in range(row):  # filing 1st col
            dp[r][0]= matrix[r][0]
            ans+= dp[r][0]
        for c in range(col):    # filing  1st row
            dp[0][c]= matrix[0][c]
            if c!= 0:  # for (0,0) we already added above
                ans+= dp[0][c]

        for r in range(1, row):
            for c in range(1, col):
                if matrix[r][c]== 0:
                    dp[r][c]= 0
                else:
                    dp[r][c]= 1+ min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])   # up, left, upper diagonal
                    ans+= dp[r][c]
        return ans

# writing recursive code of this will be very very tough.
# so just analyse and write the Tabulation.