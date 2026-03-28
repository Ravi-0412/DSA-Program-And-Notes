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
-> Thought Process & Logic
The Math: A product a * b is a perfect square if and only if a and b have the same square-free part.
Example: 12 = 2^2 * 3. Square-free part is 3.
Example: 27 = 3^2 * 3. Square-free part is 3.
12 * 27 = 324 = 18^2. 

The Logic: 
1. For every number in nums, simplify it by dividing out all perfect square factors (4, 9, 16...).
2. All numbers that result in the same "core" (square-free part) are automatically connected.
3. Group them using a Hash Map and Union them in DSU.

Time : O(N * root(M) + Q* alpha(N)), where root(M) is the time to find the core for each number where M is the maximum value in nums. 
Space : O(N)
"""

class DisjointSetUnion:
    """Standard DSU with Path Compression and Union by Rank."""
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int):
        root_i, root_j = self.find(i), self.find(j)
        if root_i != root_j:
            if self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            elif self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1

def get_square_free_core(n: int) -> int:
    """
    Reduces a number to its 'square-free' part by removing all factor pairs.
    Example: 12 (2*2*3) -> 3
             20 (2*2*5) -> 5
             18 (2*3*3) -> 2
    """
    if n == 0: return 0
    res = 1
    d = 2
    temp = n
    
    # Standard prime factorization up to sqrt(n)
    while d * d <= temp:
        count = 0
        while temp % d == 0:
            count += 1
            temp //= d
        
        # If the prime 'd' appears an odd number of times, 
        # it must be part of the square-free core.
        if count % 2 == 1:
            res *= d
        d += 1
        
    # If temp > 1, the remaining temp is a prime with exponent 1
    if temp > 1:
        res *= temp
        
    return res

def solve_square_product_queries(n: int, nums: list[int], queries: list[list[int]]) -> list[bool]:
    """
    Determines if two indices u and v are connected by a path where every edge (i, j) 
    satisfies: nums[i] * nums[j] is a perfect square.
    """
    dsu = DisjointSetUnion(n)
    
    # core_map stores: {square_free_core: first_index_with_this_core}
    core_map = {} 
    
    for i, val in enumerate(nums):
        # 1. Simplify the number to its fundamental 'core'
        core = get_square_free_core(val)
        
        # 2. If we've seen this core before, these two numbers 
        # multiply to a perfect square. Connect them in DSU.
        if core in core_map:
            dsu.union(i, core_map[core])
        else:
            # First time seeing this core; mark this index as the representative
            core_map[core] = i
            
    # 3. Answer queries by checking if u and v are in the same component
    return [dsu.find(u) == dsu.find(v) for u, v in queries]

# --- TEST SUITE ---
def test_square_logic():
    print("Testing Perfect Square Connectivity...")
    
    # Numbers: 12 (core 3), 27 (core 3), 5 (core 5), 20 (core 5), 7 (core 7)
    # Groups: {0, 1}, {2, 3}, {4}
    nums = [12, 27, 5, 20, 7]
    n = len(nums)
    
    queries = [
        [0, 1], # 12 * 27 = 324 (18^2) -> True
        [2, 3], # 5 * 20 = 100 (10^2)   -> True
        [0, 2], # 12 * 5 = 60 (Not sq)  -> False
        [1, 4]  # 27 * 7 = 189 (Not sq) -> False
    ]
    
    expected = [True, True, False, False]
    actual = solve_square_product_queries(n, nums, queries)
    
    assert actual == expected, f"Expected {expected}, but got {actual}"
    print("Result: Test Passed!")

if __name__ == "__main__":
    test_square_logic()

# Follow up 5
"""
Q) for follow up 4,  "What if the numbers are up to 10^7?"
-> The O(sqrtM) factorization becomes slow if you have 10^5 such numbers.
Optimization: Use a Sieve of Eratosthenes (specifically a "Smallest Prime Factor" or SPF sieve) once at the start, 
for every number up to the maximum value M.

The sieve takes O(M *log log M).
Factorization then becomes O(log M) for every number.

Logic:
A. The Sieve (Pre-calculation):
We create an array spf where spf[i] stores the smallest prime that divides i.
1. Assume every number i is prime. Initialize spf[i] = i.
2. Handle the Evens: spf[i] = 2
For every even number, set spf[i] = 2.
-> Every even number (greater than 2) is divisible by 2. Since 2 is the smallest prime, it will always be the Smallest Prime Factor for any even number.
Instead of checking these later, we "pre-fill" them: spf[4]=2, spf[6]=2, spf[8]=2...
This cuts our remaining work in half.
3. The Odd Sieve: i = 3, 5, 7...
For every odd number i starting from 3, if it's still i 
If it is, it means no smaller prime (like 3 or 5) has visited this number yet => it must be prime.

iterate through its multiples j = i * i, i*(i+2), ..... and set spf[j] = i (if not already set).
Why ?
Once we confirm i is prime, we mark all of its multiples.
Why start at i * i? Any multiple smaller than i * i (like i * 2 or i * 3) would have already been marked by a smaller prime (2 or 3). 
Starting at i^2 is a massive speed boost. 
Why i * (i+2)? => We skip i * (i+1) because if i is odd, i+1 is even. An "odd times even" number is even, and we already handled all evens in Step 2. We only care about odd multiples.

B. Fast Factorization:
To find the square-free core of a number n:
    Look up p = spf[n].
    Count how many times p divides n.
    If the count is odd, multiply our core by p.
    Repeat with n = n // (p^count) until n = 1.

