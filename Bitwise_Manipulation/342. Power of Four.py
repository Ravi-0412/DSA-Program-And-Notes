# method 1: 
# Time: O(log(4))
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n >0 and log(n  ,4) == int(log(n, 4))

# Method 2:
# Recursion
# Time: O(log(4))
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        return n> 0 and n % 4 == 0 and self.isPowerOfFour(n//4)
    

# Method 3:
# Logic: 1) There must be only one '1' if we convert 'n' into its binary and 
# This case also means 'n' must be power of '2' i.e (n & n-1 == 0).
# 2) 'n-1' must be divisible by '3'. (1,4,16,64,...)

# Time: O(1)

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n> 0 and (n & n-1 == 0 and (n-1) % 3== 0)


# Method 4:
# # Logic: 1) There must be only one '1' if we convert 'n' into its binary and 
# This case also means 'n' must be power of '2' i.e (n & n-1 == 0).
# 2) This single '1' must be at odd position(from right if we start from 1) for power of 'four'.
# In case of power of '2' , it can be at either odd or even position.

# To make sure this (odd position one) , we will take a mask of power of 4 i.e
# 1 + 4 + 16 + 64 + 256 + ..... = (1 + 100 + 10000 + 1000000 + ...)= ........010101010101
# i.e 0x55555555 when written in hexadecimal. 

# And '&' of n' with this mask must be equal to 'n' only for powerof '4'.

# FOr power of '2', '&' can be either '0' or 'n' depending upon position of single '1'.

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & n-1 == 0 and (n & 0X55555555 == n))     


# method 5:
# find the no of consecutive zeros from MSB(right), if even then it is power of 4 else not.
# .eg:1 -> 0 , 4 -> 2, 16 -> 4 , 64 -> 6 etc.
# time: O(32*n)