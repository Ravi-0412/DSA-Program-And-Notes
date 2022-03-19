# method 1:
# correct only but showing time limit exceed for bigger matrix
# try again later by DP and Back Tracking
# you can remove the variable p1,p2 also ..just for understanding purpose
# page n: 14
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.Paths(0,0, m, n)
    
    def Paths(self,p1,p2,m,n):
        count= 0
        if n==1 or m==1:       # base case because after this there will be only one path
        # if p1==m-1 or p2==n-1:  # either only right or only down
            return 1
        count+= Solution().Paths(p1+1,p2,m-1,n)   # when you choose down
        count+= Solution().Paths(p1,p2+1,m,n-1)   # when you choose down
        return count


# Q)Print all the paths
# def Paths(ans,m,n):      
#     if n==1 and m==1:   # means you have reached the destination    
#     # if p1==m-1 or p2==n-1:
#         print(ans)
#         return
#     if m>1:  # call the function for 'down' until you reach the last row
#         Paths(ans+ 'D', m-1, n)   # when you choose down
#     if n>1: # call the function for 'down' until you reach the last col
#         Paths(ans+ 'R', m, n-1)   # when you choose down

# Paths("",3,3)


# Q) you can go down, left as well as diagonally

# def Paths(ans,m,n):      
#     if n==1 and m==1:   # means you have reached the destination    
#     # if p1==m-1 or p2==n-1:
#         print(ans)
#         return
#     if m>1:  # call the function for 'down' until you reach the last row
#         Paths(ans+ 'D', m-1, n)   # when you choose down
#     if n>1: # call the function for 'down' until you reach the last col
#         Paths(ans+ 'R', m, n-1)   # when you choose down
#     if m>1 and n>1:    # when move in the diagonal m,n both >1.  & for this
#                        # condition base case of count- if m>1 and n>1 and m==n:
#                        # as after reaching just one diagonal before there will be 
#                        # only one possible diagonal path
#         Paths(ans + 'L', m-1, n-1)    # 'L' stands for diagonal movement

# Paths("",3,3)


# counts the path for above Q
# You can also pass count as para in above soln 
def Paths(m,n): 
    count= 0     
    if n==1 or  m==1:   # means you have reached the destination 
                        # this condition will also handle the diagonal case
                        # as getting either m==1 or n==1 means you have reached the destination
                        # since both 'm' and 'n' will be always equal in case of diagonal   
    # if p1==m-1 or p2==n-1:
        return 1  
    if m>1:  # call the function for 'down' until you reach the last row
        count+= Paths(m-1, n)   # when you choose down
    if n>1: # call the function for 'down' until you reach the last col
        count+= Paths(m, n-1)   # when you choose down
    if m>1 and n>1:    # when move in the diagonal m,n both >1.  & for this
                       # condition base case of count- if m>1 and n>1 and m==n:
                       # as after reaching just one diagonal before there will be 
                       # only one possible diagonal path
        count+= Paths(m-1, n-1)    # 'L' stands for diagonal movement
    return count

print(Paths(3,3))

