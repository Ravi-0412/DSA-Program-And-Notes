# method 1: using the inbuilt function to convert decimal into binary
# then count the number of '1'
# time: O(n)

# bin(N) converts the integer N to its binary representation as a string. For example, if N is 5, bin(5) returns '0b101'.
# '.replace("ob", "") : is used to remove the "0b" part of the binary string

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

# method3: VVI
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


# java
"""
// Method 3:
public class Solution {
    public int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            count++;
            n = n & (n - 1);
        }
        return count;
    }
}
"""

