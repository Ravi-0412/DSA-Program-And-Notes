# method 1:
# just change the pointer for each node going top- bottom.
# Bottom - up will also work.

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        root.left, root.right= root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


# method 2:
# converting the above one into iterative using 'BFS'
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        q= deque([root])
        while q:
            curr= q.popleft()
            curr.left, curr.right= curr.right, curr.left
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return root
