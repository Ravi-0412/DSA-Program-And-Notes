# logic came as very first only but was not able to code
# very concise and to the point but will take O(n^2), due to pop operation each time
# write the l;ogic in notes
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:  # means we have not completed the build tree for current subtree
            # find the index of 1st ele of prerorder in inorder
            ind= inorder.index(preorder.pop(0))
            # ele at this ind will be as parent for the upcominmg subtree as it is 1st node in preorder
            root= TreeNode(inorder[ind])

            # all the ele before the indx in inorder will come to the left subtree, and ele till this ind will come first in preorder
            root.left=  self.buildTree(preorder, inorder[:ind])
            # all the ele after the indx in inorder will come to the right subtree, and ele after the 'ind' will come on the right in prorder 
            # root.right= self.buildTree(preorder[ind+1 :], inorder[ind+1 :])    # writing like this will give error as preorder array is changing regulary

            root.right= self.buildTree(preorder, inorder[ind+1 :])               # automatically it will start from the ind as 
                                                # after doing all the operations on left side preorder will be left with ele of right part only
            return root

# same logic, just replaced the pop operation with slicing
# now time: O(n)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:  
            # find the index of 1st ele of prerorder in inorder
            ind= inorder.index(preorder[0])
            # ele at this ind will be as parent for the upcominmg subtree as it is 1st node in preorder
            root= TreeNode(inorder[ind])
            # all the ele before the indx in inorder will come to the left subtree, 
            root.left=  self.buildTree(preorder[1:ind+1], inorder[:ind])
            # all the ele after the indx in inorder will come to the right subtree, and this ele will come after the ind in prorder
            # root.right= self.buildTree(preorder[ind+1 :], inorder[ind+1 :])    
            root.right= self.buildTree(preorder[ind+1:], inorder[ind+1 :])             
                                                                               
            return root

# more readable way of above code, totally same logic
# time: O(n). Here taking help of indexing instead of pop operation
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if len(inorder)==0:
            return None
        
        root_val = preorder[0]
        root_inorder_index = inorder.index(root_val)
        
        root = TreeNode(root_val)
        inorder_left = inorder[:root_inorder_index]
        inorder_right = inorder[root_inorder_index+1:]
        preorder_left = preorder[1:root_inorder_index+1]
        preorder_right = preorder[root_inorder_index+1:]
        
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        
        return root
