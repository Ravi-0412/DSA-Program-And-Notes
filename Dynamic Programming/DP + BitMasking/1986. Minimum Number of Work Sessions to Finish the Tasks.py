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

# Java Code 
"""
import java.util.*;

class Solution {
    public int minSessions(int[] tasks, int sessionTime) {
        int n = tasks.length;
        int[][] memo = new int[1 << n][sessionTime + 1];  // memo[mask][remainingTime]
        for (int[] row : memo) Arrays.fill(row, -1);

        return dp((1 << n) - 1, 0, tasks, sessionTime, memo);  // start with all tasks and 0 time used
    }

    private int dp(int mask, int remainTime, int[] tasks, int sessionTime, int[][] memo) {
        if (mask == 0) return 0;  // All tasks done

        if (memo[mask][remainTime] != -1) return memo[mask][remainTime];

        int ans = tasks.length;  // Worst case: one task per session

        for (int i = 0; i < tasks.length; i++) {
            if (((mask >> i) & 1) == 1) {  // Task i is still pending
                int newMask = mask ^ (1 << i);  // Clear bit i (mark as done)
                if (tasks[i] <= remainTime) {
                    // Fit task in current session
                    ans = Math.min(ans, dp(newMask, remainTime - tasks[i], tasks, sessionTime, memo));
                } else {
                    // Start new session
                    ans = Math.min(ans, 1 + dp(newMask, sessionTime - tasks[i], tasks, sessionTime, memo));
                }
            }
        }

        return memo[mask][remainTime] = ans;
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minSessions(vector<int>& tasks, int sessionTime) {
        int n = tasks.size();
        vector<vector<int>> memo(1 << n, vector<int>(sessionTime + 1, -1));
        return dp((1 << n) - 1, 0, tasks, sessionTime, memo);  // Start with all tasks and 0 used time
    }

    int dp(int mask, int remainTime, vector<int>& tasks, int sessionTime, vector<vector<int>>& memo) {
        if (mask == 0) return 0;  // All tasks done

        if (memo[mask][remainTime] != -1) return memo[mask][remainTime];

        int ans = tasks.size();  // Worst case: one session per task

        for (int i = 0; i < tasks.size(); ++i) {
            if ((mask >> i) & 1) {  // Task i is still pending
                int newMask = mask ^ (1 << i);  // Clear bit i
                if (tasks[i] <= remainTime) {
                    ans = min(ans, dp(newMask, remainTime - tasks[i], tasks, sessionTime, memo));
                } else {
                    ans = min(ans, 1 + dp(newMask, sessionTime - tasks[i], tasks, sessionTime, memo));
                }
            }
        }

        return memo[mask][remainTime] = ans;
    }
};
"""


# TR to do in more optimal way, solution in sheet.
