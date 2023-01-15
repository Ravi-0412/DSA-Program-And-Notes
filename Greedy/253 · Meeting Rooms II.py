# it basically asking what is the 'maximum no of overlapping meetings at any given point of time'.
# Also this problem can be reduced to : 'Divide the intervals into minimum no of different parts 
# such that no two intervals in respective parts are overlapping. Find the no of parts.'.

# Brute Force: O(n^2)
# just sort and check the current meeting start time with the end of all the meetings before.
# if none of previous meeting has ended, incr the count by '1' because we will have to arrange the current meeting in different conference room.'
# at last return the count

# method 2: O(n*logn)
# logic: Take two arrays say start and end that will store the start and end time of meetings respectively.
# now sort these arrays
# main: now take two pointer one each to start and end array respectively.
# run the loop till all meetings has started.
# compare both the pointer value and if start value is less than incr the count by '1' and incr the start pointer.
# else decr the count by '1' and incr the end pointer.
# after every comparison update the ans

# here count will tell the no of overlapping meetings at present.

# why we came through this? if start is less than end value then it means the ongoing meeting has not started and we have to start the curr meeting
# so incr the count by '1'.
# else: one of the meetinmg has ended so decr the count by '1'.

class Solution:
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        start= sorted([i.start for i in intervals])
        end=   sorted([i.end   for i in intervals])
        ans, count= 0, 0
        s, e= 0, 0  # pointer to start and end array
        while s< len(start):  # till we have started all the meetings
            if start[s] < end[e]:
                count+= 1
                s+= 1
                ans= max(ans, count)
            else:
                count-= 1
                e+= 1
        return ans

    
