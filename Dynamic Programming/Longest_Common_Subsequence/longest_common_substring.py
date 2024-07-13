# logic: since we only need consecutive so if there is match then take the pre value 
# otherwise(if not match), make it zero . 
# but at last it may not give the final ans as in between we are making the value as zero also.
# ans will be the max of whole 2d Dp. so for this keep storing the ans in any other variable say 'count'

# method 1: Recursion
class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        return self.lcs(S1,S2,n,m,0)
    
    def lcs(self,s1,s2,n,m,count):
        if n== 0 or m== 0:
            return count   # instead of zero
        if s1[n-1]== s2[m-1]:
            return self.lcs(s1,s2,n-1,m-1,count+1)   # incr the count by '1'
        else:
            return max(count,max(self.lcs(s1,s2,n,m-1,0),self.lcs(s1,s2,n-1,m,0)))  # make the count= 0 in function

# method 2: memoization
# not able to write the memoised version, have to ask someone
# giving wrong ans
class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        dp= [[-1 for j in range(m+1)] for i in range(n+1)]
        return self.lcs(S1,S2,n,m,0,dp)
    
    def lcs(self,s1,s2,n,m,count,dp):
        if n== 0 or m== 0:
            return count
        if dp[n][m]!= -1:
            return dp[n][m]
        if s1[n-1]== s2[m-1]:
            dp[n][m]= self.lcs(s1,s2,n-1,m-1,count+1,dp)   # incr the count by '1'
        else:
            dp[n][m]= max(count,max(self.lcs(s1,s2,n,m-1,0,dp),self.lcs(s1,s2,n-1,m,0,dp)))  # make the count= 0 in function
        return dp[n][m]


# method 3:
def longestCommonSubstr(S1, S2, n, m):
    dp= [[0 for j in range(m+1)] for i in range(n+1)]  # dp[i][j]= store the ans from the last time when both has differed.
        # not giving the value like Lcs where each ele in the matrix used to mean like: 
        # considering till ith ele of string s1 and jth string till s2 what the ans will be
        # not able to write the recursive equation which can give ans like this.
    final= 0 #this will store the maximum common substring till any point
            # like when string char will not match then there may be chances that
            # already calculated common susbtring can be the final ans
    for i in range(1,n+1):
        for j in range(1,m+1):
            if S1[i-1]== S2[j-1]:
                dp[i][j]= 1+ dp[i-1][j-1]
            else:  # when doesn't match
                dp[i][j]= 0   # and in case of not match we are initialising with zero , will count again
            final= max(final,dp[i][j])   # after every check update final 
                                         # final is just storing the max till that point
                                         # because pre cal one before(making dp[i][j]= 0) can be also the maximum
    # print(dp)       # 
    return final
    