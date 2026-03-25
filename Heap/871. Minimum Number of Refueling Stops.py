# Method 1: 

"""
just similar to Q: 1642. Furthest Building You Can Reach 
First acuumulate all and use station with maximum fuel one by one.

Note: 'Stations' is already sorted according to 'position'.
from constraint: 1 <= positioni < positioni+1 < target => We can say this.

Note: Agar position ke anusar sorted nhi hota tb phle sort karte then ye logic lagate.

Logic: From all station that we can reach using current fuel, we will have to take station having maximum fuel.
so use maxHeap.
Time: O(n*logn)
"""

# My logic & mistake

"""
Why wrong?
-> Not using leftover fuel after stations are done.

Correct Thought Process & Logic (The "Refining" Strategy);
The strategy is: Drive until you run out of fuel. When you can't reach the next milestone (either the next station or the final target), 
look back at all the stations you passed and pick the one with the most fuel.

1. Current Reach: Keep track of the furthest position you can reach with your current fuel (reached).
2. The "Virtual" Stop: You don't stop at every station. You pass them and put their fuel amounts into a Max-Heap.
3. The Crisis: If the next station is further than your reached distance, or if you've run out of stations but haven't hit the target, 
you start popping from the Max-Heap (the "best" stations you passed) and adding that fuel to your reached.
4. The Termination: Repeat until reached >= target. If the heap is empty and you still haven't reached your next goal, it's impossible.

Summary :
The Heap Status: Represents "Fuel I could have taken but didn't."
The "Used" One: We always pop the Largest value from the heap because it gives us the most distance for exactly 1 stop.
The Stall Point: We only refuel when current_reach is less than the next required distance (either the next station's position or the final target).
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

# Other way: Better one

import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        # max_heap to store fuel amounts of stations we have passed
        max_fuel_heap = []
        
        # Current distance we can reach
        current_reach = startFuel
        stops_count = 0
        station_idx = 0
        n = len(stations)
        
        # We continue as long as we haven't reached the target
        while current_reach < target:
            # 1. Add all stations we can currently reach into the heap
            while station_idx < n and stations[station_idx][0] <= current_reach:
                # Store as negative for Max-Heap behavior in Python
                heapq.heappush(max_fuel_heap, -stations[station_idx][1])
                station_idx += 1
            
            # 2. If we haven't reached the target and have no fuel options left
            if not max_fuel_heap:
                return -1
            
            # 3. "Refuel" at the best station we've passed (Greedy choice)
            current_reach += -heapq.heappop(max_fuel_heap)
            stops_count += 1
            
        return stops_count


# Java Code 
"""
// My logic & mistake
import java.util.*;

class Solution {
    public int minRefuelStops(int target, int startFuel, int[][] stations) {
        if (startFuel >= target) {
            return 0;
        }

        int n = stations.length;
        int reached = startFuel;
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        int ans = 0;
        int i = 0;

        while (i < n) {
            while (i < n && stations[i][0] <= reached) {
                maxHeap.offer(stations[i][1]); 
                i++;
            }

            if (maxHeap.isEmpty()) {
                return -1;
            }

            int fuel = maxHeap.poll();
            reached += fuel;
            ans++;

            if (reached >= target) {
                return ans;
            }
        }

        System.out.println(ans + " ans");
        return -1;
    }
}

// Corrected code using above approach
// Logic: manually handle leftover fuel after stations are done
import java.util.*;

class Solution {
    public int minRefuelStops(int target, int startFuel, int[][] stations) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        int reached = startFuel;
        int ans = 0;
        int i = 0;
        int n = stations.length;

        while (i < n || !maxHeap.isEmpty()) {
            // Add all reachable stations to the heap
            while (i < n && stations[i][0] <= reached) {
                maxHeap.offer(stations[i][1]);
                i++;
            }

            // If we've reached the target, return the number of stops
            if (reached >= target) {
                return ans;
            }

            // If no fuel is available and we can't go further
            if (maxHeap.isEmpty()) {
                return -1;
            }

            // Refuel with the station offering the most fuel so far
            reached += maxHeap.poll();
            ans++;
        }

        // Final check in case the loop ends after refueling past target
        return reached >= target ? ans : -1;
    }
}
"""

# C++ Code 
"""
// My logic & mistake
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>>& stations) {
        if (startFuel >= target) {
            return 0;
        }

        int n = stations.size();
        int reached = startFuel;
        priority_queue<int> maxHeap;
        int ans = 0;
        int i = 0;

        while (i < n) {
            while (i < n && stations[i][0] <= reached) {
                maxHeap.push(stations[i][1]); 
                i++;
            }

            if (maxHeap.empty()) {
                return -1;
            }

            int fuel = maxHeap.top(); maxHeap.pop();
            reached += fuel;
            ans++;

            if (reached >= target) {
                return ans;
            }
        }

        cout << ans << " ans" << endl;
        return -1;
    }
};

// Corrected code using above approach
// Logic: manually handle leftover fuel after stations are done
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>>& stations) {
        priority_queue<int> maxHeap;
        int reached = startFuel;
        int ans = 0;
        int i = 0;
        int n = stations.size();

        while (i < n || !maxHeap.empty()) {
            // Add all reachable stations to the heap
            while (i < n && stations[i][0] <= reached) {
                maxHeap.push(stations[i][1]);
                i++;
            }

            // If we've reached the target, return the number of stops
            if (reached >= target) {
                return ans;
            }

            // If no fuel is available and we can't go further
            if (maxHeap.empty()) {
                return -1;
            }

            // Refuel with the station offering the most fuel so far
            reached += maxHeap.top(); maxHeap.pop();
            ans++;
        }

        // Final check in case the loop ends after refueling past target
        return reached >= target ? ans : -1;
    }
};
"""


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

# Java Code 
"""
import java.util.*;

class Solution {
    public int minRefuelStops(int target, int startFuel, int[][] stations) {
        if (startFuel >= target) {
            return 0;
        }

        int n = stations.length;
        int reached = startFuel;  // we can reach till here
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        int ans = 0;
        int i = 0;

        while (reached < target) {
            // add fuel of all stations till where we can reach
            while (i < n && stations[i][0] <= reached) {
                maxHeap.offer(stations[i][1]);
                i++;
            }

            if (maxHeap.isEmpty()) {
                // means we can't take help of any other station in reaching target
                return -1;
            }

            // get the station having maximum fuel
            int fuel = maxHeap.poll();
            // we can go additional distance of 'fuel' after reaching this station
            reached += fuel;
            ans++;
        }

        return ans;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>>& stations) {
        if (startFuel >= target) {
            return 0;
        }

        int n = stations.size();
        int reached = startFuel;  // we can reach till here
        priority_queue<int> maxHeap;
        int ans = 0;
        int i = 0;

        while (reached < target) {
            // add fuel of all stations till where we can reach
            while (i < n && stations[i][0] <= reached) {
                maxHeap.push(stations[i][1]);
                i++;
            }

            if (maxHeap.empty()) {
                // means we can't take help of any other station in reaching target
                return -1;
            }

            // get the station having maximum fuel
            int fuel = maxHeap.top(); maxHeap.pop();
            // we can go additional distance of 'fuel' after reaching this station
            reached += fuel;
            ans++;
        }

        return ans;
    }
};
"""
