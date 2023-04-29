# Basically points is not given, it is line segments placed betwen given coordinates.
# and you have to find "minimum no of throws such that it touches all segments".

# just like interval problems. so better understanding think all as intervals. 


# How to Approach?
# Ans: if the starting point of current balloons is <=  previous thrown point then the current balloon will get burst by the previous throw only.
# and if not then only we will need extra throw. And in case of extar row we will throw at end point of current balloons.
# just like we are merging.


# Pichla throw jis point se kiya gya h , us point tak hm jitna jyada ballons la payenge utna kam throw hmko karna hoga.

# Hm balloon ko minEnd point of any ballons se throw karna start karenge hmesha merge n hone pe.
# isliye hm array ko "ending point ke anusar sort karenge".

# so we have to check from 


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda p: p[1])
        print(points)
        ans= 1
        curEnd= points[0][1]  # just we are throwing the ballons from this coordinate
        for point in points[1: ]:
            if curEnd < point[0]:
                ans+= 1
                curEnd= point[1]
        return ans