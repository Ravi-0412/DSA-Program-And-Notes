# take the same string and find the longest common subsequence
# only this to change when both char are equal at same index
# in that case we have to exclude that count
# otherwise this char will be counted in both the subsequences
# but we have to count repeating char only 
#  and take max of other two like we used to case of unequal one


def LongestRepeatingSubsequence(s1):
    x=y= len(s1)
    dp= lcs(x,x,s1,s1)
    print("length of longest repeating subsequences is: ",dp[x][y])
    print("one of the longest repeating subsequences is: ", printing_longest_repeating_subsequence(x,y,s1,s1,dp))
    

def printing_longest_repeating_subsequence(x,y,s1,s2,dp):  # will print the one of the longest repeating subsequences, not all
                                                           # for printing do same as we have done while printing all longest common subsequences
    i,j,ans= x,y, ""
    while(i>0 and j>0):   # just logic of lcs, traverse the path in reverse direction
        if s1[i-1]== s2[j-1] and i!=j:  # exacly same as printing lcs
            ans= s1[i-1] + ans
            i,j= i-1, j-1
        else:
            if dp[i][j-1]>= dp[i-1][j]:
                j-= 1
            else:
                i-= 1
    return ans

def lcs(x,y,s1,s2):
    dp= [[0 for j in range(y+1)] for i in range(x+1)]
    for i in range(1,x+1):
        for j in range(1,y+1):
            if s1[i-1]== s2[j-1] and i!=j:  # the variation from lcs
                dp[i][j]= 1+ dp[i-1][j-1]
            else: # this will cover the above if also when i==j and when s1[i-1]!=s2[j-1]
                dp[i][j]= max(dp[i-1][j], dp[i][j-1])
    return dp

LongestRepeatingSubsequence("AABEBCDD")
# LongestRepeatingSubsequence("aabb")
