# Logic: Hmko har event pe available rooms track karna hoga and available room track karne ke bad minimum room_index me hmko cur meeting to dalna hoga.
# Available rooms minimum occupied time ke anusar check karna hoga , isliye heap chahiye hoga. 
# And then minimum room_index select karne again avalilable_rooms ko minHeap banana hoga.

# Note: We have to execute all meetings in given room only.

# So we need two heaps.

# Note: Try to understand more properly in detail.

# Time:  O(nlogn)
# Space:  O(n)

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()  # sort the meeting acc to star time
        # to get the lowest room among all available rooms (MinHeap)
        available_rooms = [i for i in range(n)]  # initially all rooms will be available. 
        occupied_rooms = []   # [end_time, room_index] . minHeap to get the meeting with lowest ending time
        heapq.heapify(available_rooms)
        meetingCount = [0] * n   # will store the no of meeting scheduled in any room
        for start, end in meetings:
            # check all occupied room where we can execute this meeting
            # if ending time of occupied_time is <= start
            while occupied_rooms and occupied_rooms[0][0] <= start:
                _, room = heapq.heappop(occupied_rooms)
                # add this room no into available one to get the lowest possible available rooms
                heapq.heappush(available_rooms, room)
            
            # Execute the cur meeting into :
            # 1) if any room is available. FIrst will try to execute into available room
            if available_rooms:
                # execute this in lowest possible room number. 1st index will give that.
                room = heapq.heappop(available_rooms)
                meetingCount[room] += 1
                # Add this room to occupied room. This room will be occupied till 'end'
                heapq.heappush(occupied_rooms, [end, room])
            else:
                # execute this meeting to room which will get available first
                curEnd, room = heapq.heappop(occupied_rooms)
                meetingCount[room] += 1
                # Now the current room will get occupied till: curEnd + end - start
                newEnd = curEnd + end - start
                # Add the cur room into occupied one again
                # Poping 1st then again adding otherwise there will be duplicates entries for a room no
                heapq.heappush(occupied_rooms, [newEnd, room])

        return meetingCount.index(max(meetingCount))
    

# Note: try to do the problem "1353. Maximum Number of Events That Can Be Attended" and compare both the Q.


# My mistake:
# I was trying to do by one heap but not getting.

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        maxEndDay = max([end for start, end in meetings])
        count = [0] *n
        meetId = 0
        day = 0 
        occupiedTill = [0] *n
        minHeap = []
        for i in range(n):
            heapq.heappush(minHeap, [0, i])
        while meetId < len(meetings) and day <= maxEndDay:
            while minHeap and minHeap[0][0] > meetings[meetId][0]:
                heapq.heappop(minHeap)
            print(day, meetId, minHeap)
            if minHeap:
                # Means there is a day available to execute this cur event
                room = minHeap[0][1]
                start , end = meetings[meetId]
                meetingDuration = start + (end- start -1)
                endDay , id = heapq.heappop(minHeap)
                heapq.heappush(minHeap, [endDay + meetingDuration, id])
                count[room] += 1
                meetId += 1
                occupiedTill[room] = minHeap[0][0]
            # Put all day in heap if occupied time 
            for i in range(n):
                if occupiedTill[i] == day:
                    heapq.heappush(minHeap, [occupiedTill[i], i])

            day += 1
        print(count)
        maxCount= 0
        roomNo= 0
        for i , cnt in enumerate(count):
            if cnt > maxCount:
                maxCount = cnt
                roomNo = i
        return roomNo