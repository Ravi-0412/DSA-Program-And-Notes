# method 1: 
# using the inbuilt function to convert decimal into binary then, count the number of '1'.
# bin(N) converts the integer N to its binary representation as a string. For example, if N is 5, bin(5) returns '0b101'.
# '.replace("ob", "") : is used to remove the "0b" part of the binary string
# time: O(n)



class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).replace("0b","").count('1')

# method 2: 
# just check the rightmost bit using bitwise operator and count
# time: O(1), as we have to check only 32 bit

class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while(n):
            if n & 1 == 1:
                count += 1
            n >>= 1
        return count

# method 3: 
# No of time loop execute =  to the no of set bits  
# Logic: as n is formed from 'n-1' by changing one bit and so on every iteration one '1' will get cancelled out when we will take '&',
# as while taking add and updating, the value tends towards zero very fast as bits changes.

# More better logic:
"""
For eavery two consecutive numbers, we are sure that there are (n - 1) 1's which are common between the two numbers
where n is the total number of 1's in the larger number.
"""

# time: o(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n:    
            count += 1
            n= n & n-1    # concise way of writing abobe two lines    
        return count      # no of times loop will execute that will give the ans


# Java Code
"""
//Method 1
class Solution {
    public int hammingWeight(int n) {
        return Integer.bitCount(n); // Inbuilt function to count set bits
    }
}

//Method 2
class Solution {
    public int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            if ((n & 1) == 1) count++; // Check if the rightmost bit is 1
            n >>= 1; // Right shift the number
        }
        return count;
    }
}

//Method 3
class Solution {
    public int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {    
            count++;
            n = n & (n - 1); // Removes the rightmost 1-bit in every iteration
        }
        return count; // Number of times loop executes gives the number of set bits
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
    int hammingWeight(uint32_t n) {
        return __builtin_popcount(n); // Inbuilt function to count set bits in integer
    }
};

//Method 2
#include <iostream>

using namespace std;

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        while (n) {
            if (n & 1) count++; // Check if the rightmost bit is 1
            n >>= 1; // Right shift the number
        }
        return count;
    }
};

//Method 3
#include <iostream>

using namespace std;

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        while (n) {    
            count++;
            n = n & (n - 1); // Removes the rightmost 1-bit in every iteration
        }
        return count; // Number of times loop executes gives the number of set bits
    }
};
"""
