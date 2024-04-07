# by Recursion

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n= len(s), len(p)
        return self.helper(m, n, s, p)
    
    def helper(self, m, n, s, p):
        if n== 0:     # simplest one
            return m== 0
        
        # if 1st string get exhausted
        # then if all remainig char in 'p' is all "*" then return True else False
        if m==0:  
            for i in range(n-1,-1,-1):
                if p[i]!= '*':
                    return False
            return True
        
        if s[m-1]== p[n-1] or p[n-1]== '?':  # incr both indexes by '1'
            if self.helper(m-1, n-1, s, p):
                return True
        # when p[n-1]=="*", we have two choices 1)matching zero char with "*", move in pattern without keeping string index same
        # or match one or more char with "*", decr string index and keep pattern index same.
        elif p[n-1]== '*':  
            if self.helper(m, n-1, s, p) or self.helper(m-1, n, s, p):
                return True
        return False


# method 2: memoization
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n= len(s), len(p)
        dp= [[-1 for j in range(n+1)] for i in range(m+1)]
        return self.helper(m, n, s, p,dp)
    
    def helper(self, m, n, s, p, dp):
        if n== 0:     # simplest one
            return m== 0
        # if 1st string get exhausted
        # then if all remainig char in 'p' is all "*" then return True else False
        if m==0:
            for i in range(n-1,-1,-1):
                if p[i]!= '*':
                    return False
            return True
        if dp[m][n]!= -1:
            return dp[m][n]
        if s[m-1]== p[n-1] or p[n-1]== '?':
            dp[m][n]= self.helper(m-1, n-1, s, p, dp)
        elif p[n-1]== '*':
            dp[m][n]= self.helper(m, n-1, s, p, dp) or self.helper(m-1, n, s, p, dp)
        else: # in all other cases simply return False
            dp[m][n]= False
        return dp[m][n] 

# method 3: Tabulation
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n= len(s), len(p)
        dp= [[-1 for j in range(n+1)] for i in range(m+1)]
        # initailise with base cases
        dp[0][0]= True   # if n== 0 and m== 0
        for i in range(1,m+1):  # if n==0 and m!= 0 i.e 1st column
            dp[i][0]= False
        for i in range(1,n+1):  # if m==0
            flag= True
            for j in range(i-1,-1,-1):
                if p[j]!= '*':
                    flag= False
            dp[0][i]= flag
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1]== p[j-1] or p[j-1]== '?':
                    dp[i][j]= dp[i-1][j-1] 
                elif p[j-1]== '*':
                    dp[i][j]= dp[i][j-1] or dp[i-1][j] 
                else: # in all other cases simply return False
                    dp[i][j]= False
        return dp[m][n]


# method 4: space optimised to O(n)
# for base case 0th row means previous and other than zero means curr
# so initialise based on the actual means of row and col 
# we have to initialise 'curr' for every row 
# so after every row make check condition

# and in for loop 'dp[i-1]' means pre and 'dp[i]' means curr 
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n= len(s), len(p)
        # initialising 1st row
        pre= [False for i in range(n +1)]
        pre[0]= True 
        for i in range(1,n+1):  # if m==0
            flag= True
            for j in range(i-1,-1,-1):
                if p[j]!= '*':
                    flag= False
            pre[i]= flag
            
        curr= [False for i in range(n +1)]
        for i in range(1, m+1):
            curr[0]= False  # zeroth col of each row should be False
            for j in range(1, n+1):
                if s[i-1]== p[j-1] or p[j-1]== '?':
                    curr[j]= pre[j-1] 
                elif p[j-1]== '*':
                    curr[j]= curr[j-1] or pre[j] 
                else: # in all other cases simply return False
                    curr[j]= False
            pre= curr.copy()
        return pre[n]

