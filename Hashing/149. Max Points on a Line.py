# Same Q as "Hit most balloons" only difference here is no duplicate points i.e no two points having same both 'x' and 'y' coordinate.
# same code as "Hit Most ballons" just removed the lines that for counting the same point.

# Time: O(n^2)

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        N= len(points)
        ans= 1  # minimum possible ans can be '1'.
        for i in range(N-1):
            slopeCount= collections.defaultdict(int)  # will count the points having same slope.
            x1, y1= points[i]
            for j in range(i+1, N):
                x2, y2= points[j]
                
                dy= (y2 - y1)
                dx= (x2- x1)
                if dx== 0:  # handling if slope is "infinity". 
                    slopeCount[10**4]+= 1  # just any very large value. max val of x or y can be= 10**9 so slope can't be more than this
                    continue
                slope= dy/dx
                slopeCount[slope]+= 1
            
            for key,val in slopeCount.items():
                ans= max(ans, val + 1)   # '1' for current point.
        return ans