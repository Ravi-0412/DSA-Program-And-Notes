# method 1: but giving recursion depth exceeded.
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0: 
            # Just what we do to evaluate the negative power.
            x = 1/x
            n = -n
        if n == 1:   # base case
            return x
        if n %2 == 1:  # if power is odd.
            return x* self.myPow(x,n//2) *self.myPow(x,n//2)
        return self.myPow(x,n//2) * self.myPow(x,n//2)

# we have to minimise the repeatitive recursion call in above method or we can use DP.
# time: O(logn)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0: 
            x=1/x
            n= -n
        if n==0: 
            return 1
        smallAns = self.myPow(x, n//2)
        smallAns = smallAns * smallAns
        if n%2 == 1:  
            return x* smallAns
        # if even
        return smallAns


# 2nd method- time: O(logn)

# Using Bit

# Basic Idea is to divide the work using binary representation of exponents
# i.e. 1 ) keep multiplying pow with x, if the bit is odd, and 2 )  multiplying x with itself until we get bit =  0

# 'x' will only update in power of '2' i.e x, x^2, x^4....

# We will update the ans in similar way we convert from 'binary' to 'decimal'.
# i.e value changes when bit is '1' only.
# Here we will also update the ans in same way only. It is same that we are adding the power when there is '1'.

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x= 1/x
            n= -n
        ans = 1.0
        while n:
            if n % 2==1: 
                # multiply only when power is odd
                ans*= x
            x*= x  # reducing the power by '2' so also need to square only 'x'.
            n = n >> 1         # right shift means dividing by 2 only  
        return ans

