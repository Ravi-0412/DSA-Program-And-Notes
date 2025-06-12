"""
Problem: "Find the minimum no of rooms required to schdule all meeting without any conflict".

Note: it basically asking what is the 'maximum no of overlapping meetings at any given point of time'.
Also this problem can be reduced to : 'Divide the intervals into minimum no of different parts 
such that no two intervals in respective parts are overlapping. Find the no of parts.
Meeting in same part can be executed after completion of previous meeting without any overlap.
so max no of room = no of parts.
"""

"""
Brute force but will fail
just sort and check the current meeting start time with the end of all the meetings before.
if none of previous meeting has ended, incr the count by '1' because we will have to arrange 
the current meeting in different conference room, at last return the count

fails on test cases where multiple overlapping meetings occur with the same start time 
or overlap with multiple existing meetings, such as:
intervals = [[1,5],[8,9],[8,9]]

❌ Why the brute-force logic fails:
The current approach only checks if the current meeting can reuse any one previous meeting's room
 (i.e., if it starts after another ends), and breaks early, assuming a single room can be reused for the current meeting.

But this doesn't track whether multiple overlapping meetings might require more than one room.

Time : O(n^2)
"""

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        n = len(intervals)
        count = 0

        for i in range(n):
            need_room = True
            for j in range(i):
                # if the current meeting starts after or at the end of a previous one
                if intervals[i].start >= intervals[j].end:
                    need_room = False
                    break
            if need_room:
                # no previous meeting ended before this one, need a new room
                count += 1

        return count

# Java
"""
import java.util.*;

class Interval {
    int start, end;
    Interval(int s, int e) { start = s; end = e; }
}

class Solution {
    public int minMeetingRooms(Interval[] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a.start, b.start));
        int count = 0;

        for (int i = 0; i < intervals.length; i++) {
            boolean needRoom = true;
            for (int j = 0; j < i; j++) {
                // if the current meeting starts after or at the end of a previous one
                if (intervals[i].start >= intervals[j].end) {
                    needRoom = false;
                    break;
                }
            }
            if (needRoom) {
                // no previous meeting ended before this one, need a new room
                count++;
            }
        }

        return count;
    }
}
"""

# C++
"""
#include <vector>
#include <algorithm>
using namespace std;

struct Interval {
    int start, end;
    Interval(int s, int e): start(s), end(e) {}
};

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        sort(intervals.begin(), intervals.end(), [](Interval a, Interval b) {
            return a.start < b.start;
        });

        int count = 0;
        for (int i = 0; i < intervals.size(); i++) {
            bool needRoom = true;
            for (int j = 0; j < i; j++) {
                // if the current meeting starts after or at the end of a previous one
                if (intervals[i].start >= intervals[j].end) {
                    needRoom = false;
                    break;
                }
            }
            if (needRoom) {
                // no previous meeting ended before this one, need a new room
                count++;
            }
        }
        return count;
    }
};
"""

# Method 1:

"""
Using a heap (can also term it Greedy)
As you might have understood from the problem statement, our main goal is to fit non-overlapping intervals into one day, as return the minimum days possible.

So, while iterating through the intervals, we want to know if there is any other interval, which is non-overlapping with it, that can we fit along with it in the same day.
To know more about overlapping and non-overlapping intervals, solve Meeting Rooms - 1. 

Heap is a data which the minimum value on its top and we can heappop it out.
So, if we can send the end times we encounter into the heap, and while iterating through the array, if we find the top is the heap <= satrt time of current interval, that means we can fit these both in a single day.
Hence, we will push the end times into a heap and heappop it each time the start time is more than it.

The, final length of the heap will be our answer.
This is because, the ones left in the heap are the ones which cant be merged anymore, and that is the minimum number of days required.
"""
"""
# TIME COMPLEXITY :
# -> heap opertaing takes 0(n log n ) time .
# -> itertaing throught the array is 0(n)
# -> overall time complexity is 0(nlogn)

# SPACE COMPLEXITY:
# -> 0(n) for the heap.
"""

# PYTHON :

import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])  # sort by start time
        min_heap = []  # heap to store end times

        for interval in intervals:
            # if the room due to free earliest is free before the current meeting starts
            if min_heap and min_heap[0] <= interval[0]:
                heapq.heappop(min_heap)  # reuse the room
            heapq.heappush(min_heap, interval[1])  # push current meeting's end time

        return len(min_heap)


# JAVA:

"""
import java.util.*;

class Solution {
    public int minMeetingRooms(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0])); // sort by start time
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(); // stores end times

        for (int[] interval : intervals) {
            // if the room due to free earliest is free before the current meeting starts
            if (!minHeap.isEmpty() && minHeap.peek() <= interval[0]) {
                minHeap.poll(); // reuse the room
            }
            minHeap.offer(interval[1]); // push current meeting's end time
        }

        return minHeap.size(); // number of rooms used concurrently
    }
}

"""


# C++ :

"""
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];  // sort by start time
        });

        priority_queue<int, vector<int>, greater<int>> minHeap;  // min-heap to store end times

        for (auto& interval : intervals) {
            // if the room due to free earliest is free before the current meeting starts
            if (!minHeap.empty() && minHeap.top() <= interval[0]) {
                minHeap.pop(); // reuse the room
            }
            minHeap.push(interval[1]); // push current meeting's end time
        }

        return minHeap.size(); // number of rooms used concurrently
    }
};
"""


