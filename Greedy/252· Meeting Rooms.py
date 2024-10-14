# submitted on Neetcode.io

# if starting time of any meeting is < ending time of previous ongoing meeting then person can't atttend all meetings.
# And we can only compare if we know the timing of prevoius meeeting.
# And to know which meeting is going before we need to sort the intervals based on starting time.


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

