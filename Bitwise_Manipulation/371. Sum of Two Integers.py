# Method 1: Just add the value at every bit from both the numbers like we convert binary to decimal.
# 1) for each bit count the no of '1' -> for two number it will be max '2'.
# say count of '1' = cnt 
# 2) Then add the value at that bit for both the numbers .
# ans += cnt * (2 ** i)

# Note: Not a valid solution because using '+' operator.

class Solution {
    public int getSum(int a, int b) {
        int ans = 0;
        for (int i = 0; i < 32; i++) {
            // Get the i-th bit of a and b
            int setBitCount = (a >> i) & 1;
            setBitCount += (b >> i) & 1;
            // Add the result to ans if setBitCount is 1 or 2
            ans += setBitCount * (1 << i);
        }
        return ans;
    }
}

# Method 2:
# 1) xor can give the answer if there is no carry at any bit.
# for handling carry we will use '&'.
# Logic: We need to shift carry to '1-bit' left and this carry will be used in the next iteration.

# se link: https://leetcode.com/problems/sum-of-two-integers/solutions/132479/simple-explanation-on-how-to-arrive-at-the-solution/
class Solution {
    public int getSum(int a, int b) {
      int c; 
      while(b !=0 ) {
        c = (a&b);     # storing the carry
        a = a ^ b;     # first find the sum assuming no carry
        b = (c) << 1;  # Move the carry to one position left 
      }
      return a; 
    }
}

# Note: All methods won't work in python if number is negative.
# Reason: In python integers have arbitrary precision, meaning they can grow as large as the memory allows. 
# This is in contrast to languages like Java, C, or C++, where integers are typically of fixed size (e.g., 32-bit or 64-bit).
# e.g: In Java, the int type is a 32-bit signed integer (−2^31 to 2^31−1 (i.e., -2,147,483,648 to 2,147,483,647)). 

# int maxInt = 2147483647; // 2^31 - 1
# int result = maxInt + 1; // Results in -2147483648 due to overflow in java

# But in python:
# In Python, the int type can represent an integer of any size. It grows dynamically as needed, limited only by the available memory. 
# This means that Python integers do not overflow. Instead, they continue to grow larger as necessary:
# e.g: 
# max_int = 2**31 - 1  # 2147483647
# result = max_int + 1
# print(result)  # 2147483648

# Note: Negative integers are stored in python in 2's complement.
# Steps to Find Two's Complement:

#  a)  Write the binary representation of the positive number.
#  b)  Invert all the bits (0s become 1s and 1s become 0s).
#  c)   Add 1 to the inverted number.

# Example: Representing -5 in a 32-bit System
#   a)  Positive Number +5 in 32 bits:
#         00000000000000000000000000000101

#  b)   Invert the bits:
#         11111111111111111111111111111010

#   c)  Add 1:
#         11111111111111111111111111111010 + 1 = 11111111111111111111111111111011
# d) so, the 32-bit two's complement representation of −5 is : 11111111111111111111111111111011

# Converting Back to Decimal

# To convert a two's complement binary number back to decimal:

#  a)   If the MSB is 0, it's positive number, and you can convert directly.
#   b)  If the MSB is 1, it's negative:
#       i)  Invert all bits.
#      ii)   Add 1 to the result.
#      iii)   Convert to decimal and add a negative sign.


# Note: you can see numbers becomes very big in case of negative(due to 2's complement), it happens in all languages.
# But python don't wrap like other languages so ans will become very big.
# so we need to ensure that our operations are constrained to 32-bit integer behavior like other languages.

# for this we will use mask(maximum value of 32-bit or any given bit).
# And '&' with 'mask' at each step.


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Mask to get 32-bit integer results
        mask = 0xFFFFFFFF
        while b != 0:
            # Calculate carry
            carry = (a & b) & mask
            # Calculate the sum without carry
            a = (a ^ b) & mask
            # Calculate the carry and shift it left
            b = (carry << 1) & mask
        
        # If a is negative, return a properly signed integer i.e return equivalent positive number i.e -5 -> 5
        if a > 0x7FFFFFFF:  # 0x7FFFFFFF is the maximum positive value for a 32-bit signed integer
            a = ~(a ^ mask)
        
        return a

# 'a = ~(a ^ mask) :  is used to convert a 32-bit unsigned integer result into its equivalent signed integer 
# representation in Python. This is necessary because Python's integers are of arbitrary precision and 
# don't have fixed-width, so they don't overflow or wrap around automatically.

# for positive number 'a':
# a = ~(a ^ mask) only 


# 0x7FFFFFFF:
#     0x: Prefix indicating that the number is in hexadecimal format.
#     7: Hexadecimal digit representing the value 7.
#     F: Hexadecimal digit representing the value 15.
#     The remaining digits (FFFFFFF) represent the hexadecimal values equivalent to 15 each.

# The entire number 0x7FFFFFFF represents the maximum signed 32-bit integer in hexadecimal format. 
# In decimal, it is equal to 231−1231−1, which is 2,147,483,6472,147,483,647.
