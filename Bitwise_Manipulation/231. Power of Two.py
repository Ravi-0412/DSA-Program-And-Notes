
# method 1: 
# No in power of two should have log val(base 2) equal to a natural no
# so log val of ceiling and floor must be same only 

import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return math.ceil(math.log2(n))== math.floor(math.log2(n)) if n> 0 else False  

# Java Code 
"""
class Solution {
    public boolean isPowerOfTwo(int n) {
        if (n <= 0) return false;
        double log2 = Math.log(n) / Math.log(2);
        return Math.ceil(log2) == Math.floor(log2);
    }
}

"""

# C++ Code 
"""
#include <cmath>
using namespace std;

class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n <= 0) return false;
        double log2n = log2(n);
        return ceil(log2n) == floor(log2n);
    }
};

"""
# method 2: 
# Power of two has 2's complement equal to the num itself
# but there is no direct way to find 2's complemnt and compare so take '&' of  num with 2's comp(-n) 
# and that should be equal to no itself.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n & -n== n if n!= 0 else False

# Java Code 
"""
class Solution {
    public boolean isPowerOfTwo(int n) {
        return n != 0 && (n & -n) == n;
    }
}

"""

# C++ Code 
"""
class Solution {
public:
    bool isPowerOfTwo(int n) {
        return n != 0 && (n & -n) == n;
    }
};
"""
# method 3: Best
# for no in power of 2, it has one bit more than the its pre no
# so '&'  with pre no should always give 0

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n & (n-1)==0 if n> 0 else False

# Java Code 
"""
class Solution {
    public boolean isPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }
}

"""

# C++ Code 
"""
class Solution {
public:
    bool isPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }
};

"""

# method 4: 
# for no in power of 2, it has one bit more than the its pre no
# so '&'  with pre no should always give 0 and pre no contain all 1's only at bit position where power of two contain all 0's only
# so neagtion of pre num with the given no should be equal to the number itself


import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n & (~(n - 1))) == n

# Java Code 
"""
class Solution {
    public boolean isPowerOfTwo(int n) {
        return (n & (~(n - 1))) == n;
    }
}

"""

# C++ Code 
"""
class Solution {
public:
    bool isPowerOfTwo(int n) {
        return (n & (~(n - 1))) == n;
    }
};

"""

# method 5: 
# Num '2' se divisible hona chahiye and remaining no i.e n //2 bhi power of 2 hona chahiye.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # return n > 0 & (n == 1 | (n%2 == 0 & self.isPowerOfTwo(n/2)))  # true
        # return (n> 0 and n==1) or (n % 2 == 0 and self.isPowerOfTwo(n//2))   # will lead to infinite loop for n=0
        return n>0 and (n==1 or (n % 2 == 0 and self.isPowerOfTwo(n//2)))      # n zero se bda hona chahiye aur (n '1' hona chahiye ya n even hona chahiye )

# Java Code 
"""
class Solution {
    public boolean isPowerOfTwo(int n) {
        // return n > 0 & (n == 1 | (n%2 == 0 & isPowerOfTwo(n/2)))  // true
        // return (n > 0 && n == 1) || (n % 2 == 0 && isPowerOfTwo(n / 2));  // will lead to infinite loop for n = 0
        return n > 0 && (n == 1 || (n % 2 == 0 && isPowerOfTwo(n / 2)));  // n zero se bda hona chahiye aur (n '1' hona chahiye ya n even hona chahiye )
    }
}

"""

# C++ Code 
"""
class Solution {
public:
    bool isPowerOfTwo(int n) {
        // return n > 0 & (n == 1 | (n % 2 == 0 & isPowerOfTwo(n / 2)))  // true
        // return (n > 0 && n == 1) || (n % 2 == 0 && isPowerOfTwo(n / 2));  // will lead to infinite loop for n = 0
        return n > 0 && (n == 1 || (n % 2 == 0 && isPowerOfTwo(n / 2)));  // n zero se bda hona chahiye aur (n '1' hona chahiye ya n even hona chahiye )
    }
};

"""