# method 1: Recursion
# time: O(2^(m*n))  # for every n^2 cell we have two choices
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.helper(0,0,triangle)   # starting from zeroth row, zeroth index 
    
    def helper(self,row,ind,triangle):
        if row== len(triangle) -1:   # after you reach the last row, return the value at that index in last row
            return triangle[row][ind]
        ith_val=      triangle[row][ind] + self.helper(row+1, ind, triangle)    # when you take the ith ind ele in next row
        next_ind_val= triangle[row][ind] + self.helper(row+1, ind+1, triangle)  # when you take the (i+1)th ind ele in next row
        return min(ith_val, next_ind_val)

# method 2: memoization(Bottom Up)
# time: O(n^2), n^2 subproblems 
# time: O(n^2), n^2: dp space + o(n): Recursion depth
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row= len(triangle)
        dp= [[-1 for j in range(row)] for i in range(row)]
        return self.helper(0,0,triangle,dp)   # starting from zeroth row, zeroth index 
    
    def helper(self,row,ind,triangle,dp):
        if row== len(triangle) -1:   # after you reach the last row, return the value at that index in last row
            dp[row][ind]= triangle[row][ind]
            return dp[row][ind]
        if dp[row][ind]!= -1:
            return dp[row][ind]
        ith_val=      triangle[row][ind] + self.helper(row+1, ind, triangle,dp)    # when you take the ith ind ele in next row
        next_ind_val= triangle[row][ind] + self.helper(row+1, ind+1, triangle,dp)  # when you take the (i+1)th ind ele in next row
        dp[row][ind]= min(ith_val, next_ind_val)
        return dp[row][ind]  # first ind of 1st row will give the ans


# method 3: Tabulation
# Note: if you have memoized using Bottom up then for tabulation go by Top down and vice versa
# because you will knowing the base case for larger ind only in case of bottom up and for smaller index in case of Top Down
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row= len(triangle)
        dp= [[-1 for j in range(row)] for i in range(row)]
        # initialising with base case i.e when you reach the last row
        for i in range(row):
            dp[row-1][i]= triangle[row-1][i]
        for i in range(row-2,-1,-1):
            for j in range(i+1):  # as no of ele in each row will be equal to no of row 
                ith_val=      triangle[i][j] + dp[i+1][j]     # when you take the ith ind ele in next row
                next_ind_val= triangle[i][j] + dp[i+1][j+1 ]  # when you take the (i+1)th ind ele in next row
                dp[i][j]= min(ith_val, next_ind_val)
        return dp[0][0]

# optimising space complexity to O(n)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row= len(triangle)
        pre= [-1 for i in range(row)]
        # initialising with base case with last row val
        for i in range(row):
            pre[i]= triangle[row-1][i]
        print(pre)
        for i in range(row-2,-1,-1):
            curr= [0 for i in range(i+1)]   # as no of ele in each row will be equal to no of row 
            for j in range(i+1):  
                ith_val=      triangle[i][j] + pre[j]     # when you take the ith ind ele in next row
                next_ind_val= triangle[i][j] + pre[j+1]  # when you take the (i+1)th ind ele in next row
                curr[j]= min(ith_val, next_ind_val)
            pre= curr.copy()
        return pre[0]

