# Logic: Similar to "2013. Detect Squares"
"""
In case of rectangle any two points can be diagonal, won't follow property like square 'abs(x1 - x2) == abs(y1 - y2)'.
So consider each possible diagonal pair then other two points will be same as square i.e '(x1, y2)' and '(x2, y1)'.
and one side length = abs(x1 - x2) and other side length = abs(y1 - y2)
Summary : "Pick 2 points, find the other 2."

Time : O(n^2)
"""

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        pointsMap = {(points[i][0], points[i][1]): i for i in range(n)}   # for checking points in O(1)
        ans = float('inf')
        for i in range(n):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i + 1, n):
                x2, y2 = points[j][0], points[j][1]
              # x1 != x2 and y1 != y2 : for parallel axis
                if x1 != x2 and y1 != y2 and (x1, y2) in pointsMap and (x2, y1) in pointsMap:
                    ans = min(ans, abs(x1 - x2) * abs(y1 - y2))
        return ans if ans != float('inf') else 0

# Method 2: 
"""
Optimised one : Column-Pairing Approach.

How to think:
1. Identify the Bottleneck of O(N2)
The O(N^2) approach is "Point-Pair Centric." You are picking two random points and asking, "Are you a diagonal?"
This is inefficient because most pairs of points don't even share an X or Y coordinate, let alone form a rectangle.
2. Recognize "Fixed Axis" Constraints
Whenever an interviewer gives you coordinates, look at the distribution.
    If they say "Few unique X values," they are giving you a hint to group the data.
    Thought: "If I group points by their X-coordinate, I effectively turn the cloud of points into a set of vertical columns."
3. Change the Atomic Unit (From Point to Segment)
This is the most important "click" in the thought process.
    Instead of looking for 4 points, look for 2 vertical segments that are identical.
    A rectangle is just two vertical lines of the same height (y1​ to y2​) located at two different X positions (Xprev​ and Xcurr​).
    Thought: "If I see a vertical segment from y = 10 to y = 20 in column x = 5, and then I see the exact same segment in column x = 15, I have found a rectangle."

4. Optimize the Search with Hashing
Now that you are looking for segments, how do you find them quickly?
    You process columns one by one.
    In each column, you find every possible pair of Y-coordinates.
    You use a Hash Map to remember: "When was the last time I saw a vertical segment starting at y1​ and ending at y2​?"
    Thought: "I'll store (y1, y2) as a key in a map. The value will be the x-coordinate where I last saw it."
    
Summary : "Find 2 identical vertical segments."
Note VVI : If the interviewer says there are 100 unique X but 10,000 unique Y, group by X. 
If it's the other way around (100 unique Y), group by Y! You should always pick the axis with the fewer unique coordinates to minimize the inner nested loops.

Complexity Analysis
1. Time Complexity: O(N⋅avg_points_per_column).
    In the worst case, this is O(N⋅Rows).
    If the number of unique X is small (C), and unique Y is small (R), it performs roughly O(C⋅R^2).
    For the specific hint "40,000 points but only 100 unique X", the previous O(N2) would be 1.6×10^9 (too slow), while this approach processes the columns efficiently.
2. Space Complexity: O(N) to store the columns dictionary and the last_x_for_y_pair map.
"""
import collections

class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        # Step 1: Group Y-coordinates by their X-coordinate
        # columns = {x_coord: [y1, y2, y3...]}
        columns = collections.defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        
        # Sort Ys for each column to allow efficient intersection or processing
        for x in columns:
            columns[x].sort()
            
        # Sort unique X-coordinates to process columns in order
        sorted_x = sorted(columns.keys())
        ans = float('inf')
        
        # Step 2: Last-seen pair of Ys tracker
        # key: (y_small, y_large), value: last x_coordinate that had these two Ys
        last_x_for_y_pair = {}

        # Step 3: Iterate through each column
        for x in sorted_x:
            ys = columns[x]
            # Iterate through every pair of Y-coordinates in the current column
            for i in range(len(ys)):
                for j in range(i + 1, len(ys)):
                    y1, y2 = ys[i], ys[j] # This is a vertical segment
                    
                    # If we've seen this vertical segment (y1, y2) before
                    if (y1, y2) in last_x_for_y_pair:
                        prev_x = last_x_for_y_pair[(y1, y2)]
                        width = x - prev_x
                        height = y2 - y1
                        ans = min(ans, width * height)
                    
                    # Update the tracker with the current X
                    last_x_for_y_pair[(y1, y2)] = x
                    
        return ans if ans != float('inf') else 0


