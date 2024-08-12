# Method 1:
"""
public boolean isPowerOfThree(int n) {
    return n>0 && (n==1 || (n%3==0 && isPowerOfThree(n/3)));
}
"""

# Method 2:
# Note : works only when the base is prime. For example, we cannot use this algorithm 
# to check if a number is a power of 4 or 6 or any other composite number.

"""
public class Solution {
public boolean isPowerOfThree(int n) {
    // 1162261467 is 3^19,  3^20 is bigger than int  
    return ( n>0 &&  1162261467%n==0);
}
"""