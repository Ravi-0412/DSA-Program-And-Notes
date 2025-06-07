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
        Arrays.sort(meetings, Comparator.comparingInt(a -> a[0])); // Sort meetings by start time

        PriorityQueue<Integer> availableRooms = new PriorityQueue<>(); // Min heap for available room numbers
        PriorityQueue<long[]> occupiedRooms = new PriorityQueue<>(Comparator.comparingLong(a -> a[0])); // Min heap for [end_time, room_index]
        int[] meetingCount = new int[n]; // Stores the number of meetings scheduled in each room

        for (int i = 0; i < n; i++) {
            availableRooms.add(i); // Initially all rooms are available
        }

        for (int[] meeting : meetings) {
            long start = meeting[0], end = meeting[1];

            // Free up rooms that have finished their meetings
            while (!occupiedRooms.isEmpty() && occupiedRooms.peek()[0] <= start) {
                availableRooms.add((int) occupiedRooms.poll()[1]);
            }

            // Assign meeting to an available room if possible
            if (!availableRooms.isEmpty()) {
                int room = availableRooms.poll();
                meetingCount[room]++;
                occupiedRooms.add(new long[]{end, room});
            } else {
                // Assign meeting to the room that will become available first
                long[] earliestRoom = occupiedRooms.poll();
                int room = (int) earliestRoom[1];
                meetingCount[room]++;
                occupiedRooms.add(new long[]{earliestRoom[0] + (end - start), room});
            }
        }

        // Find the room with the maximum number of meetings
        int maxMeetingRoom = 0;
        for (int i = 1; i < n; i++) {
            if (meetingCount[i] > meetingCount[maxMeetingRoom]) {
                maxMeetingRoom = i;
            }
        }

        return maxMeetingRoom;
    }
}
"""

# C++ Code 
"""
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    int mostBooked(int n, vector<vector<int>>& meetings) {
        sort(meetings.begin(), meetings.end());  // Sort meetings by start time

        priority_queue<int, vector<int>, greater<int>> available_rooms;  // Min heap for available room numbers
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> occupied_rooms;  // Min heap for [end_time, room_index]
        vector<int> meetingCount(n, 0);  // Stores the number of meetings scheduled in each room

        for (int i = 0; i < n; i++) {
            available_rooms.push(i);  // Initially all rooms are available
        }

        for (auto& meeting : meetings) {
            long long start = meeting[0], end = meeting[1];

            // Free up rooms that have finished their meetings
            while (!occupied_rooms.empty() && occupied_rooms.top().first <= start) {
                available_rooms.push(occupied_rooms.top().second);
                occupied_rooms.pop();
            }

            // Assign meeting to an available room if possible
            if (!available_rooms.empty()) {
                int room = available_rooms.top();
                available_rooms.pop();
                meetingCount[room]++;
                occupied_rooms.push({end, room});
            } else {
                // Assign meeting to the room that will become available first
                auto [curEnd, room] = occupied_rooms.top();
                occupied_rooms.pop();
                meetingCount[room]++;
                occupied_rooms.push({curEnd + (end - start), room});
            }
        }

        return distance(meetingCount.begin(), max_element(meetingCount.begin(), meetingCount.end()));
    }
};
"""

# Note: try to do the problem "1353. Maximum Number of Events That Can Be Attended" and compare both the Q.