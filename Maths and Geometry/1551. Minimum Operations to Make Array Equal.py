# In this type of question where you have to each element equal and both
# increment and decrement operation is allowed then 
# just make all element equal to the median.

"""
finding median
=> Here due to symmetry median = n only. So no need to find by finding middle element.
"""

# Method 1: 
# Time: O(n)
class Solution:
    def minOperations(self, n: int) -> int:
        median = n  
        # Total operations needed to make all elements equal to the median
        operations = 0  
        for i in range(n // 2):
            # Since we have to pick element in pair so we will pick symmetrical 
            # smaller and bigger element w.r.t median.
            # in one operation , add this much to lesser number to make equal to median
            # and subtract this much number from bigger number to make equal to median.
            operations += (median - (2 * i + 1))
        return operations

# Method 2: Optimising to O(1)
# Logic: 
"""
There are two possible cases:
1) n is odd
let's consider n=5.
array contains
1 3 5 7 9
Here, middle element of array is -> 5.
Now, we need to choose elements in a pair (which are not equal to the mid element), 
perform some operation on a pair to make them equal to middle element.
Let's take pair (3,7) ,We will decrement 7 and incement 3, two times to make them equal to 5(middle element).
So it takes 2 steps.
Let's take another pair (1,9) We will decrement 9 and incement 1, four times to make them equal to 5.
So it takes 4 steps.
After performing these steps, all elements will become 5.
So, Total steps: 2+4=6. (sum of first n/2 even numbers)
Sum of first k EVEN numbers = k(k+1)
ans would be n/2(n/2+1)

2)n is even
let's consider n=6.
array contains
1 3 5 7 9 11
Here, middle element of array is -> (5+7)/2=6.
Let's take pair (5,7), We will decrement 7 and incement 5, one time to make them equal to 6.
So it takes 1 step.
Let's take 2nd pair (3,9), We will decrement 9 and incement 3, three times to make them equal to 6.
So it takes 3 steps.
Let's take last pair (1,11), We will decrement 11 and incement 1, five times to them equal to 6.
So it takes 5 steps.
After performing these steps, all elements will become 6.
Total steps: 1+3+5=9. (sum of first n/2 odd numbers)
Sum of first k ODD numbers = k*k.
ans would be n/2*n/2
"""

class Solution:
    def minOperations(self, n: int) -> int:
        # If n is odd, return n//2 * (n//2 + 1)
        # If n is even, return n//2 * n//2
        return (n // 2) * (n // 2 + 1) if n % 2 == 1 else (n // 2) * (n // 2)


# java
"""
class Solution {
    public int minOperations(int n) {
        // If n is odd, calculate n/2 * (n/2 + 1)
        // If n is even, calculate n/2 * n/2
        return (n % 2 == 1) ? (n / 2) * (n / 2 + 1) : (n / 2) * (n / 2);
    }
}
"""