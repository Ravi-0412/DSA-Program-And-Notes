# just apply the formula if tree is fully complete otherwise go on finding the fully complete tree further. 
# my mistke: was coming into mind to something like this but didn't came fully, should have thought litle more.
# time complexity= O(logn* logn). in worst case we have to traverse logn times
# (as other side if found full complete binary tree then no need to check further) 
# and each time we have to find the height and this will take logn times so time: O(logn*logn).

# for checking a Full Binary Tree:
# calculate the height on both the left and right side by only going only left and right respectively.
# if both left and right height equal then means that subtree is a full binary Tree else not
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root== None:
            return 0
        l= self.FindLeftHeight(root)
        r= self.FindRightHeight(root)
        if l== r:  # means from root tree is fully complete so we can directly apply the formula and return from here no need to check further
            return (1<< l) -1   # root is also included in calculating height(height of one node=1), so this formula will be valid
        return 1+ self.countNodes(root.left) + self.countNodes(root.right)
    
    def FindLeftHeight(self, root):  # only you have to go left 
        curr,height= root, 0
        while curr:
            height+= 1
            curr= curr.left
        return height
    
    def FindRightHeight(self, root): # only you have to go right
        curr,height= root, 0
        while curr:
            height+= 1
            curr= curr.right
        return height
        