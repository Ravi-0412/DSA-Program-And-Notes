# just the same logic as method 2 Q" path from root to node"
# only differnec here is we don't have to stop after finding any leaf node
# we have to continue our search i.e we have to visit every node

# Method 1: 
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans,path= [], []
        self.helper(root, path, ans)
        return ans
    
    def helper(self,root, path, ans):  
        if root== None:
            return 
        path.append(root.val)  # simply add the node you visit
        if root.left== None and root.right==None:
            ans.append("->".join(str(e) for e in path))
            path.pop()  # pop the last added one 
            return 
        self.helper(root.left, path, ans)
        self.helper(root.right, path, ans)
        path.pop()   # after you have visited both left and right child then pop the curr ele
        # since no path to leaf can go via this node


# Method 2:
# Best one: Store path in string

class Solution:
    def binaryTreePaths(self, root):

        def dfs(node, path):
            if not node:
                return
            if not node.left and not node.right:
                res.append(path + str(node.val))
                return
            dfs(node.left, path + str(node.val) + "->")
            dfs(node.right,path + str(node.val) + "->")

        res = []
        dfs(root,"")
        return res
    
    