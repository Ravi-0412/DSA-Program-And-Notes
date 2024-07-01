# Here row and column is sorted in descending order.

# logic: "just we have to find the no of ele smaller than 0 in each row using binary search"

# starting from top_right .

# time: O(m + n)

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans= 0
        m, n = len(grid), len(grid[0])
        j = n- 1
        for i in range(m):
            while j >= 0 and grid[i][j] < 0:
                j -= 1
            ans += n- 1 -j   # this much no of ele is < 0 in 'i'th row.
        return ans


# other way when we start from 'top-right'
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        r, c, cnt = 0, n - 1, 0
        while r < m and c >= 0:
            if grid[r][c] < 0:
                cnt += m - r
                c -= 1
            else:
                r += 1
        return cnt

# Why calculation row wise.
# Because if you will write 'while loop' condition like : "240. Search a 2D Matrix II" then it will wrong ans.

# e.g: [[3,2],[-3,-3],[-3,-3],[-3,-3]] . It will give ans = 2 but ans should be = 6

# Why ?
# Because if inner while loop 'c' becomes < 0 at any row then outer while won't run for other remaining row.

# Note: To write in same way as "240. Search a 2D Matrix II", inner while loop must be replaced by 'if'.
# For this traverse in such a way that once we get any ele that can be ans then from that index all ele in that 
# row either 'left' or 'right' should be our ans.

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row , col = len(grid) , len(grid[0])
        r , c = 0, col - 1
        ans = 0
        while r < row and c >= 0:
            while c >= 0 and grid[r][c] < 0:
                c -= 1
            ans += col - c - 1
            r += 1
        return ans


# Method 2: Replaced inner 'while' with 'if'.
# starting from : Bottom - left

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row , col = len(grid) , len(grid[0])
        r , c = row - 1, 0
        ans = 0
        while r >= 0 and c < col:
            if grid[r][c] < 0 :
                # then in current row from column 'c' to last 'column' all will be negative only.
                ans += col - c
                r -= 1   # to check in next above row
            else:
                c += 1   # increase 'c' to get more smaller value
        return ans


# if we write method 2 using 'while loop instead of if'
# then it may go index out of bound because of 'c' is there is no negative number.
# For handling this we have to use 'if'.
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row , col = len(grid) , len(grid[0])
        r , c = row - 1, 0
        ans = 0
        while r >= 0 and c < col:
            while grid[r][c] >= 0 :
                c += 1
            ans += col - 1 -  c
            r -= 1   # to check in next above row
        return ans