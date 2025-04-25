"""
1) Let dp(mask, remainTime) is the minimum of work sessions needed to finish all the tasks represent by mask (where ith bit = 1 means tasks[i] need to proceed) with the remainTime we have for the current session.
Then dp((1 << n) - 1, 0) is our result
2) We use mask as 111...1111, represent we need to process all n tasks.
We pass remainTime = 0, which means there is no remain time for the current session; ask them to create a new session.

Time: O(2^n * sessionTime * n), where n <= 14 is length of tasks, sessionTime <= 15.
Explain: There is total 2^n * sessionTime dp states, they are dp[0][0], dp[1][0]..., dp[2^n-1][remainTime]. 
Each dp state needs an inner loop O(n) to calculate the result.
Space: O(2^n * sessionTime)
"""

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        memo = [[-1] * (sessionTime + 1) for _ in range(1 << n)]  # Initialize with -1 (unvisited)

        def clearBit(x, k):
            return ~(1 << k) & x

        def dp(mask, remainTime):
            if mask == 0: 
                return 0  # All tasks done, 0 sessions needed

            # If already computed, return memoized result
            if memo[mask][remainTime] != -1:
                return memo[mask][remainTime]

            ans = n  # In worst case, up to n sessions

            for i in range(n):
                if (mask >> i) & 1:  # If task i is still pending
                    newMask = clearBit(mask, i)  # we are completing this task
                    if tasks[i] <= remainTime:
                        # Fit the task into the current session
                        ans = min(ans, dp(newMask, remainTime - tasks[i]))
                    else:
                        # Task doesn't fit, so start a new session
                        ans = min(ans, dp(newMask, sessionTime - tasks[i]) + 1)

            memo[mask][remainTime] = ans  # Store the result in memo
            return ans

        # Start with all tasks remaining (mask = (1 << n) - 1), and no time used in the current session
        return dp((1 << n) - 1, 0)

# Java
"""
class Solution {
    int n, sessionTime;
    int[][] memo;

    public int minSessions(int[] tasks, int sessionTime) {
        n = tasks.length;
        this.sessionTime = sessionTime;

        // Initialize memo array with -1 (unvisited state)
        memo = new int[1 << n][sessionTime + 1];
        for (int i = 0; i < (1 << n); i++) {
            for (int j = 0; j <= sessionTime; j++) {
                memo[i][j] = -1;  // -1 indicates unvisited
            }
        }

        return dp(tasks, (1 << n) - 1, 0);  // Start with all tasks pending and 0 time left
    }

    private int clearBit(int x, int k) {
        return ~(1 << k) & x;
    }

    // DP function with memoization
    private int dp(int[] tasks, int mask, int remainTime) {
        if (mask == 0) return 0;  // All tasks done

        // If already computed, return memoized result
        if (memo[mask][remainTime] != -1) return memo[mask][remainTime];

        int ans = n;  // Worst case: up to n sessions

        for (int i = 0; i < n; i++) {
            if (((mask >> i) & 1) == 1) {  // Task i is still pending
                int newMask = clearBit(mask, i);  // Mark task i as done
                if (tasks[i] <= remainTime) {
                    // Fit the task into the current session
                    ans = Math.min(ans, dp(tasks, newMask, remainTime - tasks[i]));
                } else {
                    // Task doesn't fit, start a new session
                    ans = Math.min(ans, dp(tasks, newMask, sessionTime - tasks[i]) + 1);
                }
            }
        }

        memo[mask][remainTime] = ans;  // Memoize the result
        return ans;
    }
}
"""

# TR to do in more optimal way, solution in sheet.
