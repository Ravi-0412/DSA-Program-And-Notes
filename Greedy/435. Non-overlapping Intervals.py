# my mistakes: i was thinking like 'find the max no of overlapping interval at once' and subtract '-1'.
# which is same as "253. meeting rooms 2"
# but it won't work. => Why ? 

# Reason: Because intervals in one room can come after any interval of other room.

# Note: Here one interval can start on ending day of another interval.

# Note: Another way of asking some Q is "max no of non-overlapping interval we can get ".
# Ans = total - removed_one.
# Finding "max no of non-overlapping interval" is exactly same as classical problem i.e "Interval scheduling"
# https://en.wikipedia.org/wiki/Interval_scheduling#Interval_Scheduling_Maximization

# for intervlas problems, draw the intervals on the number line and see.
# Diagram in notes. page : 165

# How to solve ?
# Vvi: Just think intervals as real life event then to attend the maximum no of events ,
# you will attend the event having lesser ending time.

# logic: once you find any overlapping intervals, just delete the one having larger end value.
# How to think? 
# Ans: just think in real life, when you will see events overlapping you will attend the event having lesser ending time 
# I.e you will not attend the event with greater ending time in case of overlapping one.

# More explanation:
# Now, let's say there's an optimal solution different from ours that keeps an interval i with an end time later than the one we chose
# (let's call our interval x). We can replace i with x in this solution, 
# and it's guaranteed not to create more overlaps because x ends earlier than i. 

# greedy about:  always pick the interval with the earliest end time as we an start the upcoming interval earlier and faster.

# How to think of greedy i.e greedy will give the optimal solution?
# The greedy choice property means that a local optimum can lead to a global optimum. For this problem,
# the local optimum is to always select the interval with the earliest end time that doesn't overlap with the current one. 
# This choice leaves as much space as possible for the remaining intervals. 
# If we can prove that making the greedy choice at each step leads to the solution of the overall problem, 
# then greedy will work perfectly.

# Method 1:
# sorting based on starting time.

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
                preEnd= min(preEnd, end)  # No need of this as earlier one will have lesser ending time
        return ans


# 2nd method :
# just count the max no of non-overlappping interval say = count
# Then our ans will equal to 'len(intervals) - count'.
# Exactly same above logic only.


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        preEnd= intervals[0][1]  # will keep tarck of last added inetrval.
        count = 1  # will count the max no of non-overlapping intervals. 
                   # Starting from '1 because if not overlap then at 1st time we will have to add both the intervals.
        for start, end in intervals[1:]:
            if start>= preEnd:  # if they are not overlapping
                preEnd= end
                count += 1
            else:  # if they are overlapping
                # delete the one having larger ending time and keep the one having lesser ending time.
                preEnd= min(preEnd, end)  
        return len(intervals) - count
    

# Method 3:  way of doing 
# Since we will take the interval having lesser end in case of overlapping so we can sort them based on ending time only in increasing order.

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x : x[1])   
        preEnd= intervals[0][1]  # will keep track of last added inetrval.
        count = 1  # will count the max no of non-overlapping intervals. 
                   # Starting from '1 because if not overlap then at 1st time we will have to add both the intervals.
        for start, end in intervals[1:]:
            # if they are not overlapping
            if start >= preEnd: 
                preEnd= end
                count += 1
            # if overlapping,  skip the cur one since pre ending interval will be before only and we already taken that.
        return len(intervals) - count



# To directly get the ans. 
# Method 3 only.
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x : x[1])
        # 1st interval must be included we can't remove 1st one.
        preEnd= intervals[0][1]  # will keep track of last added inetrval.
        ans= 0
        for start, end in intervals[1:]:
            # if they are not overlapping, no need to remove
            if start >= preEnd: 
                preEnd= end
            else:
                # if overlapping then we have to remove
                ans += 1
        return ans
