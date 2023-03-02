
# time: O(n)
# just do on pen and paper for visualisation like how slicing is doing perfect work.
# same logic as we used to do in GATE exam i.e:
# Preorder will decide the which ele will be the parent of the upcoming tree.
# preorder[0] will be the parent always.
# inorder will decide the which ele will go the left and right of the parent.
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:  # or 'if preorder'
            root= TreeNode(preorder[0])   # this will be the root

            # find the index of 1st ele of prerorder in inorder to check all nodes will go the left of parent and right of parent.
            ind= inorder.index(preorder[0])
            # all the ele from index '1' till 'ind' will come to the left in preorder(1st ele already included.) and all the ele before the indx in inorder will come to the left subtree(ind ele already included)
            root.left=  self.buildTree(preorder[1:ind+1], inorder[:ind])
            # all the ele after the indx will come to right of both preorder and inorder.
            root.right= self.buildTree(preorder[ind+1 :], inorder[ind+1 :])                

            return root


# more readable way of above code, totally same logic
# time: O(n).
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if len(inorder)==0:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        root_inorder_index = inorder.index(root_val)
        
        preorder_left = preorder[1:root_inorder_index+1]
        inorder_left = inorder[:root_inorder_index]
        preorder_right = preorder[root_inorder_index+1:]
        inorder_right = inorder[root_inorder_index+1:]
        
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        
        return root
