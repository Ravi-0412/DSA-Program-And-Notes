# will print length of shortest common supersequence
# logic: lcs will be common in both the string for sure
# so just add the length of given string and minus
# the length of the lcs to get the ans
# as you can delete only the common char not any extra char
# after deleting lcs after merging both the strings, you will be
# left with minimal string that will contain the both the given string as subsequences within it
def shortestCommonSupersequence(x,y,s1,s2):
        lcs_length= lcs(x,y,s1,s2)
        return x+y-lcs_length
def lcs(x,y,s1,s2):
    dp= [[0 for j in range(y+1)] for i in range(x+1)]
    for i in range(1,x+1):
        for j in range(1,y+1):
            if s1[i-1]== s2[j-1]:
                dp[i][j]= 1+ dp[i-1][j-1]
            else:
                dp[i][j]= max(dp[i-1][j], dp[i][j-1])
    return dp[x][y]

# s1= "qpqrr"
# s2= "pqprqrp"
# s1= "abcbdab"
# s2= "bdcaba" 
s1= "abcd"
s2 = "xycd"

x,y= len(s1), len(s2)
print("the length of shortest common supersequence is: ")
print(shortestCommonSupersequence(x,y,s1,s2))


# best one: will give the possible supersequences
