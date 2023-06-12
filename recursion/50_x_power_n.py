# method 1: but giving recursion depth exceeded.
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0: 
            x=1/x
            n= -n
        if n==1:   # base case
            return x
        if n%2==1:  # if power is odd.
            return x* self.myPow(x,n//2) *self.myPow(x,n//2)
        return self.myPow(x,n//2) * self.myPow(x,n//2)

# we have to minimise the repeatitive recursion call in above method or we can use DP.
# time: O(logn)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0: 
            x=1/x
            n= -n
        ans= 1
        if n==0: 
            return 1
        elif n%2==1:
            smallAns= self.myPow(x,n//2)
            ans= x* smallAns* smallAns
        else:
            smallAns= self.myPow(x,n//2)
            ans= smallAns* smallAns
        return ans


# 2nd method- time: O(logn)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x= 1/x
            n= -n
        ans=1.0
        base= x
        i= n 
        while i:
            if i % 2==1:   # to check the last bit ,update the ans only when last bit is one
                            # just think the operation like binary numbers
                ans*= base
            base*= base
            i = int(i/2)          # right shift means dividing by 2 only  
        return ans

