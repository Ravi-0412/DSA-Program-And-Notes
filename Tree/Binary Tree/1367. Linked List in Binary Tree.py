# My mistake:
# This is not checking or making confirm that all nodes are seen consecutively.

# Note: This will work if asked to check if any subsequence of head values are present in linked list.

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root:
            return False
        if head.val == root.val:
            return self.isSubPath(head.next, root.left) or self.isSubPath(head.next, root.right)
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


# How to solve this error and check consecutively.
# Logic:
"""
if head elements are not consecutive then we need to start from 'intial head' from that node.
Means from each node we have to check from 'initial head'.
It means we need to check from each node.
"""

# Time: O(m * min(n, h)), where n is size of binary tree, m is size of linked list
# Space: O(h), h is height of the binary tree.

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root:
            return False
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
        # checking from each node i.e root, left, right

    def dfs(self, head, root):
        if not head:
            return True
        if not root:
            return False
        return head.val == root.val and (self.dfs(head.next, root.left) or self.dfs(head.next, root.right))

# Java
"""
    public boolean isSubPath(ListNode head, TreeNode root) {
        if (head == null) return true;
        if (root == null) return false;
        return dfs(head, root) || isSubPath(head, root.left) || isSubPath(head, root.right);
    }

    private boolean dfs(ListNode head, TreeNode root) {
        if (head == null) return true;
        if (root == null) return false;
        return head.val == root.val && (dfs(head.next, root.left) || dfs(head.next, root.right));
    }
"""

# Method 2: Do it later
# Optimisation using KMP algo
