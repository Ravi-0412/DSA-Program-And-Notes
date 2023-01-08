# time= O(n^2)
# space= O(n)

# logic: we are greedily trying to form the palindrome using two pointer.
# we can only move lefrt and right, when we are sure that char at placed at proper position from left and right.
class Solution:
    def minMovesToMakePalindrome(self, s):
        left , right= 0, len(s) -1
        s= list(s)   # we cant't modify string so converting into list
        ans= 0
        while left < right:
            # if ele from left and right is not same
            if s[left]!= s[right]:  
                #search for nearest char from right which matches the char at left.
                r= right
                while s[left]!= s[r]:
                    r-= 1
                if r== left:  # means chat at 'left' has occurrence odd no of times, so this char should be at centre only.
                    # so move this char towards centre. we are not moving the char at centre at once to minimise the move. 
                    # we are moving only one time and then continue our checking keeping left and right same.
                    # As after swapping we can get the matching ele at left and right
                    ans+= 1
                    s[r], s[r+1]= s[r+1], s[r]
                else: # means we have found the dupliacate of the char
                    # so move this char to the right position one by one
                    while r < right:
                        s[r], s[r+1]= s[r+1], s[r]
                        ans+= 1
                        r+= 1
                    # # after moving update left and right since we have moved one char from left and right at proper index to form 'palindrome'.
                    # left, right= left +1 , right -1
            # already char at left and right is at proper position so simply update left amnd right.
            else: 
                left, right= left +1 , right -1
        return ans