# method 2: 
"""
Logic: Jo room khali hoga koi interval ke bad uske hmko use karna h and apna sb interval ko run karbana h.
Hmko bs sb meeting start kar dena h.
Iske liye koi meeting end ho rha h ki nhi , cur meeting ke start se phle wo hmko track karna hoga
for minimum ans we need the smallest ending time .
from here we get intuition that we have to sort according to minimum ending time.

Now we will try to schedule the meeting having minimum starting time first if any meeting ends
from here we get intuition of soting base on starting time also.

finally we have to sort based on starting and ending time separately.

Note: Just focus on that "we have to start all the meetings".

How to do?: Take two arrays say start and end that will store the start and end time of meetings respectively.
now sort these arrays
vvi: now take two pointer one each to start and end array respectively.
run the loop till all meetings has started because after all meeting have started then no need to alloacate any different room.
compare both the pointer value and if overlapping i.e start value is less than incr the count by '1' and incr the start pointer.
else decr the count by '1' and incr the end pointer.
after every comparison update the ans

here count will tell the 'no of conferernce room at present' after each meeting.

why we came through this? if start is less than end value then it means the ongoing meeting has not ended and we have to start the new meeting
so incr the count by '1'.
else: one of the meeting has ended so decr the count by '1'.

Note: Another way of asking this Q :"Find the maximum no of overlapping intervals at once"

Time: O(n*logn), space: O(n)
"""

# Python 
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end   = sorted([i[1] for i in intervals])
        ans, count = 0, 0
        s, e = 0, 0  # pointer to start and end array

        while s < len(start):  # till we have started all the meetings
            # overlapping so we will need one new room.
            if start[s] < end[e]:
                count += 1  # allocated new room for overlapping meeting 
                s += 1   # started one so incr 's' by '1'.
                ans = max(ans, count)
            else:
                # one meeting ended. now the previous can be used for different meeting so decr total no of room required.
                count -= 1   
                e += 1  
        return ans



# java
""""
import java.util.*;

class Solution {
    public int minMeetingRooms(int[][] intervals) {
        int[] start = new int[intervals.length];
        int[] end   = new int[intervals.length];

        for (int i = 0; i < intervals.length; i++) {
            start[i] = intervals[i][0];
            end[i]   = intervals[i][1];
        }

        Arrays.sort(start);
        Arrays.sort(end);
        int ans = 0, count = 0;
        int s = 0, e = 0;  // pointer to start and end array

        while (s < start.length) {  // till we have started all the meetings
            // overlapping so we will need one new room.
            if (start[s] < end[e]) {
                count++;  // allocated new room for overlapping meeting 
                s++;   // started one so incr 's' by '1'.
                ans = Math.max(ans, count);
            } else {
                // one meeting ended. now the previous can be used for different meeting so decr total no of room required.
                count--;   
                e++;  
            }
        }
        return ans;
    }
}

"""
# C++ Code 
"""
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        vector<int> start, end;
        for (auto& i : intervals) {
            start.push_back(i[0]);
            end.push_back(i[1]);
        }

        sort(start.begin(), start.end());
        sort(end.begin(), end.end());

        int ans = 0, count = 0;
        int s = 0, e = 0;  // pointer to start and end array

        while (s < start.size()) {  // till we have started all the meetings
            // overlapping so we will need one new room.
            if (start[s] < end[e]) {
                count++;  // allocated new room for overlapping meeting 
                s++;   // started one so incr 's' by '1'.
                ans = max(ans, count);
            } else {
                // one meeting ended. now the previous can be used for different meeting so decr total no of room required.
                count--;   
                e++;  
            }
        }
        return ans;
    }
};

"""

# Method 3: 
"""
Note: Using Sweep Line Algorithm 
If you do not have prior knowledge about the Sweep Line Algorithm, learn it and come back again - Prefix Sums is a pre-requisite.

For those have an idea about sweep Line - Here's a quick revision :
-> It is mostly used for interval related problems
-> To count or to populate the number of elements present at a certain time in 0(1) time, we used this algorithm.
-> We define an empty array set to 0 of n size.
-> We add 1 to the initial points of all the starting points of the intervals and -1 to the end points.
-> This way, while iterating through the created array, we can keep a count of the sum acquired at each point, giving us the population of it at that time in 0(1).


How is sweep line used in this question ? 

After making ready the prefix array, while iterating through it, we keep a count of the maximum sum encountered.
This, in turn will be the no. of days required.

You can do a dry run of this for better understanding.
"""
"""
TIME COMPLEXITY ANALYSIS :
-> We run through the array and the prefix array once each, making it 0(n)

SPACE COMPLEXITY :
-> 0(N) for storing the prefix array 
"""

from typing import List
from collections import defaultdict

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        mp = defaultdict(int)
        for i in intervals:
            mp[i[0]] += 1  # increment count at meeting start
            mp[i[1]] -= 1  # decrement count at meeting end

        prev = 0
        res = 0
        for time in sorted(mp.keys()):
            prev += mp[time]
            res = max(res, prev)

        return res

    
# java
"""
import java.util.*;

class Solution {
    public int minMeetingRooms(int[][] intervals) {
        TreeMap<Integer, Integer> map = new TreeMap<>();
        for (int[] interval : intervals) {
            map.put(interval[0], map.getOrDefault(interval[0], 0) + 1);  // increment at start
            map.put(interval[1], map.getOrDefault(interval[1], 0) - 1);  // decrement at end
        }

        int prev = 0, res = 0;
        for (int count : map.values()) {
            prev += count;
            res = Math.max(res, prev);
        }

        return res;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        map<int, int> mp;
        for (auto& interval : intervals) {
            mp[interval[0]]++;  // increment at meeting start
            mp[interval[1]]--;  // decrement at meeting end
        }

        int prev = 0, res = 0;
        for (auto& [time, count] : mp) {
            prev += count;
            res = max(res, prev);
        }

        return res;
    }
};
"""
# Related Q:
# 1) Minimum Platforms
