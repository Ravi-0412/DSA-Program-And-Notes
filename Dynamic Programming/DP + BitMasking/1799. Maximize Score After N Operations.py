# Method 1:
"""
Brute Force : 
we would try every possible pair for the first operation, then every possible pair from the remaining numbers for the second, and so on.
Complexity:\
For 14 numbers:
Operations cost: (C(2n,2)⋅C(2n−2,2)⋅⋯⋅C(2,2) / n!) , (We divide by $n!$ because the order in which we pick the pairs doesn't matter for the final set).
= (2n)! / (2^n * n!) = (2n-1)! = 13! => TLE
Note : C(n, k) = n choose k = (n! * (n-k)!) / k!
Note : This is the number of ways to partition 2𝑛 elements into n unordered pairs — also known as:
the number of perfect matchings
or double factorial:​

General formula to find time complexity :
1. Backtracking Questions:
Total Time ~=  Work per Node * (Branching Factor)^(Depth) 

Step 1: Identify the "Branching Factor" (B):
How many recursive calls are made inside the function?
In N-Queens, it's N (one for each column).
In a binary tree traversal, it's 2.
In our Brute Force, it's roughly C(remaining_N , 2)

Step 2: Identify the "Depth of the Tree" (D):
How many times can you recurse before hitting the base case?
In our GCD problem, the depth is n (total operations).
In N-Queens, the depth is N (total rows).

2. DP : O(Total Unique States *  Work per State)

Final Brute Force Calculation:
Substituting into the formula:
Work per Node: O((2n)^2) — the nested loops to find the next available i and j.
Total Recursive Nodes: O((2n-1)!!).
Total Time : O(n^2 * (2n-1)!!)
"""

import math

class Solution:
    def maxScore(self, nums: list[int]) -> int:
        n = len(nums)
        # Using a boolean array to track used numbers
        used = [False] * n

        def backtrack(op_num):
            # Base Case: All n operations completed
            if op_num > n // 2:
                return 0
            
            max_val = 0
            # Try every pair of numbers
            for i in range(n):
                if not used[i]:
                    for j in range(i + 1, n):
                        if not used[j]:
                            # ACTION: Choose this pair
                            used[i] = used[j] = True
                            
                            # RECURSE: Calculate score for this op + future ops
                            score = (op_num * math.gcd(nums[i], nums[j])) + backtrack(op_num + 1)
                            max_val = max(max_val, score)
                            
                            # BACKTRACK: Un-choose the pair for next iteration
                            used[i] = used[j] = False
            return max_val

        return backtrack(1)


# Method 2:
"""
Optimisation using DP + BitMasking

Two major optimizations:
Pre-calculate GCDs: Calculating GCD is O(log(min(x,y))). Doing this inside the recursion is expensive. We do it once at the start.
Implicit op_idx: Instead of passing the operation index, we derive it from the number of bits set in the mask. This simplifies the state.

The Logic:
The State: memo[mask] represents the maximum score achievable using the elements not yet used (bits set to 0 in the mask).
Bit Counting: If 4 bits are set, it means 2 operations have been completed. The next operation will be the 3rd one. Formula: (bits_set // 2) + 1.

Time: O(2^N * N^2), where mask = 2^N, N = 2*n <= 14
Space : O(2^N) 
"""

class Solution:
    def maxScore(self, nums: list[int]) -> int:
        import math

        n_total = len(nums)  # Always even (2 * n)

        # Pre-compute GCDs for all pairs to avoid recomputation during recursion.
        # gcd_map[i][j] = gcd(nums[i], nums[j]) for i < j.
        # Only the upper triangle is filled since pairs are unordered.
        gcd_map = [[0] * n_total for _ in range(n_total)]
        for i in range(n_total):
            for j in range(i + 1, n_total):
                gcd_map[i][j] = math.gcd(nums[i], nums[j])

        # memo maps bitmask → best score achievable from this state onward.
        # A bitmask encodes which elements have already been used:
        #   bit k is 1  →  nums[k] has been consumed in a previous operation.
        #   bit k is 0  →  nums[k] is still available.
        memo = {}

        def solve(mask):
            # Base case: every element has been used → no operations left.
            if mask == (1 << n_total) - 1:
                return 0

            # Return cached result if this state was already solved.
            if mask in memo:
                return memo[mask]

            # Derive the current operation index (1-indexed) from how many
            # elements have been consumed so far.
            # Each operation uses 2 elements, so:
            #   operations_done = bits_set / 2
            #   current_op      = operations_done + 1
            current_op = (mask.bit_count() // 2) + 1

            max_res = 0

            # Try every unordered pair (i, j) of still-available elements.
            # i < j avoids counting the same pair twice.
            for i in range(n_total):
                if not (mask & (1 << i)):          # nums[i] is available
                    for j in range(i + 1, n_total):
                        if not (mask & (1 << j)):  # nums[j] is available

                            # Mark both elements as used in the new state.
                            new_mask = mask | (1 << i) | (1 << j)

                            # Score for this choice:
                            #   current operation index × gcd(nums[i], nums[j])
                            # plus the optimal score for all remaining operations.
                            score = (current_op * gcd_map[i][j]) + solve(new_mask)
                            max_res = max(score, max_res)

            # Cache and return the best score found from this state.
            memo[mask] = max_res
            return max_res

        # Start with mask = 0: no elements used, all operations pending.
        return solve(0)
        
# Tabulation

import math

class Solution:
    def maxScore(self, nums: list[int]) -> int:
        n = len(nums)
        # 1. Pre-calculate GCDs (Optimization)
        gcd_map = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                gcd_map[i][j] = math.gcd(nums[i], nums[j])

        # 2. DP Table: dp[mask] = max score for that subset of used numbers
        dp = [0] * (1 << n)

        # 3. Iterate through all possible bitmasks
        for mask in range(1 << n):
            # We only care about even masks (since elements are removed in pairs)
            bits_set = mask.bit_count()
            if bits_set % 2 != 0:
                continue
            
            # current_op is the multiplier for the NEXT pair we pick
            current_op = (bits_set // 2) + 1
            
            # 4. Try all pairs (i, j) that are NOT in the current mask
            for i in range(n):
                if not (mask & (1 << i)):
                    for j in range(i + 1, n):
                        if not (mask & (1 << j)):
                            # Create the new state including these two numbers
                            new_mask = mask | (1 << i) | (1 << j)
                            # Transition: New Score = Current Score + (Op * GCD)
                            score = dp[mask] + (current_op * gcd_map[i][j])
                            
                            # Update the DP table if this score is better
                            if score > dp[new_mask]:
                                dp[new_mask] = score
                                
        return dp[(1 << n) - 1]
