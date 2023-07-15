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
            next = bisect_right(startDate, events[cur][1])
            return max(solve(cur + 1, k), events[cur][2] + solve(next, k - 1))

        events.sort()   # will sort acc to start time and if start timme equal then acc to end time
        startDate = [start for start, end, value in events]

        return solve(0, k)



# My doubt
# Writing the same code in this form is not working. Have to ask someone.

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
                    notTake = events[cur][2] + solve(next, k -1)
            return max(take, notTake)

        events.sort()   # will sort acc to start time and if start timme equal then acc to end time
        return solve(0, k)


# Method 2:
