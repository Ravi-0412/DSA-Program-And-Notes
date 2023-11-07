# Note: there can be duplicate points also.

# Indirectly we have to find :" Count maximum points on same line".

# Two points can be on same line with slope say 'x' if slope of line connecting these two point will be also = "x".

# we can start(throw balloons) from any point and check how many points(balloons) we can get on same line.
# Here it will check for every direction possible indirectly because we are calculating the slope for each pair possible
#  and storing frequency of that slope.

# To store the count points with same slope, we can use hashmap('slopeCount).

# time: O(n^2)
# space: O(n)

import collections
class Solution: 
    def mostBalloons(self, N, arr):
        ans= 0
        # starting from any point
        for i in range(N):
            # we have to count the points having same slope.
            # for every possible slope from cur point we have to store the number of points.
            slopeCount= collections.defaultdict(int)  # will count the points having same slope.
            count= 0  # will count the no of same points i.e 'x1' , 'y1'.
            x1, y1= arr[i]
            for j in range(N):
                x2, y2= arr[j]
                if x1== x2 and y1== y2:  # there can be more than one balloon at starting point itself.
                    count+= 1
                    continue
                dy= (y2 - y1)
                dx= (x2- x1)
                if dx== 0:  # handling if slope is "infinity". 
                    slopeCount[10**9]+= 1  # just any very large value. max val of x or y can be= 10**9 so slope can't be more than this
                    continue
                slope= dy/dx
                slopeCount[slope]+= 1
            
            # update the ans.
            for key,val in slopeCount.items():
                ans= max(ans, val + count)
        return ans


# my mistake:
# i was only checking the diagonal throw 
# i.e abs(x2-x1)== abs(y2-y1)  then only we can hit the balloons at point(x2,y2) if we throw diagonally.


# Related Q:
"149. Max Points on a Line"