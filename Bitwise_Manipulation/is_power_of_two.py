# submitted on letcode
# for no in power of 2, it has on ebit more than the its 
# pre no. so add with pre no shpoild always give 0
import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # return (math.ceil(math.log(n,2)) == math.floor(math.log(n,2)))   # dont know why not working for some test cases   

        if n==0:
            return False
        return n & (n-1)==0
        
        # return (n & (~(n - 1))) == n

# method 2:(recursive)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 & (n == 1 | (n%2 == 0 & isPowerOfTwo(n/2)))
