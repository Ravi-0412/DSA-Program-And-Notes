# Method 1: 

"""
Explanation:
a)  binary tree will have exactly one root node i.e only one node will have indegree == 0 i.e root.
b ) from root, all nodes can be traversed exactly once.
c ) all nodes will have indegree exactly equal to 1.
d ) tree should have exactly n-1 edge.

Note: If you will check only these two conditions , will work but only in single component. Won't work in case of more than one component.
a)  There should be one node with in-degree = 0 (root node)
b) All the other nodes should have in-degree = 1 (A node can't have more than one parent)

But we can use this conditions as initial checks. 

Q) when we check the cycle in directed graph, we use two visited set, But here we are using one only. Why?
-> In a general directed graph, you use two sets (or a recursion stack) to distinguish between a Back Edge (a real cycle) 
and a Cross Edge (reaching the same node through a different path).
Here, we use one visited set because a Binary Tree is not allowed to have Cross Edges either.

1. The "Multiple Parents" Rule
In a valid Binary Tree, every node except the root must have exactly one parent.
If you encounter a node that is already in your visited set, it means one of two things:
  A Cycle: You found a path that leads back to an ancestor.
  Multiple Parents: You found a different path leading to a node you already reached.

2. Why we don't need "Path Visited"
In a typical directed graph cycle check (like Task Scheduler or Course Schedule), you need to know if a node is on the current recursion path.
  General Graph: If you hit a visited node not on the current path, it's just a different way to get there (No cycle).
  Binary Tree: If you hit a visited node at all, the structure is already broken because that node now has two incoming edges (two parents).

Space complexity: O(n)
time complexity: O(n+e)
"""

from collections import deque

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]) -> bool:
        # Step 1: Calculate indegree for all nodes
        # This helps us identify the root and ensure no node has multiple parents.
        indegree = [0] * n
        for left, right in zip(leftChild, rightChild):
            if left != -1:
                indegree[left] += 1
                if indegree[left] > 1: return False # A node cannot have 2 parents
            if right != -1:
                indegree[right] += 1
                if indegree[right] > 1: return False # A node cannot have 2 parents

        # Step 2: Find the unique root (node with indegree 0)
        root = -1
        for i in range(n):
            if indegree[i] == 0:
                if root != -1: return False # More than one root
                root = i
        
        # If no node has indegree 0, there is no root (likely a pure cycle)
        if root == -1: return False

        # Step 3: Traverse from the root to ensure all nodes are connected
        # and there are no cycles. 
        visited = set()
        queue = deque([root])
        visited.add(root)

        while queue:
            curr = queue.popleft()
            
            # Check left and right children
            for child in [leftChild[curr], rightChild[curr]]:
                if child != -1:
                    if child in visited:
                        # We already visited this child! This means a cycle or multiple parents.
                        return False
                    visited.add(child)
                    queue.append(child)

        # Step 4: Verify connectivity (All nodes must be reachable from the root)
        return len(visited) == n


# method 2: 
# https://leetcode.com/problems/validate-binary-tree-nodes/solutions/939381/python-clean-bfs-96-faster-timecomplexity-o-n-space-complexity-o-n/?envType=daily-question&envId=2023-10-17
# https://leetcode.com/problems/validate-binary-tree-nodes/solutions/4176803/87-44-easy-soluiton-with-explanation/?envType=daily-question&envId=2023-10-17
