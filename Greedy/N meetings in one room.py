# Logic: replace room -> person.
# Now question reduce to "maximum meeting this person can attend".
# For attending maximum meeting , he should attend the meeting having less ending time first.

class Solution:
    def maximumMeetings(self,n,start,end):
        meeting = []
        for i in range(n):
            meeting.append([start[i], end[i]])

        meeting.sort(key = lambda x: x[1])   # sorting based on ending time
        ans = 1
        cur = 0   # cur meeting he is attending
        for i in range(1, n):
            if meeting[i][0] > meeting[cur][1]:
                # then only we can attend the cur meeting
                cur = i
                ans += 1
            # else: skip simply because we can't attend cur meeting
        return ans