# Logic : 
"""
Take steps one by one.
If the location is inside of grid, add it to res.
But how to simulate the path?

Observation: 

move right 1 step, turn right
move down 1 step, turn right
move left 2 steps, turn right
move top 2 steps, turn right,
move right 3 steps, turn right
move down 3 steps, turn right
move left 4 steps, turn right
move top 4 steps, turn right,

we can find the sequence of steps: 1,1,2,2,3,3,4,4,5,5....

Note: We will start with steps = 1 and we will increase the step when we will start going west or
When we will complete a spiral i.e after going all directions.
"""
# Time O(max(R,C)^2)
# Space O(R*C) for output

# Method 1: Similar code as 'Spiral 1 and spiral 2'

class Solution(object):
    
    def spiralMatrixIII(self, R, C, r0, c0):
        # Initialize result list with the starting position
        res = [(r0, c0)] 
        
        # Function to check if a cell is within bounds
        def is_valid(row, col):
            return 0 <= row < R and 0 <= col < C 
        
        # Set initial values for steps and position
        steps = 1 
        r, c = r0, c0 
        
        # Continue until all cells are visited
        while len(res) < R * C: 
            # Go east
            for _ in range(steps):
                c += 1 
                if is_valid(r, c): 
                    res.append((r, c))
                    
            # Go south
            for _ in range(steps):
                r += 1
                if is_valid(r, c): 
                    res.append((r, c))
                    
            steps += 1   # increase step since we are going west
                    
            # Go west
            for _ in range(steps):
                c -= 1
                if is_valid(r, c): 
                    res.append((r, c))           
            
            # Go north
            for _ in range(steps):
                r -= 1
                if is_valid(r, c): 
                    res.append((r, c))           
                    
            steps += 1    # increase step after each spiral
            
        return res

# Method 2: Concise one
class Solution:
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        directions =  [[0, 1], [1, 0], [0, -1], [-1, 0]] # east, south, west, north
        res= [] 
        length, d = 0, 0 # move <length> steps in the <d> direction
        res.append([rStart, cStart])
        while len(res) < rows*cols:
            if d == 0 or d == 2:
                length += 1 # when move east or west, the length of path need plus 1 (this makes the outer circle each time)
            for i in range(length):
                rStart += directions[d][0]
                cStart += directions[d][1]
                if rStart >= 0 and rStart < rows and cStart >= 0 and cStart < cols: # check valid
                    res.append([rStart, cStart])
            d = (d + 1) % 4 # turn to next direction
        return res
        
