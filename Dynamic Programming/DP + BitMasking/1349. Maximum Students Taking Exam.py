# Method 1
"""
The Brute Force Logic (Backtracking)
1. Placement Rule: For every seat (r,c), we check:
    Is the seat broken (#)?
    Is there someone to the Left (r,c−1)?
    Is there someone to the Right (r,c+1)?
    Is there someone in the Upper-Left (r−1,c−1)?
    Is there someone in the Upper-Right (r−1,c+1)?
2. Recursive Step: * Option A: Place a student (if valid) and move to the next seat.
    Option B: Skip this seat and move to the next seat.
3. Base Case: When we've looked at every seat in the classroom, we return 0.

Time :  O(2^(m * n)), every seat has two choices whether place a student here(is_safe) or not.
~ 2^64 = 1.8 * 10^9
Space : O(m * n) 
"""

class Solution:
    def maxStudents(self, seats: list[list[str]]) -> int:
        m, n = len(seats) , len(seats[0])
        # Track occupied seats using a set of (r, c)
        occupied = set()

        def is_safe(r, c):
            # 1. Broken seat check
            if seats[r][c] == '#':
                return False
            
            # 2. Same row checks (Left/Right)
            if (r, c-1) in occupied or (r, c+1) in occupied:
                return False
            
            # 3. Previous row diagonal checks (Upper-Left / Upper-Right)
            if (r-1, c-1) in occupied or (r-1, c+1) in occupied:
                return False
            
            # 4. Note: We don't check "Front/Back" because the rule allows it.
            # 5. Note: Since we traverse left-to-right, row-by-row, 
            # we technically only need to check Left, Upper-Left, and Upper-Right.
            return True

        def backtrack(r, c):
            # Base Case: If we finish a row, move to the next
            if c == n:
                return backtrack(r + 1, 0)
            # Base Case: If we finish all rows
            if r == m:
                return 0

            # Option 1: Try placing a student here
            res_with_student = 0
            if is_safe(r, c):
                occupied.add((r, c))
                res_with_student = 1 + backtrack(r, c + 1)
                occupied.remove((r, c)) # Backtrack (Clean up)

            # Option 2: Skip this seat
            res_without_student = backtrack(r, c + 1)

            return max(res_with_student, res_without_student)

        return backtrack(0, 0)
        
# Method 2:
"""
Optimisation using : DP + Bitmasking

The core issue with previous code is Redundant Work. Your backtrack function explores the same "sub-problems" over and over. 
For example, the best way to seat students in Row 3 only depends on how students are seated in Row 2. It doesn't care how you arrived at that Row 2 configuration.

The Optimization Thought Process
1. Identify the State: What is the minimum information we need to make a decision for the next row?
    We need the current row index (r).
    We need to know where students sat in the previous row to avoid diagonal cheating.
2. Represent the State Efficiently: Instead of a set() or a 2D grid, we can use a Bitmask. 
Since a row has at most 8 seats, a single integer from 0 to 255 (which is 28−1) can represent every possible seating arrangement of that row.
3. Memoization: We will store the result of (row_index, previous_row_mask) in a cache. 
If we ever see this exact situation again, we return the stored answer immediately.

The optimization works because we stopped looking at the grid "seat-by-seat" and started looking at it "row-by-row."

Time Complexity : O(m * 2^n * 2^n) 
Number of states: m × 2^n (Rows × Possible masks).
Work per state: 2^n (Trying all masks for the next row).

For an 8×8 grid: 8×256×256≈524,288 operations
"""

from functools import lru_cache

class Solution:
    def maxStudents(self, seats: list[list[str]]) -> int:
        m, n = len(seats), len(seats[0])
        
        # Pre-calculate valid seats for each row (where there isn't a '#')
        row_constraints = []
        for r in range(m):
            mask = 0
            for c in range(n):
                if seats[r][c] == '.':
                    mask |= (1 << c)
            row_constraints.append(mask)

        def is_safe(current_mask, prev_mask, row_idx):
            """
            Validates if the current seating configuration is allowed.
            """
            # 1. Check if students are placed in broken seats ('#')
            if (current_mask & row_constraints[row_idx]) != current_mask:
                return False
            
            # 2. Same row check: No two students can be adjacent (Left/Right)
            if (current_mask & (current_mask << 1)) != 0:
                return False
            
            # 3. Previous row diagonal check: 
            # Current student at 'j' cannot have a student at 'j-1' or 'j+1' in row above
            if (current_mask & (prev_mask << 1)) != 0:  # Upper-Left conflict
                return False
            if (current_mask & (prev_mask >> 1)) != 0:  # Upper-Right conflict
                return False
                
            return True

        @lru_cache(None)
        def solve(row_idx, prev_mask):
            # Base Case: All rows processed
            if row_idx == m:
                return 0
            
            max_students = 0
            
            # Try all 2^n possible configurations for the current row
            for current_mask in range(1 << n):
                if is_safe(current_mask, prev_mask, row_idx):
                    # Count 1s in the bitmask (number of students in this row)
                    current_count = bin(current_mask).count('1')
                    
                    # Recurse to next row
                    res = current_count + solve(row_idx + 1, current_mask)
                    max_students = max(max_students, res)
            
            return max_students

        # Initial call: Start at row 0, no previous row exists (mask 0)
        return solve(0, 0)

