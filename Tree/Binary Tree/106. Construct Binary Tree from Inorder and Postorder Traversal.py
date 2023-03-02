# just saem logic as Q: 105
# only difference in indexing because of working of postorder and inorder together
# time:O(n)
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder: return None
        root= TreeNode(postorder[-1])   # this will the parent for the cur subtree.
        # now find its child i.e which all nodes will come to the left and right.
        # find the index of last ele of postorder in inorder
        ind= inorder.index(postorder[-1])  
        
        # all the ele before the indx in inorder will come to the left subtree.
        # and all nodes till index 'ind' in postorder will come to the left subtree
        root.left=  self.buildTree(inorder[:ind], postorder[:ind])
        
        # all the ele after the index ind in inorder will come to the right subtree
        # and all from the index 'ind' and excluding the last one in postorder will come to the right subtree
        root.right= self.buildTree(inorder[ind+1:], postorder[ind :-1])  
        return root
    