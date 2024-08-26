# For better understanding of question:
"""
You can perform only 2 types of modification operations to convert the integer to Zero.
i) Can change the rightmost bit to 0 or 1 in a single operation
ii) to change any other bit of any index, For example if we need to change the bit at position i , 
It is required that (i-1) positioned bit (i.e the bit to the immediate right of i) 
should be "1" and (i-2),(i-3),(i-4),..........2,1,0 positioned bits must be zero.

Note: simplification of 'ii' => 
you can only modify 'the bit to the left of the rightmost 1 bit'.

[0, 1, 1, 0, 1, 0]= BITS
[5, 4, 3, 2, 1, 0]= INDICES
"""

# intitution:
"""
Note that the number of operations for n to become 0 is the same as the number of operations for 0 to become n...

Let's see how it can be done for numbers that are powers of 2.
1 -> 0 => 1
10 -> 11 -> 01 -> ... => 2 + 1
100 -> 101 -> 111 -> 110 -> 010 -> ... => 4 + 2 + 1
1000 -> 1001 -> 1011 -> 1010 -> 1110 -> 1111 -> 1101 -> 1100 -> 0100 -> ... => 8 + 4 + 2 + 1
We can find that for 2^n, it needs 2^(n+1) - 1 operations to become 0.

Now suppose we want to know the number of operations for 1110 to become 0. We know it takes 15 operations for 0 to become 1000, 
and it takes 4 operations for 1000 to become 1110. We get the solution by 15 - 4.
Note that 4 here is the number of operations from 1000 to become 1110, which is the same as the number of operations 
from 000 to 110 (ignoring the most significant bit), and it can be computed recursively.
The observation gives us: minimumOneBitOperations(1110) + minimumOneBitOperations(0110) = minimumOneBitOperations(1000).
"""

# Link: https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/solutions/877741/c-solution-with-explanation/?envType=problem-list-v2&envId=ahiwan5d

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n <= 1:
            return n
        bit = 0  # finding the largest number which is power of '2' and <= n
        while (1 << bit) <= n:
            bit += 1
        # for that number(power of 2), we will need '(1 << bit) - 1)' operation 
        # - operation needed for remaing number i.e 'n - (1 << (bit - 1)'.
        return ((1 << bit) - 1) - self.minimumOneBitOperations(n - (1 << (bit - 1)))