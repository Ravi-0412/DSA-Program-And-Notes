# just the same logic as method 2 Q" path from root to node"
# only differnec here is we don't have to stop after finding any leaf node
# we have to continue our search i.e we have to visit every node

# this will return the ans in the form list[list]
# when we have to traverse then doesn't return aby value like integer or boolean , just simply write 'return'

# logic: after you see any node, add them into path
# when you find any leaf node add the path into the ans and delete the last added in path(this will delete the left or right child which is root)
# now traverse to other child and 
# after you have visited both the child then simply pop the curr root as this root can't be part of our ans for next root 
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans,path= [], []
        self.helper(root, path, ans)
        return ans
    
    def helper(self,root, path, ans):  
        if root== None:
            return 
        path.append(root.val)
        if root.left== None and root.right==None:
            ans.append(path.copy())
            path.pop()
            return 
        self.helper(root.left, path, ans)
        self.helper(root.right, path, ans)
        path.pop()


# this will print in leetcode format
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

# better one
# instead of storing the paths in list, we can store in string then we don't have to use backtracking
# as string doesn't get modified automatically like list
# this approach make the q easier one
class Solution:
    def binaryTreePaths(self, root):
        res = []
        self.rec(root,"",res)
        return res
    def rec(self,node,ls,res):
            if not node:
                return
            ls+=str(node.val)
            if not node.left and not node.right:
                res.append(ls)
            self.rec(node.left,ls+"->",res)
            self.rec(node.right,ls+"->",res)