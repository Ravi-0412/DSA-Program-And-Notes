# submitted on lintcode
class Solution:
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda i: i.start)
        for i in range(1, len(intervals)):
            end1=   intervals[i-1].end
            start2= intervals[i].start
            if start2 < end1:
                return False
        return True

