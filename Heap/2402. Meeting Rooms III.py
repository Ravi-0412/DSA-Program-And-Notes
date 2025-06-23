# Method 1:

# what to do?
# for each room find the lowest available room.

# Logic: We have to get the minimum available room each time and we can use same room later also.
# (after completion of meeting of that room is lowest room no available).

# Whenever you have to perform same operation again and again on min/max , we use heap.
# so will use minHeap to get minimum available room currently.

# Also we need to keep track of rooms already occupied and which can be available for any meeting
# after finishing current meeting. Room where meeting will end sooner will have higher chance of being available.
# For this also we will need minHeap.

# So we need two minHeaps.


# Time:  O(nlogn)
# Space:  O(n)

import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()  # sort the meeting acc to star time
        # to get the lowest room among all available rooms (MinHeap)
        available_rooms = [i for i in range(n)]  # initially all rooms will be available. 
                        # minHeap to get the lowest possible room among all available room.
        occupied_rooms = []   # [end_time, room_index] . minHeap to get the meeting with lowest ending time.
        heapq.heapify(available_rooms)
        meetingCount = [0] * n   # will store the no of meeting scheduled in any room

        # For every meeting check all available rooms.
        for start, end in meetings:
            # check all occupied room where we can execute this meeting
            # if ending time of occupied_time is <= start. (= because of half interval i.e [start, end) )
            while occupied_rooms and occupied_rooms[0][0] <= start:
                # Remove that room and add this room no into available one to get the lowest possible available rooms.
                _, room = heapq.heappop(occupied_rooms)
                heapq.heappush(available_rooms, room)
            
            # Execute the cur meeting into :
            # 1) if any room is available. FIrst will try to execute into available room
            if available_rooms:
                # execute this in lowest possible room number.
                room = heapq.heappop(available_rooms)
                meetingCount[room] += 1
                # Add this room to occupied room. This room will be occupied till 'end'
                heapq.heappush(occupied_rooms, [end, room])
            else:
                # execute this meeting to room which will get available first
                curEnd, room = heapq.heappop(occupied_rooms)
                meetingCount[room] += 1
                # Now the current room will get occupied till: curEnd + total_meeting duration
                newEnd = curEnd + (end - start)
                # Add the cur room into occupied one again
                # Poping 1st then again adding otherwise there will be duplicates entries for a room no
                heapq.heappush(occupied_rooms, [newEnd, room])

        return meetingCount.index(max(meetingCount))

# Java Code 
"""
import java.util.*;

class Solution {
    public int mostBooked(int n, int[][] meetings) {
        Arrays.sort(meetings, Comparator.comparingInt(a -> a[0])); // sort the meeting acc to start time

        PriorityQueue<Integer> availableRooms = new PriorityQueue<>(); // to get the lowest room among all available rooms (MinHeap)
        for (int i = 0; i < n; i++) availableRooms.offer(i); // initially all rooms will be available

        PriorityQueue<long[]> occupiedRooms = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        // [end_time, room_index]. MinHeap to get the meeting with lowest ending time

        int[] meetingCount = new int[n]; // will store the no of meetings scheduled in any room

        // For every meeting check all available rooms
        for (int[] meeting : meetings) {
            int start = meeting[0], end = meeting[1];

            // check all occupied rooms where we can execute this meeting
            // if ending time of occupied_time is <= start. (= because of half interval i.e [start, end) )
            while (!occupiedRooms.isEmpty() && occupiedRooms.peek()[0] <= start) {
                long[] roomInfo = occupiedRooms.poll();
                availableRooms.offer((int) roomInfo[1]); // Remove that room and add this room no into available one
            }

            // Execute the current meeting into :
            // 1) if any room is available. First will try to execute into available room
            if (!availableRooms.isEmpty()) {
                int room = availableRooms.poll(); // execute this in lowest possible room number
                meetingCount[room]++;
                occupiedRooms.offer(new long[]{end, room}); // this room will be occupied till 'end'
            } else {
                long[] roomInfo = occupiedRooms.poll(); // room which will get available first
                long curEnd = roomInfo[0];
                int room = (int) roomInfo[1];
                meetingCount[room]++;
                long newEnd = curEnd + (end - start); // current room will be occupied till curEnd + meeting duration
                occupiedRooms.offer(new long[]{newEnd, room}); // add the room again into occupied one
            }
        }

        int maxMeetings = 0, resultRoom = 0;
        for (int i = 0; i < n; i++) {
            if (meetingCount[i] > maxMeetings) {
                maxMeetings = meetingCount[i];
                resultRoom = i;
            }
        }
        return resultRoom;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    int mostBooked(int n, vector<vector<int>>& meetings) {
        sort(meetings.begin(), meetings.end()); // sort the meeting acc to start time

        priority_queue<int, vector<int>, greater<>> availableRooms; // minHeap to get the lowest room
        for (int i = 0; i < n; ++i) availableRooms.push(i); // initially all rooms available

        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> occupiedRooms;
        // [end_time, room_index]. MinHeap to get the meeting with lowest ending time

        vector<int> meetingCount(n, 0); // no. of meetings in each room

        for (auto& meeting : meetings) {
            int start = meeting[0], end = meeting[1];

            // free up rooms whose end_time <= current meeting start time
            while (!occupiedRooms.empty() && occupiedRooms.top().first <= start) {
                int room = occupiedRooms.top().second;
                occupiedRooms.pop();
                availableRooms.push(room);
            }

            if (!availableRooms.empty()) {
                int room = availableRooms.top(); availableRooms.pop(); // lowest available room
                meetingCount[room]++;
                occupiedRooms.push({end, room});
            } else {
                auto [curEnd, room] = occupiedRooms.top(); occupiedRooms.pop();
                meetingCount[room]++;
                long long newEnd = curEnd + (end - start);
                occupiedRooms.push({newEnd, room});
            }
        }

        int maxCount = 0, resultRoom = 0;
        for (int i = 0; i < n; ++i) {
            if (meetingCount[i] > maxCount) {
                maxCount = meetingCount[i];
                resultRoom = i;
            }
        }

        return resultRoom;
    }
};
"""