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
Q) 
"""

