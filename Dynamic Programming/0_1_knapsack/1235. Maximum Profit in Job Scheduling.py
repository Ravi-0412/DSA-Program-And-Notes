# method 1: 

# This Q is exactly same as: "1751. Maximum Number of Events That Can Be Attended II".
# Difference : Here  1) there is no limit on taking the job like :'k' jobs only.
# 2) next job can start at ending time of another job.

# Same code of Q: "1751. Maximum Number of Events That Can Be Attended II"  

# Using linear Search : To find the next job
# Time: O(n^2) , 
# Note: Giving Memory limit exceeded even with 2-d array

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        for i in range(len(startTime)):
            jobs.append([startTime[i], endTime[i], profit[i]])
        # jobs = sorted(list(zip(startTime, endTime, profit)))   # shortcut

        jobs.sort()   # will sort acc to start time and if start time equal then acc to end time
                      # To decide easily which event we can pick next.
        
        n = len(jobs)
        dp = [-1] * n  # dp[cur] = max profit we can earn starting from index `cur`

        def solve(cur):
            # either we have traversed all the events or we have chosen the maximum no of events allowed.
            if cur >= n:
                return 0
            
            if dp[cur] != -1:
                return dp[cur]

            # we have two choices:
            # 1)  either don't take the cur event
            # 2) if we take it then we need to find the next event we can take after this
            # next event we can only take if there start time is greater than the end time of this event.
            next = cur + 1
            while next < n:
                if jobs[next][0] >= jobs[cur][1]:
                    break
                next += 1

            # max(notTake, take)
            dp[cur] = max(
                solve(cur + 1),
                jobs[cur][2] + solve(next)
            )
            return dp[cur]

        return solve(0)

# Java Code 
"""
import java.util.*;

public class Solution {
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        List<int[]> jobs = new ArrayList<>();
        for (int i = 0; i < startTime.length; i++) {
            jobs.add(new int[]{startTime[i], endTime[i], profit[i]});
        }

        // Sort jobs by start time (and then end time if needed)
        jobs.sort(Comparator.comparingInt(a -> a[0]));

        // dp[cur] will store the maximum profit we can earn starting from index `cur`
        Map<Integer, Integer> memo = new HashMap<>();
        return solve(0, jobs, memo);
    }

    private int solve(int cur, List<int[]> jobs, Map<Integer, Integer> memo) {
        // either we have traversed all the events
        if (cur >= jobs.size()) return 0;
        if (memo.containsKey(cur)) return memo.get(cur);

        // we have two choices:
        // 1) either don't take the cur event
        int notTake = solve(cur + 1, jobs, memo);

        // 2) if we take it then we need to find the next event we can take after this
        int next = cur + 1;
        while (next < jobs.size()) {
            if (jobs.get(next)[0] >= jobs.get(cur)[1]) break;
            next++;
        }
        int take = jobs.get(cur)[2] + solve(next, jobs, memo);

        memo.put(cur, Math.max(take, notTake));
        return memo.get(cur);
    }
}
"""

# C++ Code 
"""
class Solution {
public:
    int jobScheduling(std::vector<int>& startTime, std::vector<int>& endTime, std::vector<int>& profit) {
        std::vector<std::vector<int>> jobs;
        for (int i = 0; i < startTime.size(); ++i) {
            jobs.push_back({startTime[i], endTime[i], profit[i]});
        }

        // Sort jobs by start time (and then by end time if needed)
        std::sort(jobs.begin(), jobs.end());

        std::unordered_map<int, int> memo;
        return solve(0, jobs, memo);
    }

private:
    int solve(int cur, const std::vector<std::vector<int>>& jobs, std::unordered_map<int, int>& memo) {
        // either we have traversed all the events
        if (cur >= jobs.size()) return 0;
        if (memo.count(cur)) return memo[cur];

        // we have two choices:
        // 1) either don't take the cur event
        int notTake = solve(cur + 1, jobs, memo);

        // 2) if we take it then we need to find the next event we can take after this
        int next = cur + 1;
        while (next < jobs.size()) {
            if (jobs[next][0] >= jobs[cur][1]) break;
            next++;
        }
        int take = jobs[cur][2] + solve(next, jobs, memo);

        memo[cur] = std::max(take, notTake);
        return memo[cur];
    }
};
"""

# method 2: 

# Using Binary Search: To find the next jobs

