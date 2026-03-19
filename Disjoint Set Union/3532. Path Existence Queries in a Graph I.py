# Method 1:
"""
Brute force: Combine every pair(i, j) using Disjoint Set Union with path compression and for each query check if they have same parent or not.

Q) Why DSU ?
DSU is perfect for "Is node A connected to node B?" queries. It provides two main operations:
i) Union(i, j): Connects two sets containing i and j.
ii) Find(i): Returns the representative (root) of the set containing 'i'.

Time : O(n^2) , because we are checking every pair. (TLE)
"""

# Method 2:
"""
Think how can we use the sorted property ?
The array nums is already sorted.
Logic: If nums[i] and nums[i+2] are close enough to have an edge (|nums[i+2] - nums[i]| <= maxDiff), 
then the intermediate node i+1 must also be within maxDiff of both because nums[i] <= nums[i+1] <= nums[i+2].
Therefore, we only need to check adjacent elements. If nums[i+1] - nums[i] <= maxDiff, they belong to the same connected component.

Time : O(n * alpha(n) + q * alpha(n)) ~ O(n + q) 
"""

class DisjointSetUnion:
    def __init__(self, n: int):
        # Each node is its own parent initially
        self.parent = list(range(n))
        # Rank is used to keep the tree flat
        self.rank = [0] * n

    def find(self, i: int) -> int:
        # Path Compression: Point nodes directly to the root
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int):
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i != root_j:
            # Union by Rank: Attach smaller tree to the larger one
            if self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            elif self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1
            return True
        return False

class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[bool]:
        # Step 1: Initialize the DSU
        dsu = DisjointSetUnion(n)
        
        # Step 2: Build the 'Chain' of connectivity
        # Since the array is sorted, we only need to link adjacent elements
        # if they satisfy the maxDiff constraint.
        for i in range(1, n):
            if nums[i] - nums[i-1] <= maxDiff:
                dsu.union(i, i-1)
        
        # Step 3: Answer Queries
        answer = []
        for u, v in queries:
            # Two nodes are connected if they share the same root
            answer.append(dsu.find(u) == dsu.find(v))
            
        return answer

# Method 3:
"""
Best One
Since we only care about adjacent connections in a sorted array, we don't even need a full DSU class. 
We can simply iterate through the array once and assign "Component IDs." If two nodes have the same ID, they are connected.

Time : O(n + q) 
"""

class Solution:
    def existenceQueries(self, n: int, nums: list[int], max_diff: int, queries: list[list[int]]) -> list[bool]:
        # Step 1: Pre-calculate Connected Components
        # Since the array is sorted, node i and node i+1 are connected 
        # IF AND ONLY IF their difference is <= max_diff.
        # This reduces our edge-checking from O(N^2) to O(N).
        
        component_ids = [0] * n
        current_id = 0
        
        for i in range(1, n):
            # Check if the current node is reachable from the previous node
            if nums[i] - nums[i-1] <= max_diff:
                # They belong to the same 'bridge' of connectivity
                component_ids[i] = current_id
            else:
                # The gap is too wide; start a new component
                current_id += 1
                component_ids[i] = current_id
        
        # Step 2: Answer Queries
        # Two nodes have a path if they share the same Component ID.
        results = []
        for u, v in queries:
            # A trivial path always exists if u == v, 
            # but our logic handles this as they'd have the same ID anyway.
            is_connected = (component_ids[u] == component_ids[v])
            results.append(is_connected)
            
        return results

  # follow ups :
