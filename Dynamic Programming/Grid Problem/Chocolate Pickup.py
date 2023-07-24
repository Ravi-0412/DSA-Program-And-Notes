# Q says they will always stay inside the grid and has to pick maximum no of chocolate, this means
# take max of all cases when they reach the last row

# 1st method: call the function separately for Alice and Bob and remove the common node visited by them.
# indirectly finding the max chocolates that Alice can pick and max chocolate that Bob can pick and then remove the common cell visited by them.

# Q: fixed starting point and variable ending point. so better go from top to bottom(i.e start from fixed points)
# if variable starting point and variable ending point. Then either go 'top to down' or 'bottom to top'

# method 2: Start path for Bob and Alice together
# Note: both will reach the destination simultaneously i.e last row because in every step we are going down.
# But yeah they might land on different col or on same col on last row.

# time complexity= O(3^n * 3^n)  # in each row both Alice and Bob has three choices
# space: O(n)
# submitted on coding ninjas. correct but giving TLE
def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    return helper(0,0,c-1,grid)   # similar to helper(0,0,0,c-1)  # first two para is starting point for Alice and last two for Bob but they will always move to the same row.

def helper(r,c1,c2,mat):
    if c1<0 or c1>= len(mat[0]) or c2<0 or c2>= len(mat[0]) : # out of bound cases and False cases
        return 0
    # when they reaches the last row destination
    if r== len(mat)-1:
        # check if Alice and both land up at the same col
        # if they are at same col then return the val only one 
        if c1== c2:
            return mat[r][c1]
        # if they land up at different col
        return mat[r][c1] + mat[r][c2]
 
    maxChocolates= 0
    # since they are moving simulataneously, for every one move of Alice Bob will have three options i.e
    #  in total there will be 3*3 different choices
    path= [-1,0,1]  # either they can go left diagonal, or down or right diagonal
    for Alice_col in range(3):  # there are three possible path
        for Bob_col in range(3):
            # check if Alice and bob are at the same col, add the value only one time
            if c1== c2:
                maxChocolates= max(maxChocolates, mat[r][c1] + helper(r+1,c1+ path[Alice_col], c2 + path[Bob_col], mat))
            else: # add values of both Alice and Bob
                maxChocolates= max(maxChocolates, mat[r][c1] + mat[r][c2] + helper(r+1,c1+ path[Alice_col],c2 + path[Bob_col], mat))
    return maxChocolates


# method 2: memoization
# logic: Here three variable is changing, so we need 3D dp but size will depend on max val each variable can go
# r can go till 'm' and  c1 and c2 can go till 'n'
# other things are totally similar to other Q

# Time complexity= O(m*n*n)*9, for every state we are running function '9' times
# space: O(m*n*n) + O(n) Recursive 
def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    dp= [[[-1 for k in range(c)] for j in range(c)] for i in range(r)]
    return helper(0,0,c-1,grid,dp)   # similar to helper(0,0,0,c-1)  # first two para is starting point of                                 for Alice and last two for Bob bu they will always move to the same                                 row so we can right the row only one time

def helper(r,c1,c2,mat,dp):
    if c1<0 or c1>= len(mat[0]) or c2<0 or c2>= len(mat[0]) : # out of bound cases and False cases
        return 0
    # when they reaches the last row destination
    if r== len(mat)-1:
        # check if Alice and both land up at the same col
        # if they are at same col then return the val only one 
        if c1== c2:
            dp[r][c1][c2]= mat[r][c1]
            return dp[r][c1][c2]
        # if they land up at different col
        dp[r][c1][c2]= mat[r][c1] + mat[r][c2]
        return dp[r][c1][c2]
    if dp[r][c1][c2]!= -1:
        return dp[r][c1][c2]

    maxChocolates= 0
    # since they are moving simulataneously, for every one move of Alice Bob will have three options i.e in total         there will be 3*3 different choices
    path= [-1,0,1]  # either they can go left diagonal, or down or right diagonal. instead of this do by for loop like in tabulation for more readable ans
    for Alice_col in range(3):  # there are three possible path   
        for Bob_col in range(3):
            # check if Alice and bob are at the same col, add the value only one time
            if c1== c2:
                maxChocolates= max(maxChocolates, mat[r][c1] + helper(r+1,c1+ path[Alice_col],c2 + path[Bob_col], mat, dp))
            else: # add values of both Alice and Bob
                maxChocolates= max(maxChocolates, mat[r][c1] + mat[r][c2] + helper(r+1,c1+ path[Alice_col],c2 + path[Bob_col], mat, dp))
    dp[r][c1][c2]= maxChocolates
    return dp[r][c1][c2]


# Method 3:
# Tabulation: Here three variable is changing so there will be three nested loops
# tabulation just means go from base case to up always
# after writing the base case just copy paste the code of recurrence inside the nested loop
def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    dp= [[[-1 for k in range(c)] for j in range(c)] for i in range(r)]
    # initialising with base case, for last row(1st 1D array)
    for alice in range(c):  
        for bob in range(c):
            if alice== bob:
                dp[r-1][alice][bob]= grid[r-1][alice]
            else:
                dp[r-1][alice][bob]= grid[r-1][alice] + grid[r-1][bob]
    # run the three nested loop
    # row will start from n-2 and col for alice and bob can range from 0 to c-1
    for row in range(r-2,-1,-1):
        for c1 in range(c):
            for c2 in range(c):
                maxChocolates= 0
                # either they can go left diagonal, or down or right diagonal i.e -1,0,+1
                for dc1 in range(-1,2):  # there are three possible path
                    for dc2 in range(-1,2):
                        if c1== c2 and c1+dc1>= 0 and c1+dc1 <c and c2+dc2>=0 and c2+dc2< c:
                            maxChocolates= max(maxChocolates, grid[row][c1] + dp[row+1][c1+ dc1][c2 + dc2])  
                        elif c1!= c2 and c1+dc1>= 0 and c1+dc1 <c and c2+dc2>=0 and c2+dc2< c:
                            maxChocolates= max(maxChocolates, grid[row][c1] + grid[row][c2] + dp[row+1][c1+ dc1][c2 + dc2])     
                dp[row][c1][c2]= maxChocolates
                                                               
    return dp[0][0][c-1]   # Alice started at (0,0) and Bob started at (0,m-1) so return dp[0][0][c-1]   .. This is the way we return the ans at last in tabulation
                            # return the dp value for which we have called the recursive function.
                            






