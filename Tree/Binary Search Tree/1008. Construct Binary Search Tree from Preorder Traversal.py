# Method1: 
#  just find out the inorder traversal by sorting the array and Apply "convert into binary tree given preorder and inorder".

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder= sorted(preorder)
        return self.buildTree(preorder, inorder)
    
    def buildTree(self, preorder, inorder):
        if not inorder: # or preorder
            return None
        root= TreeNode(preorder[0])   # this will be the root

        # find the index of 1st ele of prerorder in inorder to check all nodes will go the left of parent and right of parent.
        ind= inorder.index(preorder[0])
        # all the ele from index '1' till 'ind' will come to the left in preorder(1st ele already included.) and all the ele before the indx in inorder will come to the left subtree(ind ele already included)
        root.left=  self.buildTree(preorder[1:ind+1], inorder[:ind])
        # all the ele after the indx will come to right of both preorder and inorder.
        root.right= self.buildTree(preorder[ind+1 :], inorder[ind+1 :])                

        return root

# method 2: simply sort and then apply the "convert the given sorted array into Balanced BST".
# time: O(n*logn) for both methods.

# method 3: Take each ele in preorder and apply the normal method to form BST i.e insert node in BST one by one.
# time: O(n*logn).

# method 4: 
# time: O(n)
# Q. How to come up with this logic?
# Ans: Just given the preorder, draw the BST on paper and analyse how you are putting the nodes and 
# which Data Structure we can use to get BST directly from preorder.

# Q. why we are directly adding when num is samller and poping before adding when num is greater?
# Ans: if smaller means that must be the left child of the just previous ele in stack , 
# Because we are doing acc to the preorder and in preorder we will move to left after root and it is BST so smaller ele will be on left.(root, left right,)
# vvi: until we find any ele greater than top of stack, all those num will be go as left child only(like skew tree).
# And we will find any ele greater then we will search for the node to which 'num' will be the right child.  
# (now direction of tree will change).
# i.e we will find the last smaller ele from the current num. 'num' will be the right child of that ele.

# That's why we are using stack.

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root=  TreeNode(preorder[0])  # first ele will be the root only.
        stack= [root]
        for num in preorder[1:]:
            node= TreeNode(num)
            if num < stack[-1].val:  # means num will be the left child
                stack[-1].left= node
            else: # Finding the last smaller ele than 'num' in stack for which 'num' can be the right child.
                #  so pop until you find any greater ele than 'num'.
                while stack and num > stack[-1].val:
                    last= stack.pop()
                # last will be the just smaller than 'num' and num will be the right of 'last' only.
                last.right= node
            stack.append(node)
        return root


