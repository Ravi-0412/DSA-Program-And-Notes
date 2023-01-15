# did myself but don't know why giving incorrect answer. Have to ask someone
# after memoizing it will go in time= space= O(n^2)
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        return self.helper(startTime, endTime, profit, -1, 0)  # '-1' last included index, '0': current index
    
    def helper(self, start, end, profit, pre, curr):
        if curr== len(start):
            return 0
        if pre < 0 or start[curr] >= end[pre]:  # we can include this ele. but we have two choices either include in ans or not include.
            return max(profit[curr] + self.helper(start, end, profit, curr, curr+1), self.helper(start, end, profit, pre, curr +1))
        else:  # only one choice we can't include this ele
            return self.helper(start, end, profit, pre, curr +1)

# other method which is working.
# method 1: using linear search to find the next job.
# time: O(n^2). 
# space: O(n)
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # sorting the jobs according to startTime to find the next job having startTime>= endTime of last included job.
        jobs= sorted(list(zip(startTime, endTime, profit)))
        n= len(jobs)
        startTime= [jobs[i][0] for i in range(n)]    # to find the next job easily. now this array will be in sorted order

        def dp(i):
            if i== n: return 0
            ans= dp(i+1)     # when we don't include the current ele 
            next= bisect_left(startTime, jobs[i][1])   # will return the index of next job having startTime >= endTime of curr job.
            ans= max(ans, jobs[i][2]+ dp(next))      # when we include the curr job.
            return ans
        
        return dp(0)


# method 2: using binary search to find the next job.
# time: O(nlogn). : sorting or also to find the next job for each index (logn)
# space: O(n)
# Recursive way
from collections import bisect_left
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # sorting the jobs according to startTime to find the next job having startTime>= endTime of last included job.
        jobs= sorted(list(zip(startTime, endTime, profit)))
        n= len(jobs)
        startTime= [jobs[i][0] for i in range(n)]    # to find the next job easily. now this array will be in sorted order

        def dp(i):
            if i== n: return 0
            next= bisect_left(startTime, jobs[i][1])   # will return the index of next job having startTime >= endTime of curr job.
            return max(dp(i+1), jobs[i][2]+ dp(next))  # when we don't include the current ele and when we include the curr job

        return dp(0)


# memoisation. just added the '@lru_cache(None)'.
from collections import bisect_left
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # sorting the jobs according to startTime to find the next job having startTime>= endTime of last included job.
        jobs= sorted(list(zip(startTime, endTime, profit)))
        n= len(jobs)
        startTime= [jobs[i][0] for i in range(n)]    # to find the next job easily. now this array will be in sorted order

        def dp(i):
            if i== n: return 0
            next= bisect_left(startTime, jobs[i][1])   # will return the index of next job having startTime >= endTime of curr job.
            return max(dp(i+1), jobs[i][2]+ dp(next))  # when we don't include the current ele and when we include the curr job

        return dp(0)

