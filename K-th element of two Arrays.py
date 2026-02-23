"""
Just extension of : https://leetcode.com/problems/median-of-two-sorted-arrays/
Target Partition Size: We want the combined left side of both arrays to contain exactly $k$ elements.
The Formula: If we take i+1 elements from array A, we must take j+1 elements from array B such that (i+1) + (j+1) = k.
This gives us: j = k - i - 2.
The Result: The k-th smallest element will be the maximum of the two elements at the boundaries of the left partition (max(A_left, B_left)).

Time : O(log(min(m,n)))

Q) while low <= high:

why not while True :

like "median' approach

Ans: 1. Why while True worked for your Median codeIn your Median approach, you used while True because the median always exists in two non-empty arrays. 
You were guaranteed that the if A_left <= B_right and B_left <= A_right condition would eventually be met at some partition.2. Why while low <= high
is safer for k-th SmallestThe k-th smallest problem has stricter constraints. If $k$ is out of bounds (e.g., $k=10$ but total elements are 5), a while True would loop forever.

In k-th Smallest: The search space is the number of elements we take from the smaller array.
low = max(0, k - len(B))
high = min(k, len(A))
"""

# My mistake:
"""
Giving out of bound
for this method we are already init with deafukat values then wy index out of bound

Aleft  = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if (i + 1) < n else float('inf')
            Bleft  = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if (j + 1) < m else float('inf')

Ans :
you calculated i as a middle index. If your binary search low and high boundaries aren't perfectly tuned for the k-th element,
i can occasionally equal len(A). Even though you have if (i + 1) < n for Aright, your Aleft was simply A[i]. If i is n, A[i] crashes before the if check even happens.

Input: A = [10], B = [1, 2, 3], k = 4

Total elements = 4. You want the 4th one.
If your binary search picks i = 1 (the only index in A).
j = 4 - 1 - 2 = 1.
Your code tries to check Aleft = A[i]. But A[1] does not exist! CRASH.

Q) why not taking default value : +infinity or -infinity ? 

In your code, you have this line:
Aleft = A[i] if i >= 0 else float('-inf')
When i = 1 and len(A) = 1:
Python first looks at the condition i >= 0. It is True.
Because it is True, Python attempts to execute the first part: A[i].
It looks for A[1].
CRASH: The list only has index 0. The "default value" float('-inf') is never reached because that branch of the if statement was not chosen.

Q) Why the "Count" Method avoids thisIn the Count/Cut method, we change the definition. 
We don't ask "What is the element at this index?" We ask "If I take X elements, what is the boundary?
"If A = [10] and we take cut1 = 1 (the only element):
  L1 = A[cut1 - 1] -> A[1 - 1] -> A[0]. (Safe!)
  R1 = A[cut1] if cut1 < len(A) else float('inf').Since cut1 (1) is NOT < len(A) (1), Python skips A[cut1] and immediately picks float('inf'). (Safe!)

For correct logic: 
cut1 is the number of elements you take.
Range is simply 0 to n.
The Safety: You never access A[cut1] unless you first check cut1 < n. You never access A[cut1-1] unless you check cut1 > 0.

"""

class Solution:
    def kthElement(self, a, b, k):
        # 1. Ensure 'a' is the smaller array
        if len(a) > len(b):
            return self.kthElement(b, a, k)
        
        n, m = len(a), len(b)
        
        # 2. Define the Search Space
        # How many elements can we take from array 'a'?
        # At most 'k' (if a is large) or 'n' (all of a).
        # At least 0 (if b is large enough) or 'k - m' (if b is too small).
        low = max(0, k - m)
        high = min(k, n)
        
        while low <= high:
            # cut1 = number of elements taken from 'a'
            cut1 = low + (high - low) // 2
            # cut2 = number of elements taken from 'b'
            cut2 = k - cut1
            
            # Boundary values (i-1 is the last element in left, i is the first in right)
            l1 = a[cut1 - 1] if cut1 > 0 else float('-inf')
            r1 = a[cut1] if cut1 < n else float('inf')
            
            l2 = b[cut2 - 1] if cut2 > 0 else float('-inf')
            r2 = b[cut2] if cut2 < m else float('inf')
            
            # 3. Partition Check
            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            
            elif l1 > r2:
                # Too many elements from 'a'
                high = cut1 - 1
            else:
                # Too many elements from 'b' (i.e., l2 > r1)
                low = cut1 + 1
        
        return 0 # Should not be reached given constraints


# Correct and working one
"""
"""

class Solution:
    def kthElement(self, a, b, k):
        # 1. Ensure 'a' is the smaller array
        if len(a) > len(b):
            return self.kthElement(b, a, k)
        
        n, m = len(a), len(b)
        
        # 2. Define the Search Space
        # How many elements can we take from array 'a'?
        # At most 'k' (if a is large) or 'n' (all of a).
        # At least 0 (if b is large enough) or 'k - m' (if b is too small).
        low = max(0, k - m)
        high = min(k, n)
        
        while low <= high:
            # cut1 = number of elements taken from 'a'
            cut1 = low + (high - low) // 2
            # cut2 = number of elements taken from 'b'
            cut2 = k - cut1
            
            # Boundary values (i-1 is the last element in left, i is the first in right)
            l1 = a[cut1 - 1] if cut1 > 0 else float('-inf')
            r1 = a[cut1] if cut1 < n else float('inf')
            
            l2 = b[cut2 - 1] if cut2 > 0 else float('-inf')
            r2 = b[cut2] if cut2 < m else float('inf')
            
            # 3. Partition Check
            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            
            elif l1 > r2:
                # Too many elements from 'a'
                high = cut1 - 1
            else:
                # Too many elements from 'b' (i.e., l2 > r1)
                low = cut1 + 1
        
        return 0 # Should not be reached given constraints
