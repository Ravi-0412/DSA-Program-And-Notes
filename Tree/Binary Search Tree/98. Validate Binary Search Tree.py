# method 1: 
# just store the inorder traversal in the array and check if this array is sorted or not if sorted then BST else NOT.
# time = space = O(n)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder_vals = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            inorder_vals.append(node.val)
            inorder(node.right)

        inorder(root)

        # Check if the inorder list is strictly increasing
        for i in range(1, len(inorder_vals)):
            if inorder_vals[i] <= inorder_vals[i - 1]:
                return False

        return True


# Method 2: 
# Optimised logic of above logic.
# Time = O(n), space = O(1)
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

# Method 3: 

# my mistakes 
# 1) i am checking Top To Down
# comparing the root value with its adjacent left and right node only
# but these left subtree can contain value greater than root val and similarly right subtree can contain value lesser than root val
# and in these cases also it will give True since we are comparing only adjacent left and right node.

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root== None or (root.left== None and root.right== None):
            return True
        l,r= True,True
        if root.left:
            l= root.val > root.left.val and self.isValidBST(root.left)
        if root.right:
            r= root.right.val > root.val and self.isValidBST(root.right)
        return l and r


# 2) even if you do the bottom up same thing will happen. WIll give wrong only
# e.g: root = [5,4,6,null,null,3,7], exepected = False
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

# Correct solution : Method 3
# Top - Down
# i) Store the minimum and maximum seen till now.
# ii) If at any node if you see ki: current node ka value 'minimum' se bhi chota h ya 'maximum' se bhi bda h.
# Then it means kahin na kahin current tak aane me bst rule follow nhi hua h.
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


# Method 4: 
# Bottom -up
# Logic: 1) Store minimum and maximum for each node.
# 2) At any node if current node value is <= maximum_val from left subtree or >= minimum_value from right subtree
# Then it Bst is not valid from this node.

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ans = True

        def check(root):
            if not root:
                return [float('inf'), float('-inf')]  # [minimum, maximum]. For base case return such value which will be valid always
            min1, max1 = check(root.left)
            min2, max2 = check(root.right)
            if root.val <= max1 or root.val >= min2:
                self.ans = False
            return [min(min1, root.val), max(root.val, max2)]

        check(root)
        return self.ans
    
# Related Q:
# 1) 1373. Maximum Sum BST in Binary Tree
# It is based exactly on 'method 3' of this question.

