"""
take the same string and find the longest common subsequence
only thing to change when both char are equal at same index
in that case we have to exclude that count,
otherwise this char will be counted in both the subsequences.
but we have to count repeating char only 
 and take max of other two like we used to case of unequal one.

vvi: we only have to check whether the curr char is present somewhere also in the string for repeating and for this 
only thing you have to keep in mind that when both char are equal then must not be at the same index that's it. 
 This is the only difference from lcs
this will mean that same char is present at somewhere also means it is repeating
"""

# 1st write the recursive equation

# method 1: memoized 
class Solution:
    def LongestRepeatingSubsequence(self, str):
	    n= len(str)
        dp= [[-1 for i in range(n+1)]for i in range(n+1)]
        return self.LCS(n, n, str, str, dp)
    
    def LCS(self, m, n, s1, s2, dp):
        if m==0 or n==0:
            return 0
        if dp[n][m]!= -1:
            return dp[n][m]
        elif s1[m -1] == s2[n -1] and m!= n:  # this will mean that there exist the same char somewhere in the given string
            dp[n][m]= 1+ self.LCS(m-1, n-1, s1, s2,dp)
        else: # s1[m -1] == s2[n -1] and this will cover the above if also when m==n and when s1[m-1]!=s2[n-1] and all the cases
            dp[n][m]= max (self.LCS(m, n-1, s1, s2,dp), self.LCS(m-1, n, s1, s2,dp))
        return dp[n][m]


# method 2: To print the string also
class Solution:
    def LongestRepeatingSubsequence(self, str):
        x = y = len(str)
        dp = self.lcs(x, x, str, str)
        # print("Length of longest repeating subsequence is: ")
        return dp[x][y]
        # print("One of the longest repeating subsequences is: ", self.printing_longest_repeating_subsequence(x, y, str, str, dp))
    
    def printing_longest_repeating_subsequence(self, x, y, s1, s2, dp):  
        # Will print one of the longest repeating subsequences, not all
        i, j, ans = x, y, ""
        while i > 0 and j > 0:
            # Traverse the DP table in reverse direction (similar to LCS)
            if s1[i-1] == s2[j-1] and i != j:  
                ans = s1[i-1] + ans
                i, j = i-1, j-1
            else:
                if dp[i][j-1] >= dp[i-1][j]:
                    j -= 1
                else:
                    i -= 1
        return ans

    def lcs(self, x, y, s1, s2):
        dp = [[0 for j in range(y+1)] for i in range(x+1)]
        for i in range(1, x+1):
            for j in range(1, y+1):
                # Slight variation of LCS where we ensure that i != j to avoid picking the same character at the same index
                if s1[i-1] == s2[j-1] and i != j:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp

# LongestRepeatingSubsequence("AABEBCDD")
# LongestRepeatingSubsequence("aabb")
# LongestRepeatingSubsequence("axbxcxdx")  


# my mikstakes
# to print the string and count together
# just add the string when you were finding any repeating ele
# but  this will give the incorrect ans
# # will print each char no of times they are repeated since it is checking all the possiblity.
# so to eliminate the repeating char just store the string ans in set then convert into string but
#  this will give ans into any order(because of set)
# so better store into the dic and print the key for ans. this will work

# same thing will happen when you will print lcs like this 
def LongestRepeatingSubsequence1(str):
    n = len(str)
    length, ans= LCS(n, n, str, str)
    # store each char of ans into dict and then print the key , you will get the correct ans
    print("length of longest repeaing subsequence is: ", length)
    print("longest repeaing subsequence is: ", (ans))
def LCS(x,y,s1,s2):
    dp= [[0 for j in range(y+1)] for i in range(x+1)]
    ans= ""
    for i in range(1,x+1):
        for j in range(1,y+1):
            if s1[i-1]== s2[j-1] and i!= j:
                ans+= s1[i-1]   # when you will print then this will give incorrect ans due to else condition
                                # will print each char no of times they are repeated since it is checking all the possiblity
                dp[i][j]= 1+ dp[i-1][j-1]
            else:
                dp[i][j]= max(dp[i-1][j], dp[i][j-1])
    return dp[x][y], ans


# LongestRepeatingSubsequence1("aabebcdd")
# ob.LongestRepeatingSubsequence1("axbxcxdx")
