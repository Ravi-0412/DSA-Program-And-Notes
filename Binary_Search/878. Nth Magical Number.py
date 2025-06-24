# Method 1: 

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

# Java Code
"""
public class Solution {
    public int nthMagicalNumber(int n, int a, int b) {
        int mod = 1_000_000_007;

        // storing the lcm values into variable
        long ab = lcm(a, b);

        // our ans can start from this value only.
        long start = Math.min(a, b);
        // our ans can go upto this value.
        long end = start * n;

        while (start < end) {
            long mid = start + (end - start) / 2;
            if (count(mid, a, b, ab) >= n) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return (int)(start % mod);
    }

    // giev the count of magical numbers <= num
    private long count(long num, int a, int b, long ab) {
        return num / a + num / b - num / ab;
        // return (num / a + num / b - num / ab) % mod; // DON'T do modulo here, it breaks binary search
    }

    private long lcm(long x, long y) {
        return x * y / gcd(x, y);
    }

    private long gcd(long x, long y) {
        return y == 0 ? x : gcd(y, x % y);
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int nthMagicalNumber(int n, int a, int b) {
        constexpr int mod = 1e9 + 7;

        // storing the lcm values into variable
        long long ab = lcm(a, b);

        // our ans can start from this value only.
        long long start = min(a, b);
        // our ans can go upto this value.
        long long end = start * n;

        while (start < end) {
            long long mid = start + (end - start) / 2;
            if (count(mid, a, b, ab) >= n) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return start % mod;
    }

private:
    // giev the count of magical numbers <= num
    long long count(long long num, int a, int b, long long ab) {
        return num / a + num / b - num / ab;
        // return (num / a + num / b - num / ab) % mod; // DON'T do modulo here, it breaks binary search
    }

    long long gcd(long long a, long long b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    long long lcm(long long a, long long b) {
        return a * b / gcd(a, b);
    }
};
"""

# Method 2: 
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

# Java Code
"""
public class Solution {
    public int nthMagicalNumber(int n, int a, int b) {
        int mod = 1_000_000_007;

        // our ans can start from this value only.
        long start = Math.min(a, b);
        // our ans can go upto this value.
        long end = start * n;

        long lcm = lcm(a, b);  // storing the lcm values into variable

        while (start < end) {
            long mid = start + (end - start) / 2;
            if (count(mid, a, b, lcm) >= n) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return (int)(start % mod);
    }

    private long count(long num, int a, int b, long lcm) {
        return num / a + num / b - num / lcm;
    }

    private long lcm(long x, long y) {
        return x * y / gcd(x, y);
    }

    private long gcd(long x, long y) {
        return y == 0 ? x : gcd(y, x % y);
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int nthMagicalNumber(int n, int a, int b) {
        const int mod = 1e9 + 7;

        // our ans can start from this value only.
        long long start = min(a, b);
        // our ans can go upto this value.
        long long end = start * n;

        long long lcm_ab = lcm(a, b);  // storing the lcm values into variable

        while (start < end) {
            long long mid = start + (end - start) / 2;
            if (count(mid, a, b, lcm_ab) >= n) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return start % mod;
    }

private:
    long long count(long long num, int a, int b, long long lcm) {
        return num / a + num / b - num / lcm;
    }

    long long gcd(long long a, long long b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    long long lcm(long long a, long long b) {
        return a * b / gcd(a, b);
    }
};
"""