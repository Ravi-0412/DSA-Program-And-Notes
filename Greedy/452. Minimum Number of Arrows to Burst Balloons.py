"""
Just extension of Q: "Hit most Balloons".
https://practice.geeksforgeeks.org/problems/hit-most-balloons--170637/1


Basically points is not given, it is line segments placed between given coordinates.
and you have to find "minimum no of throws such that it touches all segments".

just like interval problems. so better understanding think all as intervals. 

How to Approach?
Agar hm balloons ko minimum ending point ke anusar sort kar de then ,

Ans: If the starting point of current balloons is <=  previous thrown point then the current balloon will get burst by the previous throw only.
and if not then only we will need extra throw. And in case of extra row we will throw at end point of current balloon.

why this will work?
Because we have already sorted based on minimum ending point then, if start[i] <= start[pre_throw] ,
This means make sure that end point of cur one will be >= thrown point so it will get burst by pre throw only.

just like we are trying to merge this curr balloon with last  arrow end point(balloon end point at we thrown the last one).

Hm balloon ko minEnd point of any ballons se throw karna start karenge hmesha, merge nhi hone pe(kyonki yhi min ending point hoga us time pe).

Note: If we sort according to starting point and apply the same logic then, it won't give correct ans.
Reason: if 1st point has bigger ending point then many point which has lesser end point, we will miss those points giving incorrect ans.

"""

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

# Java
"""
class Solution {
    public int findMinArrowShots(int[][] points) {
        if (points.length == 0) return 0;

        // Sort the balloons by their end coordinates
        Arrays.sort(points, Comparator.comparingInt(a -> a[1]));

        int arrows = 1;  // We need at least one arrow
        int curEnd = points[0][1];  // First arrow is shot at the end of the first balloon

        for (int i = 1; i < points.length; i++) {
            if (points[i][0] > curEnd) {  
                // A new arrow is needed
                arrows++;
                curEnd = points[i][1];  // Update the shooting point
            }
            // Else, the current balloon is already burst by the previous arrow
        }

        return arrows;
    }
}
"""
