"""
Note: 'Stations' is already sorted according to 'position'.
from constraint: 1 <= positioni < positioni+1 < target => We can say this.

Note: Agar position ke anusar sorted nhi hota tb phle sort karte then ye logic lagate.

Logic: From all station that we can reach using current fuel, we will have to take station having maximum fuel.
so use maxHeap.
Time: O(n*logn)
"""

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


# Java Code 
"""
import java.util.PriorityQueue;

class Solution {
    public int minRefuelStops(int target, int startFuel, int[][] stations) {
        if (startFuel >= target) return 0;

        int n = stations.length, reached = startFuel, ans = 0, i = 0;
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a); // Max heap for fuel amounts

        while (reached < target) {
            // Add fuel from stations we can reach with current fuel
            while (i < n && stations[i][0] <= reached) {
                maxHeap.offer(stations[i][1]);
                i++;
            }

            // If no reachable station with fuel, return -1
            if (maxHeap.isEmpty()) return -1;

            // Refuel using the most fuel-efficient station
            reached += maxHeap.poll();
            ans++;
        }

        return ans;
    }
}
"""

# C++ Code 
"""
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>>& stations) {
        if (startFuel >= target) return 0;

        int n = stations.size(), reached = startFuel, ans = 0, i = 0;
        priority_queue<int> maxHeap;  // Max heap to store available fuel from stations

        while (reached < target) {
            // Add fuel from stations we can reach with current fuel
            while (i < n && stations[i][0] <= reached) {
                maxHeap.push(stations[i][1]);
                i++;
            }

            // If no reachable station with fuel, return -1
            if (maxHeap.empty()) return -1;

            // Refuel using the most fuel-efficient station
            reached += maxHeap.top();
            maxHeap.pop();
            ans++;
        }

        return ans;
    }
};
"""

# My logic:
"""
Just same logic as above only changed first while loop
but not working.

Reason:
outer loop terminates too early — it only runs while there are unprocessed stations.
But the car might still need to refuel after the last station to reach the target, and your loop doesn’t handle that case.

i.e 
The loop stops when i == n (all stations processed), regardless of whether you've reached the target.
But there might still be fuel in the heap (from previous stations), which you can use to continue.

How above one handling this?
i) Outer loop continues until the car reaches the target.
ii) This ensures you keep considering refuels even after all stations are processed, as long as reached < target.
iii) Even if i == n (no more stations), the car might still need to refuel from stored stations in the heap to reach the goal.

Note: if we want to write using same logic then , see the correct code below.
"""
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

# Java Code 
"""
import java.util.PriorityQueue;

class Solution {
    public int minRefuelStops(int target, int startFuel, int[][] stations) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a); // Max heap for fuel amounts
        int reached = startFuel, ans = 0, i = 0, n = stations.length;

        while (i < n || !maxHeap.isEmpty()) {
            // Add all reachable stations to the heap
            while (i < n && stations[i][0] <= reached) {
                maxHeap.offer(stations[i][1]);
                i++;
            }

            // If we reach the target, return the number of stops
            if (reached >= target) return ans;

            // If no available fuel and target isn't reached
            if (maxHeap.isEmpty()) return -1;

            // Refuel using the station offering the most fuel so far
            reached += maxHeap.poll();
            ans++;
        }

        // Final check in case loop ends after refueling past the target
        return (reached >= target) ? ans : -1;
    }
}
"""

# C++ Code 
"""
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>>& stations) {
        priority_queue<int> maxHeap;  // Max heap for fuel from reachable stations
        int reached = startFuel, ans = 0, i = 0, n = stations.size();

        while (i < n || !maxHeap.empty()) {
            // Add all reachable stations to the heap
            while (i < n && stations[i][0] <= reached) {
                maxHeap.push(stations[i][1]);
                i++;
            }

            // If we reach the target, return the number of stops
            if (reached >= target) return ans;

            // If no available fuel and target isn't reached
            if (maxHeap.empty()) return -1;

            // Refuel using the most fuel-efficient station available
            reached += maxHeap.top();
            maxHeap.pop();
            ans++;
        }

        // Final check in case loop ends after refueling past the target
        return (reached >= target) ? ans : -1;
    }
};
"""