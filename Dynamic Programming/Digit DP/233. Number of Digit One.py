# logic: just same as "No having exactly k non_zero digits"

# Recursion + memoisation using lru_cache
class Solution:
    def countDigitOne(self, n: int) -> int:
        s= str(n)
    
        @lru_cache(None)
        def solve(ind, tight, count):
            if ind == len(s):
                # we have formed one number < n as all generated no will be less than 'n' only
                return count
            ans= 0
            end= int(s[ind]) if tight else 9
            for digit in range(end + 1):
                newTight= tight and digit== end
                if digit== 1:
                    ans+= solve(ind + 1, newTight, count + 1)  # incr count by '1'.
                else:
                    ans+= solve(ind + 1, newTight, count)
            return ans
        
        return solve(0, 1, 0)   # [ind, tight, count__digit_1]


# Recursion + Memoisation using dp array
class Solution:
    def countDigitOne(self, n: int) -> int:
        s= str(n)
        l= len(s)
        
        dp= [[[-1 for c in range(l + 1)] for bound in range(2)] for i in range(l + 1)]  # here count can go till '100' because we are not using any base case if count > k.
        # because there is possiblity that count > k and some indexes are still left to fill.
        def solve(ind, tight, count):
            if ind == len(s):
                return count
            if dp[ind][tight][count] != -1:
                return dp[ind][tight][count]
            ans= 0
            end= int(s[ind]) if tight else 9
            for digit in range(end + 1):
                newTight= tight and digit== end
                if digit== 1:
                    ans+= solve(ind + 1, newTight, count + 1)
                else:
                    ans+= solve(ind + 1, newTight, count )
            dp[ind][tight][count]= ans
            return ans
        
        return solve(0, 1, 0)   # [ind, tight, count_non_zero]


# Later do by other approaches using maths
# https://leetcode.com/problems/number-of-digit-one/solutions/64382/java-python-one-pass-solution-easy-to-understand/
# (Read comments inside this also by "IronCore864").