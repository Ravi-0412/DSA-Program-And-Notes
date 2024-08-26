# Logic:
"""
whenever you have to do complement of a bit just think of xor with '1'.
And here we need to complement every bit so we will take xor with 111111.....
But keep no of 1 in xor = no of digit in given number.
"""

class Solution:
    def findComplement(self, num: int) -> int:
        temp = num
        noBits = 0
        while num:
            noBits += 1
            num //= 2
        mask = (1<< noBits) - 1
        return temp ^ mask

# My mkstake
# took xor with '1111111.....' and got wrong ans.
class Solution:
    def findComplement(self, num: int) -> int:
        return num ^ (1 << 31)
    
