# observe: For the input 5, we can reach with only 7 steps: AARARAA. Because we can step back.

# in case of 'R' , we only need to modify based on conditions otherwise we will get memory limit exceeded.

class Solution:
    def racecar(self, target: int) -> int:
        
        #1. Initialize double ended queue as 0 moves, 0 position, +1 velocity
        queue = collections.deque([(0, 0, 1)])  # moves, position, velocity
        while queue:
            moves, pos, vel = queue.popleft()
            if pos == target:
                return moves
            
            #2. Always consider moving the car in the direction it is already going
            # Minimum number of sequence ke liye position ko to increase karna hi hoga hmesha isliye ye move har ek step pe lenge.
            queue.append((moves + 1, pos + vel, 2 * vel))
            
            #3. Only consider changing the direction of the car if one of the following conditions is true
            #   i.  The car is crossing beyone target(higher coordinate than target). 
            # will happen when speed > 0 . in this case we will make speed = -1 so that it comes close to target
            #   ii. The car is going far from target (lower coordinate than target). this will happen when speed < 0. 
            # In this case we will make speed = 1 so that it comes close to target

            if (pos + vel > target and vel > 0) or (pos + vel < target and vel < 0):   # this 'if' is optimisng our code otherwise will get TLE
                queue.append((moves + 1, pos, -vel / abs(vel)))


# Note: if we don't optimise the sequence of Reverse(R) in above we will get memory limit exceeded.
class Solution:
    def racecar(self, target: int) -> int:
        
        #1. Initialize double ended queue as 0 moves, 0 position, +1 velocity
        queue = collections.deque([(0, 0, 1)])  # moves, position, velocity
        while queue:
            # print(queue)
            moves, pos, vel = queue.popleft()
            if pos == target:
                return moves
            
            #2. Always consider moving the car in the direction it is already going
            # Minimum number of sequence ke liye position ko to increase karna hi hoga hmesha isliye ye move har ek step pe lenge.
            queue.append((moves + 1, pos + vel, 2 * vel))
            if vel > 0:
                queue.append((moves + 1, pos, -1))
            else:
                queue.append((moves + 1, pos, 1))


# Mine solution using Recursion: I thought will memoise
# I have to properly analyse why this won't work.? why giving memory limit exceeded?
# Note: Also analyse when to use bfs and when to use DP.(bfs vs dp) && other solutions also.
class Solution:
    def racecar(self, target: int) -> int:

        def solve(position, speed):
            if position == target:
                return 0
            return min(1 + solve(position + speed, speed *2), 1 + solve(position, -1), 1 + solve(position, 1))
        return solve(0, 1)
    

# my mistake:
# since it will not reach the base case(target) taking any path so will get 'Memory limit exceeded' as will start returning from base case only but may not reach base case.
# So this to make work , we have to mix other condition as well.
# And for mixing the conditions, we have to choice:
# 1) call the function based on some conditions wo path we take get mixed , OR
# 2) use bfs. Also asking for shortest no of sequence so it will work.
# In bfs all choices get mixed automatically when we add element in 'queue' considering all choices.

# Note: This is difference between bfs and dfs(DP). 
# Use above observation to see what should we use.

# Note vvi: When subproblems are repeating then try to do by DP only because through bfs you will get mostly TLE.
# sometime your solution may get accepted using bfs like this and few more Q.

# We used bfs. Later try by dfs(dp also).


# One more q that i tried by DP but didn't get but got by 'bfs'.
# "1553. Minimum Number of Days to Eat N Oranges".
