# logic: If we can get the ele in sorted order then our ans = 'min difference between consecutive ele'

# And in BST, we can get ele in sorted order in o(N) time.

# time: O(n)

# Recursive one in java. Later do in Python.
public class Solution {
    
    int minDiff = Integer.MAX_VALUE;
    TreeNode prev;
    
    public int getMinimumDifference(TreeNode root) {
        inorder(root);
        return minDiff;
    }
    
    public void inorder(TreeNode root) {
        if (root == null) return;
        inorder(root.left);
        if (prev != null) minDiff = Math.min(minDiff, root.val - prev.val);
        prev = root;
        inorder(root.right);
    }

}

# 2nd method:
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/solutions/338515/python-recursive/
# Have to understand and analyse this properly.
class Solution(object):
    def getMinimumDifference(self, root):
        def fn(node, lo, hi):
            if not node: return hi - lo
            left = fn(node.left, lo, node.val)
            right = fn(node.right, node.val, hi)
            return min(left, right)
        return fn(root, float('-inf'), float('inf'))


# Note: for general Binary tree.
# time: 0(n*logn), to get the ele in sorted order.
