# my mistakes: i was thinking like 'find the max no of overlapping subproblem' and sbtract '-1'.
# but it won't work. 

# for intervlas problems, draw the intervals on the number line and see.

# logic: once you find any overlapping intervals, just delete the one having larger end value.
# greddy about:  always pick the interval with the earliest end time as we an start the upcoming interval earlier and faster.
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        preEnd= intervals[0][1]  
        ans= 0
        for start, end in intervals[1:]:
            if start>= preEnd:  # if they are not overlapping
                preEnd= end
            else:  # if they are overlapping
                ans+= 1
                # delete the one having larger ending time and keep the one having lesser ending time.
                preEnd= min(preEnd, end)
        return ans

