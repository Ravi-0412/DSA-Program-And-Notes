# logic: just find the sum of left subtree height and right subtree height of all nodes
# max of all will be your ans and this will be maximum only between two leaves
# see: the solution on gfg brute force (same logic)
# so another way of asking this Q can be " longest path between any two leaves"

# optimised way ,O(n)
# bottom up approach.
# we can traverse recursively and store the final ans in same function as height and final ans will differ that's why made another fn
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans= [0]
        def Height(root):   # just the logic of height only
            if root== None:
                return 0
            left= Height(root.left)
            right= Height(root.right)
            ans[0]= max(ans[0],left+ right)
            return 1+ max(left,right)
        
        # read from here    
        Height(root)
        return ans[0]

