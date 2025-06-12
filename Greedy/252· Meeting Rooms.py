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

"""
# TIME COMPLEXITY : 

# -> Sorting : 0(n log n), Iteration : 0(n)

# Overall : 0(n log n)

# SPACE COMPLEXITY : O(1) 
"""

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # sort intervals by start time
        intervals.sort(key=lambda i: i[0])

        for i in range(1, len(intervals)):
            prev = intervals[i - 1]
            curr = intervals[i]

            # if the previous meeting ends after the current one starts, conflict
            if prev[1] > curr[0]:
                return False

        return True

# java
"""
import java.util.*;

class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        // sort intervals by start time
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        for (int i = 1; i < intervals.length; i++) {
            // if the previous meeting ends after the current one starts, conflict
            if (intervals[i - 1][1] > intervals[i][0]) {
                return false;
            }
        }

        return true;
    }
}
"""


# C++
"""
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool canAttendMeetings(vector<vector<int>>& intervals) {
        // sort intervals by start time
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        for (int i = 1; i < intervals.size(); i++) {
            // if the previous meeting ends after the current one starts, conflict
            if (intervals[i - 1][1] > intervals[i][0]) {
                return false;
            }
        }

        return true;
    }
};
"""









