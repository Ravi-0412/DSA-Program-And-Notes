"""
Q) "Given a tree with n nodes, identify all current leaves and 'remove' them from the tree, printing their values. 
Repeat this process: in each subsequent step, identify the new leaves created by the previous removals and print them. 
Continue until all nodes have been removed and printed."

Logic : 
1. Start at the edges: Find every node with degree == 1.
2. Cut the branches: Remove those nodes. When you do, the nodes they were attached to "lose" a connection (their degree minus 1).
3. Find new edges: Check if any of those "parent" nodes now have a degree == 1.
4. Repeat: Keep going until no nodes are left.

Time Complexity: O(V+E) = space
"""

from collections import deque, defaultdict

class TreePeeler:
    def solve(self, n, edges):
        # Base cases: No nodes or a single isolated node
        if n <= 0: return []
        if n == 1: return [0]
        
        # 1. Build Adjacency List and Degree Count
        adj = defaultdict(list)
        degree = [0] * n
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
            
        # 2. Find initial leaves
        # In a tree, nodes with degree 1 are the starting perimeter
        queue = deque([i for i in range(n) if degree[i] == 1])
        result = []
        
        # 3. Peeling process
        while queue:
            leaf = queue.popleft()
            result.append(leaf)
            
            for neighbor in adj[leaf]:
                # Decrement neighbor's degree as the current leaf is 'removed'
                degree[neighbor] -= 1
                
                # Once a neighbor's degree hits 1, it becomes a leaf for the next layer
                if degree[neighbor] == 1:
                    queue.append(neighbor)
                    
        return result

# n = 4
# edges = [(0, 1), (1, 2), (1, 3)]

# Follow ups
"""
Q) Given a sequence , check whether that is a valid sequence of removal or not?

Just reverse of above logic

Thought process:
1. Is it currently a leaf? The node being removed must have a degree of 1 (or 0 if it's the very last node) at the moment it is removed.
2. Is the order valid? You can't remove a "parent" node before its "children" (the nodes that make it a leaf) have been removed.

The Logic
    Initialize: Build the degree array and adjacency list exactly like before.
    Iterate: Walk through the user's provided sequence one by one.
    Validate: For each node in the sequence:
        Check if its current degree is ≤1. If it's >1, the sequence is Invalid (you're trying to pull a node from the middle of the tree).
        "Remove" it by decrementing the degrees of all its neighbors.
    Final Check: Ensure the number of nodes in the sequence matches N.

Time = sapce = O(V + E)
"""

from collections import defaultdict

class TreeValidator:
    def is_valid_peeling(self, n, edges, sequence):
        # 1. Basic length check
        if len(sequence) != n:
            return False
        if n == 1:
            return sequence == [0]

        # 2. Build Adjacency List and initial Degrees
        adj = defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1

        # 3. Track removed nodes to avoid processing the same edge twice
        removed = [False] * n

        # 4. Simulate the sequence
        for node in sequence:
            # A node must be a leaf (degree 0 or 1) at the time of removal
            if degree[node] > 1:
                return False # Logic: It's still a hub, not a leaf
            
            removed[node] = True
            
            # "Remove" the node and update neighbors
            for neighbor in adj[node]:
                if not removed[neighbor]:
                    degree[neighbor] -= 1
                    
        return True

# --- Test Case ---
n = 4
edges = [(0, 1), (1, 2), (1, 3)]
# Valid: [0, 2, 3, 1]
# Invalid: [1, 0, 2, 3] (1 has degree 3 at the start)

validator = TreeValidator()
print(f"Is [0, 2, 3, 1] valid? {validator.is_valid_peeling(n, edges, [0, 2, 3, 1])}") 
print(f"Is [1, 0, 2, 3] valid? {validator.is_valid_peeling(n, edges, [1, 0, 2, 3])}")
