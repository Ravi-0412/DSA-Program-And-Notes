"""
The deletion can be divided into two stages:
1. Search for a node to remove.
2. If the node is found, delete the node.

The deletion process follows three distinct scenarios based on the node's structure:

Case 1: Leaf Node (No children)
We simply return None to the parent, effectively cutting the connection.

Case 2: Single Child
We "bypass" the current node. If the node has only a right child, we return that right child to the parent. The parent now points directly to the grandchild.

Case 3: Two Children
We can't just delete this node because it would leave two orphaned subtrees.
We find the Inorder Successor (the smallest value in the right subtree).
We replace the current node's value with the successor's value.
Finally, we recursively delete that successor node from the right subtree.
"""

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Deletes a node from a BST and returns the new root.
        Ensures the BST property is maintained.
        """
        # BASE CASE: If the key is not in the tree
        if not root:
            return None

        # --- STEP 1: FIND THE NODE ---
        if key < root.val:
            # Look in the left subtree and re-link the result
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # Look in the right subtree and re-link the result
            root.right = self.deleteNode(root.right, key)
        
        # --- STEP 2: DELETE THE NODE (Found it!) ---
        else:
            # SCENARIO A: Leaf or Single Child (Right only)
            if not root.left:
                return root.right
            
            # SCENARIO B: Single Child (Left only)
            elif not root.right:
                return root.left
            
            # SCENARIO C: Two Children
            else:
                # Find the Inorder Successor (Smallest in the right subtree)
                successor = self._get_min(root.right)
                
                # Copy successor's value to current node
                root.val = successor.val
                
                # Recursively delete the successor node from the right subtree
                # Important: Re-link root.right to the modified subtree
                root.right = self.deleteNode(root.right, successor.val)
        
        return root

    def _get_min(self, node: TreeNode) -> TreeNode:
        """to find the leftmost (minimum) node in a subtree."""
        curr = node
        while curr.left:
            curr = curr.left
        return curr
