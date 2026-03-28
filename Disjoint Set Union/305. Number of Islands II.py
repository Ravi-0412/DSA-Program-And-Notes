"""
my mistake: 
I thought correct but made some minor mistakes like:
1.1)  i was thinking that count will increase or will be same as previous operation always..(what the fuck , i couldn't thought of this)..
if we are putting the nodes in between land then it will decrease also.
it may increase or decrease, it depends on position we are inserting.

1.2) was checking if in any of four direction we can merge.And for all combined together i was decr the count by '1'.
but in every possible direction if we can merge then we should decr the count by '1'.

2) cell could have repeat in the input, but i was not considering that.
3) was changing the land value(input) to '1' at start itself.

Difference from 'No of island 1': We have count after each operation
"""

"""
Logic :
1. Look at the four neighbors (Up, Down, Left, Right). If a neighbor is already land, we try to union our new cell with that neighbor.
2. The Union Rule: If the union is successful (meaning the new land and the neighbor were previously in different components), 
we decrement our total island count because two islands have just become one.

Time : O(K * alpha(row * col)), k : no of operations
"""

class DSU:
    def __init__(self, n):
        # Every cell starts as its own parent
        self.parent = list(range(n))
        # Size array for Union by Size optimization
        self.size = [1] * n
    
    def findUPar(self, node):
        # Path Compression: Connects node directly to the root
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    
    def unionBySize(self, n1, n2):
        root1, root2 = self.findUPar(n1), self.findUPar(n2)
        if root1 == root2:
            return False # Already in the same island
            
        # Merge smaller island into larger island
        if self.size[root1] < self.size[root2]:
            self.parent[root1] = root2
            self.size[root2] += self.size[root1]
        else:
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]
        return True # Successful merge

class Solution:
    def numIslands2(self, m: int, n: int, positions: list[list[int]]) -> list[int]:
        dsu = DSU(m * n)
        is_land = [False] * (m * n) # Track which cells are currently land
        count = 0
        ans = []
        
        # Directions for neighbor checks: (row_offset, col_offset)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for r, c in positions:
            idx = r * n + c
            
            # Edge Case: If position is already land, count doesn't change
            if is_land[idx]:
                ans.append(count)
                continue
            
            is_land[idx] = True
            count += 1 # Assume it's a new island first
            
            # Check 4 neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                neighbor_idx = nr * n + nc
                
                # If neighbor is within bounds and is also land
                if 0 <= nr < m and 0 <= nc < n and is_land[neighbor_idx]:
                    # If we can merge with this neighbor, decrease total islands
                    if dsu.unionBySize(idx, neighbor_idx):
                        count -= 1
            
            ans.append(count)
            
        return ans
    
