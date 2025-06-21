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
