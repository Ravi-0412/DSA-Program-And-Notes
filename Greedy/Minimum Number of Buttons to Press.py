"""
Q) You have a digital clock that shows the time using the AM and PM format. 
That clock also has 4 buttons which add to the time 1 minute, 5 minutes, 10 minutes respectively 15 minutes. 
You are given a future time. Get the least amount of presses to get the desired time. 

Similar to coin change : 322. Coin Change
But it can solved using greedy because buttons are multiple of each other not any random number.

Logic:
The most efficient way to reach a future time is to always use the largest "jump" possible that does not overshoot the target.
1. Calculate the Total Minutes Gap: Convert both the current time and the target time into "minutes since midnight" and find the difference. 
If the target time is "earlier" in the day, it means we have to wrap around to the next day.
2. Greedy Subtraction: Start with the largest button (15 mins). Use it as many times as possible until the remaining gap is smaller than 15. Then move to 10, then 5, then 1.

Step-by-Step Thought Process
1. Time Normalization: Since digital clocks reset every 12 or 24 hours, it's easiest to work with a 24-hour scale (0–1439 minutes).
        Example: 11:50 PM to 12:10 AM is a 20-minute gap.
2. Handle the Wrap-Around: If Target < Current, the gap is (1440−Current)+Target.
3. The Math: Number of Presses=(Gap//15)+(Remainder//10)+(Remainder//5)+(Remainder//1).

Time : O(1440) , in worst case
Space: O(1)

Note : For the buttons 1, 5, 10, 15, the Greedy approach is perfectly safe and much faster (O(1) vs O(Gap)).
the buttons are 1, 5, 10, and 15.
These are multiples of each other in a way that "taking the biggest first" never traps you into a bad path.
For any target, replacing two "10s" (20 mins) with a "15 and a 5" (20 mins) results in the same number of presses (2). 
Replacing three "5s" (15 mins) with one "15" (15 mins) reduces presses from 3 to 1.

If the interviewers change the buttons to "weird" numbers, you must pivot to Dynamic Programming.
(See below method similar to: 322. Coin Change)
"""

def min_button_presses(current_time, target_time):
    """
    Calculates the minimum button presses to reach target_time from current_time.
    Time format: "HH:MM AM/PM" (e.g., "11:50 PM")
    """
    
    def to_minutes(t_str):
        # Splitting "11:50 PM" into "11:50" and "PM"
        time_part, period = t_str.split()
        hours, minutes = map(int, time_part.split(':'))
        
        # Convert to 24-hour format
        if period == "PM" and hours != 12:
            hours += 12
        if period == "AM" and hours == 12:
            hours = 0
            
        return hours * 60 + minutes

    curr_min = to_minutes(current_time)
    target_min = to_minutes(target_time)
    
    # Calculate the total forward gap in minutes
    if target_min >= curr_min:
        gap = target_min - curr_min
    else:
        # If target is earlier, we must go to the next day (1440 mins in a day)
        gap = (1440 - curr_min) + target_min
        
    presses = 0
    # Greedy choices: 15, 10, 5, 1
    for button in [15, 10, 5, 1]:
        count = gap // button # How many times can we use this button?
        presses += count
        gap %= button         # Remaining gap to cover
        
    return presses

# --- Sample Cases ---
# 1. 10:00 AM to 10:32 AM (Gap: 32)
# 32 = (15 * 2) + (1 * 2) -> 4 presses
print(f"Presses: {min_button_presses('10:00 AM', '10:32 AM')}") 

# 2. 11:55 PM to 12:05 AM (Gap: 10)
# 10 = (10 * 1) -> 1 press
print(f"Presses: {min_button_presses('11:55 PM', '12:05 AM')}")


