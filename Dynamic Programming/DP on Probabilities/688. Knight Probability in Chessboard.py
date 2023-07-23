# Method 1: Recursion + memoisation using 'cache'.

# Logic: When we are at any cell (r, c) then probability = Average of probability in all '8' directions(moves).


# TIme = space = O(n*n*k)
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions= [[-1, 2], [1, 2],[-1, -2], [1, -2],[-2, 1], [-2, -1],[2, 1], [2, -1]]
    	         # right-up, right-left, left-up, left-down, up-right, up-left, down-right, down-left
        
        @lru_cache(None)
        def solve(r, c , moves):
            if moves == 0:
                # If inside the board and now no move to take so probability = 1
                return 1
            ans = 0  # will store the average of all probabilities from (r, c)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr <= n -1 and 0 <= nc <= n -1:
                    ans += solve(nr, nc, moves - 1)
            return ans / 8  # Average of all '8' directions

        return solve(row, column, k)
    

# W ecan reduce the space complexity to (n*n*2) 
# Reason: ans for cur cell (r, c) depends only the previous moves 'k-1' and for updating the cur cell we need one more 2d array.


# Note: Not able to do by Tabulation
# Have to analyse properly and ask someone

# Also further reduce space to : O(n*n*2)
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions= [[-1, 2], [1, 2],[-1, -2], [1, -2],[-2, 1], [-2, -1],[2, 1], [2, -1]]
    	         # right-up, right-left, left-up, left-down, up-right, up-left, down-right, down-left
        dp = [[[0 for m in range(k + 1)] for j in range(n)] for i in range(n)]  # Alraedy initialised with base case.
        # Initialise with base case 
        for i in range(n):
            for j in range(n):
                dp[i][j][0] = 1
                
        for r in range(n):
            for c in range(n):
                for moves in range(k, 0, -1):
                    ans = 0  # will store the sum of all probabilities from (r, c)
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr <= n -1 and 0 <= nc <= n -1:
                            ans += dp[nr][nc][moves -1]
                    dp[r][c][moves] = ans /8
        return dp[row][column][k]