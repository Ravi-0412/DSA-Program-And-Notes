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
    

# Note: try to do the problem "1353. Maximum Number of Events That Can Be Attended" and compare both the Q.