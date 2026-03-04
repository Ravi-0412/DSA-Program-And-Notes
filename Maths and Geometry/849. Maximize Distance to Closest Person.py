# method 1:
"""
Focus on finding the largest block of zeros in the middle, at the start, and at the end.
ans = max(first_gap, last_gap, (max_mid_gap + 1) // 2)

Time = O(n), space : O(1)
"""

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        """
        Logic:
        1. Find the maximum consecutive zeros between two people (max_mid_gap).
        2. Find zeros at the very beginning (first_gap).
        3. Find zeros at the very end (last_gap).
        4. Result is max of (first_gap, last_gap, (max_mid_gap + 1) // 2).
        """
        max_mid_gap = 0
        current_gap = 0
        first_gap = -1
        last_gap = 0
        
        for s in seats:
            if s == 0:
                current_gap += 1
            else:
                # If this is the first '1' we've hit, the current_gap is the 'first_gap'
                if first_gap == -1:
                    first_gap = current_gap
                else:
                    # Otherwise, it's a middle gap
                    max_mid_gap = max(max_mid_gap, current_gap)
                # Reset for the next potential gap
                current_gap = 0
        
        # After the loop, the remaining current_gap is the 'last_gap'
        last_gap = current_gap
        
        # Calculate the distances
        # For middle gaps, distance is (gap + 1) // 2
        # For edge gaps, distance is the gap itself
        return max(first_gap, last_gap, (max_mid_gap + 1) // 2)

# Method 2:
"""
To solve it, we need to look at three different scenarios where Alex could sit to be as far away as possible from others.
"""
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        """
        Logic:
        1. Keep track of the 'last_person' index.
        2. When we find a person at index 'i':
           - If it's the first person found, the distance is just 'i' (Leading Gap).
           - Otherwise, the distance is (i - last_person) // 2 (Middle Gap).
        3. After the loop, check the distance from the last person to the end (Trailing Gap).
        """
        n = len(seats)
        last_person = -1
        max_dist = 0
        for i in range(n):
            if seats[i] == 1:
                if last_person == -1:
                    # Case 1: Leading zeros (distance from start to first person)
                    max_dist = i
                else:
                    # Case 2: Middle zeros (distance between two people)
                    # We sit in the middle, so distance is half the gap
                    max_dist = max(max_dist, (i - last_person) // 2)
                # Update the last person seen
                last_person = i
        # Case 3: Trailing zeros (distance from last person to the end)
        # The number of seats from last_person to index n-1 is n - 1 - last_person
        max_dist = max(max_dist, n - 1 - last_person)
        
        return max_dist
