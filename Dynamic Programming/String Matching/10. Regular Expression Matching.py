# only difference from "44. Wildcard Matching" is the meaning of "*".
# in "44. Wildcard Matching", "*" can match to any sequence of char , doesn't depend on the pre char before "* but in this Q
# "*" can 1) either match to zero char or 2) one or more char when characters in string is same char as char before "*" in pattern. 
# just like we write the regular expression.

# 'a*' means: ["", a, aa, aaa, aaaa, ....], this can match to zero or more a 
# simlarly '.*' means: ["", ., .., ..., & so on] . 
# Given: ".*" means "zero or more (*) of any character (.)".

# for understanding better draw tree of pattern comparing with sring.

# Method 1: Better one

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n= len(s), len(p)
        return self.helper(m, n, s, p)
    
    def helper(self, m, n, s, p):
        if n== 0:
            return m== 0
        if m== 0: # n!= 0
            # then remaining char of 'p' must be either : 1) s[0]*. Since matches '0' or more prev char  or 2) .* 
            # Other than these two all combination will be invalid.
            for i in range(n-1, -1, -1):
                if i== n-1 and p[i]!= "*":
                    # Last char must be '*'.
                    return False
                elif p[i]!= (s[0] or '.'):
                    return False
            return True 

        if s[m-1]== p[n-1] or p[n-1]== '.':  # decr both indexes by '1'
            if self.helper(m-1, n-1, s, p):
                return True
        elif p[n-1]== '*':
            if n-2>= 0 and (s[m-1]== p[n-2] or p[n-2]=='.') :  
                if self.helper(m, n-1, s, p) or self.helper(m-1, n, s, p):
                    return True
        return False

# Memoised this later 


# Method 2: 


# neetcode video
# base case when i>= len(s) and j is not out of bond will get handled by the case when we don't use the "*" and return false simply.
# take this and check.1) s= a, p= a*b*c(or .*) and let i out of bound by matching with "*" and j still at '0' 
# we will get true by taking the path "don't use '*' "

# if no "*" then will get handled by "return 'False' "

# simle thing keep in mind: if "*" comes then we have two choice 1) either skip it simply(incr 'j' by 2) or
# 2) use "*" again and again if there is match. if not match then simply return False
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.dfs(0, 0, s, p)
    
    def dfs(self, i, j, s, p):
        if j>= len(p):  # then 'i' must be also out of bound
            return i>= len(s)
        # check if char is matching and store them in variable instead of using 'if' condition again and again
        match= i< len(s) and (s[i]== p[j] or p[j]=='.')   # in this there will be match 
        # check if p[j+1]== "*"
        if (j+1) < len(p) and p[j+1]== "*":
            return (self.dfs(i, j+2, s, p) or                 # don't use '*'
                   (match and self.dfs(i+1, j, s, p)))   # if match then use "*" further again and again
        if match:  # same as wildcard
            return self.dfs(i+1, j+1, s, p)
        # in all other cases return False
        return False

# Brute force of above one but got submitted.
# here handled the base case of "i>= len(s)" clearly 
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.dfs(0, 0, s, p)
    
    def dfs(self, i, j, s, p):
        if j>= len(p):  # then 'i' must be also out of bound
            return i>= len(s)
        # if i>= len(s) then only chance if we can get True if there is alternate '*' and
        # we have to skip the "*" and for that 'j+1' < len(s).
        if i>= len(s):  
            return j+1 < len(p) and p[j+1]== "*" and self.dfs(i, j+2, s, p)
        # check if char is matching and store them in variable instead of using 'if' condition again and again
        match= i< len(s) and (s[i]== p[j] or p[j]=='.')   # in this there will be match 
        # check if p[j+1]== "*"
        if (j+1) < len(p) and p[j+1]== "*":
            return (self.dfs(i, j+2, s, p) or                 # don't use '*'
                   (match and self.dfs(i+1, j, s, p)))   # if match then use "*" further again and again
        if match:  # same as wildcard
            return self.dfs(i+1, j+1, s, p)
        # in all other cases return False
        return False

# memoised one
# time: O(m*n)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp= [[-1 for j in range(len(p)+1)] for i in range(len(s)+1)]
        return self.dfs(0, 0, s, p, dp)
    
    def dfs(self, i, j, s, p, dp):
        if j>= len(p):  # then 'i' must be also out of bound
            return i>= len(s)
        # if i>= len(s) then only chance if we can get True if there is alternate '*' and
        # we have to skip the "*" and for that 'j+1' < len(s).
        if i>= len(s):  
            return j+1 < len(p) and p[j+1]== "*" and self.dfs(i, j+2, s, p, dp)
        if dp[i][j]!= -1:
            return dp[i][j]
        # check if char is matching and store them in variable instead of using 'if' condition again and again
        match= i< len(s) and (s[i]== p[j] or p[j]=='.')   # in this there will be match 
        # check if p[j+1]== "*"
        if (j+1) < len(p) and p[j+1]== "*":
            dp[i][j]= (self.dfs(i, j+2, s, p, dp) or                 # don't use '*'
                   (match and self.dfs(i+1, j, s, p, dp)))   # if match then use "*" further again and again
            return dp[i][j]
        if match:  # same as wildcard
            dp[i][j]= self.dfs(i+1, j+1, s, p, dp)
            return dp[i][j]
        dp[i][j]= False
        return dp[i][j]

# Tabulation
# will do later


