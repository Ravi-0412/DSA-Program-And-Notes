# Method 1: 

"""
Note: 'Stations' is already sorted according to 'position'.
from constraint: 1 <= positioni < positioni+1 < target => We can say this.

Note: Agar position ke anusar sorted nhi hota tb phle sort karte then ye logic lagate.

Logic: From all station that we can reach using current fuel, we will have to take station having maximum fuel.
so use maxHeap.
Time: O(n*logn)
"""

# My logic & mistake

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        n = len(stations)
        reached = startFuel
        maxHeap = []
        ans = 0
        i = 0
        while i < n:
            while i < n and stations[i][0] <= reached:
                heapq.heappush(maxHeap, -1*stations[i][1])
                i += 1
            if not maxHeap:
                return -1
            fuel = heapq.heappop(maxHeap)
            reached += -1*fuel
            ans += 1
            if reached >= target:
                return ans
        print(ans,"ans")
        return -1

# Corrected code using above approach
# Logic: manually handle leftover fuel after stations are done

import heapq
from typing import List

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        maxHeap = []
        reached = startFuel
        ans = 0
        i = 0
        n = len(stations)
        
        while i < n or maxHeap:
            # Add all reachable stations to the heap
            while i < n and stations[i][0] <= reached:
                heapq.heappush(maxHeap, -stations[i][1])
                i += 1
            
            # If we've reached the target, return the number of stops
            if reached >= target:
                return ans
            
            # If no fuel is available and we can't go further
            if not maxHeap:
                return -1
            
            # Refuel with the station offering the most fuel so far
            fuel = -heapq.heappop(maxHeap)
            reached += fuel
            ans += 1
        
        # Final check in case the loop ends after refueling past target
        return ans if reached >= target else -1


# Method 2: 

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        n = len(stations)
        reached = startFuel   # we can reach till here
        maxHeap = []
        ans = 0
        i = 0
        while reached < target:
            # add fuel of all station till where we can reach
            while i < n and stations[i][0] <= reached:
                heapq.heappush(maxHeap, -1*stations[i][1])
                i += 1
            if not maxHeap:
                # means we can't take help of any other station in reaching target
                return -1
            # get the station having maximum fuel
            fuel = heapq.heappop(maxHeap) 
            # we can go additional distance of 'fuel' after reaching this station
            reached += -1*fuel
            ans += 1
        return ans

