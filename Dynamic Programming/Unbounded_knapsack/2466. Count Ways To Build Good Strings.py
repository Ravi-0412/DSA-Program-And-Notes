# method 1:
# Logic: we try to form all possible string then calculate their lenth. 
# we have two choices i.e 1) include zero or 2) include one
# for base case check the length.

# Note: In this we will not get the overlapping subproblem because we are forming string always by appending
# two diff char each time so we will not get the same anymore time.

# time: O(2^n). TLE

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        self.ans= 0
        mod= 10 **9 + 7

        def count(s):
            if len(s) > high:
                return 0
            if low <= len(s) <= high:
                self.ans+= 1
                # return      # DON'T return because we may from more string using this 's'.
            count(s + "0"*zero)
            count(s + "1"*one)

        count("")
        return self.ans % mod
    

# method 2: Recursion + memoisation
# logic: instead of keeping track of string, just keep track of length of string.
# Then we will get duplicate but all those string will be unique only.

# Here only length matter i.e if length in that range then that is one of possible ans.
#  ans is only dependent on 'one' and 'zero' value.

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod= 10 **9 + 7
        dp= {}

        def dfs(length):
            if length > high:
                return 0
            if length in dp:
                return dp[length]
            res= 0
            if low <= length <= high:
                res+= 1  
            # After adding length will increse by 'zero' or 'one'
            res+= dfs(length + zero) + dfs(length + one)
            dp[length]= res % mod
            return res % mod

        return dfs(0)

# Tabulation

# Note: Here going opposite of memoisation so subtracting instead of adding.
# z = dp.get(length- zero, 0)  # zero
# o = dp.get(length- one, 0)   # one

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod= 10 **9 + 7
        dp = {0: 1}  # {length : no_string}
        for length in range(1, high +1):
            # no of string of length 'i' ,
            #  we will get after adding value of (length- zero) and (length- one) respectively.
            z= dp.get(length- zero, 0)  # zero
            o= dp.get(length- one, 0)   # one
            dp[length]= (z + o) % mod

        ans= 0
        for length in range(low, high + 1):
            ans+= dp[length]
        return ans % mod

# tabulation top-down
# dp = {high: 1}
# then traverse from 'high -1' to '0'
# in this you can do '+' instead of '-'.