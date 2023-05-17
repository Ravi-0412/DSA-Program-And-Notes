# logic: https://leetcode.com/problems/maximize-score-after-n-operations/solutions/1118797/c-python-top-down-dp-bitmask-efficient-clean-detail-explanation/

# len(mask)= len(nums), 1 : nums[i] is used, 0: not used.

# Time: O(2^m * m^2), where mask = 2^m, m = 2n <= 14

# Firstly, we thought that there are total op * mask = n * 2^m states, 
# but op information is already included in mask (op = numberBit1s(mask) / 2 + 1).
# That's why, we have total mask states, each state needs 2 loops with m^2 to compute, so dp takes O(mask * m^2).
# And since we cache gcd(x, y), so we plus with time complexity to calculate gcd(x,y) for m^2 pairs of (x, y) is 
# O(m^2 * logMAX_NUM), where MAX_NUM <= 10^6.
# Total time complexity: O(mask * m^2 + m^2 * logMAX_NUM) ~ O(2^m * m^2), 
# we can remove m^2 * logMAX_NUM part, since it's too small compared to O(2^m * m^2).

# Space: O(mask) = O(2^m)
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def dp(op, mask):
            # have performed all opertaions
            if op== n+ 1:
                return 0
            ans= 0
            for i in range(m):
                # if mask bit at ith index is '1' means  nums[i] is used -> Skip
                if (mask >> i) & 1:
                    continue
                for j in range(i+1, m):
                    # if mask bit at jth index is '1' means  nums[j] is used -> Skip
                    if (mask >> j) & 1:
                        continue
                    # Mark nums[i] and nums[j] as used. making 'ith' bit and 'jth' bit in mask= 1.
                    newMask= (1 <<i) | (1 <<j) |mask
                    score= op*math.gcd(nums[i], nums[j]) + dp(op+1, newMask)
                    ans= max(ans, score)
            return ans

        m= len(nums)
        n= m//2
        return dp(1, 0)
