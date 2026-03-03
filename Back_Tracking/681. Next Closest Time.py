"""
Extract Available Digits: First, identify all unique digits present in the input string (e.g., "19:34" gives us {1, 9, 3, 4}).
Simulation: Starting from the current time, add 1 minute at a time.Validation: 
For each new time (HH:MM):Check if every digit in the new HH:MM string exists in our "Available Digits" set.
If all digits are valid, that is our "Next Closest Time."Modulo Arithmetic: Since the clock wraps around (23:59 becomes 00:00), 
we use modulo $1440$ to keep the simulation within a single 24-hour cycle.

Time : O(1440) = O(24 * 60)

A) if all(d in allowed_digits for d in time_digits):
return f"{h:02d}:{m:02d}" ?


Part,Meaning
h,The variable name (the hour integer).
:,"The separator that tells Python ""Formatting rules are coming next."""
0,The padding character. Use 0 instead of a space.
2,The minimum width. Ensure the result is at least 2 characters long.
d,The type. Treat the variable as a decimal (integer).
"""

class Solution:
    def nextClosestTime(self, time: str) -> str:
        # Step 1: Parse the current time into total minutes from 00:00
        hour, minute = map(int, time.split(":"))
        curr_total_minutes = hour * 60 + minute
        
        # Step 2: Identify the set of allowed digits
        # We ignore the ':' character
        allowed_digits = {int(d) for d in time if d != ':'}
        
        # Step 3: Simulate forward minute-by-minute (max 1440 iterations)
        while True:
            # Move 1 minute forward, wrap around 24 hours using modulo 1440
            curr_total_minutes = (curr_total_minutes + 1) % 1440
            
            # Convert minutes back to HH:MM format
            h, m = divmod(curr_total_minutes, 60)
            
            # Format as strings with leading zeros (e.g., 01:09)
            # We check if every digit in "01", "09" is in our allowed set
            time_digits = [h // 10, h % 10, m // 10, m % 10]
            
            # If all 4 digits of the new time are in the allowed set, we found it!
            if all(d in allowed_digits for d in time_digits):
                return f"{h:02d}:{m:02d}"


# method 2: Backtracking
"""
Extract Unique Digits: Get all unique digits from the input (e.g., "19:34" -> {1, 9, 3, 4}).
Generate Combinations: Use recursion to build a 4-digit sequence [d1, d2, d3, d4].There are at most 4^4 = 256 combinations.
Validate on the Fly:Hours: 
    (d1 * 10 + d2) must be < 24.
    Minutes: (d3 * 10 + d4) must be < 60 .
Calculate Circular Distance:
  If the generated time $T$ is greater than the current time $C$, the distance is T - C.
  If the generated time $T$ is less than or equal to $C$, it means it's the next day. The distance is (1440 - C) + 
  T.Keep the Minimum: Track the time that gives the smallest positive distance.
"""

class Solution:
    def nextClosestTime(self, time: str) -> str:
        # Step 1: Parse input and get unique allowed digits
        hour_str, min_str = time.split(":")
        start_time = int(hour_str) * 60 + int(min_str)
        allowed = sorted(list({int(d) for d in time if d != ':'}))
        
        self.min_diff = float('inf')
        self.result = time # Default fallback
        
        def backtrack(current_digits):
            # Base Case: We have picked 4 digits
            if len(current_digits) == 4:
                h = current_digits[0] * 10 + current_digits[1]
                m = current_digits[2] * 10 + current_digits[3]
                
                # Check if it's a valid clock time
                if h < 24 and m < 60:
                    new_time = h * 60 + m
                    
                    # Calculate circular distance (minutes until this time occurs)
                    # If new_time is 10:00 and start is 09:00, diff is 60.
                    # If new_time is 08:00 and start is 09:00, diff is (1440-540) + 480 = 1380.
                    if new_time > start_time:
                        diff = new_time - start_time
                    else:
                        diff = 1440 - start_time + new_time
                    
                    # Update if this is the closest time we've seen (must be > 0)
                    if 0 < diff < self.min_diff:
                        self.min_diff = diff
                        self.result = f"{h:02d}:{m:02d}"
                return

            # Recursive Step: Try every allowed digit for the current position
            for digit in allowed:
                current_digits.append(digit)
                backtrack(current_digits)
                current_digits.pop() # Undo choice (backtrack)

        backtrack([])
        return self.result
