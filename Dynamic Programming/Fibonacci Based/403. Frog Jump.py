# logic: from cur stone move to next stone we can reach by taking the possible jump.

# note: we can reach the same stone by taking the same number of jump many times.
# That's why it will give TLE by Recursion.

"""
The goal is to determine whether the frog can reach the last stone.
Use map/set to represent a mapping from the stone.
Notice that no need to calculate the last stone.
On each step, we look if any other stone can be reached from it, 
if so, we update that stone's steps by adding step, step + 1, step - 1. 
If we can reach the final stone, we return true
"""


# method 1: Recursive
class Solution(object):
    def canCross(self, stones):
        self.target = stones[-1]
        stoneSet = set(stones)

        # will tell the cur stone where we are, and last jump we took.
        def solve(stone, jump):
            if stone== self.target:
                return True
            for j in (jump-1, jump, jump +1):
                # we can only go forward and the stone to whcih we will go must be in our stoneSet.
                if j >0 and (stone + j) in stoneSet:  
                    if solve(stone + j, j):
                        return True
            return False

        return solve(0, 0)

# method 2: 
# memoising 
# logic: store the (stone, jump) in set so that we can skip when we will reach that stone with same jump again.

class Solution(object):
    def canCross(self, stones):
        self.target = stones[-1]
        stoneSet = set(stones)
        stoneToLastJump= set()

        # will tell the cur stone where we are, and last jump we took.
        def solve(stone, jump):
            if stone== self.target:
                return True
            # simply skip 
            if (stone, jump) in stoneToLastJump:
                return 
            for j in (jump-1, jump, jump +1): 
                # first move should be of '1' will be automatically handled by 'j > 0'.
                if j >0 and (stone + j) in stoneSet:
                    if solve(stone + j, j):
                        return True
            stoneToLastJump.add((stone, jump))
            return False

        return solve(0, 0)

# Method 3: 
#Tabulation
#time: O(n^2), space : O(n^2)
class Solution(object):
    def canCross(self, stones):
        self.target = stones[-1]
        stoneSet = set(stones)

        # key = current stone, value = set of all jump sizes we can use to reach that stone
        dp = {stone: set() for stone in stones}
        dp[0].add(0)  # start at stone 0 with jump 0

        for stone in stones:
            for jump in dp[stone]:
                for j in (jump - 1, jump, jump + 1):
                    if j > 0 and (stone + j) in stoneSet:
                        dp[stone + j].add(j)
                        if (stone + j) == self.target:
                            return True  # early exit if target is reached

        return False
   


# method 4: 
# itertaive
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # first jump must be of one unit only.
        if stones[1] - stones[0] > 1:
            return False
        stonesSet= set(stones)
        visited= set()  # to avoid repition when we will reach anh stone with same jump.
        stack= [(0, 0)]  # [(stone, lastJump)]
        visited.add((0, 0)) 
        while stack:
            stone, jump= stack.pop()
            # visited.add((stone, jump))
            # possible jumps we can take from this stone
            for j in (jump -1, jump, jump + 1):
                # stone(s) to which we will reach after taking the jump 'j'
                s= stone + j
                # can only go forward and s must be in set and (s, j) must not be in visited
                if j > 0 and s in stonesSet and (s, j) not in visited:
                    if s== stones[-1]:
                        return True
                    stack.append((s, j))
                    visited.add((s, j))
        return False
    