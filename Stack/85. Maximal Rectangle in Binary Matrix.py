# Logic: Brute force
# Find the area of each possible rectangle and take maximum i.e 
# area of rectangle from (0, 0) to (i, j) where 0<= i < row and 0 <= j < col.

# But for getting height of rectangle 
# add the heights(+1) to the pre heights if value of matrix at that position is = 1 
# else heights at that index will be equal to zero.

# Assume that you are making building so if base height is zero , you can't make the building
# so height at that position will be equal to zero

# just find the area of 1st row then '1st + 2nd row' then '1st + 2nd+ 3rd row' and so on'
# and go on updating the heights like you are making a building.

# For each rectangle question reduces to:'84.largest rectangle in histogram'.

# Time: O(row*col)

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row,col,max_area= len(matrix), len(matrix[0]), 0
        heights= [0 for i in range(col)]
        for i in range(row):
            for j in range(col):
                # if matrix[i][j]== 0:   # don't know why writing like this is not working in leetcode but working in GFG
                if matrix[i][j]== '0':  # this is working properly in leetcode but giving error in GFG
                    heights[j]= 0 
                else:
                    heights[j]+= 1                
            local_area= self.largestRectangleArea(heights)  # adding heights and calculating area row wise
            max_area= max(max_area,local_area)
        return max_area
    
    def largestRectangleArea(self, heights):
        stack, index= [], 0
        maxArea= 0
        while(index < len(heights)):
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index+= 1
            else:
                topOfStack= stack.pop()
                currArea= heights[topOfStack] *((index- stack[-1]-1) if stack else index)
                maxArea= max(maxArea, currArea)  # here getting error : '>' is not supported bw instance of str and int
        while stack:
            topOfStack= stack.pop()
            currArea= heights[topOfStack] *((index- stack[-1]-1) if stack else index)
            maxArea= max(maxArea, currArea)
        return maxArea


# Later do by DP also
