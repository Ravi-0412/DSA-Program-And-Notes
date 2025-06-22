# This Q is exactly same as: "1751. Maximum Number of Events That Can Be Attended II".
# Difference : Here  1) there is no limit on taking the job like :'k' jobs only.
# 2) next job can start at ending time of another job.

# Same code of Q: "1751. Maximum Number of Events That Can Be Attended II"  

# 1) Using linear Search : To find the next job
# Time: O(n^2) , 
# Note: Giving Memory limit exceeded even with 2-d array
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        for i in range(len(startTime)):
            jobs.append([startTime[i], endTime[i], profit[i]])
        # jobs= sorted(list(zip(startTime, endTime, profit)))   # shortcut

        @lru_cache(None)      # dp = [[-1] * (n + 1) for _ in range(n)]
        def solve(cur):
            # either we have traversed all the events or we have chosen the maximum no of events allowed.
            if cur >= len(jobs):
                return 0
            # we have two choices:
            # 1)  either don't take the cur event
            # 2) if we take it then we need to find the next event we can take after this
            # next event we can only take if there start time is greater than the end time of this event.
            next = cur + 1
            while next  < len(jobs):
                if jobs[next][0] >= jobs[cur][1]:
                    break
                next += 1
            # max(notTake, take)
            return max(solve(cur + 1), jobs[cur][2] + solve(next))

        jobs.sort()   # will sort acc to start time and if start time equal then acc to end time
                        # To decide easily which event we can pick next.
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

# 2) Using Binary Search: To find the next jobs

# Note: Here we can choose the next job starting from ending time of cur job.
# So here we need to search for next job whose startTime >= endTime of cur job.
# so we will use 'bisect_left' not 'bisect_right' like Q : ""1751. Maximum Number of Events That Can Be Attended II".

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        jobs= sorted(list(zip(startTime, endTime, profit)))
        startTime= [jobs[i][0] for i in range(len(startTime))]

        @lru_cache(None)
        def solve(cur):
            # either we have traversed all the events or we have chosen the maximum no of events allowed.
            if cur >= len(jobs):
                return 0
            # we have two choices:
            # 1)  either don't take the cur event
            # 2) if we take it then we need to find the next event we can take after this
            # next event we can only take if there start time is greater than the end time of this event.
            next = bisect_left(startTime, jobs[cur][1])
            # max(notTake, take)
            return max(solve(cur + 1), jobs[cur][2] + solve(next))

        jobs.sort()   # will sort acc to start time and if start time equal then acc to end time
                        # To decide easily which event we can pick next.
        return solve(0)

# Java Code 
"""
import java.util.*;

public class Solution {
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        int n = startTime.length;
        int[][] jobs = new int[n][3];

        for (int i = 0; i < n; i++) {
            jobs[i] = new int[]{startTime[i], endTime[i], profit[i]};
        }

        Arrays.sort(jobs, Comparator.comparingInt(a -> a[0]));  // will sort acc to start time and if start time equal then acc to end time
                                                                // To decide easily which event we can pick next.
        int[] starts = new int[n];
        for (int i = 0; i < n; i++) {
            starts[i] = jobs[i][0];
        }

        Map<Integer, Integer> memo = new HashMap<>();

        return solve(0, jobs, starts, memo);
    }

    private int solve(int cur, int[][] jobs, int[] starts, Map<Integer, Integer> memo) {
        // either we have traversed all the events or we have chosen the maximum no of events allowed.
        if (cur >= jobs.length) return 0;

        if (memo.containsKey(cur)) return memo.get(cur);

        // we have two choices:
        // 1) either don't take the cur event
        // 2) if we take it then we need to find the next event we can take after this
        // next event we can only take if there start time is greater than the end time of this event.
        int next = Arrays.binarySearch(starts, jobs[cur][1]);  // simulates bisect_left
        if (next < 0) next = -next - 1;

        // max(notTake, take)
        int notTake = solve(cur + 1, jobs, starts, memo);
        int take = jobs[cur][2] + solve(next, jobs, starts, memo);

        memo.put(cur, Math.max(take, notTake));
        return memo.get(cur);
    }
}
"""

# C++ Code 
"""
class Solution {
public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        int n = startTime.size();
        vector<tuple<int, int, int>> jobs;

        for (int i = 0; i < n; ++i)
            jobs.emplace_back(startTime[i], endTime[i], profit[i]);

        sort(jobs.begin(), jobs.end());  // will sort acc to start time and if start time equal then acc to end time
                                         // To decide easily which event we can pick next.

        vector<int> starts;
        for (auto& [s, e, p] : jobs) {
            starts.push_back(s);
        }

        unordered_map<int, int> memo;
        return solve(0, jobs, starts, memo);
    }

private:
    int solve(int cur, const vector<tuple<int, int, int>>& jobs, const vector<int>& starts,
              unordered_map<int, int>& memo) {
        // either we have traversed all the events or we have chosen the maximum no of events allowed.
        if (cur >= jobs.size()) return 0;

        if (memo.count(cur)) return memo[cur];

        auto [s, e, p] = jobs[cur];

        // Binary search equivalent to bisect_left
        int next = lower_bound(starts.begin(), starts.end(), e) - starts.begin();

        // max(notTake, take)
        int notTake = solve(cur + 1, jobs, starts, memo);
        int take = p + solve(next, jobs, starts, memo);

        return memo[cur] = max(take, notTake);
    }
};
"""
# Without inbuilt binary search and with 2-d array for interview
"""
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
"""
# Java Code 
"""
import java.util.*;

public class Solution {
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        // Create jobs as a list of tuples (startTime, endTime, profit) and sort them
        int n = startTime.length;
        int[][] jobs = new int[n][3];
        for (int i = 0; i < n; i++)
            jobs[i] = new int[]{startTime[i], endTime[i], profit[i]};
        Arrays.sort(jobs, Comparator.comparingInt(a -> a[0]));  // Sort by start time and then by end time

        // Initialize a 2D array for memoization
        int[][] dp = new int[n][2];  // dp[i][0]: max profit from job i, dp[i][1]: not used
        for (int[] row : dp) Arrays.fill(row, -1);

        return solve(0, jobs, dp);
    }

    private int solve(int cur, int[][] jobs, int[][] dp) {
        int n = jobs.length;

        // Base case: If we have traversed all jobs
        if (cur >= n) return 0;

        // Check if we already computed this state
        if (dp[cur][0] != -1) return dp[cur][0];

        // Option 1: Don't take the current job
        int notTake = solve(cur + 1, jobs, dp);

        // Option 2: Take the current job
        int nextJob = binarySearchNext(jobs[cur][1], cur, jobs);  // Find the next job that can be taken
        int take = jobs[cur][2] + solve(nextJob, jobs, dp);

        // Store the maximum profit in the dp array
        dp[cur][0] = Math.max(take, notTake);
        return dp[cur][0];
    }

    // Binary search to find the next job that starts after the current job ends
    private int binarySearchNext(int endTime, int cur, int[][] jobs) {
        int low = cur + 1, high = jobs.length - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (jobs[mid][0] >= endTime)
                high = mid - 1;  // Move left to find the first non-conflicting job
            else
                low = mid + 1;  // Move right
        }
        return low;  // Return the index of the next job
    }
}
"""

