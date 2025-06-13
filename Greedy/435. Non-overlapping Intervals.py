"""
my mistake: i was thinking like 'find the max no of overlapping interval at once' and subtract '-1'.
which is same as "253. meeting rooms 2"
Reason: if some interval is very big then it make make a lot of intervals overlapping so our ans will be more than expected.
e.g: [1, 10], [2, 3], [3, 4], [4,5]... 
[1, 10] will make all interval overlapping so our ans will increase.
But if we remove [1, 10] then all interval will non-overlapping

Reason: Because intervals in one room can come after any interval of other room.

Note: Here one interval can start on ending day of another interval.

Note: Another way of asking some Q is "max no of non-overlapping interval we can get ".
Ans = total - removed_one.
Finding "max no of non-overlapping interval" is exactly same as classical problem i.e "Interval scheduling"
https://en.wikipedia.org/wiki/Interval_scheduling#Interval_Scheduling_Maximization

for intervlas problems, draw the intervals on the number line and see.

How to solve ?
Vvi: Just think intervals as real life event then to attend the maximum no of events ,
you will attend the event having lesser ending time.

logic: once you find any overlapping intervals, just delete the one having larger end value.
How to think? 
Ans: just think in real life, when you will see events overlapping you will attend the event having lesser ending time 
I.e you will not attend the event with greater ending time in case of overlapping one.

More explanation:
Now, let's say there's an optimal solution different from ours that keeps an interval i with an end time later than the one we chose
(let's call our interval x). We can replace i with x in this solution, 
and it's guaranteed not to create more overlaps because x ends earlier than i. 

greedy about:  always pick the interval with the earliest end time as we an start the upcoming interval earlier and faster.

How to think of greedy i.e greedy will give the optimal solution?
The greedy choice property means that a local optimum can lead to a global optimum. For this problem,
the local optimum is to always select the interval with the earliest end time that doesn't overlap with the current one. 
This choice leaves as much space as possible for the remaining intervals. 
If we can prove that making the greedy choice at each step leads to the solution of the overall problem, 
then greedy will work perfectly.
"""

# Method 1:
"""
Find the maximum no of non-overlapping interval.
Then, ans = total - max_no_of_non-overlapping_interval
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x : x[1])   
        preEnd= intervals[0][1]  # will keep track end time of last added interval.
        count = 1  # will count the max no of non-overlapping intervals. 
                   # Starting from '1 because if not overlap then at 1st time we will have to add both the intervals.
        for start, end in intervals[1:]:
            # if they are not overlapping
            if start >= preEnd: 
                preEnd = end
                count += 1
            # if overlapping,  skip the cur one since pre ending interval will be before only and we already taken that.
        return len(intervals) - count
    

# Java
"""
import java.util.Arrays;

class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        intervals = Arrays.copyOf(intervals, intervals.length);
        // sort by end time
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));

        int preEnd = intervals[0][1];  // will keep track end time of last added interval.
        int count = 1;  // will count the max no of non-overlapping intervals. 
                        // Starting from '1' because if not overlap then at 1st time we will have to add both the intervals.

        for (int i = 1; i < intervals.length; i++) {
            int start = intervals[i][0];
            int end = intervals[i][1];

            // if they are not overlapping
            if (start >= preEnd) {
                preEnd = end;
                count += 1;
            }
            // if overlapping, skip the cur one since pre ending interval will be before only and we already taken that.
        }

        return intervals.length - count;
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
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        // sort by end time
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });

        int preEnd = intervals[0][1];  // will keep track end time of last added interval.
        int count = 1;  // will count the max no of non-overlapping intervals. 
                        // Starting from '1' because if not overlap then at 1st time we will have to add both the intervals.

        for (int i = 1; i < intervals.size(); i++) {
            int start = intervals[i][0];
            int end = intervals[i][1];

            // if they are not overlapping
            if (start >= preEnd) {
                preEnd = end;
                count += 1;
            }
            // if overlapping, skip the cur one since pre ending interval will be before only and we already taken that.
        }

        return intervals.size() - count;
    }
};
"""

# Method 2: 
"""
Directly find the ans.
Sorting based on starting time. But endTime to minimum h rakhna h.
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        preEnd = intervals[0][1] 
        ans= 0
        for start, end in intervals[1:]:
            if start>= preEnd:  # if they are not overlapping
                preEnd = end
            else:  # if they are overlapping
                ans += 1
                # delete the one having larger ending time and keep the one having lesser ending time.
                preEnd= min(preEnd, end)  # No need of this in 1st method because  earlier one will have lesser ending time
        return ans
    

# Java
"""
import java.util.Arrays;

class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        int preEnd = intervals[0][1];
        int ans = 0;

        for (int i = 1; i < intervals.length; i++) {
            int start = intervals[i][0];
            int end = intervals[i][1];

            if (start >= preEnd) {  // if they are not overlapping
                preEnd = end;
            } else {  // if they are overlapping
                ans += 1;
                // delete the one having larger ending time and keep the one having lesser ending time.
                preEnd = Math.min(preEnd, end);  // No need of this in 1st method because earlier one will have lesser ending time
            }
        }

        return ans;
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
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());

        int preEnd = intervals[0][1];
        int ans = 0;

        for (int i = 1; i < intervals.size(); i++) {
            int start = intervals[i][0];
            int end = intervals[i][1];

            if (start >= preEnd) {  // if they are not overlapping
                preEnd = end;
            } else {  // if they are overlapping
                ans += 1;
                // delete the one having larger ending time and keep the one having lesser ending time.
                preEnd = min(preEnd, end);  // No need of this in 1st method because earlier one will have lesser ending time
            }
        }

        return ans;
    }
};
"""
# Method 3: 
# Directly find the 'max no of non-overlapping interval' when we sort based on start time.


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


# Java
"""
import java.util.Arrays;

class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        int preEnd = intervals[0][1];  // will keep track of last added interval.
        int count = 1;  // will count the max no of non-overlapping intervals. 
                        // Starting from '1' because if not overlap then at 1st time we will have to add both the intervals.

        for (int i = 1; i < intervals.length; i++) {
            int start = intervals[i][0];
            int end = intervals[i][1];

            if (start >= preEnd) {  // if they are not overlapping
                preEnd = end;
                count += 1;
            } else {  // if they are overlapping
                // delete the one having larger ending time and keep the one having lesser ending time.
                preEnd = Math.min(preEnd, end);
            }
        }

        return intervals.length - count;
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
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());

        int preEnd = intervals[0][1];  // will keep track of last added interval.
        int count = 1;  // will count the max no of non-overlapping intervals. 
                        // Starting from '1' because if not overlap then at 1st time we will have to add both the intervals.

        for (int i = 1; i < intervals.size(); i++) {
            int start = intervals[i][0];
            int end = intervals[i][1];

            if (start >= preEnd) {  // if they are not overlapping
                preEnd = end;
                count += 1;
            } else {  // if they are overlapping
                // delete the one having larger ending time and keep the one having lesser ending time.
                preEnd = min(preEnd, end);
            }
        }

        return intervals.size() - count;
    }
};
"""