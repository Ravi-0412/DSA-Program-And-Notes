# Note: thought to do by same method as 'printing lcs' but was becoming very tough and not getting how to do.

# method 1: Try all substring
# Time: O(n^3)

# Method 2: 

# this one is very easy and logical.
# just the another way to check whether a string is palindrome or not.
# normally we used to check by taking two pointer, one at the start and one at the end and we go till 'mid'.

# another way VVI: start checking from mid and move the pointer to it left and right 
# and check whether they are equal or not.
# using same logic: take each ele as mid and take two pointer left and right
# (initailisation will depend on what we are checking i.e even or odd len palindrome) 
# and move left pointer one position to left and right pointer one position to right.

# logic: we are just calculating the max len of odd and even length palindrome from each index.
# just treat each index as mid and move left and right from that.

#  time: O(n*n)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans= ""
        ansLen= 0
        for i in range(len(s)):
            # check for odd length palindrome
            l, r= i, i
            while l>= 0 and r < len(s) and s[l]== s[r]:
                if r-l+1 > ansLen:
                    ans=    s[l: r+1]
                    ansLen= r-l +1
                l-= 1
                r+= 1
            
            # now check for even length palindrome
            l, r= i, i+1
            while l>= 0 and r < len(s) and s[l]== s[r]:
                if r-l+1 > ansLen:
                    ans=    s[l: r+1]
                    ansLen= r-l +1
                l-= 1
                r+= 1
        return ans
    
# Method 2: Using DP
# logic: 
"""
Observation: how we can avoid unnecessary re-computation while validating palindromes.
 Consider the case "ababa". If we already knew that "bab" is a palindrome, it is obvious 
 that "ababa" must be a palindrome since the two left and right end letters are the same.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))] 
        # dp[j][i] : whether string from 'j to i' is palindrome or not.
        # j: starting index , i: last index
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i-j+1 > Max_Len:
                        Max_Len = i-j+1
                        Max_Str = s[j:i+1]
        return Max_Str

# later try in O(n). SOlution in sheet.