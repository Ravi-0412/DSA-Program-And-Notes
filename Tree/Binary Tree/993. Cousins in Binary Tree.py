# method 1: using bfs.
# logic : cousins must be at same level .
# so we can apply level order traversal (multisource bfs) or simple bfs with (depth, parent) also in queue
# when we find any node we will store (depth, parent) in ans.
# ans will have two ele one for 'x' and one for 'y'.
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        ans= []
        q= collections.deque()
        q.append((root, 0, None))   # [(node, depth, parent)]
        while q:
            node, depth, parent= q.popleft()
            if node.val== x or node.val== y:
                ans.append([depth, parent])
            if node.left:
                q.append((node.left, depth +1, node))
            if node.right:
                q.append((node.right, depth +1, node))
        # check for cousins
        return ans[0][0]== ans[1][0] and ans[0][1] != ans[1][1]
    

# method 2: Using Dfs (will try later).
# links in sheet.