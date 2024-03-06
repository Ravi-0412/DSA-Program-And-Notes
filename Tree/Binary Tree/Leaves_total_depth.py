# 1) Total nodes

def TotalNodes(self, root):
        if root== None:
            return 0
        return 1+ self.TotalNodes(root.left) + self.TotalNodes(root.right)

# Later try by iterative way

# 2) Leaf Nodes
def LeafNode(self, root):
    if root== None:
        return 0
    if root.left== None and root.right== None:
        return 1
    return self.LeafNode(root.left) + self.LeafNode(root.right)
        # Later try by iterative way

# 3) Depth / Height
def Depth(self,root):
    if root== None:
        return 0
    return 1 + max(self.Depth(root.left), self.Depth(root.right))

# max depth that submitted on leetcode
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root== None:
            return 0
        l= self.maxDepth(root.left)
        r= self.maxDepth(root.right)
        return 1+ max(l,r)

