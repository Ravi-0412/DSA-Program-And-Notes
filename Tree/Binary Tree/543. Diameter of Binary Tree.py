# logic: just find the sum of left subtree height and right subtree height of all nodes
# max of all will be your ans and this will be maximum only between two leaves
# so another way of asking this Q can be " longest path between any two leaves"

# optimised way ,O(n)
# bottom up approach, 
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans= [0]
        def Diameter(root):   # just the logic of height only
            if root== None:
                return 0
            left= Diameter(root.left)
            right= Diameter(root.right)
            ans[0]= max(ans[0],left+ right)
            return 1+ max(left,right)
        
        # read from here    
        Diameter(root)
        return ans[0]

