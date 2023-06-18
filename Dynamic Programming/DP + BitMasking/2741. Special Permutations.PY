# logic: we have to check all possibility and any number can come after any number.
# So just go and if number follows property and mask it as visited and keep continue.

# Note: we need pre number to check.

# Method 1: Recursion + memoisation

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7

        @lru_cache(None)
        def solve(cnt , pre, mask):
            if cnt == n:
                # all number added
                return 1
            ans = 0
            for i in range(n):
                if mask & (1 << i):
                    continue
                if pre == -1 or nums[i] % nums[pre] == 0 or nums[pre] % nums[i] == 0:
                    # mask = mask | (1 << i)
                    ans += solve(cnt + 1, i, mask | (1<<i))   # add all possibility
            return ans % mod
            
        return solve(0 , -1, 0) 

# my mistake:
# Wasted a lot of time.
# Changing 'mask' like changes amsk value globally. so will give incorrect ans.
# Note: for local always change inside function only like above
if pre == -1 or nums[i] % nums[pre] == 0 or nums[pre] % nums[i] == 0:
    mask = mask | (1 << i)
    ans += solve(cnt + 1, i, mask).


# method 2: 
# we don't need count varible
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        found = 2**n - 1  # when mask value will become equal to this means we ahve added all number

        @lru_cache(None)
        def solve(pre, mask):
            if mask == found:
                # means all number got added following that property.
                return 1
            ans = 0
            for i in range(n):
                if mask & (1 << i):
                    continue
                if pre == -1 or nums[i] % nums[pre] == 0 or nums[pre] % nums[i] == 0:
                    # mask = mask | (1 << i)
                    ans += solve(i, mask | (1<<i))
            return ans % mod
            
        return solve(-1, 0) 


# memoising using dp array.
# for 'pre', we will have to do coordinate shift by '1'.
# and range of pre = (-1 to 13) , after shift => (0, 14). 16 elements

# And mask range ->(0, 2**14 + 1)
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        found = 2**n - 1  # when mask value will become equal to this means we ahve added all number

        def solve(pre, mask):
            if mask == found:
                return 1
            if dp[pre + 1][mask] != -1:
                return dp[pre + 1][mask]
            ans = 0
            for i in range(n):
                if mask & (1 << i):
                    continue
                if pre == -1 or nums[i] % nums[pre] == 0 or nums[pre] % nums[i] == 0:
                    # mask = mask | (1 << i)
                    ans += solve(i, mask | (1<<i))
            ans %= mod
            dp[pre + 1][mask] = ans
            return ans % mod

        dp = [[-1 for m in range(2**14 + 1)] for i in range(16)]   
        return solve(-1, 0) 