# method 1: 
# Brute force
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        inorder = [0]*101  # if 'num' is present in bst then inorder[num] = num

        def findInorder(root):
            if not root:
                return 0
            inorder[root.val] = root.val
            findInorder(root.left)
            findInorder(root.right)

        def update(root):
            if not root:
                return 
            root.val = inorder[root.val]    # this will be new value
            update(root.left)
            update(root.right)

        findInorder(root)

        for i in range(99, -1, -1):
            inorder[i] = inorder[i] + inorder[i + 1]
        # after this inorder[i] = sum from 'i' to last index.
        # now update the value of all nodes
        update(root)
        return root

# method 2:

# logic: We need to do the work from biggest to smallest, right to left.
# pre(value) will record the previous value the we get, which the total sum of bigger values.
# For each node, we update root.val with root.val + pre.

# time: O(n)
# space: O(height)

class Solution:
    value = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root.right: 
            self.bstToGst(root.right)
        root.val = self.value = root.val + self.value
        if root.left:
            self.bstToGst(root.left)
        return root

# Method 3: 
# Other way to write method 2
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node, rightSum):
            if not node: return rightSum
            rightSum = dfs(node.right, rightSum)
            node.val += rightSum
            return dfs(node.left, node.val)
        dfs(root, 0)
        return root


# same question
# 1) 538. Convert BST to Greater Tree
