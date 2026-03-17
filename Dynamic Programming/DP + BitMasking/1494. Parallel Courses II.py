"""
Thought Process:

Step 1: Recognize the Pattern

n ≤ 15 → bitmask DP immediately
Need to track which courses are done → bitmask as state
Same set of completed courses = same subproblem → overlapping subproblems → memoization works

Step 2: Model the State
mask = bitmask of courses already completed

dp(mask) = minimum semesters needed to complete
           ALL remaining courses, given that
           'mask' courses are already done

Step 3: Figure Out What's Available Each Semester
A course is available this semester if:

It hasn't been taken yet (bit not in mask)
All its prerequisites are already done (all prereq bits are in mask)

prereq[i] = bitmask of ALL prerequisites of course i

course i is available if:
    - bit i NOT in mask
    - (prereq[i] & mask) == prereq[i]   ← all prereqs satisfied

Step 4: Handle the k Constraint
From the available courses, we can pick at most k this semester. We want to try all subsets of the available set of size ≤ k, and pick the one that minimizes total semesters.
available = {all courses unlocked but not yet taken}

try every subset S of available where |S| <= k:
    dp(mask) = 1 + dp(mask | S)   ← take S this semester

Step 5: Enumerate Subsets Efficiently
To iterate over all subsets of a bitmask available

Q) How 'sub = (sub - 1) & available' is generating all non-empty subset of a bitmask one by one.
=> 
sub = available      # start with the full set
while sub:
    # use sub here
    sub = (sub - 1) & available   # step to next subset

i) Why `-1` Works — The Core Idea
Subtracting 1 from a binary number **flips the rightmost `1` bit to `0`, and all bits to its right become `1`.**
```
  0b101100
-        1
----------
  0b101011   ← rightmost 1 flipped to 0, everything right of it → 1
```
This is just how binary subtraction works — it "borrows" all the way from the rightmost set bit.

Small Concrete Example

Let `available = 0b0111` (courses 0, 1, 2 are available):
```
sub (used this iter) │  sub - 1      │  & 0b0111     │  next sub     │  courses
─────────────────────┼───────────────┼───────────────┼───────────────┼──────────
0b0111 = 7           │  0b0110 = 6   │  0b0110       │  0b0110       │  {1, 2}
0b0110 = 6           │  0b0101 = 5   │  0b0101       │  0b0101       │  {0, 2}
0b0101 = 5           │  0b0100 = 4   │  0b0100       │  0b0100       │  {2}
0b0100 = 4           │  0b0011 = 3   │  0b0011       │  0b0011       │  {0, 1}
0b0011 = 3           │  0b0010 = 2   │  0b0010       │  0b0010       │  {1}
0b0010 = 2           │  0b0001 = 1   │  0b0001       │  0b0001       │  {0}
0b0001 = 1           │  0b0000 = 0   │  0b0000       │  0b0000       │  loop ends

Exactly 2³ - 1 = 7, non-empty subsets, all visited.

Example 2: 
sub (used this iter) │  sub - 1      │  & 0b1010     │  next sub     │  courses
─────────────────────┼───────────────┼───────────────┼───────────────┼──────────
0b1010 = 10          │  0b1001 = 9   │  0b1000       │  0b1000       │  {3}
0b1000 = 8           │  0b0111 = 7   │  0b0010       │  0b0010       │  {1}
0b0010 = 2           │  0b0001 = 1   │  0b0000       │  0b0000       │  loop ends

Exactly 2^2 - 1 = 3, non-empty subsets, all visited.

In short :
  sub - 1  <  sub           (subtracting 1 makes it smaller)
  x & mask <= x             (AND can only turn bits off, never on)

So sub is strictly decreasing → must eventually hit 0 → loop terminates
And every integer between 0 and available that is a subset
of available is hit exactly once on the way down.
```

Time Complexity : 
States
mask can be any subset of n courses
→ 2ⁿ possible states
Work Per State
For each mask, we:

Find available courses → O(n)
Enumerate all subsets of available → O(2^|available|)

In the worst case available = all n courses, so 2ⁿ subsets per state.
But summing subsets across ALL states uses the identity:
Sum over all masks S of 2^|S| = 3ⁿ

Why?
For each of the n bits, it contributes independently:
  - not in mask       → 1 way
  - in mask, not sub  → 1 way  
  - in mask, in sub   → 1 way
       = 3 choices per bit → 3ⁿ total
So total work across all states is O(3ⁿ), not O(4ⁿ).

Space : O(2^n)
"""


from typing import List
from functools import lru_cache

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:

        # Precompute prereq masks (0-indexed internally)
        # prereq[i] = bitmask of all courses that must be done before course i
        prereq = [0] * n
        for prev, nxt in relations:
            # Convert 1-indexed to 0-indexed
            prereq[nxt - 1] |= (1 << (prev - 1))

        # Goal state: all n courses completed
        all_done = (1 << n) - 1

        @lru_cache(maxsize = None)   # unlimited — never evicts anything , it works on LRU algorithm
        def dp(mask):
            # Base case: all courses are done
            if mask == all_done:
                return 0

            # --- Find all currently available courses ---
            # A course i is available if:
            #   1. It hasn't been taken (bit i not set in mask)
            #   2. All its prerequisites are satisfied (prereq[i] is subset of mask)
            available = 0
            for i in range(n):
                if not (mask & (1 << i)):                    # not yet taken
                    if (prereq[i] & mask) == prereq[i]:      # all prereqs done
                        available |= (1 << i)

            # --- Try every subset of available courses of size <= k ---
            # We want to find the subset to take THIS semester that
            # minimizes the total number of semesters overall.
            best = n  # worst case: n semesters (loose upper bound)

            # Enumerate all subsets of 'available' using the standard trick:
            #   start from the full set, keep removing bits
            sub = available
            while sub:
                # Only consider subsets of size <= k
                if bin(sub).count('1') <= k:
                    # Take 'sub' courses this semester:
                    # cost = 1 (this semester) + optimal cost from new state
                    best = min(best, 1 + dp(mask | sub))

                # Standard way to enumerate all subsets of a bitmask:
                # This steps through every non-empty subset of 'available'
                sub = (sub - 1) & available

            return best

        # Start with mask=0: no courses completed yet
        return dp(0)

        
