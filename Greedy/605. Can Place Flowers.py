"""
Given flowerbed[i] = 1 means there is already flower planted so you can't plant there.

Logic:
We don't need to try every combination; we just need to plant a flower the moment we find a valid spot.

1. To plant a flower at index i, three things must be true:
    flowerbed[i] is 0 (empty).
    Left neighbor is 0 (or we are at the very beginning).
    Right neighbor is 0 (or we are at the very end).
2. Immediate Planting: Once we plant a flower (change 0 to 1), we decrement our target n.
3. Early Exit: If n hits 0, we can stop early and return True. 

Time : O(N)
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Thought Process:
        # Iterate through the bed. If a plot is empty and its neighbors 
        # are also empty, plant a flower.
        
        count = 0
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:
                # Check if left neighbor is empty or it's the start
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                # Check if right neighbor is empty or it's the end
                empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)
                
                if empty_left and empty_right:
                    # Plant the flower
                    flowerbed[i] = 1
                    count += 1
                    
                    # Optimization: return immediately if we reached n
                    if count >= n:
                        return True
                        
        return count >= n

# Method 2:
"""
Better one : Without changing input array

Logic : 
1. If the current spot is 1, we know the next spot must be empty. We skip the next index entirely.
2. If the current spot is 0:
    We check the next spot.
    If the next spot is also 0 (or we are at the end), we "plant" here and skip the next spot because we know we can't plant there anyway.

Time : O(N) , space : O(1)    
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # We use a pointer to jump through the array
        i = 0
        count = 0
        length = len(flowerbed)
        
        while i < length:
            # If current is 1, we can't plant here OR at i+1. Jump to i+2.
            if flowerbed[i] == 1:
                i += 2
            # If current is 0:
            else:
                # Check if it's the last element OR if the next element is 0
                if i == length - 1 or flowerbed[i + 1] == 0:
                    # We can plant here! 
                    # Because we know i-1 was handled by the previous jump
                    # Reason : " There are no two adjacent flowers in flowerbed." , this it make sure that 
                  # left one is empty only from the previous jump
                    count += 1
                    i += 2 # Skip the neighbor of our new "virtual" flower
                else:
                    # If i is 0 but i+1 is 1, we can't plant at i.
                    # We also know we can't plant at i+1. Jump to i+3.
                    i += 3
            
            if count >= n:
                return True
                
        return count >= n
