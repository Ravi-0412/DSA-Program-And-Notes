# observation : we must cross each row and each column between given positions to go
#  from the startPos to the homePos. 
# So, we will always incur cost of each row and column between home and start positions atleast once.

# It must also be observed that it's always best to travel through rows and column in the direction 
# of start to end position and never beneficial to go in the opposite direction since we would then 
# incur costs twice with no benefits. That is, we must traverse the shortest path from start to end.

# In the below solution, we are travelling from end to start just to avoid extra condition 
# (as we incur cost of rows & columns of ending cell but not of the start cell).

class Solution:
    def minCost(self, startPos, homePos, rowCosts, colCosts):
        ans, i, j = 0, homePos[0], homePos[1]
        while i != startPos[0]:
            ans += rowCosts[i]
            i += -1 if i > startPos[0] else 1
        while j != startPos[1]:
            ans += colCosts[j]
            j += -1 if j > startPos[1] else 1
        return ans