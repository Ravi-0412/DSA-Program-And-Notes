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

i) bisect_left : It finds the first spot where the number could be placed without breaking the sorted order.
If the number is already there, you stand to the left of the duplicates.
ii) bisect_right : It finds the last spot where the number could be placed without breaking the sorted order.
If the number is already there, you stand to the right of the duplicates.

arr = [1, 3, 4, 7, 7, 7, 8, 10], target : 7
bisect_left : 3 , bisect_right : 6

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
        # 1. Sort points by X to enable horizontal pruning
        points.sort()
        points_x = [p[0] for p in points]
        n = len(points_x)
        res = []

        for qx, qy, r in queries:
            x_min, x_max = qx - r, qx + r
            
            # 2. Template: Find FIRST index >= x_min
            # Logic: If mid is >= x_min, it could be the start, so we check left (high = mid - 1)
            low, high = 0, n - 1
            while low <= high:
                mid = (low + high) // 2
                if points_x[mid] >= x_min:
                    high = mid - 1
                else:
                    low = mid + 1
            left_idx = low # 'low' lands on the first valid index

            # 3. Template: Find LAST index <= x_max
            # Logic: If mid is <= x_max, it could be the end, so we check right (low = mid + 1)
            low, high = 0, n - 1
            while low <= high:
                mid = (low + high) // 2
                if points_x[mid] <= x_max:
                    low = mid + 1
                else:
                    high = mid - 1
            right_idx = high # 'high' lands on the last valid index

            # 4. Filter and Check
            count = 0
            # Note: We use right_idx + 1 because right_idx is inclusive
            for i in range(left_idx, right_idx + 1):
                px, py = points[i]
                # Using squared distance to avoid math.sqrt() overhead
                if (px - qx)**2 + (py - qy)**2 <= r * r:
                    count += 1
            res.append(count)
            
        return res
