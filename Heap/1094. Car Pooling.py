# Method 1:
"""
Similar to 2402. Meeting Rooms III

Note: Aisa samjho ki you are travelling in a bus with given capacity
Diff stops pe fix log utar rhe and onboard kar rhe.
from these we get two things:
1. Bus ko based on starting position se run karna h till last stop. 
-> For this sort based on starting time to traverse based on starting km.
2. Jo utar rhe unka space ko utilise karna hoga. wahi log utarenge jinka ending time kam hoga.
-> For this at each stop check if some people have reached their destination
-> We need to use minHeap based on (ending time, people boarding off), end time jiska kam hoga uska space use karna h.

Ekdum jaise bus me travel karte ho , wahi scenario h. Easy one.

Logic:
1. Sort the trips by their starting location. This ensures we process the pick-ups in the order the car encounters them.
2. Use a Min-Heap to keep track of passengers who need to be dropped off. The heap will store tuples: (drop_off_location, num_passengers).
3. For every new trip [num, start, end]:
  Check the Heap: Before picking up new people, check if anyone in the heap has a drop_off_location <= current_start.
  Drop Off: Pop them from the heap and add their seats back to the current_capacity.
  Pick Up: Add the new passengers. If current_capacity < 0, return False.
  Push to Heap: Add this trip's drop-off info (end, num) to the heap.

Time: O(N * logN)
Space : O(N) 
"""

import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 1. Sort trips by start location so we process them chronologically
        trips.sort(key=lambda x: x[1])
        
        # 2. Min-Heap to track (end_location, num_passengers)
        # We want to drop off people with the EARLIEST end_location first
        drop_off_heap = []
        current_capacity = capacity
        
        for num, start, end in trips:
            # 3. Before picking up new passengers, drop off everyone 
            # whose destination is at or before the current 'start'
            while drop_off_heap and drop_off_heap[0][0] <= start:
                _, released_passengers = heapq.heappop(drop_off_heap)
                current_capacity += released_passengers
            
            # 4. Try to pick up the new passengers
            current_capacity -= num
            # If capacity goes negative, we don't have enough seats
            if current_capacity < 0:
                return False
            # 5. Add this trip's drop-off milestone to the heap
            heapq.heappush(drop_off_heap, (end, num))
        return True

# Method 2 :
"""
The Difference Array (Bucket Sort)
Sweep Line Algorithm 

Thought Process:
Since the coordinates are small (0 to 1000), we can treat the road as an array of 1001 "buckets." Each bucket represents a kilometer marker.
  When passengers get in, the passenger count goes up at that specific kilometer.
  When passengers get out, the passenger count goes down at that specific kilometer.
  By calculating the prefix sum (running total) of this array, we get the exact number of passengers in the car at every point on the road.
  
Logic:
Create an array road of size 1001.
For each trip [num, start, end]:
  road[start] += num
  road[end] -= num
Iterate through road, adding the values to a current_occupancy variable.
If current_occupancy > capacity at any index, return False.

Time = Space = O(1)

Comparison of Approaches:

Feature                              Difference Array                         Min-Heap
Best Used                     When,Coordinates are small (0-1000)    Coordinates are large (109)
Time Complexit                      O(N+L) (L = road length)          O(NlogN) (sorting + heap ops)
Space Complexity                    O(L)                              O(N) (to store the heap)
Meeting Room Analogy            Like a reservation calendar            Like tracking active meetings
"""

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Step 1: Create a timeline of 1001 kilometers
        # The constraints say locations are 0 to 1000.
        timeline = [0] * 1001
        
        # Step 2: Record pick-ups and drop-offs
        for num, start, end in trips:
            timeline[start] += num  # Passengers get in
            timeline[end] -= num    # Passengers get out
            
        # Step 3: Check cumulative passengers at each kilometer
        current_passengers = 0
        for change in timeline:
            current_passengers += change
            if current_passengers > capacity:
                return False
                
        return True
