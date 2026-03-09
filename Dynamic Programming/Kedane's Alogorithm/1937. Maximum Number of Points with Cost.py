# Method 1: 
"""
Extension of: "1014. Best Sightseeing Pair" in 2-D

Logic:
For each cell (r, c), we want to find the best cell (r-1, prev_c) from the row above.
The score for dp[r][c] would be:
dp[r][c] = points[r][c] + max(dp[r-1][prev_c] - abs(c - prev_c) for prev_c in range(n))
Time : O(M * N^2)
"""



# Method 2:
"""
Optimised one

Logic: Breaking the Absolute Value
The expression : dp[r-1][prev_c] - |c - prev_c| can be split into two cases to remove the absolute value:
i)  If prev_c <= c (Left side): dp[r-1][prev_c] - (c - prev_c) =>  (dp[r-1][prev_c] + prev_c) - c
ii) If prev_c > c (Right side): dp[r-1][prev_c] - (c - prev_c) =>  (dp[r-1][prev_c] - prev_c) + c

Instead of re-scanning the whole row for every c, we can pre-calculate the best values coming from the left and the right in just two passes.

Time Complexity: O(M * N) - We visit each cell a constant number of times.
Space Complexity: O(N) - We only store the previous and current row data.
"""

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        m, n = len(points), len(points[0])
        
        # prev_row stores the max points achievable up to the previous row
        prev_row = points[0]
        
        for r in range(1, m):
            # left_max[i] stores the max value of (prev_row[k] + k) for k <= i
            left_max = [0] * n
            # right_max[i] stores the max value of (prev_row[k] - k) for k >= i
            right_max = [0] * n
            
            # Pass 1: Left to Right
            # We carry over the "best" value from the left, subtracting 1 for each step
            left_max[0] = prev_row[0]
            for c in range(1, n):
                left_max[c] = max(left_max[c-1] - 1, prev_row[c])
            
            # Pass 2: Right to Left
            # We carry over the "best" value from the right, subtracting 1 for each step
            right_max[n-1] = prev_row[n-1]
            for c in range(n-2, -1, -1):
                right_max[c] = max(right_max[c+1] - 1, prev_row[c])
            
            # Pass 3: Calculate current row
            current_row = [0] * n
            for c in range(n):
                # The best value for current cell is its own points + max of left/right options
                current_row[c] = points[r][c] + max(left_max[c], right_max[c])
            
            # Update prev_row for the next iteration
            prev_row = current_row
            
        return max(prev_row)

# Little concise way to write
class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        m, n = len(points), len(points[0])
        # dp stores the maximum points for the previous row processed
        dp = points[0]

        for r in range(1, m):
            # 1. Left-to-Right Pass: Calculate the best possible score coming from the left
            # We use 'left_max' to track: max(dp[k] - (c - k)) -> max(dp[k] + k) - c
            left_max = [0] * n
            left_max[0] = dp[0]
            for c in range(1, n):
                # Either take the current cell directly or take the one from the left with a -1 penalty
                left_max[c] = max(left_max[c-1] - 1, dp[c])

            # 2. Right-to-Left Pass: Calculate the best from the right AND update the row
            # We track 'right_running_max' to represent the best score from columns >= c
            right_running_max = dp[n-1]
            for c in range(n-1, -1, -1):
                # Update right_running_max with -1 penalty for each step left
                right_running_max = max(right_running_max - 1, dp[c])
                
                # The new dp[c] is the cell's points + the better of the two directions
                dp[c] = points[r][c] + max(left_max[c], right_running_max)

        return max(dp)
