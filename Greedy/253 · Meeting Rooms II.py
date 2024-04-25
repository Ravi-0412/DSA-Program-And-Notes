# it basically asking what is the 'maximum no of overlapping meetings at any given point of time'.
# Also this problem can be reduced to : 'Divide the intervals into minimum no of different parts 
# such that no two intervals in respective parts are overlapping. Find the no of parts.'.

# meeting in same part can be executed after completion of previous meeting without any overlap.
# so max no of room = no of parts

# Brute Force: O(n^2)
# just sort and check the current meeting start time with the end of all the meetings before.
# if none of previous meeting has ended, incr the count by '1' because we will have to arrange the current meeting in different conference room.'
# at last return the count

# method 2: O(n*logn)
# Logic: Jo room khali hoga koi interval ke bad uske hmko use karna h and apna sb interval ko run karbana h.
# Hmko bs sb meeting start kar dena h.
# Iske liye koi meeting end ho rha h ki nhi , cur meeting ke start se phle wo hmko track karna hoga
# for minimum ans we need the smallest ending time .
# from here we get intuition that we have to sort according to minimum ending time.

# Now we will try to schedule the meeting having minimum starting time first if any meeting ends
# from here we get intuition of soting base on starting time also.

# finally we have to sort based on starting and ending time separately.

# Note: Just focus on that "we have to start all the meetings".

# How to do?: Take two arrays say start and end that will store the start and end time of meetings respectively.
# now sort these arrays
# vvi: now take two pointer one each to start and end array respectively.
# run the loop till all meetings has started because after all meeting have started then no need to alloacate any different room.
# compare both the pointer value and if overlapping i.e start value is less than incr the count by '1' and incr the start pointer.
# else decr the count by '1' and incr the end pointer.
# after every comparison update the ans

# here count will tell the 'no of conferernce room at present' after each meeting.

# why we came through this? if start is less than end value then it means the ongoing meeting has not ended and we have to start the new meeting
# so incr the count by '1'.
# else: one of the meeting has ended so decr the count by '1'.

# Note: Another way of asking this Q :"Find the maximum no of overlapping intervals at once"

class Solution:
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        start= sorted([i.start for i in intervals])
        end=   sorted([i.end   for i in intervals])
        ans, count= 0, 0
        s, e= 0, 0  # pointer to start and end array
        while s< len(start):  # till we have started all the meetings
            # overlapping so we will need one new room.
            if start[s] < end[e]:
                count+= 1  # allocated new room for overlapping meeting 
                s+= 1   # started one so incr 's' by '1'.
                ans= max(ans, count)
            else:
                # one meeting ended. now the previous can be used for different meeting so decr total no of room required.
                count-= 1   
                e+= 1  # 
        return ans


# Related Q:
# 1) Minimum Platforms