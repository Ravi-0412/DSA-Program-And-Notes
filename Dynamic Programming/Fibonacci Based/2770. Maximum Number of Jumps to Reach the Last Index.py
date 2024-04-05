# Logic: Just start from index '0' and take all possible indices and finally take maximum of all.

# Time: O(n^2)

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        
        @lru_cache(None)
        def solve(i):   # denotes max length to reach last index from index 'i'.
            if i == len(nums) -1:
                return 0
            ans = float('-inf')
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) <= target:
                    ans = max(ans , 1 + solve(j))
            return ans
        
        ans = solve(0)
        return ans if ans != float('-inf') else -1
        
# Note: if we initialise ans = -1 then it will return '0' in case if not possible in some test cases.
# Because in this case it will return from last i.e 'return ans= -1' and after adding '+1' in '1 + solve(j)'
# it will take max(ans, 1 + -1)= ans(-1, 0)= 0

# e.g [1,3,6,4,1,2] , target = 0

# using dp array
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:

        def solve(i):
            if i == len(nums) -1:
                return 0
            if dp[i] != -1:
                return dp[i]
            ans = float('-inf')
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) <= target:
                    ans = max(ans , 1 + solve(j))
            dp[i] = ans
            return ans
        
        dp = [-1] * len(nums)
        ans = solve(0)
        return ans if ans != float('-inf') else -1