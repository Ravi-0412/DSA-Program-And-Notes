# just totally the same logic as 'Q: 5 longest palindromic substring".
# take each char as middle
# just incr the count after we found any palindrome.
# here only thing we have to take care that index of char in any two plaindrome should not be same.
# time: O(n^2)
class Solution:
    def countSubstrings(self, s: str) -> int:
        n= len(s)
        count= 0
        for i in range(n):
            # checking for odd length palindrome that can be formed at index 'i'
            l, r= i, i
            while l>= 0 and r < n and s[l]== s[r]:
                count+= 1    
                l-= 1
                r+= 1
            # checking for even len palindrome that can be formed at index 'i'
            l,r= i, i+1
            while l>= 0 and r < n and s[l]== s[r]:
                count+= 1
                l-= 1
                r+= 1
        return count


# make a separate function to count palindrome for each char(taking as mid) instead of two while loop.
class Solution:
    def countSubstrings(self, s: str) -> int:
        n= len(s)
        count= 0
        for i in range(n):
            # checking for odd length palindrome
            l, r= i, i
            count+= self.CountPalindrome(s, l, r, n)

            # checking for even len palindrome
            l,r= i, i+1
            count+= self.CountPalindrome(s, l, r, n)
        return count
    
    def CountPalindrome(self, s, l, r, n):
        count= 0
        while l>= 0 and r < n and s[l]== s[r]:
                count+= 1
                curr_len= r-l + 1
                l-= 1
                r+= 1
        return count