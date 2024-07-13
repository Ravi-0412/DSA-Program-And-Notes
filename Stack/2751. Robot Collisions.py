# Just extended version of: "735. Asteroid Collision".

# lOgic: for checking whether they will collide or not, we need to sort according to position.
# Note: Now position has no meaning because in case of "R(+), L(-1)" they will collide for sure i.e
# just same as "735. Asteroid Collision".

# so 1) sort according to position 
# 2) then reduce convert this question to ""735. Asteroid Collision" by adding '-' to health of robots going left
# and apply same logic.

# Difference from q: "735. Asteroid Collision"
# Note: i) Also we need to return answer in given initial order so we need to keep track of 'index' also.
# ii) also we need to decrase energy of stronger robot in collision.

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        position_health = []
        for i in range(n):
            if directions[i] == "L":
                position_health.append([positions[i] , -1* healths[i], i])   # adding index also to return ans at last in given order
            else:
                position_health.append([positions[i] , healths[i], i])

        position_health.sort()
        sorted_health = [[position_health[i][2], position_health[i][1]] for i in range(n)]
        stack = []
        for i in range(n):
            ind , num = sorted_health[i][0], sorted_health[i][1]
            if num > 0:
                stack.append([ind, num])
            else:
                # keep on poping as the curr one will cancel the stack top.
                while stack and stack[-1][1] > 0 and stack[-1][1] < abs(num):
                    stack.pop()
                    num += 1  # because health of stronger robot decreases by '1' when they collide with weaker robot
                              # for decrement adding '+1' because 'num is negative'

                # stack top is of same sign i.e -ve only, so append in stack
                if not stack or stack[-1][1] < 0:  
                    stack.append([ind, num])
                # if magnitude of both equal then both will get cancelled, so pop from stack.
                elif stack[-1][1]== abs(num):
                    stack.pop()
                elif stack[-1][1] >  abs(num):
                    # here we need to decrease th health of stack top by '1'
                    # because health of stronger robot decreases by '1'.
                    stack[-1][1] -= 1
    
        stack.sort()  # sort according to index to return ans in given order
        ans = []
        for ind, health in stack:
            ans.append(abs(health))
        return ans