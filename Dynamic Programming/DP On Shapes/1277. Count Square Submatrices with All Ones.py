# method 1: 
# Recursion


"""
Logic: Har ek cell (r, c) se check kar rhe ki maximum kitne side ka square form kar sakte h.
Iske liye hmko 3 direction ka length ka min lena hoga i.e (diagonally upper-left, upper_cell, left_cell) => 
min(r-1, c-1), (r, c- 1), (r-1, c)) and current cell ka '1' add karna hoga agar cur cell (r, c) ka value '1' h tb.

Let cur cell se ans = 3 then means including this cell we can form squre of side of length '3'.
But yahan number puch rha square ka then ye side '1' ka square  , side '2' and side '3' ka square form kar sakta h adjacent cell
se combine hoke. Isliye jo side aayega wahi mera count hoga(new squares) us cell ke liye.

Isse hm direct Tabulation DP likh sakte h, Top - Down . See method 4.
"""

"""
note: jyada dimag mat lagao recursion me , bs sahi logic socho or likh do.
Yahan (0, 0) se ja rhe isliye hmko check karne ka direction change karna hoga.
i.e min(down, right, lower_right diagonal).
"""

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col= len(matrix), len(matrix[0])
        ans= 0
        for r in range(row):
            for c in range(col):
                if matrix[r][c]== 1:
                    ans+= self.dfs(matrix, r, c)   # Add the side length i.e count of each cell.
        return ans
    
    # Will give side length if we include cur cell.
    def dfs(self, matrix, r, c):
        if r<0 or r>= len(matrix) or c<0 or c>= len(matrix[0]) or matrix[r][c]!= 1:
            return 0
        return 1 + min(self.dfs(matrix, r+1, c), self.dfs(matrix, r, c+1), self.dfs(matrix, r+1, c+1))  


# method 2: 
# memoization
# Time : O(m*n)

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



# method 3: 
# Tabulation (Bottom Up)
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
"""
time: O(m*n)= space
logic is totally same as above.

logic: just find the no of square matrix whose lower right corner is matrix[i][j].
for 1st row and 1st col, ans will be matrix value only.

why taking min of all three?
since we are considering square so from all the three sides it should be a valid square then,adding the current ele will make valid square only.
if we not take minimum of all three then it can't be a square, it can be a rectangle also.

why counting the square ending with bottom right corner not starting with?
because we only need to compare the three values but in later one we will have to find the no of square recursively.
"""


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
                if matrix[r][c] == 1:
                    dp[r][c]= 1+ min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])   # up, left, upper-left diagonal
                    ans+= dp[r][c]
        return ans


# Method 5: 
# Other way of write method 4
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[0 for j in range(col + 1)] for i in range(row + 1)]
        ans= 0
        for r in range(1, row + 1):
            for c in range(1, col + 1):
                if matrix[r-1][c-1] == 1:
                    dp[r][c]= 1+ min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])   # side length = min(up, left, upper-left diagonal)
                    ans += dp[r][c]  # new formed square using current cell = side_length only
        return ans

