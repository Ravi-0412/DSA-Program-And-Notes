# just exactly same as "523. Continuous Subarray Sum".
# in that Q we have to keep track of length also in case we see any duplicates, so we were storing {modulus: index}

# Here we have to find no of subarray, so we are storing {modulus: count}.
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans= 0
        modulusCount= {0: 1}   # {modulo_sum: count}
        curSum= 0
        for i in range(len(nums)):
            curSum += nums[i]
            curSum = curSum % k
            if curSum in modulusCount:
                count= modulusCount[curSum]
                ans += count
                modulusCount[curSum] += 1
            else:
                modulusCount[curSum] = 1
        return ans
    

# Note: python '%' operator behave very differently if numerator is negative.
# But still it will work because ans will depend on dulicates so it won't create any problem.
