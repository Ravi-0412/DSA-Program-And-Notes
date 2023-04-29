# very easy and good Q.

# How we can get the new node val?
# new_node_val= sum(level) - node.val- val_direct_sibling.

# so first we have to find the sum of nodes val at each level.
# we can use either bfs or dfs. DFS is more simple and concise

# Then for updating the  value we will run dfs , but in this we also need to keep track of sibling_val
# so in this we will pass one more parameter 'siblingVal'.

# for left child, siblingVal= right child val if not None else '0'.
# for right child, siblingVal= left child val if not None else '0'.

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levelSum= collections.defaultdict(int)

        # One dfs to calculate sum at each level(depth)
        def dfs1(node, depth):
            if not node:
                return
            levelSum[depth]+= node.val
            dfs1(node.left, depth + 1)
            dfs1(node.right, depth + 1)
        
        # now run another dfs to replace nodes
        def dfs2(node, siblingVal, depth):
            if not node:
                return
            node.val= levelSum[depth] - node.val- siblingVal
            leftVal= node.left.val if node.left else 0
            rightVal= node.right.val if node.right else 0
            dfs2(node.left, rightVal, depth +1)
            dfs2(node.right, leftVal, depth +1)
        
        dfs1(root, 0)  # for getting the sum of node value at each depth(level)
        dfs2(root, 0, 0)  # intially sibling val will be zero.

        return root