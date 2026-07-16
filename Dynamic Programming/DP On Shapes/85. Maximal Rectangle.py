# just convert the problems of 2D into 1D like 'largest rectangle in histogram'
# rule for converting
# add the heights(+1) to the pre heights if value of matrix at that position is= 1
# else heights at that index will be equal to zero.
# assume that you are making building so if base height is zero , you can't make the building
# so height at that position will be equal to zero.

# just find the area of 1st row then '1st + 2nd row' then '1st + 2nd+ 3rd row' and so on'
# and go on updating the heights like you are making a building
# max_area of all the above will give the ans.

# time: O(n^2)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row,col,max_area= len(matrix), len(matrix[0]), 0
        heights= [0 for i in range(col)]
        for i in range(row):
            for j in range(col):
                if matrix[i][j]== '0':  
                    heights[j]= 0 
                else:
                    heights[j]+= 1                
            local_area= self.largestRectangleArea(heights)  # adding heights and calculating area row wise
            max_area= max(max_area,local_area)
        return max_area
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        
        # A height of 0 at the end guarantees every remaining index in the stack 
        # encounters a "Next Smaller Element" and is processed before the loop terminates.
        extended_heights = heights + [0]
        
        for i, h in enumerate(extended_heights):
            # Maintain a monotonic strictly increasing stack of indices.
            # A drop in height means 'i' acts as the Right Boundary (Next Smaller Element) 
            # for the bar currently at the top of the stack.
            while stack and extended_heights[stack[-1]] > h:
                # Target bar to calculate area for. Its maximum height is fixed.
                target_idx = stack.pop()
                height = extended_heights[target_idx]
                
                # If stack is empty after pop, target_idx was the smallest bar seen so far;
                # it can expand all the way left to index 0, so total width is 'i'.
                # If not empty, the new top of stack is the Left Boundary (Previous Smaller Element);
                # the bar can safely expand left up to (stack[-1] + 1).
                width = i if not stack else i - stack[-1] - 1
                
                # Maximize area using the full continuous span discovered for this height
                max_area = max(max_area, height * width)
                
            # Current index is pushed as it is greater than or equal to the current stack top
            stack.append(i)
            
        return max_area


# Later do by DP also


