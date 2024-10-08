# Logic: Similar to "2013. Detect Squares"
"""
# In case of rectangle any two points can be diagonal, won't follow property like square 'abs(x1 - x2) == abs(y1 - y2)'.
# So consider each possible diagonal pair then other two points will be same as square i.e '(x1, y2)' and '(x2, y1)'.
and one side length = abs(x1 - x2) and other side length = abs(y1 - y2)
"""

# Time: O(n^2)

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        pointsMap = {(points[i][0], points[i][1]): i for i in range(n)}   # for checking points in O(1)
        ans = float('inf')
        for i in range(n):
            x1, y1 = points[i][0], points[i][1]
            for j in range(n):
                x2, y2 = points[j][0], points[j][1]
              # x1 != x2 and y1 != y2 : for parallel axis
                if x1 != x2 and y1 != y2 and (x1, y2) in pointsMap and (x2, y1) in pointsMap:
                    ans = min(ans, abs(x1 - x2) * abs(y1 - y2))
        return ans if ans != float('inf') else 0

# Java
"""
import java.util.HashSet;

class Solution {
    public int minAreaRect(int[][] points) {
        // Use a HashSet to store all the points for fast lookup
        HashSet<String> pointSet = new HashSet<>();
        for (int[] point : points) {
            pointSet.add(point[0] + "," + point[1]);
        }
        
        int minArea = Integer.MAX_VALUE;  // Initialize the minimum area as a large value
        
        // Loop through all pairs of points
        for (int i = 0; i < points.length; i++) {
            for (int j = 0; j < points.length; j++) {
                int x1 = points[i][0], y1 = points[i][1];
                int x2 = points[j][0], y2 = points[j][1];
                
                // Only consider points that form diagonal corners (x1 != x2 and y1 != y2)
                if (x1 != x2 && y1 != y2) {
                    // Check if the other two points exist in the set
                    if (pointSet.contains(x1 + "," + y2) && pointSet.contains(x2 + "," + y1)) {
                        // Calculate the area of the rectangle
                        int area = Math.abs(x1 - x2) * Math.abs(y1 - y2);
                        minArea = Math.min(minArea, area);  // Update the minimum area
                    }
                }
            }
        }
        
        // If minArea was not updated, return 0 (no rectangle found)
        return minArea == Integer.MAX_VALUE ? 0 : minArea;
    }
}
"""
