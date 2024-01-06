# Approach
# We need to check for 5 ways in our recursive calls :

# 1) Just abs diff of x & y can be ans. So initialise res = abs(x - y)
# 2) We may go to multiple of 5 which is smaller than x. 
# This can be achieved by just subtracting x%5 from x and divide x by 5. 
# Here total operations = x%5 ( this many time decreament ) + 1( for division by 5).
# 3) We may go to multiple of 5 which is larger than x. 
# This can be achieved by just adding (5 - x%5) to x and then divid x by 5. 
# Here total operations = 5 - x%5 ( this many time increment ) + 1( for division by 5).
# 4) We may go to multiple of 11 which is smaller than x. 
# This can be achieved by just subtracting x%11 from x and divide x by 11. 
# Here total operations = x%11 ( this many time decreament ) + 1( for division by 11).
# 5) We may go to multiple of 11 which is larger than x. 
# This can be achieved by just adding (11 - x%11) to x and then divid x by 11. 
# Here total operations = 11 - x%11 ( this many time increment ) + 1( for division by 11).

# Complexity
# Time : O(N)
# Space : O(N)

class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if y >= x:
            # In this case we can only decrement 
            return y - x
        
        def solve(x):
            if y >= x:
                return y - x
            if dp[x] != -1:
                return dp[x]
            ans = abs(y - x )  # maximum possible ans
            option1 = 1 + x % 5 + solve(x// 5)   # After this operation next x = x //5
            option2 = 1 + (5 - x % 5) + solve(x// 5 + 1) # After this operation next x = x //5 + 1
            option3 = 1 + x % 11 + solve(x// 11)   # After this operation next x = x //11
            option4 = 1 + (11 - x % 11) + solve(x// 11 + 1) # After this operation next x = x //11 + 1
            ans = min(ans, option1, option2, option3, option4)
            dp[x] = ans
            return dp[x]

        dp = [-1] * (10**4 + 11)
        # dp[i] : no of operation needed to convert 'i' to 'y'. so dp[x] will also give the ans.
        return solve(x)
