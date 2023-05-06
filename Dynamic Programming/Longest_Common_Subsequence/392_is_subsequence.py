# if s is a subsequence of 't' then lcs of 's' and 't'
# must be equal to the 's' itself as lcs of two strings is
# always less than or equal to the length of min(length of either string)
# time; O(n*m)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x,y= len(s), len(t)
        lcs_length= self.lcs(x,y,s,t)
        if lcs_length== x:  # check if length of lcs= len(substring)
            return True
        return False
    def lcs(self,x,y,s1,s2):
        dp= [[0 for j in range(y+1)] for i in range(x+1)]
        for i in range(1,x+1):
            for j in range(1,y+1):
                if s1[i-1]== s2[j-1]:
                    dp[i][j]= 1+ dp[i-1][j-1]
                else:
                    dp[i][j]= max(dp[i-1][j], dp[i][j-1])
        return dp[x][y]


# method 2:
# Best way yo solve is: using Two pointer
# logic: traverse both simultaneoulsy and when both char is same incr both pointer else incr pointer of 't' only(say 'j').

# 'i' will tell the no of char of 's' that we seen in 't' at any point of time.

# At last if value of 'i' >= len(s) means we have got all char of 's' in 't'.

# time: O(m + n)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j= 0, 0  # will point to 's' and 't' respectively
        while i < len(s) and j < len(t):
            if s[i]== t[j] :
                i+= 1
                j+= 1
            else:
                j+= 1 
        return i== len(s)  # means we have got all char of 's' in 't'.
    

    
