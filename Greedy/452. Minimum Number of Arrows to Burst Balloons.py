# Just extension of Q: "Hit most Balloons".
# https://practice.geeksforgeeks.org/problems/hit-most-balloons--170637/1


# Basically points is not given, it is line segments placed between given coordinates.
# and you have to find "minimum no of throws such that it touches all segments".

# just like interval problems. so better understanding think all as intervals. 

# How to Approach?
# Agar hm balloons ko minimum ending point ke anusar sort kar de then ,

# Ans: If the starting point of current balloons is <=  previous thrown point then the current balloon will get burst by the previous throw only.
# and if not then only we will need extra throw. And in case of extra row we will throw at end point of current balloon.

# why this will work?
# Because we have already sorted based on minimum ending point then, if start[i] <= start[pre_throw] ,
# This means make sure that end point of cur one will be >= thrown point so it will get burst by pre throw only.

# just like we are trying to merge this curr balloon with last  arrow end point(balloon end point at we thrown the last one).

# Hm balloon ko minEnd point of any ballons se throw karna start karenge hmesha, merge nhi hone pe(kyonki yhi min ending point hoga us time pe).


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda p: p[1])  # sorting based on endging point
        ans= 1
        curEnd= points[0][1]  # just we are throwing the ballons from this coordinate
        for point in points[1: ]:
            if curEnd < point[0]:
                # we will need new throw.
                ans+= 1
                curEnd= point[1]   # new throw point, end point of cur one.
            # else it will get bursted by pre throw only
        return ans