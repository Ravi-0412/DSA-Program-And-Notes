# Logic: 
"""
The required number L is the one that satisfies several criteria:

    After removing all multiples of D1 from the range [1,L], there should remain at least C1 elements to fill the first array.
    After removing all multiples of D2 from the range [1,L], there should remain at least C2 elements to fill the second array.
    Numbers from the range [1,L] that are multiples of both D1 and D2 (thus, multiples of lcm(D1,D2)) should be skipped, 
    thus, increasing the candidate value by 1.

So basically we should check every L starting from C1+C2. The first one that satisfies all the criteria is our winner. 
Given the constraints, it is better to use binary search to perform the scan.
"""

import math
class Solution:
    def minimizeSet(self, D1: int, D2: int, C1: int, C2: int) -> int:
        
        L, R, G = 0, 10**10, math.lcm(D1, D2)

        while L < R:
            
            M = (L+R)//2                # [0] try middle value
            
            x = M - M//D1 >= C1         # [1] criterion 1
            y = M - M//D2 >= C2         # [2] criterion 2
            z = M - M//G  >= C1 + C2    # [3] criterion 3
            
            if x and y and z : R = M    # [4] classical step of
            else             : L = M+1  #     the binary search

        return L
    
# java
"""
import java.math.BigInteger;

class Solution {
    public int minimizeSet(int D1, int D2, int C1, int C2) {
        
        long L = 0, R = 10000000000L; // Java doesn't support 10**10 directly, so we use a long type
        long G = lcm(D1, D2); // Finding LCM of D1 and D2
        
        while (L < R) {
            long M = (L + R) / 2; // [0] try middle value
            
            boolean x = M - M / D1 >= C1; // [1] criterion 1
            boolean y = M - M / D2 >= C2; // [2] criterion 2
            boolean z = M - M / G  >= C1 + C2; // [3] criterion 3
            
            if (x && y && z) {
                R = M; // [4] classical step of binary search
            } else {
                L = M + 1;
            }
        }
        
        return (int)L;
    }
    
    // Method to compute LCM (Least Common Multiple)
    private long lcm(int a, int b) {
        return (long)a * (b / gcd(a, b));
    }
    
    // Method to compute GCD (Greatest Common Divisor) using Euclidean algorithm
    private int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }
}

"""