"""
1) what is input array is not sorted.
-> First sort and apply above logic to do in O(n* logn) rather than O(n^2).

How to do?
1. If the array isn't sorted, we can't just check neighbors. We would need to sort it first, but we must keep track of original indices.
2. We would create pairs of (value, original_index), sort by value, and then use the same adjacent-check logic to unite original indices in a DSU.

After this apply the same as above.
1. If sorted_nums[i].val - sorted_nums[i-1].val <= maxDiff, they belong to the same component.
2. Assign a component_id to the original index of each number
3. For any query [u, v], if component_ids[u] == component_ids[v], a path exists.

"""
class Solution:
    def existenceQueries(self, n: int, nums: list[int], max_diff: int, queries: list[list[int]]) -> list[bool]:
        # Step 1: Pair each value with its original index
        # This is critical because sorting will shuffle the positions.
        indexed_nums = []
        for i in range(n):
            indexed_nums.append((nums[i], i))
            
        # Step 2: Sort based on the values
        # O(N log N)
        indexed_nums.sort()
        
        # Step 3: Assign Component IDs using a Linear Scan
        # O(N)
        component_ids = [0] * n
        current_id = 0
        
        # The first element in the sorted list starts the first component
        first_val, first_idx = indexed_nums[0]
        component_ids[first_idx] = current_id
        
        for i in range(1, n):
            curr_val, curr_idx = indexed_nums[i]
            prev_val, _ = indexed_nums[i-1]
            
            # If the gap between adjacent values in the sorted list is too large,
            # it's impossible to bridge these two 'islands' of numbers.
            if curr_val - prev_val > max_diff:
                current_id += 1
            
            # Map the component ID back to the ORIGINAL index
            component_ids[curr_idx] = current_id
            
        # Step 4: Process Queries
        # O(Q)
        results = []
        for u, v in queries:
            # Constant time check for connectivity
            results.append(component_ids[u] == component_ids[v])
            
        return resultsclass Solution:
    def existenceQueries(self, n: int, nums: list[int], max_diff: int, queries: list[list[int]]) -> list[bool]:
        # Step 1: Pair each value with its original index
        # This is critical because sorting will shuffle the positions.
        indexed_nums = []
        for i in range(n):
            indexed_nums.append((nums[i], i))
            
        # Step 2: Sort based on the values
        # O(N log N)
        indexed_nums.sort()
        
        # Step 3: Assign Component IDs using a Linear Scan
        # O(N)
        component_ids = [0] * n
        current_id = 0
        
        # The first element in the sorted list starts the first component
        first_val, first_idx = indexed_nums[0]
        component_ids[first_idx] = current_id
        
        for i in range(1, n):
            curr_val, curr_idx = indexed_nums[i]
            prev_val, _ = indexed_nums[i-1]
            
            # If the gap between adjacent values in the sorted list is too large,
            # it's impossible to bridge these two 'islands' of numbers.
            if curr_val - prev_val > max_diff:
                current_id += 1
            
            # Map the component ID back to the ORIGINAL index
            component_ids[curr_idx] = current_id
            
        # Step 4: Process Queries
        # O(Q)
        results = []
        for u, v in queries:
            # Constant time check for connectivity
            results.append(component_ids[u] == component_ids[v])
            
        return results

"""
Follow ups 2:
Q)  "What if maxDiff changes per query?" Each query has its own maxDiff.
The Problem: Each query now looks like [u, v, limit]. You can only use an edge if |nums[i] - nums[j]| <= limit.

Ans: Using 'Offline Queries Technique"
-> Instead of solving queries one-by-one in input order (online), you process them in a smarter order to reduce time complexity.
-> Think of it like this:
Online: Answer each question immediately (no flexibility)
Offline: You collect all questions, rearrange them, and solve cleverly

Q) Why Use Offline Queries?
-> Because many problems become much faster when queries are processed together.
Common benefit: Reduce complexity from O(N × Q) → O((N + Q) log N) or similar

Thought Process & Logic
The Challenge: If we rebuild the DSU for every query, we are back to O(Q * N).
The Repetition: If query A has limit=5 and query B has limit=10, all edges used in A are also valid for B.  We shouldn't "redo" the work for A.
The "Offline" Trick: We sort both the potential edges and the queries by their weight/limit.
    Create all possible adjacent edges: (diff, i, i-1). Sort them by diff.
    Sort queries by their limit.
    Use a pointer to add edges to the DSU only when their diff <= query.limit
    Since the limit only increases, we never have to remove an edge.

Time Complexity: O(N *log N + Q *log Q)
space : O(N + Q)
"""

import math

class DisjointSetUnion:
    """
    A production-grade Disjoint Set Union (DSU) implementation.
    Uses Path Compression and Union by Rank to achieve near O(1) time complexity
    for both 'find' and 'union' operations (Inverse Ackermann complexity).
    """
    def __init__(self, n: int):
        # Every node starts as its own parent (n separate components)
        self.parent = list(range(n))
        # Rank stores the depth of each tree to ensure we attach smaller trees 
        # under larger ones during union, keeping the structure balanced.
        self.rank = [0] * n
    
    def find(self, i: int) -> int:
        """Finds the representative (root) of the set containing element i."""
        if self.parent[i] == i:
            return i
        # PATH COMPRESSION: Recursively points every node in the path to the root.
        # This significantly flattens the tree for future lookups.
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i: int, j: int) -> bool:
        """Merges the sets containing i and j. Returns True if a merge occurred."""
        root_i, root_j = self.find(i), self.find(j)
        
        if root_i != root_j:
            # UNION BY RANK: Always attach the shorter tree to the root of the taller tree.
            if self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            elif self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            else:
                # If ranks are equal, pick one as parent and increment its rank.
                self.parent[root_i] = root_j
                self.rank[root_j] += 1
            return True
        return False

