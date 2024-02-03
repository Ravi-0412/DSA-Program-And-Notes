# logic: we are using the formula i.e given three numbers(a, b, c) and a num 'num', 
# find the number of positive number from '1' to 'num' that is divisible by either a or b or c.
# formula is: num/a + num/b + num/c – num/lcm(a, b) – num/lcm(b, c) – num/lcm(a, c) + num/lcm(a, b, c). 

# just the set theory logic. Subtracting to avoid duplicates.
# vvi: so now Q reduces to "find the smallest num such that count of numbers that is divisible till 'num' 
# by either 'a' or 'b' or 'c' is equal to 'n' ".
# Nd for this we can use binary search as usual.


# No. of numbers upto N divisible by A = N/A;
# No. of numbers upto N divisible by B = N/B;
# No. of numbers upto N divisible by C = N/C;

# No. of numbers upto N divisible by both A and B = N / lcm(A, B);
# No. of numbers upto N divisible by both B and C = N / lcm(B, C);
# No. of numbers upto N divisible by both A and C = N / lcm(A, C);

# No. of numbers upto N divisible by all A, B and C = N / lcm(A, B, C);  


# time: O(log(max(n))*log(A))  # since every time we are calculating the lcm from gcd.
# better use inbuilt lcm function to make code more readable.
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        def gcd(num1, num2):
            if num1== 0:
                return num2
            return gcd(num2 % num1, num1)
        
        def lcm(num1, num2):
            return (num1 * num2)// gcd(num1, num2)


        def count(num):  # giev the count of numbers from '1' to 'num' that is divisible by either a or b or c.
            return num//a + num//b + num//c - num//lcm(a, b) - num//lcm(b, c) - num//lcm(a, c) + num//lcm(a, lcm(b,c))

        start= 1
        # end= 2*(10**9)   # maximum we may have to check till here. Given in Q only that result will be in range [1, 2 * 109].
        end= n * max(a, b, c)   # max can't go after this.
        while start < end:
            mid= start + (end- start)//2
            if count(mid) >= n:   # search for even more smaller number.
                end= mid
            else:
                start= mid + 1
        return start

# to avoid calculating lcm again and again for same thing, we can store those lcm value into variabales.
# to make code concise, used 'math.lcm(a,b)' to find lcm.
# Also updated the range to which start and end can vary logically.
# best one:
# time: # time: O(log(max(n))  

import math
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        def count(num):
            return num//a + num//b + num//c - num//ab - num//bc - num//ca + num//abc

        start= min(a,b,c)   # min from here our ans will start
        end= min(a,b,c) *n  # max till here we need to check
        # storing the lcm values into variables
        ab= math.lcm(a, b)
        bc= math.lcm(b, c)
        ca= math.lcm(c, a)
        abc= math.lcm(a, math.lcm(b, c))
        while start < end:
            mid= start + (end- start)//2
            if count(mid) >= n:
                end= mid
            else:
                start= mid + 1
        return start
        


# if given 'a', b, c are prime numbers then we can do directly like this.
# since lcm of prime numbers= multiplications of number.

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def count(num):
            return num//a + num//b + num//c - num//(a*b) - num//(b*c)- num//(c*a) + num//(a*b*c)

        start= min(a,b,c)   # min from here our ans will start
        end= min(a,b,c) *n  # max till here we need to check
        while start < end:
            mid= start + (end- start)//2
            if count(mid) >= n:
                end= mid
            else:
                start= mid + 1
        return start


# Similar Q:
# i) 878. Nth Magical Number    => Exactly same Q