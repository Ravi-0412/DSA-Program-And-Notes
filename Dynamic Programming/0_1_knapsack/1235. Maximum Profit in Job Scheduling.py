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

# Java
"""
class Solution {
    // 2D array to store jobs and a dp array for memoization
    private int[][] jobs;
    private int[][] dp;
    private int n;

    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        n = startTime.length;
        jobs = new int[n][3];

        // Create jobs as a 2D array and sort them
        for (int i = 0; i < n; i++) {
            jobs[i][0] = startTime[i]; // Start time
            jobs[i][1] = endTime[i];   // End time
            jobs[i][2] = profit[i];     // Profit
        }

        // Sort jobs by start time
        Arrays.sort(jobs, Comparator.comparingInt(a -> a[0]));

        // Initialize a 2D array for memoization
        dp = new int[n][2];
        for (int[] row : dp) {
            Arrays.fill(row, -1);
        }

        return solve(0);
    }

    // Function to perform binary search for the next job
    private int binarySearchNext(int startTime, int cur) {
        int low = cur + 1, high = n - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (jobs[mid][0] >= startTime) {
                high = mid - 1; // Move left to find the first non-conflicting job
            } else {
                low = mid + 1; // Move right
            }
        }
        return low; // Return the index of the next job
    }

    // Recursive function to calculate maximum profit
    private int solve(int cur) {
        // Base case: If we have traversed all jobs
        if (cur >= n) {
            return 0;
        }

        // Check if we already computed this state
        if (dp[cur][0] != -1) {
            return dp[cur][0];
        }

        // Option 1: Don't take the current job
        int notTake = solve(cur + 1);

        // Option 2: Take the current job
        int nextJob = binarySearchNext(jobs[cur][1], cur); // Find the next job that can be taken
        int take = jobs[cur][2] + solve(nextJob);

        // Store the maximum profit in the dp array
        dp[cur][0] = Math.max(notTake, take);
        return dp[cur][0];
    }
}


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

