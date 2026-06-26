# method 1:
"""
1. find the inorder traversal , you will get elements in sorted order 
2. Find the index of 'target' element in above resulting array.

Time = space = O(N)
"""

# Method 2:
"""
Valid for unique keys only
1. x == current.val: Found it. Add its left subtree nodes (all < x) plus 1 (for current itself). Return rank.
2. x < current.val: current and its right subtree are too large. Move left.
3. x > current.val: current and its left subtree are safely <= x. Add 1 + left_subtree_count to rank, then move right.

Time : O(n), Space ; O(H) recursive depth

Sum of height calculation at each level: 
Level 0 (root):    left subtree has n/2 nodes  → cost n/2
Level 1:           left subtree has n/4 nodes  → cost n/4
Level 2:           left subtree has n/8 nodes  → cost n/8
...
Level h:           cost 1

Total = n/2 + n/4 + n/8 + ... + 1
      = n × (1/2 + 1/4 + 1/8 + ...)
      = n × 1          (geometric series → 1)
      = O(n)
"""

class SolutionStandardBST:
    def _count_nodes(self, node: TreeNode) -> int:
        """Helper to compute total nodes inside a subtree."""
        if not node:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    def get_rank_inclusive(self, root: TreeNode, x: int) -> int:
        rank = 0
        current = root
        
        while current:
            if x == current.val:
                # 1. We count all elements in the left subtree (which are < x)
                # 2. We ALSO count the current node itself (since current.val == x)
                rank += 1 + self._count_nodes(current.left)
                return rank
                
            elif x < current.val:
                # Target is smaller; discard current and its right subtree
                current = current.left
                
            else:
                # Target is larger; current and left subtree are strictly smaller than x
                rank += 1 + self._count_nodes(current.left)
                current = current.right
                
        return rank

# Recursive way : 
def get_rank_inclusive(self, root, x):
    # base case — fell off tree, no contribution
    if not root:
        return 0

    left_size = self._count_nodes(root.left)

    if x == root.val:
        # found x
        # left subtree all < x  +  root itself
        return left_size + 1

    elif x < root.val:
        # x is in left subtree
        # root and right subtree are all > x → contribute nothing
        return self.get_rank_inclusive(root.left, x)

    else:
        # x is in right subtree
        # left subtree + root are all < x → bank them
        # then recurse right for the remainder
        return left_size + 1 + self.get_rank_inclusive(root.right, x)

# Follow ups: 
# 1. If duplicates are allowed (say duplicaets are stored in the right subtree)
def get_rank_inclusive_with_duplicates(self, root: TreeNode, x: int) -> int:
        rank = 0
        current = root
        
        while current:
            if x >= current.val:
                # If target x is greater than OR equal to current.val:
                # Both the current node and its entire left subtree are <= x.
                rank += 1 + self._count_nodes(current.left)
                # Keep moving right to check for duplicates or other smaller values
                current = current.right
            else:
                # Target x is strictly smaller than current.val
                current = current.left
                
        return rank


