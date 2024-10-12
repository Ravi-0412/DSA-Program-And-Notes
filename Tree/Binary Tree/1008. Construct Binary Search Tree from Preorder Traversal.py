# just sort the array to get the inorder and then apply the same logic as binary Tree.
# Time: O(n* logn)

# Method 2:
# Time = O(n), space = O(1)

"""
Idea is simple: 
1) First item in preorder list is the root to be considered.
2) For next item in preorder list, there are 2 cases to consider:
2.a) If value is less than last item in stack, it is the left child of last item.
2.b) If value is greater than last item in stack, pop it.
      The last popped item will be the parent and the item will be the right child of the parent.
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


# Method 2: Optimising space to O(n)
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

