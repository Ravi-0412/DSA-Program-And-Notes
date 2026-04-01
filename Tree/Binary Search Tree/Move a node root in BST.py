"""
Question: Given a Binary Search Tree (BST) and a target_val existing in the tree, 
transform the tree such that the node containing target_val becomes the new root. 
The transformation must preserve the Binary Search Tree property (In-order traversal remains sorted).
"""

"""
Logic & Thought Process:
This is a classic problem often called "BST Root Insertion" or "BST Splay to Root."

You cannot simply "swap" nodes. You must use Tree Rotations. Rotations change the parent-child structure but preserve the In-order Traversal (the sorted order).

1. The Two Tools
Right Rotation: If the target is a Left Child, pull it up and push the parent down-right.
Left Rotation: If the target is a Right Child, pull it up and push the parent down-left.

2. The "Bubble Up" Process
The algorithm works recursively in two phases:
Search (Down): Recursively find the target_val.
Rotate (Up): As the recursion "unwinds" back to the root, perform a rotation at every level. This "bubbles" the target node one level higher at each step until it becomes the root.

3. Handling Children (Re-grafting):
If the target node has its own children:
    Outer Children stay attached to the target.
    Inner Children (those between the target and the parent) are re-grafted to the old parent's vacant spot to maintain the BST property (Left < Root < Right).

Time Complexity: O(H) — where H is the tree height.
Space Complexity: O(H) — for the recursion stack.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTUtils:
    @staticmethod
    def insert(root, val):
        """Standard BST insertion."""
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = BSTUtils.insert(root.left, val)
        else:
            root.right = BSTUtils.insert(root.right, val)
        return root

    @staticmethod
    def get_inorder(root, res):
        if root:
            BSTUtils.get_inorder(root.left, res)
            res.append(root.val)
            BSTUtils.get_inorder(root.right, res)
        return res

    @staticmethod
    def get_preorder(root, res):
        if root:
            res.append(root.val)
            BSTUtils.get_preorder(root.left, res)
            BSTUtils.get_preorder(root.right, res)
        return res

class Solution:
    def makeNewRoot(self, root: TreeNode, target_val: int) -> TreeNode:
        """
        Recursively moves the target_val node to the root of the BST 
        using rotations while maintaining the BST property.
        """
        # Base Case: If tree is empty or target is already at the current root
        if not root or root.val == target_val:
            return root

        # Step 1: Target is in the left subtree
        if target_val < root.val:
            # Recursively bring the target to the root of the left subtree
            root.left = self.makeNewRoot(root.left, target_val)
            # After recursion, target is now root.left. Perform Right Rotation
            # to pull it up one level to become the new root.
            root = self.rotateRight(root)
            
        # Step 2: Target is in the right subtree
        else:
            # Recursively bring the target to the root of the right subtree
            root.right = self.makeNewRoot(root.right, target_val)
            # After recursion, target is now root.right. Perform Left Rotation
            # to pull it up one level to become the new root.
            root = self.rotateLeft(root)
            
        return root

    def rotateRight(self, p: TreeNode) -> TreeNode:
        """
        Performs a Right Rotation around parent 'p'.
        Brings left child 'x' up, pushes 'p' down to the right.
        """
        # 
        x = p.left
        # p's new left child becomes x's old right child (the 're-graft')
        p.left = x.right
        # x's new right child becomes the old parent p
        x.right = p
        return x

    def rotateLeft(self, p: TreeNode) -> TreeNode:
        """
        Performs a Left Rotation around parent 'p'.
        Brings right child 'x' up, pushes 'p' down to the left.
        """
        x = p.right
        # p's new right child becomes x's old left child
        p.right = x.left
        # x's new left child becomes the old parent p
        x.left = p
        return x

# --- TEST SUITE ---
def run_tests():
    sol = Solution()
    utils = BSTUtils()

    # TEST CASE 1: Target is a direct left child
    # Initial: 10 -> 5, 15
    # Target: 5
    root1 = None
    for v in [10, 5, 15]: root1 = utils.insert(root1, v)
    
    print("Test 1: Rotate Left Child (5) to Root")
    new_root1 = sol.makeNewRoot(root1, 5)
    print(f"New Root: {new_root1.val} (Expected: 5)")
    print(f"In-order: {utils.get_inorder(new_root1, [])} (Expected: [5, 10, 15])")
    print(f"Pre-order: {utils.get_preorder(new_root1, [])} (Expected: [5, 10, 15])")
    print("-" * 30)

    # TEST CASE 2: Target is a grandchild (Zig-Zig)
    # Initial: 10 -> 5 -> 2
    # Target: 2
    root2 = None
    for v in [10, 5, 2]: root2 = utils.insert(root2, v)
    
    print("Test 2: Rotate Grandchild (2) to Root")
    new_root2 = sol.makeNewRoot(root2, 2)
    print(f"New Root: {new_root2.val} (Expected: 2)")
    print(f"In-order: {utils.get_inorder(new_root2, [])} (Expected: [2, 5, 10])")
    print(f"Pre-order: {utils.get_preorder(new_root2, [])} (Expected: [2, 5, 10])")
    print("-" * 30)

    # TEST CASE 3: Complex Re-grafting
    # Initial: 10 -> 5 -> (3, 7)
    # Target: 5 (Node 7 must move from 5's right to 10's left)
    root3 = None
    for v in [10, 5, 15, 3, 7]: root3 = utils.insert(root3, v)
    
    print("Test 3: Complex Re-grafting (Target 5)")
    new_root3 = sol.makeNewRoot(root3, 5)
    print(f"New Root: {new_root3.val} (Expected: 5)")
    # After rotation, 5's right child should be 10, and 10's left child should be 7
    print(f"In-order: {utils.get_inorder(new_root3, [])} (Expected: [3, 5, 7, 10, 15])")
    print(f"Pre-order: {utils.get_preorder(new_root3, [])} (Expected: [5, 3, 10, 7, 15])")
    print("-" * 30)
    
    # TEST CASE 4: 3-Level Balanced BST
    # Initial:
    #        50
    #       /  \
    #     30    70
    #    /  \  /  \
    #   20  40 60  80
    # Target: 20
    
    root4 = None
    for v in [50, 30, 70, 20, 40, 60, 80]: 
        root4 = BSTUtils.insert(root4, v)
    
    print("Test 4: Move Leaf Node (20) to Root")
    new_root4 = sol.makeNewRoot(root4, 20)
    
    print(f"New Root: {new_root4.val} (Expected: 20)")
    
    # Verification:
    # In-order MUST remain sorted: [20, 30, 40, 50, 60, 70, 80]
    print(f"In-order: {utils.get_inorder(new_root4, [])}")
    
    # Pre-order for this specific transformation:
    # Node 20 is root. Its right child is 30. 30's right is 50.
    # 50's left is 40, 50's right is 70. 70's children are 60, 80.
    # Expected Pre-order: [20, 30, 50, 40, 70, 60, 80]
    print(f"Pre-order: {utils.get_preorder(new_root4, [])}")
    print("-" * 30)
    
    root5 = None
    for v in [50, 30, 70, 20, 40, 60, 80,35,45]: 
        root5 = BSTUtils.insert(root5, v)
    
    print("Test 5: Move Leaf Node (40) to Root")
    # 50 (Root)
    #       /  \
    #      30    70
    #     /  \   / \
    #   20   [40] 60 80
    #       /  \
    #       35  45    <-- Target [40] has two children
          
    new_root5 = sol.makeNewRoot(root5, 40)
    
    print(f"New Root: {new_root5.val} (Expected: 40)")
    print(f"In-order: {utils.get_inorder(new_root5, [])}")
    print(f"Pre-order: {utils.get_preorder(new_root5, [])}")
    print("-" * 30)
    
    # Initial phase:
    # 50 (Root)
    #       /  \
    #      [40]  70
    #      /  \  / \
    #     30  45 60 80
    #   /  \
    #   20  35        <-- 35 was re-grafted to 30
    
    # 1st rotation : left
    # 40 (NEW ROOT)
    #       /  \
    #      30    50
    #     /  \   /  \
    #   20  35 45  70
    #               / \
    #              60 80
    
    # 2nd rotation: right
    # 40 (NEW ROOT)
    #       /  \
    #      30    50
    #     /  \   /  \
    #   20  35 45  70
    #               / \
    #              60 80

if __name__ == "__main__":
    run_tests()
