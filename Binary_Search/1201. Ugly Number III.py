# Method 1: 

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

# Java Code 
"""
public class Solution {
    public int nthUglyNumber(int n, int a, int b, int c) {

        int start = 1;
        int end = n * Math.max(a, Math.max(b, c));  // max can't go after this.

        while (start < end) {
            int mid = start + (end - start) / 2;
            // if count(mid) >= n, search for even more smaller number.
            if (count(mid, a, b, c) >= n) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return start;
    }

    // giev the count of numbers from '1' to 'num' that is divisible by either a or b or c.
    private int count(int num, int a, int b, int c) {
        return num / a + num / b + num / c
             - num / lcm(a, b) - num / lcm(b, c) - num / lcm(a, c)
             + num / lcm(a, lcm(b, c));
    }

    private int gcd(int num1, int num2) {
        if (num1 == 0) return num2;
        return gcd(num2 % num1, num1);
    }

    private int lcm(int num1, int num2) {
        return (num1 * num2) / gcd(num1, num2);
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int nthUglyNumber(int n, int a, int b, int c) {
        int start = 1;
        int end = n * max({a, b, c});  // max can't go after this.

        while (start < end) {
            int mid = start + (end - start) / 2;
            // if count(mid) >= n, search for even more smaller number.
            if (count(mid, a, b, c) >= n) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return start;
    }

private:
    // giev the count of numbers from '1' to 'num' that is divisible by either a or b or c.
    long long count(long long num, int a, int b, int c) {
        return num / a + num / b + num / c
             - num / lcm(a, b) - num / lcm(b, c) - num / lcm(a, c)
             + num / lcm(a, lcm(b, c));
    }

    int gcd(int num1, int num2) {
        if (num1 == 0) return num2;
        return gcd(num2 % num1, num1);
    }

    long long lcm(int num1, int num2) {
        return 1LL * num1 * num2 / gcd(num1, num2);
    }
};
"""

# Method 2: 
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

# Java Code 
"""
public class Solution {
    public int nthUglyNumber(int n, int a, int b, int c) {
        // min from here our ans will start
        int start = Math.min(a, Math.min(b, c));
        // max till here we need to check
        int end = start * n;

        // storing the lcm values into variables
        long ab = lcm(a, b);
        long bc = lcm(b, c);
        long ca = lcm(c, a);
        long abc = lcm(a, (int)lcm(b, c));

        while (start < end) {
            int mid = start + (end - start) / 2;
            if (count(mid, a, b, c, ab, bc, ca, abc) >= n) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return start;
    }

    private long count(long num, int a, int b, int c, long ab, long bc, long ca, long abc) {
        return num / a + num / b + num / c
             - num / ab - num / bc - num / ca
             + num / abc;
    }

    private long lcm(int x, int y) {
        return (long)x * y / gcd(x, y);
    }

    private int gcd(int x, int y) {
        return y == 0 ? x : gcd(y, x % y);
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int nthUglyNumber(int n, int a, int b, int c) {
        // min from here our ans will start
        int start = min({a, b, c});
        // max till here we need to check
        int end = start * n;

        // storing the lcm values into variables
        long long ab = lcm(a, b);
        long long bc = lcm(b, c);
        long long ca = lcm(c, a);
        long long abc = lcm(a, lcm(b, c));

        while (start < end) {
            int mid = start + (end - start) / 2;
            if (count(mid, a, b, c, ab, bc, ca, abc) >= n) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return start;
    }

private:
    long long count(long long num, int a, int b, int c,
                    long long ab, long long bc, long long ca, long long abc) {
        return num / a + num / b + num / c
             - num / ab - num / bc - num / ca
             + num / abc;
    }

    long long gcd(long long a, long long b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    long long lcm(long long a, long long b) {
        return a * b / gcd(a, b);
    }
};
"""        
# method 3: 

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

# Java Code 
"""
public class Solution {
    public int nthUglyNumber(int n, int a, int b, int c) {
        int start = Math.min(a, Math.min(b, c));   // min from here our ans will start
        int end = start * n;                       // max till here we need to check

        while (start < end) {
            int mid = start + (end - start) / 2;
            if (count(mid, a, b, c) >= n) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return start;
    }

    private int count(int num, int a, int b, int c) {
        return num / a + num / b + num / c
             - num / (a * b) - num / (b * c) - num / (c * a)
             + num / (a * b * c);
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int nthUglyNumber(int n, int a, int b, int c) {
        int start = min({a, b, c});        // min from here our ans will start
        int end = start * n;               // max till here we need to check

        while (start < end) {
            int mid = start + (end - start) / 2;
            if (count(mid, a, b, c) >= n) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return start;
    }

private:
    int count(int num, int a, int b, int c) {
        return num / a + num / b + num / c
             - num / (a * b) - num / (b * c) - num / (c * a)
             + num / (a * b * c);
    }
};
"""
