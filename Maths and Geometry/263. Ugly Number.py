# method 1: Brute Force  (TLE)
# time: O(num *root(num))

class Solution:
    def is_ugly(self, num: int) -> bool:
        if num== 0:
            return False
        for n in range(7, num +1):
            if self.isPrime(n) and num % n== 0:
                return False
        return True
    
    def isPrime(self, n):
        if n==2:
            return True
        root= int(math.sqrt(n))
        i= 2
        while(i<=root):  # check from 2 to root of that number  
        # or while(i*i<=n):   # if you don't want to find the square root of the num
            if n%i==0:
                return False
            i+= 1
        return True
    

# method 2: 
# just like we reduce the num into its coprime factors with power.
# But instead of reducing by finding its coprime and factors we are trying to reduce it to '1' using coprime factors [2,3,5]
# first we will reduce by 2 then by 3 and then by 5 and last check if num== 1.
# vvi: Agar hm num ko '1' tak leke chal jate h powers of 2,3,5 ko use karke then wo ugly number hoga.

# time: O(a + b + c) where num= 2^a + 3^b + 5^c
class Solution:
    def is_ugly(self, num: int) -> bool:
        if num > 0:
            for n in [2,3, 5]:
                while num % n== 0:   # divide by same number till it is divisible. just like we are finding the power of 'n' in coprime factors.
                    num/= n
        return num== 1


# we can also write like this.
class Solution:
    def is_ugly(self, num: int) -> bool:
        if num > 0:
            for n in range(2, 6):    # only four is extra but 4 means 2^2 so will affect our ans.
                while num % n== 0:
                    num/= n
        return num== 1