# Follow ups:
"""
1. "What if the points are not axis-aligned?" 
Ans : When the rectangle is not axis-aligned (tilted), you can't simply look for (x1​,y2​). 
Instead, you have to use the fundamental properties of a rectangle.

The Logic: The Midpoint & Diagonal Rule
For any four points to form a rectangle (even a tilted one), two conditions must be met:
1. The diagonals must bisect each other: The midpoint of diagonal AC must be the exact same coordinate as the midpoint of diagonal BD.
2. The diagonals must be equal in length: The distance between A and C must equal the distance between B and D.

How to Find the Points: 
Instead of searching for "missing points" in a hash map, we group pairs of points based on their potential to be diagonals.
1. Iterate through every possible pair of points (P1​,P2​).
2. Calculate two things for each pair:
        The Midpoint: M =((x1​+x2) / 2 ​​,(y1​+y2​​) / 2)
        The Squared Distance: D^2 = (x1​−x2​)^2+(y1​−y2​)^2
3. Group pairs in a Hash Map: Use the tuple (Midpoint, Distance) as the key.
        Map[(Midpoint, Distance)] = [ (P1, P2), (P3, P4), ... ]
4. Find Rectangles: Any two pairs in the same bucket form a rectangle! Because they share a midpoint and have equal length diagonals.

Time : O(N^2) for the first part + O(N^2) for the group processing = O(N^2) although it's like O(N^3).
Sum of squares of group sizes (Max group size is N/2).

Space : O(N^2)
"""

import collections

class Solution:
    def minAreaFreeRectangle(self, points: list[list[int]]) -> float:
        # Key: (midpoint_x, midpoint_y, squared_distance)
        # Value: List of pairs that share this diagonal property
        diag_groups = collections.defaultdict(list)
        n = len(points)
        
        for i in range(n):
            p1x, p1y = points[i]
            for j in range(i + 1, n):
                p2x, p2y = points[j]
                
                # 1. Calculate Midpoint
                mid_x = (p1x + p2x) / 2
                mid_y = (p1y + p2y) / 2
                
                # 2. Calculate Squared Distance (avoiding sqrt for precision)
                dist_sq = (p1x - p2x)**2 + (p1y - p2y)**2
                
                # 3. Store the pair by its diagonal properties
                diag_groups[(mid_x, mid_y, dist_sq)].append((points[i], points[j]))
        
        ans = float('inf')
        
        # 4. Check each group. Any two pairs in a group form a rectangle.
        for group in diag_groups.values():
            if len(group) > 1:
                for i in range(len(group)):
                    for j in range(i + 1, len(group)):
                        # Points of the two diagonals
                        p1, p2 = group[i]
                        p3, p4 = group[j]
                        
                        # Use side lengths to find area: L1 * L2
                        # Side 1: dist(p1, p3), Side 2: dist(p1, p4)
                        side1 = ((p1[0]-p3[0])**2 + (p1[1]-p3[1])**2)**0.5
                        side2 = ((p1[0]-p4[0])**2 + (p1[1]-p4[1])**2)**0.5
                        ans = min(ans, side1 * side2)
                        
        return ans if ans != float('inf') else 0


# Java Code
"""
import java.util.*;

class Solution {
    public int minAreaRect(int[][] points) {
        int n = points.length;
        Map<Integer, Set<Integer>> pointsMap = new HashMap<>(); // For checking points in O(1)

        for (int[] point : points) {
            pointsMap.putIfAbsent(point[0], new HashSet<>());
            pointsMap.get(point[0]).add(point[1]);
        }

        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            int x1 = points[i][0], y1 = points[i][1];
            for (int j = 0; j < n; j++) {
                int x2 = points[j][0], y2 = points[j][1];

                // x1 != x2 and y1 != y2 : for parallel axis
                if (x1 != x2 && y1 != y2 && pointsMap.get(x1).contains(y2) && pointsMap.get(x2).contains(y1)) {
                    ans = Math.min(ans, Math.abs(x1 - x2) * Math.abs(y1 - y2));
                }
            }
        }

        return (ans == Integer.MAX_VALUE) ? 0 : ans;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <unordered_map>
#include <limits>

using namespace std;

class Solution {
public:
    int minAreaRect(vector<vector<int>>& points) {
        int n = points.size();
        unordered_map<int, unordered_map<int, int>> pointsMap; // For checking points in O(1)

        for (int i = 0; i < n; i++) {
            pointsMap[points[i][0]][points[i][1]] = i;
        }

        int ans = numeric_limits<int>::max();
        for (int i = 0; i < n; i++) {
            int x1 = points[i][0], y1 = points[i][1];
            for (int j = 0; j < n; j++) {
                int x2 = points[j][0], y2 = points[j][1];

                // x1 != x2 and y1 != y2 : for parallel axis
                if (x1 != x2 && y1 != y2 && pointsMap[x1].count(y2) && pointsMap[x2].count(y1)) {
                    ans = min(ans, abs(x1 - x2) * abs(y1 - y2));
                }
            }
        }

        return (ans == numeric_limits<int>::max()) ? 0 : ans;
    }
};
"""
