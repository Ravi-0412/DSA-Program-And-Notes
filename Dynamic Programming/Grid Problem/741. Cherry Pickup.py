# Similar logic to : "Chocolate Pickup (3D DP)".

# Let person p1 is at (0, 0) , person p2 at (n-1, n-1).

# 1st method that comes into mind is : 1) p1 will go from top to bottom and will collect the max cherries
# 2) Then, p2 will go bottom to top and will collect the max cherries
# 3) After that we will remove the common cherries collected by them to get the final ans.

# code for top to botttom

# def dfs1(r, c):
#     if r >= n or c >= n or grid[r][c] == -1:
#         return 0 
#     return grid[r][c] + max(dfs1(r , c + 1), dfs1(r+ 1 , c))


# But this will not work in case, when grid:

# [1,1,1,1,0,0,0],
# [0,0,0,1,0,0,0],
# [0,0,0,1,0,0,1],
# [1,0,0,1,0,0,0],
# [0,0,0,1,0,0,0],
# [0,0,0,1,0,0,0],
# [0,0,0,1,1,1,1]]

# our solution will give '14' but ans= 15(all available cherries).

# How 15?
# You can actually pick all 15 cherries:

# 1) Start from (0,0) and pick the first 4 cherries.
# 2) Go down only 2 fields. You are now at (2,3) and have picked 6 cherries.
# 3)Move to the right end and pick the cherry there. Now, you've got 7.
# 4) Go down to the bottom right and pick the cherry there. Now, you've got 8.

# In the next step, you do this:

# 5) You move 3 fields to the left to (n, n-3) and pick up 3 cherries. Total: 11
# 6) Go up 3 fields and collect 3 more cherries. Total: 14
# 7) Go to the left of the field now and pick the cherry there. Total: 15
# 8) Move to (0,0)

# Though here is the case where local maximum is not global maximum. 
# So having cherry pick up by person1 and then person2 won't give the correct result. 
# This approach fails to find the best answer to this case."

# finally 15 cherries without violating the rules.

# why not working?
# The obvious difference is that now the maximum number of cherries of the trip not only depends on the starting position (i, j),
# but also on the status of the grid matrix when that position is reached. 
# This is because the grid matrix may be modified differently along different paths towards the same position (i, j), 
# therefore, even if the starting position is the same, the maximum number of cherries may be different since we are working with different grid matrix now.

# Note: The above method is working in "Chocolate Pickup (3D DP)", have to see and check once again and compare both the Q.



# correct way:
# Instead of going one by one, we can go simultaneoulsy.
# Also going top to bottom(right, down) and bottom to top(left, up) both is same.
# So instead of taking initial rows and cols values as (0, 0, n-1, n-1) we can take (0, 0, 0,0) i.e we can start both from (0,0) only.

# Now Q reduces to reach (n-1, n-1) from (0,0).

# In detail: 

# Instead of going once from 0,0 to n-1,n-1 and then back, we simply go twice from 0,0 to n-1,n-1 
# because every path from n-1,n-1 to 0,0 can be interpreted as a path from 0,0 to n-1,n-1.

# Note vvi: that the one person can never cross the past path of the other person 
# (they can only meet at the same position) because both are moving simultaneously, 
# so we don't need to worry about one person picking up an already picked up cherry from the past .

# Transitions between states? we collect cherries on current positions of the two people (r1,c1 and r2,c2),
# then we go through all possible next states and choose the best one (max number of cherries) 
# as the next state (we do this by adding the number of cherries of the best next state to the number of cherries 
# we picked up on the current two positions of the people).

# Note vvi: r1+c1 = r2+c2. why?
# Both are moving at same time and moving only (right and down).

# What does a state represent? dp[r1]][r2][c1][c2] represents the max number of cherries that 
# can be collected by 2 people going from r1,c1 and r2,c2 to n-1,n-1.

# Recursion + memoisation

# time = space = O(n^3)

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        @lru_cache(None)
        def dfs(r1, c1, r2, c2):
            # since we're only going down and to the right, no need to check for < 0

            # if we went out of the grid or hit a thorn, discourage this path by returning Integer.MIN_VALUE
            if r1 >= n or c1 >= n or  r2 >= n or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            
            # if person 1 reached the bottom right, return what's in there (could be 1 or 0)
            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]
            # if person 1 reached the bottom right, return what's in there (could be 1 or 0)
            if r2 == n - 1 and c2 == n - 1:
                return grid[r2][c2]
            
            maxCherry = 0
            # if both persons standing on the same cell, add value only one time (could be 1 or 0)
            if r1 == r2 and c1 == c2:
                maxCherry = grid[r1][c1]
            else:
                # if both persons standing on the diff cell, add values at both the cells.
                maxCherry = grid[r1][c1] + grid[r2][c2]
            # for every move of p1(out of two), p2 will have two choice.
            #   P1      |     P2
            #   DOWN    |     DOWN
            #   DOWN    |     RIGHT
            #   RIGHT   |     DOWN
            #   RIGHT   |     RIGHT
            maxCherry += max((dfs(r1 + 1, c1, r2 + 1, c2), dfs(r1 + 1, c1, r2, c2 + 1),
                                dfs(r1, c1 + 1, r2 + 1, c2), dfs(r1, c1 + 1, r2, c2 + 1)))
            return maxCherry

        return max(0, dfs(0 , 0, 0, 0))   # if we can't collect any then 'dfs()' will return 'float('-inf')' and in this case we will return 0.


