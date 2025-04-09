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

# Java
"""
import java.util.Arrays;

public class Solution {
    public int maxSumIS(int[] arr, int n) {
        int[] dp = new int[n];
        for (int i = 0; i < n; i++) {
            dp[i] = arr[i];
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (arr[i] > arr[j]) {
                    dp[i] = Math.max(dp[i], arr[i] + dp[j]);
                }
            }
        }

        return Arrays.stream(dp).max().getAsInt();
    }
}
"""