VVI:  The "If not already set" Rule
This is the most critical part of the SPF logic.
Let's look at the number 15.
When we sieve for 3, we hit 15 and set spf[15] = 3.
When we sieve for 5, we hit 15 again. But we do not overwrite it.
Because 3 is smaller than 5, we keep spf[15] = 3.

Why this makes Factorization O(log n) ?
-> Why this makes Factorization O(log n) 
Because you have the "Smallest" factor, you can decompose a number like a ladder.
Example: Factorizing 120
Check spf[120]: It's 2. (120 / 2 = 60)
Check spf[60]: It's 2. (60 / 2 = 30)
Check spf[30]: It's 2. (30 / 2 = 15)
Check spf[15]: It's 3. (15 / 3 = 5)
Check spf[5]: It's 5. (5 / 5 = 1)
Result: 2 * 2 * 2 * 3 * 5. 
In the standard way, you would have to try dividing by 2, 3, 5, 7, 11... manually. 
With the SPF sieve, you instantly know the next divisor, making it extremely fast for large datasets.
"""

class DisjointSetUnion:
    """
    Manages connectivity components using Disjoint Set Union (DSU).
    Optimized with:
    1. Path Compression: Flattens the tree during find() for near O(1) lookups.
    2. Union by Rank: Keeps the tree balanced by attaching smaller trees to larger ones.
    """
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i: int) -> int:
        """Finds the root of the component containing i with path compression."""
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int):
        """Merges two components if they are not already connected."""
        root_i, root_j = self.find(i), self.find(j)
        if root_i != root_j:
            # Union by Rank: Attach shorter tree to taller tree
            if self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            elif self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1

class SquareProductSolver:
    """
    Solves path existence queries where edges exist between nodes if their 
    product is a perfect square.
    
    Mathematical Insight: 
    A * B = Square IFF they share the same 'square-free core'.
    The core is the product of prime factors that appear an odd number of times.
    Example: 12 (2^2 * 3) -> Core 3 | 27 (3^3) -> Core 3.
    """
    def __init__(self, max_val: int):
        # Pre-computing Smallest Prime Factor (SPF) allows O(log N) factorization.
        # This is essential when many large numbers need to be factorized.
        self.spf = self._precompute_spf(max_val)

    def _precompute_spf(self, limit: int) -> list[int]:
        """
        Sieve of Eratosthenes variant to pre-calculate the Smallest Prime Factor.
        Time: O(M log log M) | Space: O(M)
        """
        spf = list(range(limit + 1))
        
        # Optimization: Handle even numbers separately
        for i in range(4, limit + 1, 2):
            spf[i] = 2
            
        # Standard sieve loop up to sqrt(limit)
        for i in range(3, int(limit**0.5) + 1, 2):
            if spf[i] == i:  # i is prime
                # Mark all odd multiples of i starting from i*i
                for j in range(i * i, limit + 1, i * 2):
                    if spf[j] == j:
                        spf[j] = i
        return spf

    def get_square_free_core(self, n: int) -> int:
        """
        Calculates the product of prime factors with odd exponents.
        Time: O(log N) due to SPF-based prime jumping.
        """
        if n == 0: return 0
        core = 1
        
        while n > 1:
            p = self.spf[n]
            count = 0
            # Extract current smallest prime factor entirely
            while n % p == 0:
                count += 1
                n //= p
            
            # If the prime factor appears an odd number of times, it is 
            # part of the square-free representative.
            if count % 2 == 1:
                core *= p
        return core

    def solve(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        """
        Groups indices by their square-free cores and answers connectivity queries.
        Time: O(N log M + Q) | Space: O(M + N)
        """
        n = len(nums)
        dsu = DisjointSetUnion(n)
        
        # Mapping: square_free_core -> first_index_seen_with_this_core
        # All indices sharing a core belong to the same connected component.
        core_map = {}

        for i, val in enumerate(nums):
            core = self.get_square_free_core(val)
            if core in core_map:
                # Union the current index with the representative of this core
                dsu.union(i, core_map[core])
            else:
                core_map[core] = i

        # A path exists if nodes share the same root in DSU
        return [dsu.find(u) == dsu.find(v) for u, v in queries]

# --- TEST SUITE ---
def test_spf_logic():
    """
    Validates logic with various numeric properties:
    - 12 and 27: (2^2 * 3) and (3^3) both simplify to Core 3.
    - 8 and 18: (2^3) and (2 * 3^2) both simplify to Core 2.
    - 5: Simplifies to Core 5.
    """
    print("Execution: Testing SPF Sieve + Perfect Square connectivity...")
    
    # Initialize solver with maximum possible value in nums
    solver = SquareProductSolver(max_val=100)
    
    nums = [12, 27, 8, 18, 5]
    queries = [
        [0, 1], # 12 * 27 = 324 (18^2) -> Expected: True
        [2, 3], # 8 * 18 = 144 (12^2)  -> Expected: True
        [0, 2], # 12 * 8 = 96 (Not sq)  -> Expected: False
        [4, 0]  # 5 * 12 = 60 (Not sq)  -> Expected: False
    ]
    
    results = solver.solve(nums, queries)
    expected = [True, True, False, False]
    
    assert results == expected, f"Assertion Failed: Expected {expected}, got {results}"
    print("Result: All Test Cases Passed Successfully!")

if __name__ == "__main__":
    test_spf_logic()


# Follow up 6:
"""
3534. Path Existence Queries in a Graph II
"""
