# # method 1:
# # correct only but showing time limit exceed for bigger matrix
# # try again later by DP and Back Tracking
# # you can remove the variable p1,p2 also ..just for understanding purpose
# # page n: 14
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         return self.Paths(0,0, m, n)
    
#     def Paths(self,p1,p2,m,n):
#         count= 0
#         if n==1 or m==1:       # base case because after this there will be only one path
#         # if p1==m-1 or p2==n-1:  # either only right or only down
#             return 1
#         count+= Solution().Paths(p1+1,p2,m-1,n)   # when you choose down
#         count+= Solution().Paths(p1,p2+1,m,n-1)   # when you choose down
#         return count

# shorter one
def ways(r,c,n,m):
    if r==m or c==n:
        return 1
    return ways(r,c+1,m,n) + ways(r+1,c,m,n)   # right or down


# # Q)Print all the paths
# # def Paths(ans,m,n):      
# #     if n==1 and m==1:   # means you have reached the destination    
# #     # if p1==m-1 or p2==n-1:
# #         print(ans)
# #         return
# #     if m>1:  # call the function for 'down' until you reach the last row
# #         Paths(ans+ 'D', m-1, n)   # when you choose down
# #     if n>1: # call the function for 'down' until you reach the last col
# #         Paths(ans+ 'R', m, n-1)   # when you choose down

# # Paths("",3,3)


# # Q) you can go down, left as well as diagonally

# # def Paths(ans,m,n):      
# #     if n==1 and m==1:   # means you have reached the destination    
# #     # if p1==m-1 or p2==n-1:
# #         print(ans)
# #         return
# #     if m>1:  # call the function for 'down' until you reach the last row
# #         Paths(ans+ 'D', m-1, n)   # when you choose down
# #     if n>1: # call the function for 'down' until you reach the last col
# #         Paths(ans+ 'R', m, n-1)   # when you choose down
# #     if m>1 and n>1:    # when move in the diagonal m,n both >1.  & for this
# #                        # condition base case of count- if m>1 and n>1 and m==n:
# #                        # as after reaching just one diagonal before there will be 
# #                        # only one possible diagonal path
# #         Paths(ans + 'L', m-1, n-1)    # 'L' stands for diagonal movement

# # Paths("",3,3)


# # counts the path for above Q
# # You can also pass count as para in above soln 
# def Paths(m,n): 
#     count= 0     
#     if n==1 or  m==1:   # means you have reached the destination 
#                         # this condition will also handle the diagonal case
#                         # as getting either m==1 or n==1 means you have reached the destination
#                         # since both 'm' and 'n' will be always equal in case of diagonal   
#     # if p1==m-1 or p2==n-1:
#         return 1  
#     if m>1:  # call the function for 'down' until you reach the last row
#         count+= Paths(m-1, n)   # when you choose down
#     if n>1: # call the function for 'down' until you reach the last col
#         count+= Paths(m, n-1)   # when you choose down
#     if m>1 and n>1:    # when move in the diagonal m,n both >1.  & for this
#                        # condition base case of count- if m>1 and n>1 and m==n:
#                        # as after reaching just one diagonal before there will be 
#                        # only one possible diagonal path
#         count+= Paths(m-1, n-1)    # 'L' stands for diagonal movement
#     return count

# print(Paths(3,3))



# # method 2 : DP(memoization)
# # submitted on leetcode
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp= [[0 for j in range(n+1)] for i in range(m+1)]
#         return self.Paths(m, n, dp)  # we are starting from bottom-right(m, n) and trying to reach the starting grid(1,1)
    
#     def Paths(self, m, n, dp):
#         if n==1 or m==1:  # since we are starting from m and n so we will have to stop at 1,1
#             dp[m][n]= 1
#         if dp[m][n] != 0:
#             return dp[m][n]
#         else:
#             dp[m][n]= self.Paths(m-1, n, dp) + self.Paths(m, n-1, dp)  # when you take left or when you take up
#         return dp[m][n]


# # better one , no need to create array of (m+1)*(n+1)
# # Also it will give ans of even subproblems like no of ways from (0,0) to any grid directly
# # logic: we are traversing opposite i.e from bottom- right to (0,0) so we can go either left or up
# # if you want to start from (0,0) and want to reach (m-1,n-1) just use the 1st method by taking two more parameter in the function
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp= [[-1 for j in range(n)] for i in range(m)]
#         return self.Paths(m-1, n-1, dp)  # we are starting from bottom-right(m-1, n-1) and trying to reach the starting grid(0,0)
    
#     def Paths(self, m, n, dp):
#         if n==0 or m==0:  # since we are starting from m-1 and n-1 so this means we are in the destination row or destination col 
#             dp[m][n]= 1   # and there will be only one path to reach 0,0 after this either you go left only or up only
#         if dp[m][n] != -1:
#             return dp[m][n]
#         else:  # since base case is 'OR' so we no need to check value of m and n. if it will be 'AND' then we will have to check it like if m>0 and n>0 separately and we have to add both
#             dp[m][n]= self.Paths(m-1, n, dp) + self.Paths(m, n-1, dp)  # when you take left or when you take up
#         return dp[m][n]


# # Top down approach
# # traversing from bottom right ang trying to reach the starting point
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp= [[0 for j in range(n)] for i in range(m)]
#         # initialise the last row and col with one as after reaching there, there will be only one possible path
#         for i in range(m):
#             for j in range(n):
#                 if i== m-1 or j== n-1:
#                     dp[i][j]= 1
#         # now for each cell there will be two choice either take down or take right
#         for i in range(m-2, -1, -1):
#             for j in range(n-2, -1, -1):
#                 dp[i][j]= dp[i+1][j] + dp[i][j+1]
#         return dp[0][0]

# # if you start from (0,0) and want to go (m-1, n-1)
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp= [[1 for j in range(n)] for i in range(m)]
#         for i in range(1,m):
#             for j in range(1, n):
#                 dp[i][j]= dp[i-1][j] + dp[i][j-1]    # either take up or left
#         return dp[m-1][n-1]

# another method when you start from (0,0) and want to go (m-1, n-1)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = 1 

        for i in range(m):
            for j in range(n):
                if i >0:
                    dp[i][j] += dp[i-1][j]
                if j >0:
                    dp[i][j] += dp[i][j-1]
        return dp[-1][-1]

#  i don't know what mistake i am making in this method
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp= [[-1 for j in range(n)] for i in range(m)]
        return self.Paths(m-1, n-1, dp)  # we are starting from bottom-right(m-1, n-1) and trying to reach the starting grid(0,0)
    def Paths(self, m, n, dp):
        if m== 0 or n==0:
            dp[m][n]= 1
        if dp[m][n] != -1:
            return dp[m][n]
        if m >0: 
            dp[m][n]+= self.Paths(m-1, n, dp)
        if n >0: 
            dp[m][n]+= self.Paths(m, n-1, dp)
        return dp[m][n]
ob= Solution()
print(ob.uniquePaths(3,3))
