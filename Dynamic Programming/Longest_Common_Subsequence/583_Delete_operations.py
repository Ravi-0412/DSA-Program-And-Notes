# submitted on GFG
class Solution:
    def minOperations(self, s1, s2):
	    x,y= len(s1), len(s2)
	    lcs_length= self.lcs(x,y,s1,s2)
	    # 1st make the 1st string equal to lcs itself
	    # for this we have to delete some char from 1st staring
	    no_deletion= x- lcs_length
	    # after deletion insert the char in left string(will be one of the lcs only)
	    # to make it equal to the 2nd string
	    no_insertion= y- lcs_length
	    total_operation= no_deletion + no_insertion
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


# Note: if only deletion would have allowed then ans will be equal to the cost of
# converting both strings to longest common subsequence
# this was the leetcode problem(but cost of both will be same only)

    
# if only insertion operations would have been allowed then 
# we will have to find the shortest common supersequences and we will 
# have to insert the char in both the strings to make its length equal to shortest supersequences
# total addition= (len(supersequences)- len(s1)) + (len(supersequences)- len(s2))

