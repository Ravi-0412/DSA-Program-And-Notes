# REcursive way:
# Time Complexity: O( 3^(m*n)*n). have to verify from someone
# method correct only
def getMaxPathSum(matrix):
    row,col= len(matrix), len(matrix[0])
    maxSum= -999999
    
    for i in range(col):  # calling the function with each cell from last row for getting the maximum 
        maxSum= max(maxSum,helper(row-1,i,matrix))
    return maxSum
                    
def helper(r,c,mat):
    if r<0 or r>=len(mat) or c<0 or c>= len(mat[0]): # out of bound cases and False cases
        return 0
    if r== 0:   # after you reach the 1st row, simply return the value
        return mat[r][c]
    up=    mat[r][c] + helper(r-1, c, mat)    # when you take up
    left=  mat[r][c] + helper(r-1, c-1, mat)  # when you take left diagonal
    right= mat[r][c] + helper(r-1, c+1, mat)  # when you take the right diagonal
    return max(up,left,right)


# optimise by memoization, tabulation and later do space optimisation
# just similar to other Q
# giving correct ans on online compiler but on coding ninja giving wrong for one test case. correct only
def getMaxPathSum(matrix):
    row,col= len(matrix), len(matrix[0])
    maxSum= -999999
    dp= [[-1 for j in range(col)] for i in range(row)]
    for i in range(col):  # calling the function with each cell from last row for getting the maximum 
        maxSum= max(maxSum,helper(row-1,i,matrix,dp))
    return maxSum
                    
def helper(r,c,mat,dp):
    if r<0 or r>=len(mat) or c<0 or c>= len(mat[0]): # out of bound cases and False cases
        return 0
    if r== 0:   # after you reach the 1st row, simply return the value
        dp[r][c]= mat[r][c]
        return dp[r][c]
    if dp[r][c]!= -1:
        return dp[r][c]
    up=    mat[r][c] + helper(r-1, c, mat,dp)    # when you take up
    left=  mat[r][c] + helper(r-1, c-1, mat,dp)  # when you take left diagonal
    right= mat[r][c] + helper(r-1, c+1, mat,dp)  # when you take the right diagonal
    dp[r][c]= max(up,left,right)
    return dp[r][c]



