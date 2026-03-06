# method 1
"""
Convert the jewels string into a set. Then, iterate through stones once and check if each stone exists in that set.
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Step 1: Convert jewels to a set for O(1) lookups
        # Case sensitivity ('a' vs 'A') is handled automatically by sets
        jewel_set = set(jewels)
        
        count = 0
        
        # Step 2: Check each stone in our possession
        for stone in stones:
            # If the stone is in our 'good' set, increment count
            if stone in jewel_set:
                count += 1
                
        return count

# Follow ups
"""
1. What if the requirement changed so that 'a' and 'A' were considered the same type of jewel? 
How would you modify the preprocessing step?"

Ans: Just change jewels to upper/lower case and check in same way.

Q 2. Large Stream: "What if stones was a multi-terabyte log file (a stream) and jewels was a small list? How would you handle the memory?"

The Solution: 1.  Keep the Jewels in RAM: Since jewels is small, a set or a small bitmask fits easily in memory.
2.  Stream the Stones: Read the stones file line-by-line or in chunks (e.g., 4KB buffers).
3.  Process and Discard: Count the jewels in the current chunk, update a global counter, and then discard the chunk from memory.
"""
