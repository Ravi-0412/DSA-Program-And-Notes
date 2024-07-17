# Logic: 1) Make adjacency list and add also 'L' /'R'/'U' to 
# identify which path we have taken.

# 2) Apply bfs as usual and taking path parameter also with nodeValue.
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        adj = collections.defaultdict(list)

        def preorder(root):
            if root.left:
                adj[root.val].append([root.left.val, "L"])
                adj[root.left.val].append([root.val, "U"])
                preorder(root.left)
            if root.right:
                adj[root.val].append([root.right.val, "R"])
                adj[root.right.val].append([root.val, "U"])
                preorder(root.right)

        preorder(root)
        
        dq = deque([(startValue, "")])
        visited = set()
        visited.add(startValue)
        while dq:
            node, path = dq.popleft()
            if node == destValue:
                return path
            for nei, dir in adj[node]:
                if nei not in visited:
                    dq.append((nei, path + dir))
                    visited.add(nei)

# later try by 'LCA' also