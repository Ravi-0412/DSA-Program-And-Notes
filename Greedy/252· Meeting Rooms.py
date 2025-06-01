# Intution first, Codes next (in Python,Java,C++) and Time complexity at the last. 

# Intution :

# Our goal is to make the person attend all the meetings - If he can do so, we need to return True, else False.
# Initially, all the meeting timings are given randomly, so we need to arrange them, according to their times, in such a way that the person can attend all the meetings.
# So, let's sort the meetings array based on the start time of each meeting.

# EDGE CASE :
# If the meetings array just contains of one meeting (n==1), then we will return True without any further checks.

# We will check if the start time of the current meeting is more than the end time of the previous meeting. If yes, we will proceed, else we will return False. 
# To check for the previous meeting, we will start iterating in the meetings array from 1st index, instead of the 0th.

# If we pass complete the iteration without returning False, then we will return True.

# CODES : 

# PYTHON


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False
        return True
    




# JAVA 




# import java.util.*;

# class Interval {
#     int start;
#     int end;

#     Interval() {}
#     Interval(int s, int e) {
#         start = s;
#         end = e;
#     }
# }

# class Solution {
#     public boolean canAttendMeetings(Interval[] intervals) {
#         Arrays.sort(intervals, (a, b) -> a.start - b.start);

#         for (int i = 1; i < intervals.length; i++) {
#             if (intervals[i - 1].end > intervals[i].start) {
#                 return false;
#             }
#         }
#         return true;
#     }
# }





# C++





#include <vector>
#include <algorithm>

# using namespace std;

# struct Interval {
#     int start;
#     int end;
#     Interval() {}
#     Interval(int s, int e) : start(s), end(e) {}
# };

# class Solution {
# public:
#     bool canAttendMeetings(vector<Interval>& intervals) {
#         sort(intervals.begin(), intervals.end(), [](const Interval &a, const Interval &b) {
#             return a.start < b.start;
#         });

#         for (int i = 1; i < intervals.size(); i++) {
#             if (intervals[i - 1].end > intervals[i].start) {
#                 return false;
#             }
#         }
#         return true;
#     }
# };





# TIME COMPLEXITY : 

# -> Sorting : 0(n log n)
# -> Iteration : 0(n)

# Overall : 0(n log n)




# SPACE COMPLEXITY :

# O(1) (if sorting is in-place)

