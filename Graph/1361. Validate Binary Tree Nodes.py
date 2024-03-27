# Method 1: 

# Explanation:
# a)  binary tree will have exactly one root node i.e only one node will have indegree == 0 i.e root.
# b ) from root, all nodes can be traversed exactly once.
# c ) all nodes will have indegree exactly equal to 1.
# d ) tree should have exactly n-1 edge.
# Space complexity: O(n)
# time complexity: O(n+e)

# Note: If you will check only these two conditions
# a)  There should be one node with in-degree = 0
# b) All the other nodes should have in-degree =1

# Won't work in case of more than one component.

# Note: Checking for no cycle and single component will wrong ans because
# in this one node can more than two children.


# method 2: 
# https://leetcode.com/problems/validate-binary-tree-nodes/solutions/939381/python-clean-bfs-96-faster-timecomplexity-o-n-space-complexity-o-n/?envType=daily-question&envId=2023-10-17
# https://leetcode.com/problems/validate-binary-tree-nodes/solutions/4176803/87-44-easy-soluiton-with-explanation/?envType=daily-question&envId=2023-10-17
