# Problem: "Find the minimum no of rooms required to schdule all meeting without any conflict".

# it basically asking what is the 'maximum no of overlapping meetings at any given point of time'.
# Also this problem can be reduced to : 'Divide the intervals into minimum no of different parts 
# such that no two intervals in respective parts are overlapping. Find the no of parts.'.

# meeting in same part can be executed after completion of previous meeting without any overlap.
# so max no of room = no of parts

# Brute Force: O(n^2)
# just sort and check the current meeting start time with the end of all the meetings before.
# if none of previous meeting has ended, incr the count by '1' because we will have to arrange the current meeting in different conference room.'
# at last return the count

# method 2: O(n*logn)
# Logic: Jo room khali hoga koi interval ke bad uske hmko use karna h and apna sb interval ko run karbana h.
# Hmko bs sb meeting start kar dena h.
# Iske liye koi meeting end ho rha h ki nhi , cur meeting ke start se phle wo hmko track karna hoga
# for minimum ans we need the smallest ending time .
# from here we get intuition that we have to sort according to minimum ending time.

# Now we will try to schedule the meeting having minimum starting time first if any meeting ends
# from here we get intuition of soting base on starting time also.

# finally we have to sort based on starting and ending time separately.

# Note: Just focus on that "we have to start all the meetings".

# How to do?: Take two arrays say start and end that will store the start and end time of meetings respectively.
# now sort these arrays
# vvi: now take two pointer one each to start and end array respectively.
# run the loop till all meetings has started because after all meeting have started then no need to alloacate any different room.
# compare both the pointer value and if overlapping i.e start value is less than incr the count by '1' and incr the start pointer.
# else decr the count by '1' and incr the end pointer.
# after every comparison update the ans

# here count will tell the 'no of conferernce room at present' after each meeting.

# why we came through this? if start is less than end value then it means the ongoing meeting has not ended and we have to start the new meeting
# so incr the count by '1'.
# else: one of the meeting has ended so decr the count by '1'.

# Note: Another way of asking this Q :"Find the maximum no of overlapping intervals at once"

class Solution:
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        start= sorted([i.start for i in intervals])
        end=   sorted([i.end   for i in intervals])
        ans, count= 0, 0
        s, e= 0, 0  # pointer to start and end array
        while s < len(start):  # till we have started all the meetings
            # overlapping so we will need one new room.
            if start[s] < end[e]:
                count+= 1  # allocated new room for overlapping meeting 
                s+= 1   # started one so incr 's' by '1'.
                ans= max(ans, count)
            else:
                # one meeting ended. now the previous can be used for different meeting so decr total no of room required.
                count-= 1   
                e+= 1  # 
        return ans


# java
""""
import java.util.Arrays;

class Solution {
    public int minMeetingRooms(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return 0;
        }

        // Separate start and end times into two arrays
        int[] start = new int[intervals.length];
        int[] end = new int[intervals.length];
        
        for (int i = 0; i < intervals.length; i++) {
            start[i] = intervals[i][0];
            end[i] = intervals[i][1];
        }

        // Sort both arrays
        Arrays.sort(start);
        Arrays.sort(end);

        // Initialize pointers and counters
        int s = 0, e = 0;
        int count = 0, ans = 0;

        // Iterate over all the meetings
        while (s < intervals.length) {
            if (start[s] < end[e]) {
                // A new room is needed
                count++;
                s++;
                ans = Math.max(ans, count);
            } else {
                // A meeting has ended, so a room gets freed up
                count--;
                e++;
            }
        }

        return ans;
    }
}
"""

# Method 2: 
# using sweep line algorithm
# Logic: 
"""
Same as '2848. Points That Intersect With Cars' just we have to keep track of maximum count of rooms and return it.
When a meeting start we plot +1 for end we do -1.
Now we scan the line, and store the value in count , 
if count is 1 that mean 1 meeting start, if its 2 that means 2nd meeting started before 1st ended, so we need 2 room atleast. 
This count we save in ans if count > ans 
"""

# Time Complexity = O(n log n )
class Solution:
    def minMeetingRooms(self, intervals):
        line = {}
        for interval in intervals:
            line[interval.start] = line.get(interval.start, 0) + 1
            line[interval.end] = line.get(interval.end, 0) - 1
            
        ans = 0
        count = 0
        for time in sorted(line.keys()):
            count += line[time]
            ans = max(ans, count)
            
        return ans
    
# java
"""
import java.util.TreeMap;

class Solution {
    public int minMeetingRooms(int[][] intervals) {
        // Use a TreeMap to simulate the line sweep method
        TreeMap<Integer, Integer> map = new TreeMap<>();

        // Populate the map with start and end times
        for (int[] interval : intervals) {
            // Increment the count for start time
            map.put(interval[0], map.getOrDefault(interval[0], 0) + 1);
            // Decrement the count for end time
            map.put(interval[1], map.getOrDefault(interval[1], 0) - 1);
        }

        int ans = 0;
        int count = 0;

        // Iterate over the sorted keys (times)
        for (int time : map.keySet()) {
            count += map.get(time);  // Update the room count
            ans = Math.max(ans, count);  // Update the maximum rooms needed
        }

        return ans;
    }
}
"""

# Related Q:
# 1) Minimum Platforms