# Logic: for each node return the extra.
# e.g: if we get '+3' from the left child, that means that the left subtree has 3 extra coins to move out. 
# If we get '-1' from the right child, we need to move 1 coin in. 
# So, we increase the number of moves by 4 (3 moves out left + 1 moves in right). 
# We then return the final balance: r->val (coins in the root) + 3 (left) + (-1) (right) - 1 (keep one coin for the root).

# Note: if left, right and root value all are = 0 then you will get:
# left = -1, right = -1 and root also will contribute '-1' => in total we require 3 moves to make all these three '1'.
# How these node will get distribution?
# Will get from upper nodes, upper node will send to root and then root will send to it's children.

# Bottom-up will cover both the casesbut top-down won't cover.

# Time: O(n)

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:

        def distribute(root):
            if not root:
                return 0
            l = distribute(root.left)
            r = distribute(root.right)
            self.ans += root.val + abs(l) + abs(r) - 1  # sum of moves at this root
            return root.val + l + r - 1   # final no of moves that it will send to its parent.

        self.ans = 0
        distribute(root)
        return self.ans
    

# in java
"""
class Solution {
    private int ans;

    public int distributeCoins(TreeNode root) {
        ans = 0;
        distribute(root);
        return ans;
    }

    private int distribute(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int l = distribute(root.left);
        int r = distribute(root.right);
        ans += Math.abs(l) + Math.abs(r);
        return root.val + l + r - 1;
    }
}
"""
