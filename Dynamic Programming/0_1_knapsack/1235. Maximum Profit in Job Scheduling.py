# This Q is exactly same as: "1751. Maximum Number of Events That Can Be Attended II".
# Difference : Here  1) there is no limit on taking the job like :'k' jobs only.
# 2) next job can start at ending time of another job.

# Same code of Q: "1751. Maximum Number of Events That Can Be Attended II"  

# 1) Using linear Search : To find the next job
# Time: O(n^2)
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        for i in range(len(startTime)):
            jobs.append([startTime[i], endTime[i], profit[i]])
        # jobs= sorted(list(zip(startTime, endTime, profit)))   # shortcut

        @lru_cache(None)
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