# C++ Code 
"""
class Solution {
public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        // Create jobs as a list of tuples (startTime, endTime, profit) and sort them
        vector<tuple<int, int, int>> jobs;
        int n = startTime.size();
        for (int i = 0; i < n; ++i)
            jobs.emplace_back(startTime[i], endTime[i], profit[i]);

        sort(jobs.begin(), jobs.end());  // Sort by start time and then by end time

        // Initialize a 2D array for memoization
        vector<vector<int>> dp(n, vector<int>(2, -1));  // dp[i][0]: max profit from job i, dp[i][1]: not used

        return solve(0, jobs, dp);
    }

private:
    int solve(int cur, const vector<tuple<int, int, int>>& jobs, vector<vector<int>>& dp) {
        int n = jobs.size();

        // Base case: If we have traversed all jobs
        if (cur >= n) return 0;

        // Check if we already computed this state
        if (dp[cur][0] != -1) return dp[cur][0];

        // Option 1: Don't take the current job
        int notTake = solve(cur + 1, jobs, dp);

        // Option 2: Take the current job
        int nextJob = binarySearchNext(get<1>(jobs[cur]), cur, jobs);  // Find the next job that can be taken
        int take = get<2>(jobs[cur]) + solve(nextJob, jobs, dp);

        // Store the maximum profit in the dp array
        dp[cur][0] = max(take, notTake);
        return dp[cur][0];
    }

    // Binary search to find the next job that starts after the current job ends
    int binarySearchNext(int endTime, int cur, const vector<tuple<int, int, int>>& jobs) {
        int low = cur + 1, high = jobs.size() - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (get<0>(jobs[mid]) >= endTime)
                high = mid - 1;  // Move left to find the first non-conflicting job
            else
                low = mid + 1;  // Move right
        }
        return low;  // Return the index of the next job
    }
};
"""

# Method 2:

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        for i in range(len(startTime)):
            jobs.append([startTime[i], endTime[i], profit[i]])
            jobs.sort()
        return self.helper(0, -1, jobs)  # '-1' last included index, '0': current index
    
    def helper(self, curr, pre, jobs):
        if curr == len(jobs):
            return 0
        if pre < 0 or jobs[curr][0] >= jobs[pre][1] :  # we can include this ele. but we have two choices either include in ans or not include.
            return max(jobs[curr][2] + self.helper(curr + 1, curr, jobs), self.helper(curr + 1, pre, jobs))
        # only one choice we can't include this ele
        return self.helper(curr + 1, pre, jobs)

# Java Code 
"""
import java.util.*;

public class Solution {
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        List<int[]> jobs = new ArrayList<>();
        for (int i = 0; i < startTime.length; i++) {
            jobs.add(new int[]{startTime[i], endTime[i], profit[i]});
        }
        jobs.sort((a, b) -> Integer.compare(a[0], b[0]));  // sort the jobs by start time

        return helper(0, -1, jobs);  // '-1' last included index, '0': current index
    }

    private int helper(int curr, int pre, List<int[]> jobs) {
        if (curr == jobs.size())
            return 0;
        if (pre < 0 || jobs.get(curr)[0] >= jobs.get(pre)[1]) {
            // we can include this ele. but we have two choices either include in ans or not include.
            return Math.max(
                jobs.get(curr)[2] + helper(curr + 1, curr, jobs),
                helper(curr + 1, pre, jobs)
            );
        }
        // only one choice we can't include this ele
        return helper(curr + 1, pre, jobs);
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
        std::sort(jobs.begin(), jobs.end());  // sort the jobs by start time

        return helper(0, -1, jobs);  // '-1' last included index, '0': current index
    }

private:
    int helper(int curr, int pre, const std::vector<std::vector<int>>& jobs) {
        if (curr == jobs.size())
            return 0;
        if (pre < 0 || jobs[curr][0] >= jobs[pre][1]) {
            // we can include this ele. but we have two choices either include in ans or not include.
            return std::max(
                jobs[curr][2] + helper(curr + 1, curr, jobs),
                helper(curr + 1, pre, jobs)
            );
        }
        // only one choice we can't include this ele
        return helper(curr + 1, pre, jobs);
    }
};
"""