# Method 2:
"""
Using DP 
Will work even for random numbers.

1. State: dp[i] represents the minimum button presses required to reach exactly i minutes.
2. Transition: To get to i minutes, we look at where we could have come from. If we just pressed the 15-minute button, we came from i−15. So:
dp[i]=1+min(dp[i−1],dp[i−5],dp[i−10],dp[i−15])
3. Base Case: dp[0]=0. It takes zero presses to add zero minutes.

Just space optimised version of Question : 322. Coin Change
Time Complexity: O(Gap⋅B), where Gap is the number of minutes (max 1440) and B is the number of buttons. In the worst case, this is 1440×4, which is still very efficient.
Space Complexity: O(Gap) to store the dp array. 
"""

class ClockOptimizer:
    def get_min_presses(self, current_time: str, target_time: str, buttons: list[int]) -> int:
        """
        Uses Dynamic Programming to find the fewest button presses.
        """
        # 1. Convert times to minutes and find the gap
        curr_min = self._to_minutes(current_time)
        target_min = self._to_minutes(target_time)
        
        if target_min >= curr_min:
            gap = target_min - curr_min
        else:
            gap = (1440 - curr_min) + target_min
            
        # 2. Initialize DP table
        # We fill with gap + 1 because the max presses would be 'gap' (using only 1s)
        dp = [gap + 1] * (gap + 1)
        dp[0] = 0 
        
        # 3. Fill the DP table
        # For every minute from 1 to the gap...
        for i in range(1, gap + 1):
            # Try every button available
            for btn in buttons:
                if i >= btn:
                    # The best way to reach 'i' is 1 + the best way to reach 'i - btn'
                    dp[i] = min(dp[i], dp[i - btn] + 1)
                    
        return dp[gap]

    def _to_minutes(self, t_str: str) -> int:
        """Helper to convert 'HH:MM AM/PM' to minutes."""
        time_part, period = t_str.split()
        hours, minutes = map(int, time_part.split(':'))
        
        if period == "PM" and hours != 12:
            hours += 12
        if period == "AM" and hours == 12:
            hours = 0
            
        return hours * 60 + minutes

# --- Execution ---
buttons = [1, 5, 10, 15]
optimizer = ClockOptimizer()

# Example: 10:00 AM to 10:32 AM (Gap 32)
# Optimal: 15+15+1+1 (4 presses)
print(f"Min Presses: {optimizer.get_min_presses('10:00 AM', '10:32 AM', buttons)}")


# follow ups:
"""
Q) How to adapt this for a scenario where you also have a button that subtracts time?

Now, This is no longer just a "forward jump" problem; it’s now a Shortest Path problem on a circular graph.
If you have a button that subtracts time, you can sometimes reach a future time faster by "overshooting" and coming back.
Example: If the gap is 14 minutes and you have a -1 minute button.
Forward only: 10+1+1+1+1=5 presses.
With subtraction: 15−1=2 presses.

The Logic: BFS (Breadth-First Search)

While DP works for forward-only paths, BFS is the gold standard for finding the shortest path when you can move in 
multiple directions (forward and backward) and every "move" has the same cost (1 press).
1. Circular Boundary: The clock is a circle of 1440 minutes. If you are at minute 5 and subtract 10, you wrap around to 1435.
2. Queue: We use a queue to explore all possible times we can reach in 1 press, then 2 presses, etc.
3. Visited Set: We track which minutes we've already "visited" so we don't walk in circles forever.

Note : since every button press has an equal "weight" (cost of 1), a simple BFS is more efficient than Dijkstra.

Time : O(V+E) where V=1440.
"""

from collections import deque

class BidirectionalClock:
    def solve(self, start_time: str, end_time: str, buttons: list[int]):
        """
        Finds the min presses where buttons can be positive or negative.
        Example buttons: [1, 5, 10, 15, -1, -5]
        """
        start_min = self._to_minutes(start_time)
        target_min = self._to_minutes(end_time)
        
        if start_min == target_min:
            return 0

        # Queue stores (current_minute, number_of_presses)
        queue = deque([(start_min, 0)])
        visited = {start_min}

        while queue:
            curr, dist = queue.popleft()

            for btn in buttons:
                # Calculate new time with circular wrap-around (modulo 1440)
                nxt = (curr + btn) % 1440
                
                if nxt == target_min:
                    return dist + 1
                
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, dist + 1))
        
        return -1 # Should not happen if a '1' or '-1' button exists

    def _to_minutes(self, t_str: str) -> int:
        time_part, period = t_str.split()
        h, m = map(int, time_part.split(':'))
        if period == "PM" and h != 12: h += 12
        if period == "AM" and h == 12: h = 0
        return h * 60 + m

