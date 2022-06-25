
# Note: if only deletion is allowed then ans will be equal to the cost of
# converting both strings to longest common subsequence
# this was the leetcode problem(but cost of both will be same only)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        x,y= len(word1), len(word2)
        lcs_length= self.lcs(x,y,word1,word2)
	    # 1st make the 1st string equal to lcs itself
	    # for this we have to delete some char from 1st staring i.e delete the lcs
        no_deletion1= x- lcs_length
        # Now make the 2nd string equal to lcs itself
	    # for this we have to delete some char from 2nd staring i.e delete the lcs
        no_deletion2= y- lcs_length
        # after this length of both string will become equal and will be left with LCS only
        # so finally both string will become equal
        total_operation= no_deletion1 + no_deletion2
        return total_operation
    def lcs(self,x,y,s1,s2):
        dp= [[0 for j in range(y+1)] for i in range(x+1)]
        for i in range(1,x+1):
            for j in range(1,y+1):
                if s1[i-1]== s2[j-1]:
                    dp[i][j]= 1+ dp[i-1][j-1]
                else:
                    dp[i][j]= max(dp[i-1][j], dp[i][j-1])
        return dp[x][y]


# if only insertion operations would have been allowed then 
# we will have to find the shortest common supersequences and we will 
# have to insert the char in both the strings to make its length equal to shortest supersequences
# total addition= (len(supersequences)- len(s1)) + (len(supersequences)- len(s2))

