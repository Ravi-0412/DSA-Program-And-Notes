# method 1: by memoization(Bottom up DP)
# tried on GFG , giving TLE
class Solution:
    def palindromicPartition(self, string):
        n, i, j= len(string), 0, len(string) -1
        dp= [[-1 for l in range(n +1)] for k in range(n + 1)]
        mn= 99999
        return self.helper(string, i, j, dp, mn)
    
    def helper(self, s, start, end, dp, mn):
        if start >= end:  # if equal means single char so no need to cut anymore
            return 0
        # if s[start: end+1]== s[start:end: -1]:  # means string is palindrome from start to end
        #     return 0
        s1= s[start: end+1]
        if s1== s1[::-1]:
            return 0
        if dp[start][end] != -1:
            return dp[start][end]
        for k in range(start, end):
            SmallAns= self.helper(s, start, k, dp, mn) + self.helper(s, k+1, end, dp, mn) + 1
            mn= min(mn, SmallAns)
            dp[start][end]= mn
        return mn


# METHOD 2 : tried by optimising the subproblem also but still giving TLE
# in this we checked whether the subproblem we are calling is already solved or not
class Solution:
    def palindromicPartition(self, string):
        n, i, j= len(string), 0, len(string) -1
        dp= [[-1 for l in range(n +1)] for k in range(n + 1)]
        mn= 99999
        return self.helper(string, i, j, dp, mn)
    
    def helper(self, s, start, end, dp, mn):
        if start >= end:  # if equal means single char so no need to cut anymore
            return 0
        # if s[start: end+1]== s[end:start-1: -1]:  # means string is palindrome from start to end
        #     return 0
        s1= s[start: end+1]
        if s1== s1[::-1]:
            return 0
        if dp[start][end] != -1:
            return dp[start][end]
        for k in range(start, end):
            left, right= 0, 0
            s2= s[start: k+1]
            s3= s[k+1: end +1]
            if dp[start][k]!= -1:
                left= dp[start][k]
            elif s2== s2[::-1]:
                left= 0
                dp[start][k]= left
            else:
                left= self.helper(s, start, k, dp, mn)
                dp[start][k]= left
            if dp[k+1][end]!= -1:
                right= dp[k+1][end]
            elif s3== s3[::-1]:
                right= 0
                dp[k+1][end]= right
            else:
                right= self.helper(s, k+1, end, dp, mn)
                dp[k+1][end]= right
                
            SmallAns= left + right + 1
            mn= min(mn, SmallAns)
            dp[start][end]= mn
        return mn



# Also try to understand the 'Striver code and logic'
