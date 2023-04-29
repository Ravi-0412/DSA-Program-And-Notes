# submitted on lintcode

# if starting time of any meeting is < neding time of previous ongoing meeting then person can't atttend all meetings.
# And we can only compare if we know the timing of prevoius meeeting.
# And to know which meeting is going before we need to sort the intervals based on starting time.

# Reason for sorting based on starting time: we have to first start with interval having minimum starting time and
#  after that we have to schedule  next interval with minimum time.
# but before scheduling we have to check whether that is overlapping with previous one.
# That's why we need to sort intervals based on starting time. 

# overlapping check karne ke liye hmko chahiye previous interval ka "end time" and current ka "start time" and start time jitna close ho ek dusre se,
# In simplest way: Aise bhi interval ko hm starting time ke anusar hi start karenge isliye 'starting point' ke anusar sort karenge.

# time: O(n*logn)
class Solution:
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda i: i.start)  # sorting based on starting point
        for i in range(1, len(intervals)):
            end1=   intervals[i-1].end
            start2= intervals[i].start
            if start2 < end1:
                return False
        return True

