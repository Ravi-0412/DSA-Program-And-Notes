# method 1: 
# Will give recursion depth exceeded.
# O(n) time and O(n) space.
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

# Method 2: 
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


# method 3
# Using Bit

"""
Logic: Any integer n can be written as a sum of powers of 2 (binary).
    For example: x^13 = x^(1101) ​= x^8⋅x^4⋅x^1 (13 = 1101 in binary)

Mechanism:
1. If the current bit of n is 1, it means that power of 2 is part of the sum, so we multiply our ans by the current x.
2. We square x (x→x^2→x^4→x^8) at every step regardless of the bit.
At start x = x^1. In the second, it's x^2. In the third, it's x^4. It must square itself every time so that it is ready for the next bit's "weight."
If bit was 0. We didn't multiply ans by x^2.
However, we still had to square x^2 to get x^4 because the next bit needs x^4.
Complexity: O(logn) time and O(1) space. This is the most optimized version.
"""

# time: O(logn)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
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

# Java Code 
"""
//Method 1
class Solution {
    public double myPow(double x, int n) {
        if (n < 0) {  
            // Just what we do to evaluate the negative power.
            x = 1 / x;
            n = -n;
        }
        if (n == 1) {  // Base case
            return x;
        }
        if (n % 2 == 1) {  // If power is odd.
            return x * myPow(x, n / 2) * myPow(x, n / 2);
        }
        return myPow(x, n / 2) * myPow(x, n / 2);
    }
}

//Method 2
class Solution {
    public double myPow(double x, int n) {
        if (n < 0) {  
            x = 1 / x;
            n = -n;
        }
        if (n == 0) {  
            return 1;
        }

        double smallAns = myPow(x, n / 2);
        smallAns *= smallAns;

        if (n % 2 == 1) {  
            return x * smallAns;
        }
        return smallAns;  // If even
    }
}

//Method 3
class Solution {
    public double myPow(double x, int n) {
        if (n < 0) {
            x = 1 / x;
            n = -n;
        }

        double ans = 1.0;
        while (n != 0) {
            if ((n & 1) == 1) {  
                // Multiply only when power is odd
                ans *= x;
            }
            x *= x;  // Reducing the power by '2', so also need to square 'x'.
            n = n >> 1;  // Right shift means dividing by 2 only  
        }
        return ans;
    }
}
"""

# C++ Code 
"""
//Method 1
#include <iostream>

using namespace std;

class Solution {
public:
    double myPow(double x, int n) {
        if (n < 0) {  
            // Just what we do to evaluate the negative power.
            x = 1 / x;
            n = -n;
        }
        if (n == 1) {  // Base case
            return x;
        }
        if (n % 2 == 1) {  // If power is odd.
            return x * myPow(x, n / 2) * myPow(x, n / 2);
        }
        return myPow(x, n / 2) * myPow(x, n / 2);
    }
};

//Method 2
#include <iostream>

using namespace std;

class Solution {
public:
    double myPow(double x, int n) {
        if (n < 0) {  
            x = 1 / x;
            n = -n;
        }
        if (n == 0) {  
            return 1;
        }

        double smallAns = myPow(x, n / 2);
        smallAns = smallAns * smallAns;

        if (n % 2 == 1) {  
            return x * smallAns;
        }
        return smallAns;  // If even
    }
};

//Method 3
#include <iostream>

using namespace std;

class Solution {
public:
    double myPow(double x, int n) {
        if (n < 0) {
            x = 1 / x;
            n = -n;
        }

        double ans = 1.0;
        while (n) {
            if (n % 2 == 1) {  
                // Multiply only when power is odd
                ans *= x;
            }
            x *= x;  // Reducing the power by '2', so also need to square 'x'.
            n = n >> 1;  // Right shift means dividing by 2 only  
        }
        return ans;
    }
};
"""
