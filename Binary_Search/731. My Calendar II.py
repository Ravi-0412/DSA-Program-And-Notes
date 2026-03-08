# Method 1: 
"""
Logic: 
Step 1: The Triple-Booking Check. We first compare the new event against self.overlaps. If the new event overlaps with anything in this list, 
it means there are already two events there. Adding a third would create a Triple Booking. We return False immediately.

Step 2: The Double-Booking Update. If we pass Step 1, the booking is allowed. We now compare the new event against every event in self.calendar. 
Any intersection found here is a new "Double Booking", so we add the intersection (max(start, i), min(end, j)) to self.overlaps.
Step 3: The Single-Booking Update. Finally, we add the full event to self.calendar

Q) Why we don't need to "Merge" when seeing double overlapping one?
we don't need to merge [1, 3] and [2, 4] into [1, 4]. If we merged them, we would lose the information about where the double booking occurred ([2, 3]). 
Keeping them separate allows us to pinpoint exactly which segments are "dangerous" for a third booking.

Time Complexity: O(N^2). For each new booking, we iterate through overlaps and calendar. Since both lists grow up to N, each book call is O(N), leading to O(N^2) for N calls.
Space Complexity: O(N). We store N events in calendar and potentially N intersections in overlaps.

"""

class MyCalendarTwo:
    def __init__(self):
        # Stores intervals where two events are already scheduled.
        self.double_booked = []
        
        # Stores all successfully booked individual events.
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        # 1. First, check if the new event hits a double-booked segment.
        # If it does, adding it would result in a triple booking.
        for db_start, db_end in self.double_booked:
            # Overlap exists if start < existing_end AND end > existing_start.
            if start < db_end and end > db_start:
                return False

        # 2. If it's not a triple booking, see if it creates new double-booked segments.
        for b_start, b_end in self.bookings:
            if start < b_end and end > b_start:
                # The intersection is where the two events overlap.
                # It starts at the later start and ends at the earlier end.
                overlap_start = max(start, b_start)
                overlap_end = min(end, b_end)
                self.double_booked.append((overlap_start, overlap_end))

        # 3. Add the new event to the list of individual bookings.
        self.bookings.append((start, end))
        return True

# Method 2:
"""
using : Sweep Line Algorithm + Binary Search 
Note: This method can easily be generalised for 'k' overlapping, just change the condition to: if active_bookings >= K:
Logic: 
Instead of thinking about the intervals as blocks (like [10, 20]), we think about events that happen at specific times.

e.g: 
Imagine you are standing at a doorway with a counter.
When someone enters (Start), you click your counter up (+1).
When someone leaves (End), you click your counter down (-1).

At any given moment, the number on your counter tells you exactly how many people are in the room. In this problem, 
if that counter ever hits 3, the room is too crowded, and we have to kick the last person out.

How we store ?
We store (time, type) where type is +1 for start, -1 for end is the "instruction" for our counter.
+1 (Start): This marks the beginning of a booking. It increases the "booking density" of the timeline.
-1 (End): This marks the end. It decreases the density.
Crucial Point: Because the interval is [start, end), the person leaves exactly at the end time. 
If one event ends at 20 and another starts at 20, the counter will go -1 then +1, staying safe.

Let's say we already have [10, 20] and [15, 25].
self.points = [(10, 1), (15, 1), (20, -1), (25, -1)]
Now we try to book [12, 22]:
Insort: [(10, 1), (12, 1), (15, 1), (20, -1), (22, -1), (25, -1)]
Sweep:
Time 10: +1 (Ongoing = 1)
Time 12: +1 (Ongoing = 2)
Time 15: +1 (Ongoing = 3) 🔥 BOOM!
Result: ongoing_bookings hit 3. We remove (12, 1) and (22, -1) and return False.

Note: Very easily scalable to "k"

Complexity of : insort(self.time_events, (start, 1))  => O(N)
Finding : O(logN), insertion : O(N)
Note: By default, bisect.insort is equivalent to bisect_right

Time Complexity: O(N^2)
Space Complexity: O(N).
"""

from bisect import insort

class MyCalendarTwo:
    def __init__(self):
        # We store 'time_events' as (timestamp, change_in_count)
        # +1 means a booking started, -1 means a booking ended
        self.time_events = []

    def book(self, start: int, end: int) -> bool:
        # 1. Trial: Add the start (+1) and end (-1) points into our sorted timeline (Binary Search + Insert))
        # Temporarily add the start and end points
        # Using insort keeps the points list sorted (Binary Search + Insert)
        
        insort(self.time_events, (start, 1))  # O(N) 
        insort(self.time_events, (end, -1))
        
        active_bookings = 0
        
        # 2. Sweep across the timeline from past to future
        for time, change in self.time_events:
            active_bookings += change
            
            # 3. If at any point we hit 3, we have a triple booking
            # use 'k' instead of '3' to make it generalised.
            if active_bookings >= 3:
                # Undo the trial addition to keep the calendar valid
                self.time_events.remove((start, 1))
                self.time_events.remove((end, -1))
                return False
                
        return True


# Follow ups: Do using Segment Tree later
"""
Scaling to 10^9 => Time Range (Segment Trees) 
Question: "What if the time range is very large, but we need O(log N) performance for every book call?"
The Approach: A Dynamic Segment Tree or a Sparse Segment Tree. Since we can't create an array of size 10^9, 
we create nodes only when we need them (on-the-fly).Each node stores the max_bookings in its range.
Focus: Memory management. They will ask how you'd prevent the tree from taking up too much RAM.
"""





