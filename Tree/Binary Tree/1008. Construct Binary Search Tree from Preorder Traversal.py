# Method 1:
#  just find out the inorder traversal by sorting the array and Apply "convert into binary tree given preorder and inorder"
# of binary tree.
# Time: O(n* logn)

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

# Method 4:

"""
Idea is simple: 
1) First item in preorder list is the root to be considered.
2) For next item in preorder list, there are 2 cases to consider:
2.a) If value is less than last item in stack, it is the left child of last item.
2.b) If value is greater than last item in stack, pop it.
      The last popped item will be the parent and the item will be the right child of the parent.
"""

"""
How to think of this logic?
# Q. How to come up with this logic?
# Ans: Just given the preorder, draw the BST on paper and analyse how you are putting the nodes and 
# which Data Structure we can use to get BST directly from preorder.

# Q. why we are directly adding when num is samller and poping before adding when num is greater?
# Ans: if smaller means that must be the left child of the just previous ele in stack , 
# Because we are doing acc to the preorder and in preorder we will move to left after root and 
# it is BST so smaller ele will be on left.(root, left right,)
# vvi: until we find any ele greater than top of stack, all those num will be go as left child only(like skew tree).
# And we will find any ele greater then we will search for the node to which 'num' will be the right child.  
# (now direction of tree will change).
# i.e we will find the last smaller ele from the current num. 'num' will be the right child of that ele.

# That's why we are using stack.
"""

# Time = space = O(n)

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        for value in preorder[1:]:
            if value < stack[-1].val:
                stack[-1].left = TreeNode(value)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < value:
                    last = stack.pop()
                last.right = TreeNode(value)
                stack.append(last.right)
        return root

# Java
"""
class Solution {
    public TreeNode bstFromPreorder(int[] preorder) {
        if (preorder == null || preorder.length == 0) return null;

        TreeNode root = new TreeNode(preorder[0]);
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);

        for (int i = 1; i < preorder.length; i++) {
            TreeNode node = new TreeNode(preorder[i]);
            if (preorder[i] < stack.peek().val) {
                stack.peek().left = node;
                stack.push(node);
            } else {
                TreeNode last = null;
                while (!stack.isEmpty() && stack.peek().val < preorder[i]) {
                    last = stack.pop();
                }
                last.right = node;
                stack.push(node);
            }
        }

        return root;
    }
}
"""


# Method 5: Optimising space to O(1)
# Time: O(n), space = O(1) 

class Solution:
    def __init__(self):
        self.i = 0

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.build(preorder, float('inf'))

    def build(self, preorder: List[int], bound: int) -> Optional[TreeNode]:
        if self.i == len(preorder) or preorder[self.i] > bound:
            return None
        root = TreeNode(preorder[self.i])
        self.i += 1
        root.left = self.build(preorder, root.val)
        root.right = self.build(preorder, bound)
        return root

# Java
"""
class Solution {
    private int i = 0;

    public TreeNode bstFromPreorder(int[] preorder) {
        return build(preorder, Integer.MAX_VALUE);
    }

    private TreeNode build(int[] preorder, int bound) {
        if (i == preorder.length || preorder[i] > bound) {
            return null;
        }
        TreeNode root = new TreeNode(preorder[i++]);
        root.left = build(preorder, root.val);
        root.right = build(preorder, bound);
        return root;
    }
}
"""