def solve_offline_queries(n: int, nums: list[int], queries: list[list[int]]) -> list[bool]:
    """
    Solves path existence queries where each query has a unique 'maxDiff' limit.
    
    The 'Offline' strategy:
    Instead of rebuilding the graph for every query, we sort queries by their 
    limit and add edges to the DSU incrementally.
    """
    
    # 1. PRE-PROCESSING EDGES
    # Since 'nums' is sorted, any path between u and v must pass through 
    # adjacent neighbors. Thus, we only need to consider edges between (i, i-1).
    edges = []
    for i in range(1, n):
        # Format: (difference_weight, node_u, node_v)
        edges.append((nums[i] - nums[i-1], i, i-1))
    
    # Sort edges by weight so we can add them to DSU in increasing order.
    edges.sort() 

    # 2. PRE-PROCESSING QUERIES
    # We must sort queries by their limit. We store the original index 
    # so we can return the boolean results in the correct order.
    # Format: (limit, start_node, end_node, original_index)
    indexed_queries = []
    for i, (u, v, limit) in enumerate(queries):
        indexed_queries.append((limit, u, v, i))
    
    indexed_queries.sort()

    # 3. CORE LOGIC: INCREMENTAL GRAPH BUILDING
    dsu = DisjointSetUnion(n)
    results = [False] * len(queries)
    edge_ptr = 0 # Pointer to the next available edge in the sorted 'edges' list

    for limit, u, v, original_idx in indexed_queries:
        # Move the edge_ptr forward, adding all edges that satisfy the current limit.
        # Because queries are sorted by limit, edges added for query 'k' 
        # will remain valid for all queries 'k+1, k+2...'.
        while edge_ptr < len(edges) and edges[edge_ptr][0] <= limit:
            _, node_a, node_b = edges[edge_ptr]
            dsu.union(node_a, node_b)
            edge_ptr += 1
        
        # After adding all possible edges for this limit, check if u and v are connected.
        results[original_idx] = (dsu.find(u) == dsu.find(v))
    
    return results

# --- TEST SUITE ---
def test_offline():
    """
    Functional test case based on Example 2 logic.
    n=4, nums=[2, 5, 6, 8]
    Possible edges with diffs: (5-2)=3, (6-5)=1, (8-6)=2
    """
    print("Execution: Testing Offline Queries...")
    
    n, nums = 4, [2, 5, 6, 8]
    # Queries: [node_u, node_v, limit]
    queries = [
        [0, 1, 2], # Requires diff 3, but limit is 2 -> False
        [1, 3, 2], # Path 1-2 (diff 1) and 2-3 (diff 2) are both <= 2 -> True
        [1, 3, 1]  # Path 2-3 requires diff 2, but limit is 1 -> False
    ] 
    
    expected = [False, True, False]
    actual = solve_offline_queries(n, nums, queries)
    
    assert actual == expected, f"Expected {expected}, but got {actual}"
    print("Result: Test Offline Passed!")

if __name__ == "__main__":
    test_offline()


# Follow ups 3:
"""
Q) "What if nodes are points in 2D space?"
|x1 - x2| <= maxDiff and |y1 - y2| <= maxDiff 

Ans : Using 'Fixed-Radius Near Neighbor' Algorithm.

Thought Process & Logic
The Challenge: In 1D, we only check neighbors. In 2D, a point could be "close" to many points in a square region.
The Logic: This is a Fixed-Radius Near Neighbor problem.
    Divide the 2D plane into a Grid where each cell has side length L. 
    For any point in cell (r, c), its neighbors can only exist in the same cell or the 8 adjacent cells.
    Iterate through points, find their cell, and only check the points in the 3 * 3 grid area.

Q) Why 8 neighbors and 3*3 grid area?
The Geometry of the "Search Box":
When you are at a point P in a specific cell, and your connectivity limit is L, any point Q that can connect to you must be within a distance L in both the x and y directions. 
This creates a Search Window of size 2L * 2L centered around P. 
Because each of our grid cells is exactly L * L in size: 
    The Current Cell: A point in the same cell as P could be anywhere from 0 to root(L) distance away. 
    We must check these.
        Direct Neighbors (Up, Down, Left, Right): These cells are immediately adjacent. A point just across the line is only a fraction of L away.
        Diagonal Neighbors: Even at the diagonals, the "corner" of the neighbor cell is exactly root(L) away from the opposite corner of your cell. 
        Since we are checking a square distance |x1-x2| <= L, parts of these diagonal cells fall within that 2L search window.
Visualizing the 3 * 3 Iteration:
In the code, we use two nested loops to generate the relative coordinates of these 8 neighbors plus the center

Time Complexity: O(N * K + Q)
N is the number of points. K is the average number of points in a 3 * 3 grid area. 
In a sparse distribution, K is small (constant). In a very dense distribution where all points are in one spot, it could hit O(N^2).

Space : O(N)
"""

