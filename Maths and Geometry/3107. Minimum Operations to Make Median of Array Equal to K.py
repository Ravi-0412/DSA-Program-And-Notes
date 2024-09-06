# Logic: Just add cost of : 1) Making median = k   2) Making left part decreasing a/c median value
# 3) Making right part increasing a/c median value

class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = abs(k - nums[n//2])   # making median = k
        nums[n //2] = k
        if ans == 0:
            return 0

        def makeLeftPartDecreasing(j, nums):
            cnt = 0
            for i in range(j , -1, -1):
                if nums[i] >  nums[i + 1]:
                    # for minimum cost just make current ele equal to pre element
                    cnt += nums[i] - nums[i + 1]
                    nums[i] = nums[i + 1]
            return cnt
        
        def makeRightPartIncreasing(j, nums):
            cnt = 0
            for i in range(j , len(nums)):
                if nums[i] <  nums[i - 1]:
                    # for minimum cost just make current ele equal to pre element
                    cnt += nums[i - 1] - nums[i]
                    nums[i] = nums[i - 1]
            return cnt

        ans += makeLeftPartDecreasing(n // 2 - 1, nums)
        ans += makeRightPartIncreasing(n//2 + 1,  nums)
        return ans