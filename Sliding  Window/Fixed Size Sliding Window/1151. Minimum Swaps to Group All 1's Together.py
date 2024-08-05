# Logic:
"""
Note: There is no condition on swapping, we can swap with any index with any index.
we can check answer for each subarray of size 'k' in given array where k = totalOne.
# answer for this subarray = no of zero
"""

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        n = len(data)
        oneCount = 0
        for num in data:
            if num == 1:
                oneCount += 1
        i, j = 0, 0
        zeroCount = 0
        ans = oneCount
        while j < n:
            if data[j] == 0:
                zeroCount += 1
            # check each subarray of size 'oneCount' starting from index 'i' and ending at index 'j'.
            if j - i + 1 >= oneCount:   # or 'j + 1 >= oneCount'
                ans = min(ans, zeroCount)
                if data[i] == 0:
                    zeroCount -= 1
                i += 1
            j += 1
        return ans