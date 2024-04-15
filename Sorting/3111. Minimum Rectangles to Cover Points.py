# Logic: We need to take care only 'x' coordinates. 
# So just sort according to x coordinate and when difference of 'x' coordinates is greater than 'w' 
# then increase the count and initialize starting 'x' coordinate = x-coordinate of cur point. 

class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort()
        mn = points[0][0]
        cnt = 1
        for i in range(1, len(points)):
            if points[i][0] - mn > w:
                cnt += 1
                mn = points[i][0]
        return cnt