# nOte vvi: Q) why when one user reaches the end point,The above algo returns and works (without making sure the other user reached end point as well)?

# Ans: This algo has the main point that r1+c1 = r2+c2 So, when one of the user has reached the end point, 
# the other would have reached the end point too (since in other cases when r2+c2 = n-1 + n-1 is invalid like (n,n-2), 
# the code path would not have reached here. the only valid case for one user to reach (n-1,n-1) is for the other user to reach it too). 
# And, as per the logic, when both the users hit the same point in an iteration, we only cover it once - so, we just return it here.

# Another way:
# if one has reached the end it means it has taken exactly row+col (2N in our case) steps. 
# Now. the other person must also have taken the same number of steps, i.e. 2N. 
# And, taking 2N valid step will only put you at the last place in the grid.



# method 3 : most optimised
# we can optimise using the observation: r1+c1 = r2+c2.
# so we can get the value of any one of the para with other three say r2 = r1 + c1 - c2.

# What does a state represent? dp[r1][c1][c2] represents the max number of cherries that 
# can be collected by 2 people going from r1,c1 and r2,c2 to n-1,n-1.

# time = space = O(n^3)

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        @lru_cache(None)
        def dfs(r1, c1, c2):
            r2 = r1 + c1 - c2
            if r1 >= n or c1 >= n or  r2 >= n or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            
            # if person 1 reached the bottom right, return what's in there (could be 1 or 0)
            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]
            # if person 1 reached the bottom right, return what's in there (could be 1 or 0)
            if r2 == n - 1 and c2 == n - 1:
                return grid[r2][c2]
            
            maxCherry = 0
            # if both persons standing on the same cell, add value only one time (could be 1 or 0)
            if r1 == r2 and c1 == c2:
                maxCherry = grid[r1][c1]
            else:
                # if both persons standing on the diff cell, add values at both the cells.
                maxCherry = grid[r1][c1] + grid[r2][c2]
            # take max of all possible combination and add with maxCherry.
            maxCherry += max((dfs(r1 + 1, c1, c2), dfs(r1 + 1, c1, c2 + 1),
                                dfs(r1, c1 + 1, c2), dfs(r1, c1 + 1, c2 + 1)))
            return maxCherry

        return max(0, dfs(0 , 0, 0))   # if we can't collect any then 'dfs()' will return 'float('-inf')' and in this case we will return 0.


# Note : later try by method of "cholocate pick up" for taking all combination.

# Have to analyse my mistakes properly
# 1) 

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def dfs(r1, c1, r2, c2):
            if r1 >= n or c1 >= n or  r2 >= n or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return 0   # here 
            maxCherry = 0
            if r1 == r2 and c1 == c2:
                maxCherry = grid[r1][c1]
            else:
                maxCherry = grid[r1][c1] + grid[r2][c2]
            # ....
            maxCherry += max((dfs(r1 + 1, c1, r2 + 1, c2), dfs(r1 + 1, c1, r2, c2 + 1),
                                dfs(r1, c1 + 1, r2 + 1, c2), dfs(r1, c1 + 1, r2, c2 + 1)))
            return maxCherry

        return max(0, dfs(0 , 0, 0, 0))


# 2) Above mistake only but diff way of ca
# why not working?

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        direction = [[0, 1] , [1, 0]]

        def dfs(r1, c1, r2, c2):
            if r1 >= n or c1 >= n or  r2 >= n or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return 0
            maxCherry = 0
            if r1 == r2 and c1 == c2:
                maxCherry = grid[r1][c1]
            else:
                maxCherry = grid[r1][c1] + grid[r2][c2]
            maxOfAllComb = 0
            for dr1, dc1 in direction:
                for dr2, dc2 in direction:
                    maxOfAllComb = max(maxOfAllComb, grid[r1][c1] + dfs(r1 + dr1 , c1 + dc1 , r2 + dr2, c2 + dc2))
                    maxCherry += maxOfAllComb
            return maxCherry

        return dfs(0 , 0, 0, 0)