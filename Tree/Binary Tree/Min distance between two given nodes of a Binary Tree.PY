# could have come through this logic,if have thought little more, just the very simple logic only
# how lowest common ancestor will come into mind: here both the nodes can be on diff side of tree and there is no way we can reach one to another directly
# but somehow we have to connect both the nodes and till now what we done the only thing comes into mid for nodes present in diff side of tree is "LCA"

# Dist(n1, n2) = Dist(root, n1) + Dist(root, n2) - 2*Dist(root, lca) 
# 'n1' and 'n2' are the two given keys
# 'root' is root of given Binary Tree.
# 'lca' is lowest common ancestor of n1 and n2
# Dist(n1, n2) is the distance between n1 and n2.

# time: O(n)
class Solution:
    def findDist(self,root,a,b):     # 'a' and 'b' are given as value
        dist_a, dist_b, dist_lca= [0], [0], [0]
        self.FindDistance(root, a, dist_a)              # find the distance of 1st node from the root
        self.FindDistance(root, b, dist_b)              # find the distance of 2nd node from the root
        lca= self.lowestCommonAncestor(root,a,b)        # find the lowest common ancesstor of 'a' and 'b'
        self.FindDistance(root, lca.data, dist_lca)     # find the distance of lowest common ancesstor of 'a' and 'b' from the root
        # print(dist_a[0]-1, dist_b[0]-1, lca.data, dist_lca[0]-1)
        return ((dist_a[0]-1) + (dist_b[0]-1)) - 2*(dist_lca[0]-1)   # here formula only
        
        
    def FindDistance(self,root,key,ans):  
        if root== None:
            return 0
        ans[0]+= 1  # simply add the node you visit
        if root.data== key:
            return ans[0]
        if self.FindDistance(root.left,key,ans) or self.FindDistance(root.right,key,ans):  # means key has path from the given root
            return ans[0]
        # if key has not path from the curr root(neither left nor right return True) then pop root from the ans and return False
        ans[0]-= 1
        return 0
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root== None:
            return None
        if root.data== p or root.data== q:  # then return that node to the parent
            return root
        # if not equal to the nodes value then search on both left and right side
        left_search=  self.lowestCommonAncestor(root.left, p , q)
        right_search= self.lowestCommonAncestor(root.right, p , q)
        # if left_search is None and right is not None  at last then right subtree conatins both the nodes
        if left_search== None:
            return right_search
        # if left_search is not None and right is  None  at last then left subtree conatins both the nodes
        if right_search== None:
            return left_search
        # if both is None None then that None will be automatically get returned in any of the above if condition
        
        # so now condition left is both left_search and right_search is not None, an if both is not none then it means
        # both node 'p' and 'q' have path from this node 
        # i.e we have found the ans so simply return the node
        return root 


# Method 2: better solution
# first find the LCA of two nodes. Then we find the distance from two nodes from LCA
# for this make LCA as root for finding the distance of both the nodes from LCA


# method 3: in one pass (GFG method 3)
# since we are finding the lca and during finding lca we will automatically find the two given nodes also
# so that time we can calculate the distance of both the nodes.
# and when we will find the LCA, we will simply return the sum of distance of both the nodes(since distance and lca will bottom up only)
# Do this by later (VVI)