# --- Test Case ---
# Goal: Add 14 minutes. Buttons include -1 and 15.
# Path: 0 -> 15 (press 1) -> 14 (press 2)
calc = BidirectionalClock()
btns = [1, 5, 10, 15, -1, -5, -10, -15]
print(f"Min presses: {calc.solve('12:00 PM', '12:14 PM', btns)}") 
# Output: 2

# Follow ups 2:
"""
Q) How this changes if different buttons have different "costs" (e.g., the 15-minute button is harder to press)?

BFS is no longer sufficient. We must upgrade to Dijkstra’s Algorithm.
BFS assumes every "edge" has a weight of 1. Dijkstra’s is designed to find the shortest path when edges have different weights.

The Logic: Dijkstra on a Clock

Instead of a simple queue, we use a Priority Queue (Min-Heap). This ensures we always explore the "cheapest" path first, regardless of how many buttons we've actually pressed.
    Heap State: Store (cumulative_cost, current_minute).
    Distance Table: Keep a min_costs array where min_costs[time] is the lowest effort found so far to reach that specific minute.
    The Goal: Even if we find the target time early, we keep going until we've exhausted all cheaper possibilities.

Time Complexity: O(ElogV), where V=1440 (minutes) and E=V×number of buttons. This is roughly 1440×4×log(1440), which is extremely fast for a computer.
Space Complexity: O(V) to store the min_costs array and the priority queue.
"""

import heapq

class WeightedClockOptimizer:
    def solve(self, start_time, end_time, button_costs):
        """
        button_costs: Dictionary {minutes_added: effort_cost}
        Example: {15: 10, 10: 5, 1: 1, -1: 1}
        """
        start_min = self._to_minutes(start_time)
        target_min = self._to_minutes(end_time)
        
        # min_costs[minute] stores the minimum effort to reach that minute
        min_costs = [float('inf')] * 1440
        min_costs[start_min] = 0
        
        # Priority Queue: (cost, current_minute)
        pq = [(0, start_min)]
        
        while pq:
            curr_cost, curr_min = heapq.heappop(pq)
            
            # If we already found a cheaper way to this minute, skip it
            if curr_cost > min_costs[curr_min]:
                continue
                
            # If we reached the target, since it's a priority queue, 
            # this is guaranteed to be the minimum cost.
            if curr_min == target_min:
                return curr_cost
            
            for minutes, cost in button_costs.items():
                nxt_min = (curr_min + minutes) % 1440
                new_cost = curr_cost + cost
                
                # Relaxation step
                if new_cost < min_costs[nxt_min]:
                    min_costs[nxt_min] = new_cost
                    heapq.heappush(pq, (new_cost, nxt_min))
        
        return -1

    def _to_minutes(self, t_str):
        time_part, period = t_str.split()
        h, m = map(int, time_part.split(':'))
        if period == "PM" and h != 12: h += 12
        if period == "AM" and h == 12: h = 0
        return h * 60 + m

# --- Scenario ---
# Target: +14 minutes
# Button A: +15 mins (Cost: 10 effort)
# Button B: -1 min   (Cost: 1 effort)
# Button C: +1 min   (Cost: 2 effort)
# Path 1: 14 presses of '+1' = 28 effort
# Path 2: 1 press of '+15' + 1 press of '-1' = 11 effort (Winner!)

costs = {15: 10, 1: 2, -1: 1}
clock = WeightedClockOptimizer()
print(f"Min Effort: {clock.solve('12:00 PM', '12:14 PM', costs)}")
