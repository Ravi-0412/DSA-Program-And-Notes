# shortest Common Supersequence will contain all the string in order except the lcs(we have to minus lcs to avoid its repitition) i.e every char we have to add only one
# and lcs will be common in both so write lcs only one time 
# will print length of shortest common supersequence
# logic: lcs will be common in both the string for sure 
# so just add the length of given strings and minus
# the length of the lcs to get the 'length of shortest common supersequence'


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


# to print the string 'shortest common supersequence'
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        x,y= len(str1), len(str2)
        i,j, ans= x,y, ""
        dp= self.lcs(x,y,str1,str2)
        print(dp)
        while(i>0 and j>0):
            if str1[i-1]== str2[j-1]:
                ans= str1[i-1] + ans
                i, j= i-1, j-1
            # in equal case only writing one of the string , thw path we had taken to reach the curr cell
            elif dp[i][j-1]> dp[i-1][j]:  
                    ans= str2[j-1] + ans
                    j-= 1
            # and in unequal cases only writing everytime in direction we will move
            else:
                ans= str1[i-1] + ans
                i-= 1
        # now write the remaining string if left any as we have to include all the ele 
        while(i>0):
            ans= str1[i-1] + ans
            i-= 1
        while(j>0):
            ans= str2[j-1] + ans
            j-= 1  
        return ans
            
    def lcs(self,x,y,s1,s2):
        dp= [[0 for j in range(y+1)] for i in range(x+1)]
        for i in range(1,x+1):
            for j in range(1,y+1):
                if s1[i-1]== s2[j-1]:
                    dp[i][j]= 1+ dp[i-1][j-1]
                else:
                    dp[i][j]= max(dp[i-1][j], dp[i][j-1])
        return dp

