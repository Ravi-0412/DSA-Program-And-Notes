""
1. Just utilising the similar concepts of : 85.Maximal Reactangle to get maximum no of consecutive 1's then
2. Sort in reverse order after each row(means we are just merging the bigger heights together) 
3. Calculate the maximum rectangle after sorting (by finding height & width). 

Time : O(row * col * log(col)

"""

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_area = 0
        
        # Tracks running consecutive vertical heights of '1's for each column
        heights = [0] * n
        
        for i in range(m):
            for j in range(n):
                # Accumulate heights if cell is 1, reset to 0 if it breaks
                heights[j] = heights[j] + 1 if matrix[i][j] == 1 else 0
            
            # Create a copy and sort heights in descending order 
            # This simulates shifting the best columns next to each other
            sorted_heights = sorted(heights, reverse=True)
            
            # Calculate the area row by row using the sorted column bars
            for k in range(n):
                # Height is restricted by the shortest column in the sorted group
                curr_height = sorted_heights[k]
                # Width is the number of columns processed so far
                curr_width = k + 1
                
                max_area = max(max_area, curr_height * curr_width)
                
        return max_area
