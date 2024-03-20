# method 1: just store the inorder traversal in the array and check if this array is sorted or not
# if sorted then BST else NOT



# my mistake , i am checking Top To Down
# comparing the root value with its adjacent left and right node only
# but these left subtree can contain vale greater than root val and similarly right subtree can contain value lesser than root val
# and in these cases also it will give True since we are comparing only adjacent left and right node

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root== None or (root.left== None and root.right== None):
            return True
        l,r= True,True
        if root.left:
            l= root.val> root.left.val and self.isValidBST(root.left)
        if root.right:
            r= root.right.val> root.val and self.isValidBST(root.right)
        return l and r


# even if you do the bottom up same thing will happen
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root== None or (root.left== None and root.right== None):
            return True
        l, r= True, True
        if root.left:
            l= self.isValidBST(root.left)
        if root.right:
            r= self.isValidBST(root.right)
        ans= True
        if root.left:
            ans= l and root.val > root.left.val
        if root.right:
            ans= r and root.val< root.right.val
        return ans


# Just logic of method1 in o(1) space.
# Just compare cur ele with prev one to check if elements are in strictly sorted order or not. 
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root== None:
            return 
        stack, ans= [], []
        pre= None
        while stack or root:
            while root:
                stack.append(root)
                root= root.left
            # if None, it means no left child then print the stack top and append the 'poped.right'
            # it means we have reached the leftmost node 
            curr= stack.pop()
            if pre and curr.val<= pre.val:  # means ele are not in ascending order in inorder traversal so return False
                return False
            pre= curr
            ans.append(curr.val)
            root= curr.right
        # it means all element are in sorted order in case of inorder traversal
        return True  


# Method 2: 
# better one and new logic
# Time: O(n)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check(root, min, max):
            if not root:
                return True
            if root.val <= min or root.val >= max:
                return False
            # for left: Now max will be root.val and min will be same
            # for right: min will be root.val and max will be same
            return check(root.left, min, root.val) and check(root.right, root.val, max)

        return check(root, float('-inf'), float('inf'))    # (root, minimum_for_that_path, maximum_for_that_path)