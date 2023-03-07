# logic: just totally same as "1201 ugly number 3". Easier version of "ugly number 3".
# use set theory.
# find the no of number that is divisible by 'a' or 'b' till n= (num//a + num//b  - num//math.lcm(a, b)).
# vvi: must write start and end value at start properly. 
# Also take care of modulo operation properly like where to put and where not to put.


# time: O(log(A)), A= min(a, b) * n 
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:

        def gcd(num1, num2):
            if num1== 0:
                return num2
            return gcd(num2 % num1, num1)
        
        def lcm(num1, num2):
            return (num1 * num2)// gcd(num1, num2)

        def count(num):
            return (num//a + num//b  - num//ab)
            # return (num//a + num//b  - num//math.lcm(a, b)) % (10**9 + 7)   # dur to this modulo here i was getting wrong ans.(was stuck for more than hour).

        start= min(a, b)  # our ans can start from this value only.
        end= min(a, b) * n   # our ans can go upto this value.
        # storing the lcm values into variable
        ab= lcm(a, b)

        while start < end:
            mid= start + (end- start)//2
            if count(mid) >= n:
                end= mid
            else:
                start= mid + 1
        return (start) % (10**9 + 7) 

# using inbuilt lcm function.
import math
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:

        def count(num):
            return (num//a + num//b  - num//math.lcm(a, b))

        start= min(a, b)  # our ans can start from this value only.
        end= min(a, b) * n   # our ans can go upto this value.
        # storing the lcm values into variable

        while start < end:
            mid= start + (end- start)//2
            if count(mid) >= n:
                end= mid
            else:
                start= mid + 1
        return (start) % (10**9 + 7) 
