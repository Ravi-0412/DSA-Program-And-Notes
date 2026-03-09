# method 1:
# Time = O(n), space: O(1)
class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        # Logic: Scan from right to left keeping track of the max height seen so far.
        # A building has a view if it is strictly taller than the max to its right.
        
        n = len(heights)
        res = []
        max_height = -1 # Initialize with -1 since heights are positive
        
        # Iterate from right (n-1) to left (0)
        for i in range(n - 1, -1, -1):
            # If current building is taller than all buildings to the right
            if heights[i] > max_height:
                res.append(i)
                # Update the new maximum height encountered
                max_height = heights[i]
        
        # Since we collected indices from right to left, reverse them for final answer
        return res[::-1]

# method 2:

class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        # Logic: Maintain a stack of indices where heights are strictly decreasing.
        stack = []
        
        for i in range(len(heights)):
            # If current building is taller than the previous ones, 
            # the previous ones no longer have an ocean view.
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()
            stack.append(i)
            
        return stack

  # Follow ups:
"""
1. Scenario: "Now there are two oceans—one to the left and one to the right. A building has a 'Double View' if it is taller than everything to its left AND everything to its right."
  
The Logic: This is essentially finding the Global Maximum.

The Solution:
If there is a single tallest building, only that one has a double view.
If there are multiple buildings with the same maximum height, none of them have a double view (because they block each other).

2. Scenario: "Each building wants an ocean view. If a building is blocked, you can pay $1 per floor to increase its height. 
What is the minimum cost to give every building an ocean view?

"The Logic: This is a greedy approach moving from right to left.
The Solution: * The building at n-1 (closest to ocean) costs $0.
    For every other building, its height must be max_height_to_right + 1.
    Cost += max(0, (max_to_right + 1) - current_height).
"""
