# method 1: 
# Recursion
# just extension of q: "740. Delete and Earn".
# Here you need to skip 'i+1' or 'i + 2' based on condition.
# Time : O(n^3) , space: O(n)


from collections import Counter
from typing import List

class Solution:
    def maximumTotalDamage(self, nums: List[int]) -> int:
        freq = Counter(nums)
        nums = sorted(list(set(nums)))
        n = len(nums)

        def solve(i):
            if i >= n:
                return 0
            notTake = solve(i + 1)
            take = freq[nums[i]] * nums[i]
            if (i + 1 < n and nums[i + 1] != nums[i] + 1 and nums[i + 1] != nums[i] + 2):
                take += solve(i + 1)
            elif i + 2 < n and nums[i + 2] != nums[i] + 2:
                take += solve(i + 2)
            else:
                take += solve(i + 3)
            return max(take, notTake)

        return solve(0)


# Method 2 : 
# Recursion with memoization
# Time = O(n*logn) 
# Space = O(n)


from collections import Counter
from typing import List

class Solution:
    def maximumTotalDamage(self, nums: List[int]) -> int:
        freq = Counter(nums)
        nums = sorted(list(set(nums)))
        n = len(nums)
        dp = [-1] * n  # for memoization

        def solve(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            
            notTake = solve(i + 1)
            take = freq[nums[i]] * nums[i]

            # first check if we can take 'i+1' as next or not.
            if i + 1 < n and nums[i + 1] != nums[i] + 1 and nums[i + 1] != nums[i] + 2:
                take += solve(i + 1)
            # if can't take 'i+1', check if we can take 'i+2'.
            elif i + 2 < n and nums[i + 2] != nums[i] + 2:
                take += solve(i + 2)
            # if can't take both 'i+1' or 'i +2' then, take 'i +3'
            else:
                take += solve(i + 3)

            dp[i] = max(take, notTake)
            return dp[i]

        return solve(0)


# method 3:
# Tabulation
# Time: O(n*logn)
# Space: O(n) 

from collections import Counter
from typing import List

class Solution:
    def maximumTotalDamage(self, nums: List[int]) -> int:
        freq = Counter(nums)
        nums = sorted(list(set(nums)))
        n = len(nums)
        dp = [0] * (n + 3)  # To safely access i+3

        for i in range(n - 1, -1, -1):
            notTake = dp[i + 1]
            take = freq[nums[i]] * nums[i]
            
            if (i + 1 < n and nums[i + 1] != nums[i] + 1 and nums[i + 1] != nums[i] + 2):
                take += dp[i + 1]
            elif i + 2 < n and nums[i + 2] != nums[i] + 2:
                take += dp[i + 2]
            else:
                take += dp[i + 3]
                
            dp[i] = max(take, notTake)

        return dp[0]
