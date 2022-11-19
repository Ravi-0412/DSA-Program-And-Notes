# just saem logic as Q: 105
# only difference in indexing because of working of postorder and inorder together
# time:O(n)
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder:  # means we have not completed the build tree for current subtree
            # find the index of last ele of prerorder in inorder
            ind= inorder.index(postorder[-1])
            # ele at this ind will be as parent for the upcominmg subtree as it is last  node in postorder
            root= TreeNode(inorder[ind])
            
            # all the ele before the indx in inorder will come to the left subtree
            # and all nodes till index 'ind' in postorder will come to the left subtree
            root.left=  self.buildTree(inorder[:ind], postorder[:ind])
            
            # all the ele after the index ind in inorder will come to the right subtree
            # and all from the index 'ind' and excluding the last one in postorder will come to the right subtree
            root.right= self.buildTree(inorder[ind+1:], postorder[ind :-1])  
            return root