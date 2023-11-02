# Intuition vvi: : the main observation is that "we need not care about the collisions as the ants aren't unique"
# (means all cover the same distance in unit time or have same speed).
# it's just same as they keep moving in the same direction without changing the direction. 

# In detail:

# When two ants collide, we can just act like they "phased" through each other! 
# When one ant is going left, and another is going right, and they bump into each other, 
# the left ant is now going right and the right ant is going left. 
# There would be no difference if we had just swapped the ants, or let them pass through each other when they collide 
# because again in next unit of time they will exchange the position having difference same.

# so our ans= max(max(time taken to reach left ants to '0') , max(time taken to reach right ants to 'n'))
# = max(time taken by max(left) to reach 0, time taken by min(right) to reach n)

# Note vvvvi: if ants have different speed or cover different distance in unit time then this method won't work.
# in this case we have to go by Brute force only i.e after each unit of time we will have to find the position of ants
#  keeping in mind we have to change direction .
# Then find the difference from last position array.

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans= 0
        for num in left:
            ans= max(ans, num -0)
        for num in right:
            ans= max(ans, n - num)
        return ans

