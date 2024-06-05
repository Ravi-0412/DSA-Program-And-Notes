# Similar logic as : "300. Longest Increasing subsequence"
# LOGIC: For each position i,we track the maximum increasing subsequence. 
# To do that, we analyze all j < i, and if A[j] < A[i] for all strings , then dp[i] = dp[j] + 1.

# Time: O(n * n * m), where n is the number of characters, and m is the number of strings.

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])
        dp = [1] * n
        # checking each position  
        for i in range(n):
            # with previous position
            for j in range(i):
                # of all string
                for k in range(m + 1):
                    if k == m:
                        dp[i] = max(dp[i] , dp[j] + 1)
                    elif strs[k][j] > strs[k][i]:
                        break
        return n - max(dp)


# java
"""
import java.util.Arrays;

public class Solution {
    public int minDeletionSize(String[] strs) {
        int m = strs.length, n = strs[0].length();
        int[] dp = new int[n];
        Arrays.fill(dp, 1);

        // Checking each position
        for (int i = 0; i < n; ++i) {
            // With previous position
            for (int j = 0; j < i; ++j) {
                // Of all strings
                for (int k = 0; k <= m; ++k) {
                    if (k == m) {
                        dp[i] = Math.max(dp[i], dp[j] + 1);
                    } else if (strs[k].charAt(j) > strs[k].charAt(i)) {
                        break;
                    }
                }
            }
        }

        int maxDp = 0;
        for (int x : dp) {
            if (x > maxDp) {
                maxDp = x;
            }
        }
        return n - maxDp;
    }
}
"""

