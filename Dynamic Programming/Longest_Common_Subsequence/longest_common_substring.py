

# method 3:
def longestCommonSubstr(S1, S2, n, m):
    dp= [[0 for j in range(m+1)] for i in range(n+1)]
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
    # print(dp)       # not giving the value like Lcs where each ele in the matrix used to mean like: 
    # considering till ith ele of string s1 and jth string till s2 what the ans will be
    # not able to write the recursive equation which can give ans like this
    return final