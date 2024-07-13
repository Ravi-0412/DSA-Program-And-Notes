# Just try to reduce the subarray size after finding a valid answer.
# same as :"Smallest subarray with sum greater than x"

class Solution:
    def smallestSubWithSum(self, x, arr):
        n = len(arr)
        ans = float('inf')
        curSum = 0
        i , j = 0, 0
        while j < n:
            curSum += arr[j]
            while curSum > x:
                ans = min(ans, j - i + 1)
                curSum -= arr[i]
                i += 1
            j += 1
        return ans if ans != float('inf') else 0