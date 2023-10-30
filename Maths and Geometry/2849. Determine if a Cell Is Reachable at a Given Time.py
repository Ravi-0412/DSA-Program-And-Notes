# Logic: From a given point we can reach any other point in minimum time if we go diagonally.
# For this you will have to go minimum = max distance between source and destination in either direction(say distance)
# because while going diagonally you can take maximum '1' step in each direction.

# Observation: So if t is >= distance then we can reach destination through any path in time >= 't'
# Because we can take any adjacent path.
# Note: we can take the same path again.

# One corner case:
# if source and destination both are same then,
# we can reach the destination same point if t != 1 because if t = 1 then you must be outside of destination.
# And t== 0(already at destination) or if  t > 1 then you can reach destination again through any path.

# Time : O(1)

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        # max distance between source and destination in either direction
        distance = max(abs(fx - sx), abs(fy - sy))  
        if distance == 0:
            return t != 1
        return t >= distance