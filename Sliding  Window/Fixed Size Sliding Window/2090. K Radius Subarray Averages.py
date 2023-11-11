# logic: for 1st 'k' and last 'k', it will be '-1' only
# we only need to find for index (k, n-k -1).

# And for these index 'j' , we need sum in range 'j-k' to 'j +k'.
# From here we get idea of prefic sum.

# time = space = O(n)


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


# Other way of writing above logic
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = [-1]*len(nums)
        curWindowSum = sum(nums[: 2*k])   # storing sum for 1st '2k' ele
        for i in range(k, len(nums)-k):
            curWindowSum += nums[i+k]  # adding the 'i +k' ele i.e last ele of window for each index in our ans
            res[i] = curWindowSum//(2*k+1)
            curWindowSum -= nums[i-k]   # removing the 1st ele of window
        return res

# Most optimised
# space = O(1)
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1]*n
        diameter = 2 *k + 1
        i, j = 0, 0
        curSum = 0
        while j < n:
            curSum += nums[j]
            if j - i + 1 >= 2*k + 1:
                # from here we will update the ans.
                ans[i + k]= curSum // diameter
                curSum -= nums[i]
                i += 1
            j += 1
        return ans


# Note: Whenever you have to find only sum in a range while traversing the array, 
# We can replace prefix Sum with a variable.

# If some query is given and if we have to find sum in that given range query then
# we have to do by taking prefixSum array only.