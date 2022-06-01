# just store all the ancestors in an array 
# and compare both the arrays element
# wherever you will find the match that will be the ans

# thsi method not geeting ans on gfgas well as leetcode
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ances_p, ances_q= [], []
        self.Ancestors(root, p, ances_p)
        ances_p.append(p.val)
        print(ances_p)
        self.Ancestors(root, q, ances_q)
        ances_q.append(q.val)
        print(ances_q)
        i, j= 0, min(len(ances_p), len(ances_q))
        print(i,j)
        while i< j:
            if ances_p[i]== ances_q[i]:
                return ances_p[i]      # not returning the value
            i+= 1
        
    
    def Ancestors(self, root,p,ans):
        if root== None: 
            return False
        if root.val== p.val: 
            return True
        if (self.Ancestors(root.left, p, ans) or self.Ancestors(root.right, p, ans)):
            ans.append(root.val)
            return True
        return False


# 2nd method:
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root== None:
            return None
        if root== p or root== q:  # then return that node to the parent
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
        # if both left_search is either None or not None, in both case return the root
        # if both node is not None then that node will be the ans
        # if both node is None then it will forward to the other function 
        return root 