from collections import defaultdict

class DisjointSetUnion:
    """Standard DSU with Path Compression and Union by Rank."""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i, root_j = self.find(i), self.find(j)
        if root_i != root_j:
            if self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            elif self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1

from collections import defaultdict

def solve_2d_connectivity_optimized(n: int, points: list[tuple], L: int, dsu):
    """
    Optimizes the O(N^2) exhaustive search into an O(N) spatial grouping search.
    
    Logic: We use 'Grid Hashing' to bucket points into cells of size L.
    Any two points u, v with |u_x - v_x| <= L and |u_y - v_y| <= L
    must either be in the same grid cell or in adjacent grid cells.
    """
    # grid: Dictionary mapping (cell_x, cell_y) -> List of indices of points in that cell
    grid = defaultdict(list)
    
    # --- STEP 1: BUCKETING (Grouping points into spatial cells) ---
    for i in range(n):
        x, y = points[i]
        # Calculate the cell coordinate by dividing by the side length L.
        # This acts as a 'spatial hash'.
        cell_coords = (x // L, y // L)
        grid[cell_coords].append(i)
    
    # --- STEP 2: PROXIMITY CHECK (Scanning local neighborhoods) ---
    # We iterate over every non-empty cell in our grid hash map.
    for (r, c), nodes_in_cell in grid.items():
        
        # Check the 3x3 grid area centered on the current cell (r, c).
        # dr and dc range from -1 to 1, covering:
        # (-1,-1)  (-1,0)  (-1,1)  <- Top neighbors
        # ( 0,-1)  ( 0,0)  ( 0,1)  <- Middle (0,0 is current cell)
        # ( 1,-1)  ( 1,0)  ( 1,1)  <- Bottom neighbors
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                neighbor_cell = (r + dr, c + dc)
                
                # We only process if the neighbor cell actually contains points.
                # 'u' is a point in our primary cell (r, c).
                 # 'v' is a point in one of the 9 neighboring cells.
                if neighbor_cell in grid:
                    for u in nodes_in_cell:
                        for v in grid[neighbor_cell]:
                            
                            # PERFORMANCE OPTIMIZATION: 
                            # 1. 'u >= v' prevents checking the same pair twice 
                            #    (e.g., avoid checking (u,v) then (v,u)).
                            # 2. 'u == v' prevents comparing a point to itself.
                            if u >= v: 
                                continue 
                            
                            # --- DISTANCE CONSTRAINT CHECK ---
                            # Check if the absolute differences satisfy the 'maxDiff' L.
                            # Points u and v have an edge if they are within the L-box.
                            if abs(points[u][0] - points[v][0]) <= L and \
                               abs(points[u][1] - points[v][1]) <= L:
                                
                                # If they satisfy the condition, they are part of the 
                                # same connected component.
                                dsu.union(u, v)

    # Note: After this loop, we can answer any path query in O(alpha(N)) 
    # using dsu.find(u) == dsu.find(v).
    
    # 3. QUERY PROCESSING: O(Q)
    return [dsu.find(u) == dsu.find(v) for u, v in queries]

# --- TEST CASE ---
def test_2d_logic():
    print("Testing 2D Grid Connectivity...")
    # Points: A(1,1), B(2,2), C(10,10). L = 5
    # A and B are in the same/neighboring cells and |1-2| <= 5.
    # C is very far away.
    points = [(1, 1), (2, 2), (10, 10)]
    L = 5
    queries = [[0, 1], [0, 2]]
    
    result = solve_2d_connectivity(3, points, L, queries)
    assert result == [True, False]
    print("Test Passed!")

test_2d_logic()

# Follow up 4
"""
Q) What if the edges were not based on difference, but node i is connected to j if nums[i] * nums[j] is a perfect square?
"""
