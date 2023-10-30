
# just like we reduce the num into its prime factors with power.
# Here factors are given i.e 2,3,5.
# We will try to reduce 'num' using these factors to '1'.
# first we will reduce by 2 then by 3 and then by 5 and last check if num== 1.
# vvi: Agar hm num ko '1' tak leke chal jate h powers of 2,3,5 ko use karke then wo ugly number hoga.

# time: O(a + b + c) where num= 2^a + 3^b + 5^c
class Solution:
    def is_ugly(self, num: int) -> bool:
        if num > 0:
            for n in [2,3, 5]:
                while num % n== 0:   # divide by same number till it is divisible. just like we are finding the power of 'n' in prime factors.
                    num/= n
        return num== 1


# we can also write like this.
class Solution:
    def is_ugly(self, num: int) -> bool:
        if num > 0:
            for n in range(2, 6):    # only four is extra but 4 means 2^2 so will not affect our ans.
                while num % n== 0:
                    num/= n
        return num== 1
    

# Extended version: "264. Ugly Number II".