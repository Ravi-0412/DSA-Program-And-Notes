# Exactly same as "Find the length of Longest increasing subsequence".
# Here instead of increasing length , just increase the sum.

# Time: O(n^2)

class Solution:
    def maxSumIS(self, Arr, n):
		dp = [Arr[i] for i in range(n)]
		for i in range(n):
		    for j in range(i):
		        if Arr[i] > Arr[j]:
		            dp[i] = max(dp[i], Arr[i] + dp[j])
        return max(dp)