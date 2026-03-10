# Method 1:
# Brute force
"""
Just traverse matrix and maintain four variables : min_x, max_x, min_y, max_y
Ans = (max_x - min_x) * (max_y - min_y)

for this either use bfs, dfs or simply traverse.

Time : O(M*N)
"""

class Solution:
    def minArea(self, image: list[list[str]], x: int, y: int) -> int:
        # Logic: Perform a full linear scan of the grid.
        # Use min/max to shrink/expand the bounding box around any black pixel ('1').
        
        m, n = len(image), len(image[0])
        
        # Initialize boundaries with the starting black pixel coordinates
        min_x, max_x = x, x
        min_y, max_y = y, y
        
        # Iterate through every pixel in the m x n grid
        for r in range(m):
            for c in range(n):
                # If the current pixel is black
                if image[r][c] == '1':
                    # Update row boundaries
                    min_x = min(min_x, r)
                    max_x = max(max_x, r)
                    # Update column boundaries
                    min_y = min(min_y, c)
                    max_y = max(max_y, c)
        
        # Area = Height * Width
        # We add 1 because the indices are inclusive (e.g., 0 to 2 is 3 units)
        return (max_x - min_x + 1) * (max_y - min_y + 1)

# Method 2:
"""
Optimised one.

Somehow we need to find those four points without doing whole traversal to reduce the complexity.
Since it's given that black-points(x, y) are connected. So min_x will lie <= x and max_x will lie >= x and same for min_y and max_y.
Because all '1' will adjacent only either horizontally or vertically. So we can just check if that row or column contains '1' or not ? if yes then we can find the range.

so we can reduce our search space and search in this range only for finding minimum & maximum coordinates.

Logic : 
1. Horizontal Projection (Finding X boundaries):
    Think of each row as a single unit. A row is "True" if it contains at least one '1', and "False" otherwise.
    Since the pixels are connected, there is a continuous block of "True" rows.
    We use Template 4 to find the first row in the range [0,x] that contains a '1' (min_x).
    We use Template 5 to find the last row in the range [x,m−1] that contains a '1' (max_x).

2. Vertical Projection (Finding Y boundaries): Do same as above

Time : 
Instead of visiting every pixel, we only perform 4 binary searches.
    Each step of the binary search checks a row or column (O(N) or O(M)).
    Total Time: O(N*logM + M*logN)

Note : Here you can't apply bisect_left and bisect_right, because row and column might not be fully sorted.
"""

class Solution:
    def minArea(self, image: list[list[str]], x: int, y: int) -> int:
        m, n = len(image), len(image[0])
        
        # Helper to check if a specific row has any black pixels
        def has_black_in_row(r):
            for c in range(n):
                if image[r][c] == '1': return True
            return False
        
        # Helper to check if a specific column has any black pixels
        def has_black_in_col(c):
            for r in range(m):
                if image[r][c] == '1': return True
            return False

        # --- 1. Find min_x (First row with a '1' in range [0, x]) ---
        low, high = 0, x
        min_x = x
        while low <= high:
            mid = (low + high) // 2
            if has_black_in_row(mid):
                min_x = mid      # Potential start found
                high = mid - 1   # Try looking further up (Template 4)
            else:
                low = mid + 1
        
        # --- 2. Find max_x (Last row with a '1' in range [x, m-1]) ---
        low, high = x, m - 1
        max_x = x
        while low <= high:
            mid = (low + high) // 2
            if has_black_in_row(mid):
                max_x = mid      # Potential end found
                low = mid + 1    # Try looking further down (Template 5)
            else:
                high = mid - 1
                
        # --- 3. Find min_y (First col with a '1' in range [0, y]) ---
        low, high = 0, y
        min_y = y
        while low <= high:
            mid = (low + high) // 2
            if has_black_in_col(mid):
                min_y = mid      # Potential left boundary found
                high = mid - 1   # Look further left
            else:
                low = mid + 1
                
        # --- 4. Find max_y (Last col with a '1' in range [y, n-1]) ---
        low, high = y, n - 1
        max_y = y
        while low <= high:
            mid = (low + high) // 2
            if has_black_in_col(mid):
                max_y = mid      # Potential right boundary found
                low = mid + 1    # Look further right
            else:
                high = mid - 1
        
        # Smallest rectangle area
        return (max_x - min_x + 1) * (max_y - min_y + 1)

  # Method 3:
  """
  Very concise way to write above code.
  """

class Solution:
    def minArea(self, image: list[list[str]], x: int, y: int) -> int:
        m, n = len(image), len(image[0])
        
        # Helper logic to check if a row/column contains any '1'
        has_row = lambda r: '1' in image[r]
        has_col = lambda c: any(image[r][c] == '1' for r in range(m))

        # Universal Binary Search Function
        def search(low, high, check_func, find_min):
            ans = low if find_min else high
            while low <= high:
                mid = (low + high) // 2
                if check_func(mid):
                    ans = mid
                    if find_min: high = mid - 1 # Template 4: Look earlier
                    else: low = mid + 1        # Template 5: Look later
                else:
                    if find_min: low = mid + 1
                    else: high = mid - 1
            return ans

        # Call the same function 4 times for the 4 boundaries
        min_x = search(0, x, has_row, True)
        max_x = search(x, m - 1, has_row, False)
        min_y = search(0, y, has_col, True)
        max_y = search(y, n - 1, has_col, False)

        # Area = (max_x - min_x + 1) * (max_y - min_y + 1)
        return (max_x - min_x + 1) * (max_y - min_y + 1)
