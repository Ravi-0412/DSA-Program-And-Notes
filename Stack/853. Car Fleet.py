# Logic: 
# If car at lower position can catch the fleet just ahead of it then
# it will join that fleet.
# Else will run as new fleet.

# So to know whether lower position car can catch or not
# We will traverse in descending order of position.

# why stack:
# We need to find the next fleet just ahead of it and compare the time.

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for pos, vel in sorted(zip(position, speed))[::-1]:
            t = (target - pos) / vel   # time taken by current car to reach target.
            if not stack :
                stack.append(t)
            elif t > stack[-1] :
                # time taken is more. So it won't be able to catch fleet runninh ahead of it. it will form new fleet
                stack.append(t)
            # elif t <= stack[-1]:
                # it will join the fleet infront of it
        return len(stack)
            


# Method 2:
# Optimising to O(1) space
    
# Just same logic as above.

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pre_t = None
        ans = 0
        for pos, vel in sorted(zip(position, speed))[::-1]:
            t = (target - pos) / vel
            if not pre_t or t > pre_t:
                ans += 1
                pre_t = t
            # else:
                    # will join the fleet ahead of it
        return ans
