# Method 1:
"""
A point (x_1, y_1) is inside or on the boundary of a circle with center (x_0, y_0) and radius r if the distance between the point and the center is less than or equal to r.
d = sqrt{(x_1 - x_0)^2 + (y_1 - y_0)^2}  => (x_1 - x_0)^2 + (y_1 - y_0)^2 <= r^2

Time : O(Q * P), space : O(1)
"""

class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        # Result array to store the count for each query
        answer = []
        
        for qx, qy, r in queries:
            count = 0
            # Pre-calculate squared radius to save computation inside the inner loop
            r_squared = r * r 
            for px, py in points:
                # Calculate squared Euclidean distance: (x2-x1)^2 + (y2-y1)^2
                dist_squared = (px - qx)**2 + (py - qy)**2    
                # If distance squared is <= radius squared, the point is inside
                if dist_squared <= r_squared:
                    count += 1
            answer.append(count)
            
        return answer

# method 2:
"""
Optimised one
Logic: X-Axis Filtering
If a circle is centered at qx with radius r, any point outside the range [qx - r, qx + r] on the X-axis
is physically impossible to be inside the circle.
1. Sort all points by their x-coordinate once.
2. For each query, find the Left Boundary (qx - r) and Right Boundary (qx + r) 
in the sorted list using bisect_left and bisect_right. 
3. Only perform the expensive distance calculation for the points within this narrow slice.

Time : O(P*logP + Q *(logP + Kavg))
Kvag , best case : O(logP)
worst case : O(P) => Occurs if all points have the same X-coordinate (a vertical line) or if the circles are large enough to cover the entire X-range.
So in this case , time : O(P*logP + Q *P)

Space : O(P)
"""

import bisect

class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        # 1. Sort points by X-coordinate to enable binary search (O(P log P))
        points.sort()
        # Extract just the X-values for the bisect function
        points_x = [p[0] for p in points]
        
        answer = []
        
        for qx, qy, r in queries:
            count = 0
            r_squared = r * r
            
            # 2. Find the range of points whose X-coordinate is within [qx - r, qx + r]
            # This is the "Pruning" step.
            left_idx = bisect.bisect_left(points_x, qx - r)
            right_idx = bisect.bisect_right(points_x, qx + r)
            
            # 3. Only check points within this X-range
            for i in range(left_idx, right_idx):
                px, py = points[i]
                
                # Calculate squared distance
                dist_squared = (px - qx)**2 + (py - qy)**2
                
                if dist_squared <= r_squared:
                    count += 1
            
            answer.append(count)
            
        return answer

  # without using bisect_left and bisect_right

class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        # 1. Sort points by X so we can find the range of interest
        points.sort()
        points_x = [p[0] for p in points]
        n = len(points_x)
        res = []

        for qx, qy, r in queries:
            # Determine the X-range [qx-r, qx+r]
            x_min, x_max = qx - r, qx + r
            
            # 2. Binary Search for x_min (Custom bisect_left)
            low, high = 0, n
            while low < high:
                mid = (low + high) // 2
                if points_x[mid] >= x_min: high = mid
                else: low = mid + 1
            left_idx = low

            # 3. Binary Search for x_max (Custom bisect_right)
            low, high = 0, n
            while low < high:
                mid = (low + high) // 2
                if points_x[mid] > x_max: high = mid
                else: low = mid + 1
            right_idx = low

            # 4. Filter and Check
            count = 0
            # Only loop through points that are horizontally within the circle's reach
            for i in range(left_idx, right_idx):
                px, py = points[i]
                # Squared distance check (Euclidean distance)
                if (px - qx)**2 + (py - qy)**2 <= r*r:
                    count += 1
            res.append(count)
            
        return res
