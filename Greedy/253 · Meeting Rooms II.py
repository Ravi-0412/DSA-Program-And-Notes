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
Will give less answer than expected.

e.g: [[1, 10], [2, 5], [6, 15], [7, 12]] 
will give ans= 2 , but correct answer = 3

Flaws : only checks if any previous meeting has ended. It doesn't check if that "ended" meeting's room has already been taken by someone else.

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
The Logic: The "Earliest Free Room" Strategy
1. Chronological Sorting: We sort meetings by their start time. This ensures we process the "request" for a room in the order they occur.
2. Tracking Availability: We use a Min-Heap to store the end times of meetings currently taking place.
  The min_heap[0] (the root) always tells us the time the very first room will become vacant.
3. The Decision Point: For every new meeting, we ask: "Is there a room free right now?"
  Yes (min_heap[0] <= current_start): We don't need a new room. We "reuse" the room by removing the old end time and adding the new meeting's end time.
  No: All rooms are occupied. We "add" a room by pushing the current meeting's end time into the heap.
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
        # If there are no meetings, we need 0 rooms.
        if not intervals:
            return 0
        # Step 1: Sort the intervals by start time.
        # This allows us to handle meetings in the order they begin.
        intervals.sort(key=lambda x: x[0])
        # Step 2: Initialize a min-heap to keep track of end times.
        # Each element in the heap represents a room currently in use.
        # The root of the heap (min_heap[0]) is the earliest a room becomes free.
        min_heap = []
        for start, end in intervals:
            # Step 3: Check if a room has become available.
            # If the earliest end time in the heap is <= the current meeting's start time,
            # it means the room is now free and can be reused.
            if min_heap and min_heap[0] <= start:
                # We "vacate" the room by popping the old end time.
                heapq.heappop(min_heap)
            # Step 4: Occupy a room.
            # We push the current meeting's end time into the heap.
            # If we reused a room, the size stays the same. If not, it increases.
            heapq.heappush(min_heap, end)
         
        # The size of the heap at the end is the maximum number of 
        # concurrent meetings, which equals the minimum rooms needed.
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

count : the number of "Currently Occupied Rooms."

Note: Another way of asking this Q :"Find the maximum no of overlapping intervals at once"

Short :
1. Extract all events: Every interval is just a "Start" event and an "End" event.
2. Sort them: Put all start times in one list and all end times in another.
3. Walk through time: - If a meeting Starts, you must occupy a room.
  If a meeting Ends, a room becomes free.
  The answer is the maximum number of rooms occupied at any single point in time.

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
                # Q) why not incrementing 's' here ?
                # Ans : Will use the this vacated room in the next iteration.
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
Using Sweep Line Algorithm 

Logic:
Think of a meeting room building like an elevator:
1. When a meeting starts, one person (or group) enters the elevator. (+1)
2. When a meeting ends, they exit the elevator. (-1)
3. The maximum number of people in the elevator at any single moment is the minimum number of rooms you need.
"""
"""
TIME COMPLEXITY ANALYSIS :
-> O(N*logN)

SPACE COMPLEXITY :
-> 0(N) for storing the prefix array 
"""

from typing import List
from collections import defaultdict

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Step 1: Create an event map to record changes at specific times
        # Key: Time, Value: Net change in room demand
        time_diffs = defaultdict(int)
        
        for start, end in intervals:
            time_diffs[start] += 1  # A room is requested
            time_diffs[end] -= 1    # A room is vacated
            
        current_rooms = 0
        max_rooms = 0
        
        # Step 2: "Sweep" through the timeline chronologically
        # Sorting the keys is crucial so we process events in order
        for time in sorted(time_diffs.keys()):
            # Update the ongoing count of rooms currently in use
            current_rooms += time_diffs[time]
            
            # The global maximum of current_rooms tells us the 
            # peak demand at any point in time.
            max_rooms = max(max_rooms, current_rooms)
            
        return max_rooms

# follow ups
"""
Q) This logic is perfect for finding the Peak, but what if you need to know the Total Duration that at least one room was occupied?
"""

from collections import defaultdict

class Solution:
    def totalOccupiedDuration(self, intervals: List[List[int]]) -> int:
        time_diffs = defaultdict(int)
        for start, end in intervals:
            time_diffs[start] += 1
            time_diffs[end] -= 1
        
        sorted_times = sorted(time_diffs.keys())
        total_duration = 0
        current_active_meetings = 0     # minimum number of rooms required
        period_start = 0
        
        for i in range(len(sorted_times)):
            time = sorted_times[i]
            
            # Before updating the count, check if we were in an active period
            if current_active_meetings > 0:
                # Add the distance between the previous timestamp and current
                total_duration += (time - sorted_times[i-1])
            
            # Update current room occupancy
            current_active_meetings += time_diffs[time]
            
        return total_duration

# Conversions

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
