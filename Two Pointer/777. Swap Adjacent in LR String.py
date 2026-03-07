# Method 1: 

"""
Think of 'X' as empty space and 'L'/'R' as people moving in a hallway.
  "XL" -> "LX": An 'L' can only move Left (if there is an 'X' to its left).
  "RX" -> "XR": An 'R' can only move Right (if there is an 'X' to its right).
  The Wall: 'L' and 'R' can never jump over each other.

Time = O(N)
sapce : O(N) => for the replace() strings.
"""

class Solution:
    def canTransform(self, start, result):
        # 1. Quick length check (given by constraints, but good practice)
        if len(start) != len(result): return False
        
        # 2. Final Relative Order Check
        # If we remove all 'X's, the strings must be identical.
        # there is no rule that allows an 'L' to swap with an 'R' so if we replace 'X' with empty string then both must be identical 
        # this should be first check then only we will check all the possibilities
        if start.replace('X', '') != result.replace('X', ''):
            return False
  
        n = len(start)
        i, j = 0, 0
        
        while i < n and j < n:
            # Move pointers to the next non-'X' character
            while i < n and start[i] == 'X': i += 1
            while j < n and result[j] == 'X': j += 1
            # If one pointer reaches the end, both must (checked by replace() above)
            if i == n or j == n:
                break
            # 3. Directional Constraint Check
            if start[i] == 'L' and i < j:
                # 'L' in start is at index i, needs to move to j. 
                # But L can only move LEFT (i -> j where i >= j).
                # Given : XL -> LX 
                return False
            if start[i] == 'R' and i > j:
                # 'R' in start is at index i, needs to move to j.
                # But R can only move RIGHT (i -> j where i <= j).
                # Given : RX -> XR
                return False
            # Move to next characters
            i += 1
            j += 1
            
        return True

# method 2
"""
Time : O(1)
In O(1), space complexity

Logic: If start[i] (the current character in the original string) is not the same as result[j] (the current character in the target string), return False.
This is the only addition case in method 1
"""

class Solution: 
    def canTransform(self, start, result):
        # Lengths must be equal to even begin the transformation
        if len(start) != len(result):
            return False
        
        n = len(start)
        i, j = 0, 0
        
        # We iterate until both pointers have scanned the entire length
        while i < n or j < n:
            
            # 1. Skip 'X' in start: 'X' is empty space and doesn't affect relative order
            while i < n and start[i] == 'X':
                i += 1
                
            # 2. Skip 'X' in result: We only care about the final position of L and R
            while j < n and result[j] == 'X':
                j += 1
                
            # 3. If both reach the end simultaneously, the transformation is successful
            if i == n and j == n:
                return True
                
            # 4. If one reaches the end but the other doesn't, there's a character count mismatch
            if i == n or j == n:
                return False
                
            # 5. Rule: 'L' and 'R' cannot jump over each other; their relative order must match
            if start[i] != result[j]:
                return False
                
            # 6. 'L' can only move LEFT: Its index in 'start' (i) must be >= its index in 'result' (j)
            if start[i] == 'L' and i < j:
                return False
                
            # 7. 'R' can only move RIGHT: Its index in 'start' (i) must be <= its index in 'result' (j)
            if start[i] == 'R' and i > j:
                return False
                
            # Move to the next characters to continue the scan
            i += 1
            j += 1
            
        return True
        
