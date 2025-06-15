# observe: For the input 5, we can reach with only 7 steps: AARARAA. Because we can step back.


# My mistake
# since it may not reach the base case(target) only accelerating 'A' so it will keep on calling same function and
# will give Memory Limit exceeded.
# How to solve this?
# Somehow we have to mix the conditions so that it can reach the base case.

# And for mixing the conditions, we have two choice:
# 1) call the function based on some conditions so paths we take get mixed , OR
# 2) use bfs. Also asking for shortest no of sequence so it will work.
# In bfs all choices get mixed automatically when we add element in 'queue' considering all choices.

# Note: This is difference between bfs and dfs(DP). 
# Use above observation to see what should we use.

# Note vvi: When subproblems are repeating then try to do by DP only because through bfs you will get mostly TLE.
# Because bfs is just brute force only since we are considering all choices at each step.
# sometime your solution may get accepted using bfs like this and few more Q. 

# Time:  O(2^n). Each step we have two choice
class Solution:
    def racecar(self, target: int) -> int:

        def solve(position, speed):
            if position == target:
                return 0
            return min(1 + solve(position + speed, speed *2), 1 + solve(position, -1), 1 + solve(position, 1))
        return solve(0, 1)

# Trying to mix the condition using bfs
# Still getting Tle for some input.
# Time = O(2^n). Each step we have two choice
class Solution:
    def racecar(self, target: int) -> int: 
        #1. Initialize double ended queue as 0 moves, 0 position, +1 velocity
        queue = collections.deque([(0, 0, 1)])  # moves, position, velocity. we need to keep tarck of these three things
        while queue:
            # print(queue)
            moves, pos, vel = queue.popleft()
            if pos == target:
                return moves
            # Choice 1: 'A'
            queue.append((moves + 1, pos + vel, 2 * vel))
            # choice 2: 'R'
            if vel > 0:
                queue.append((moves + 1, pos, -1))
            else:
                queue.append((moves + 1, pos, 1))


# Optimisation
# In above solution , we are calling blindly i.e at every state we are taking all possible choices
# So if we can visualise the case and a/c that case if we take the choice then somewhat it will get optimised.

# Observation:
# We don't need to take 'R' everytime .
# Only consider changing the direction of the car if one of the following conditions is true:
#   i).  The car is crossing beyone target(higher coordinate than target) and speed is > 0
#        in this case we will make speed = -1 so that it comes close to target.
#   ii). The car is going far from target (lower coordinate than target) and speed < 0. 
# In this case we will make speed = 1 so that it comes close to target

# NOTE:  we have to accelerate 'A' everytime since we want to reach target in less time.

class Solution:
    def racecar(self, target: int) -> int:
        queue = collections.deque([(0, 0, 1)])  # moves, position, velocity. we need to keep tarck of these three things
        while queue:
            moves, pos, vel = queue.popleft()
            if pos == target:
                return moves
            # Case 1: "A"
            queue.append((moves + 1, pos + vel, 2 * vel))
            # case 2 : "R" based on conditions. Optimisation
            if (pos + vel > target and vel > 0) or (pos + vel < target and vel < 0):   
                queue.append((moves + 1, pos, -vel / abs(vel)))


# Later try by dp also.