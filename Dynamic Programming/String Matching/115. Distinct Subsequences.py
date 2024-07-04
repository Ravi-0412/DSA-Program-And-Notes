# in string matching you will come across only two cases i.e 'matched' and 'not matched' always 
# for base case in string matching algo, base cases will be when :
# 1) when 2nd string becomes empty(2nd index becomes zero) 2) when first string becomes empty(1st index becomes=0) and  

# easy only just slight modifiction in lcs
# modification: 1) in case of char matches then we have two choices either include that char into the ans or 
# search for same char at different index in 's'
# 2) in case doesn't matches then search for char in 's' at different index i.e doesn't decr the index of 't' 
# as we have to find the no of subsequences that's it

# Note: instead of using indexes we can also do by slicing like i used to do seeing the Q.
# and in case of slicing use dictionary to memoise the solution.

# time: O(2^m *2^n)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n= len(s), len(t)
        return self.helper(m, n, s, t)
    
    def helper(self,m,n,s,t):
        if n== 0:  # it means we have found a match of all char in 't'
            return 1
        if m==0: # n!= 0 and m==0 means matched not found
            return 0
        matched,unMatched= 0,0
        if s[m-1]== t[n-1]:
            matched= self.helper(m-1, n-1, s, t) + self.helper(m-1, n, s, t)    #if you don't want to include the current matched one in ans.  
                                                                # so finding the another occur of same char at different index in given string 's'
        else:  # search for same char of 't' in 's' at different index
            unMatched= self.helper(m-1, n, s, t)
        return matched+ unMatched 


# shorter way
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n= len(s), len(t)
        return self.helper(m, n, s, t)
    
    def helper(self,m,n,s,t):
        if n== 0:
            return 1
        if m==0:
            return 0
        if s[m-1]== t[n-1]:
            return self.helper(m-1, n-1, s, t) + self.helper(m-1, n, s, t)    #if you don't want to include the current matched one in ans. 
                                                                # so finding the another occur of same char at different index in given string 's'
        # search for same char of 't' in 's' at different index
        return self.helper(m-1, n, s, t)


# memoization
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n= len(s), len(t)
        dp= [[-1 for j in range(n+1)] for i in range(m+1)]
        return self.helper(m, n, s, t, dp)
    
    def helper(self,m,n,s,t,dp):
        if n== 0:
            return 1
        if m==0:
            return 0
        if dp[m][n]!= -1:
            return dp[m][n]
        if s[m-1]== t[n-1]:
            dp[m][n]= self.helper(m-1, n-1, s, t,dp) + self.helper(m-1, n, s, t,dp)    
        else:
            dp[m][n]= self.helper(m-1, n, s, t, dp)
        return dp[m][n]


# Tabulation
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n= len(s), len(t)
        dp= [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):   # i was doing from 1 to 'm+1'. null to null is also a match
            dp[i][0]= 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]== t[j-1]:
                    dp[i][j]= dp[i-1][j-1] + dp[i-1][j]   
                else:
                    dp[i][j]= dp[i-1][j] 
        return dp[m][n]

# method 4: optimise space to O(n)


# Related Q:
# 1) 2222. Number of Ways to Select Buildings.
# Ans: There will be only two possibility i.e '101' and '010' so Q reduces to
# find the number of distinct subsequences of '101' and '010' in string and add them.
