# Simple only

# Time: O(n*n*k) but it will never go till here.
# It will reach the base case faster i.e k==0 or also choosing next ele will also reduce the function call.

# Note vvi: When you have to select 'next' possible ele based on some condition then, no need to take 
# one more parameter 'pre' in function call, just do like this only.

# Raecursion + memoisation
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        @lru_cache(None)
        def solve(cur, k):
            # either we have traversed all the events or we have chosen the maximum no of events allowed.
            if cur >= len(events) or k == 0:
                return 0
            # we have two choices:
            # 1)  either don't take the cur event
            # 2) if we take it then we need to find the next event we can take after this
            # next event we can only take if there start time is greater than the end time of this event.
            next = cur + 1
            while next  < len(events):
                if events[next][0] > events[cur][1]:
                    break
                next += 1
            # max(notTake, take)
            return max(solve(cur + 1, k), events[cur][2] + solve(next, k - 1))

        events.sort()   # will sort acc to start time and if start timme equal then acc to end time
                        # To decide easily which event we can pick next.
        return solve(0, k)


# Note vvi: Finding the next in worst case can be O(n).
# But we can use binary search to find the 'next' in O(logn).
# Reason: we need to find the 1st event whose startDate > endDate of cur event.
# Since our events is already sorted acc to startDate, we can use binary search.
next = cur + 1
while next  < len(events):
    if events[next][0] > events[cur][1]:
        break
    next += 1

# Optimised one:
# Time: O(n*k*logn)
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        @lru_cache(None)
        def solve(cur, k):
            # either we have traversed all the events or we have chosen the maximum no of events allowed.
            if cur >= len(events) or k == 0:
                return 0
            # we have two choices:
            # 1)  either don't take the cur event
            # 2) if we take it then we need to find the next event we can take after this
            # next event we can only take if there start time is greater than the end time of this event.
            next = bisect.bisect_right(startDate, events[cur][1])
            return max(solve(cur + 1, k), events[cur][2] + solve(next, k - 1))

        events.sort()   # will sort acc to start time and if start timme equal then acc to end time
        startDate = [start for start, end, value in events]

        return solve(0, k)



# My doubt
# After finding the next , i am not breaking the loop.
# So giving incorrect because in this take will always take last index satisfying the condition and
# breaking one we can't do in for loop because 'recursion' call is also associated .

# Either do like above one or take one more parameter 'pre' in function call.


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:

        def solve(cur, k):
            # either we have traversed all the events or we have chosen the maximum no of events allowed.
            if cur >= len(events) or k == 0:
                return 0
            # we have two choices:
            # 1)  either don't take the cur event
            notTake = solve(cur + 1 , k)
            # 2) if we take it then we need to find the next event we can take after this
            # next event we can only take if there start time is greater than the end time of this event.
            take = 0
            for next in range(cur + 1 , len(events)):
                if events[next][0] > events[cur][1]:
                    take = events[cur][2] + solve(next, k -1)
            return max(take, notTake)

        events.sort()   # will sort acc to start time and if start timme equal then acc to end time
        return solve(0, k)


# Method 2:
# Take one more parameter 'pre' in function call.
# Replaced events -> jobs

# Can further optimise using binary search.

class Solution:
    def jobScheduling(self, jobs: List[List[int]], k: int) -> int:
        jobs = []
        for i in range(len(startTime)):
            jobs.append([startTime[i], endTime[i], profit[i]])
        jobs.sort()
        return self.helper(0, -1, jobs)  # '-1' last included index, '0': current index
    
    def helper(self, curr, pre, jobs, k):
        if curr == len(jobs) or k == 0:
            return 0
        if pre < 0 or jobs[curr][0] >= jobs[pre][1] :  # we can include this ele. but we have two choices either include in ans or not include.
            return max(jobs[curr][2] + self.helper(curr + 1, curr, jobs, k - 1), self.helper(curr + 1, pre, jobs, k))
        # only one choice we can't include this ele
        return self.helper(curr + 1, pre, jobs)
