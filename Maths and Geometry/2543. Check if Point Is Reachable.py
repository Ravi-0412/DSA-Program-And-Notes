# Intution:
# 1) If we move from (targetX, targetY) to the points (targetX, targetY - targetX) or 
# (targetX - targetY, targetY), the GCD of the pair remains the same.
# 2) If we move from (targetX, targetY) to the points (2 * targetX, targetY) or (targetX, 2 * targetY), 
# the GCD of the pair remains same or gets doubled.
# 3) GCD of (1, 1) is 1. From here it can either remain same or get multiplied by 2 each time. 
# Therefore, from the above observations, point (1, 1) can move to point (targetX, targetY) 
# if and only if gcd of (targetX, targetY) is a power of 2.

# Approach:
1) Find gcd of targetX and targetY
2) Check if gcd is a power of 2. If it is, return True else return False.

# Time complexity: O(gcd) = O(log(min(targetX, targetY)))
# Space complexity: O(gcd)

class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        g = gcd(targetX, targetY)
        return g & (g-1) == 0  # check if 'g' is a power of 2

# Java
"""
public boolean isReachable(int targetX, int targetY) {
    int g = gcd(targetX, targetY);
    return (g & (g - 1)) == 0; // check g is power of 2
}
private int gcd(int a, int b) {
    if (a == 0) return b;
    return gcd(b % a, a);
}

"""