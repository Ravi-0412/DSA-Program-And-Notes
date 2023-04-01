# thought to do same method as 'printing lcs' by was becoming very tough and not getting how to do.

# this one is very easy and logical.
# just the another way to check whether a string is palindrome or not.
# normally we used to check by taking two pointer, one at the start and one at the end and we go till 'mid'.

# another way VVI: start checking from mid and move the pointer to it left and right and check whether they are equal or not.
# using same logic: take each ele as mid and take two pointer left and right
# (initailisation will depend on what we are checking i.e even or odd len palindrome) 
# and move left pointer one position to left and right pointer one position to right.

# logic: we are just calculating the max len of odd and even length palindrome from each index.

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