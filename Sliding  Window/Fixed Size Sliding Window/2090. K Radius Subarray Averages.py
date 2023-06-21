# logic: for 1st 'k' and last 'k', it will be '-1' only
# we only need to find for index (k, n-k -1).

# time: O(n)
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n <= 2 *k:
            return [-1]*n
        ans= [-1]*k
        noEleInEach = 2 * k + 1   # there will be this number of ele for each ele
        prefixSum = sum(nums[: k])  # for starting index 'k', prefixsum for last 'k' ele will be equal to this only.
        suffixSum = sum(nums[k + 1: 2* k + 1])  # for starting index 'k', suffixsum for next 'k' ele  will be equal to this only.
        for i in range(k, n -k):
            curAvg= (prefixSum + nums[i] + suffixSum) // noEleInEach
            ans.append(curAvg)
            prefixSum= prefixSum - nums[i - k] + nums[i]
            suffixSum= suffixSum - nums[i + 1] + nums[i + k + 1] if (i + k + 1) < n else suffixSum
        return ans + [-1] * k


# method 2: 
# Above logic only
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n <= 2 *k:
            return [-1]*n
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i +1]= prefixSum[i] + nums[i]
        windowSize= 2* k + 1
        ans= [-1]* n
        for i in range(k, n- k):
            ans[i] = (prefixSum[i + k + 1] - prefixSum[i - k]) // windowSize
        return ans