# Note: Here we can choose the next job starting from ending time of cur job.
# So here we need to search for next job whose startTime >= endTime of cur job.
# so we will use 'bisect_left' not 'bisect_right' like Q : ""1751. Maximum Number of Events That Can Be Attended II".


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Create jobs as a list of tuples (startTime, endTime, profit) and sort them
        jobs = sorted(zip(startTime, endTime, profit))  # Sort by start time and then by end time
        
        n = len(jobs)
        # Initialize a 2D array for memoization
        dp = [[-1] * 2 for _ in range(n)]  # dp[i][0]: max profit from job i, dp[i][1]: not used

        def binary_search_next(start_time: int, cur: int) -> int:
            # Binary search to find the next job that starts after the current job ends
            low, high = cur + 1, n - 1
            while low <= high:
                mid = (low + high) // 2
                if jobs[mid][0] >= start_time:
                    high = mid - 1  # Move left to find the first non-conflicting job
                else:
                    low = mid + 1  # Move right
            return low  # Return the index of the next job

        def solve(cur: int) -> int:
            # Base case: If we have traversed all jobs
            if cur >= n:
                return 0
            
            # Check if we already computed this state
            if dp[cur][0] != -1:
                return dp[cur][0]

            # Option 1: Don't take the current job
            notTake = solve(cur + 1)

            # Option 2: Take the current job
            nextJob = binary_search_next(jobs[cur][1], cur)  # Find the next job that can be taken
            take = jobs[cur][2] + solve(nextJob)

            # Store the maximum profit in the dp array
            dp[cur][0] = max(notTake, take)
            return dp[cur][0]

        return solve(0)

# Java Code 
"""
import java.util.*;

class Solution {
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        int n = startTime.length;

        // Create jobs as a list of tuples (startTime, endTime, profit) and sort them
        int[][] jobs = new int[n][3];
        for (int i = 0; i < n; i++) {
            jobs[i][0] = startTime[i];
            jobs[i][1] = endTime[i];
            jobs[i][2] = profit[i];
        }
        Arrays.sort(jobs, Comparator.comparingInt(a -> a[0]));

        Integer[] dp = new Integer[n];  // dp[i]: max profit from job i

        return solve(0, jobs, dp);
    }

    private int solve(int cur, int[][] jobs, Integer[] dp) {
        int n = jobs.length;

        // Base case
        if (cur >= n) return 0;

        // Memoization check
        if (dp[cur] != null) return dp[cur];

        // Option 1: Don't take the current job
        int notTake = solve(cur + 1, jobs, dp);

        // Option 2: Take the current job
        int nextJob = binarySearchNext(jobs, jobs[cur][1], cur);
        int take = jobs[cur][2] + solve(nextJob, jobs, dp);

        // Store and return max profit
        return dp[cur] = Math.max(take, notTake);
    }

    private int binarySearchNext(int[][] jobs, int targetTime, int cur) {
        int low = cur + 1, high = jobs.length - 1, ans = jobs.length;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (jobs[mid][0] >= targetTime) {
                ans = mid;
                high = mid - 1;  // Move left to find the first non-conflicting job
            } else {
                low = mid + 1;
            }
        }
        return ans;
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
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        int n = startTime.size();

        // Create jobs as a list of tuples (startTime, endTime, profit) and sort them
        vector<tuple<int, int, int>> jobs(n);
        for (int i = 0; i < n; ++i) {
            jobs[i] = {startTime[i], endTime[i], profit[i]};
        }
        sort(jobs.begin(), jobs.end());

        vector<int> dp(n, -1);  // dp[i]: max profit from job i
        return solve(0, jobs, dp);
    }

private:
    int solve(int cur, const vector<tuple<int, int, int>>& jobs, vector<int>& dp) {
        int n = jobs.size();
        if (cur >= n) return 0;

        if (dp[cur] != -1) return dp[cur];

        // Option 1: Don't take the current job
        int notTake = solve(cur + 1, jobs, dp);

        // Option 2: Take the current job
        int nextJob = binarySearchNext(jobs, get<1>(jobs[cur]), cur);
        int take = get<2>(jobs[cur]) + solve(nextJob, jobs, dp);

        return dp[cur] = max(take, notTake);
    }

    int binarySearchNext(const vector<tuple<int, int, int>>& jobs, int targetTime, int cur) {
        int low = cur + 1, high = jobs.size() - 1, ans = jobs.size();
        while (low <= high) {
            int mid = (low + high) / 2;
            if (get<0>(jobs[mid]) >= targetTime) {
                ans = mid;
                high = mid - 1;  // Move left to find the first non-conflicting job
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }
};
"""