def TotalNodes(self, root):
         # just do any traversal and count
        # count= 0
        # if root== None:
        #     return 0
        # count+= 1
        # smallAns= self.TotalNodes(root.left)
        # count+= smallAns
        # smallAns1= self.TotalNodes(root.right)
        # count+= smallAns1
        # return count

        # concise way of writing
        if root== None:
            return 0
        return 1+ self.TotalNodes(root.left) + self.TotalNodes(root.right)
    # Later try by iterative way


def LeafNode(self, root):
    # count= 0
    # if root== None:
    #     return 0
    # if root.left== None and root.right== None:
    #     return 1
    # smallAns= self.LeafNode(root.left)
    # smallAns1= self.LeafNode(root.right)
    # count+= smallAns + smallAns1
    # return count
    # concise way
    count= 0
    if root== None:
        return 0
    if root.left== None and root.right== None:
        return 1
    return self.LeafNode(root.left) + self.LeafNode(root.right)
        # Later try by iterative way

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

