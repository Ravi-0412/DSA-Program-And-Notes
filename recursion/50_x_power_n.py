
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0: 
            x=1/x
            n= -n
        ans= 1
        if n==0:
            return 1
        elif n%2==1:
            smallAns= Solution().myPow(x,n//2)
            ans= x* smallAns* smallAns
        else:
            smallAns= Solution().myPow(x,n//2)
            ans= smallAns* smallAns
        return ans


# 2nd method:
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x= 1/x
            n= -n
        ans=1.0
        base= x
        i= n
        while i:
            if i % 2==1:   # to check the last bit 
                ans*= base
            base*= base
            i = int(i/2)          # right shift means dividing by 2 only 
        return ans