# Without '@lru_cache'
"""
We will use a 2D table dp[row][mask], where:
    row: The current row we are filling.
    mask: The seating arrangement of the current row.
    Value: The maximum students we can have from row 0 up to this row.

🧠 The Logic
    Initialize: A DP table of size m×2n filled with -1.
    First Row: Fill the first row of the DP table by checking all masks that are valid within that row (no neighbors, no broken seats).
    Transitions: For every row from 1 to m−1:
        Pick a configuration for the current row (curr_mask).
        Pick a configuration from the previous row (prev_mask).
        If they don't "cheat" (diagonals), update the DP:
        dp[row][curr_mask]=max(dp[row][curr_mask],dp[row−1][prev_mask]+bits(curr_mask))
"""

# Recursion + memoisation + BitMasking
class Solution:
    def maxStudents(self, seats: list[list[str]]) -> int:
        m, n = len(seats), len(seats[0])
        
        # 1. Pre-calculate 'row_constraints'
        # We represent each row as a bitmask where 1 = good seat, 0 = broken.
        # This allows us to check physical seat validity in one bitwise operation.
        row_constraints = []
        for r in range(m):
            mask = 0
            for c in range(n):
                if seats[r][c] == '.':
                    mask |= (1 << c)
            row_constraints.append(mask)

        # 2. Memoization table
        # Stores (row_idx, prev_mask) -> max_students.
        # Using a dict is more space-efficient than a 2D array for sparse states.
        memo = {}

        def is_safe(current_mask, prev_mask, row_idx):
            """
            Checks all cheating and physical rules for a specific row configuration.
            """
            # Rule A: Physical Seats
            # (current_mask & row_constraints) must equal current_mask.
            # If a bit disappears, it means we placed a student on a broken seat.
            if (current_mask & row_constraints[row_idx]) != current_mask:
                return False
            
            # Rule B: Same Row Cheating (Left/Right)
            # Shift the row by 1. If any bits overlap (AND != 0), students are adjacent.
            if (current_mask & (current_mask << 1)) != 0:
                return False
            
            # Rule C: Diagonal Cheating (Upper-Left / Upper-Right)
            # We shift the PREVIOUS row left and right to see if those students
            # collide with the current row's students.
            if (current_mask & (prev_mask << 1)) != 0:  # Upper-Left conflict
                return False
            if (current_mask & (prev_mask >> 1)) != 0:  # Upper-Right conflict
                return False
                
            return True

        def solve(row_idx, prev_mask):
            # Base Case: No more rows to process
            if row_idx == m:
                return 0
            
            # Check if this sub-problem has already been solved
            state = (row_idx, prev_mask)
            if state in memo:
                return memo[state]
            
            max_total = 0
            
            # 3. Decision Space
            # We try every possible bitmask for the current row (0 to 2^n - 1)
            for current_mask in range(1 << n):
                if is_safe(current_mask, prev_mask, row_idx):
                    # Count how many students are in this valid configuration
                    # bit_count() is O(1) in modern Python versions
                    current_count = bin(current_mask).count('1')
                    
                    # Recursive Step: current row students + best from subsequent rows
                    res = current_count + solve(row_idx + 1, current_mask)
                    max_total = max(max_total, res)
            
            # Save the result in the cache before returning
            memo[state] = max_total
            return max_total

        # Start recursion at row 0. 
        # For the first row, we assume the 'previous' row was empty (mask 0).
        return solve(0, 0)

# Tabulation

class Solution:
    def maxStudents(self, seats: list[list[str]]) -> int:
        m, n = len(seats), len(seats[0])
        
        # 1. Pre-calculate valid seats for each row
        row_constraints = []
        for r in range(m):
            mask = 0
            for c in range(n):
                if seats[r][c] == '.':
                    mask |= (1 << c)
            row_constraints.append(mask)

        # 2. Safety Check Function
        def is_safe(curr_mask, prev_mask, row_idx):
            # Check broken seats
            if (curr_mask & row_constraints[row_idx]) != curr_mask:
                return False
            # Check adjacent seats in same row
            if (curr_mask & (curr_mask << 1)) != 0:
                return False
            # Check diagonal upper-left and upper-right
            if (curr_mask & (prev_mask << 1)) != 0 or (curr_mask & (prev_mask >> 1)) != 0:
                return False
            return True

        # 3. Initialize DP table (Rows x 2^n masks)
        # dp[r][mask] = max students up to row r with row r having configuration 'mask'
        dp = [[-1] * (1 << n) for _ in range(m)]

        # 4. Fill Row 0 (Base Case)
        for mask in range(1 << n):
            # For the first row, prev_mask is effectively 0
            if is_safe(mask, 0, 0):
                dp[0][mask] = bin(mask).count('1')

        # 5. Fill subsequent rows
        for r in range(1, m):
            for curr_mask in range(1 << n):
                # Optimization: Only check masks that are valid for the current row's seats
                if (curr_mask & row_constraints[r]) != curr_mask or (curr_mask & (curr_mask << 1)) != 0:
                    continue
                
                curr_bits = bin(curr_mask).count('1')
                
                # Check against every possible mask from the previous row
                for prev_mask in range(1 << n):
                    # If the previous row state was reachable and is safe with current mask
                    if dp[r-1][prev_mask] != -1 and is_safe(curr_mask, prev_mask, r):
                        dp[r][curr_mask] = max(dp[r][curr_mask], dp[r-1][prev_mask] + curr_bits)

        # Result is the maximum value in the last row of our DP table
        return max(dp[m-1]) 
