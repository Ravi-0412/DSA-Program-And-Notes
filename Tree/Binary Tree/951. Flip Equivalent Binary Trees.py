# Explanation link: https://1drv.ms/o/c/2e0ac565ff6aeb82/IgC20s4qd35MTaU9V9Tzi1u0AYecoT4d1-sYC5x2BOWNfh8 

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 == None or root2 == None:
            return root1 == root2
        # Scenario A: The children match without flipping
        # Scenario B: The children match after flipping left and right
        return root1.val == root2.val and (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right) or \
                                           self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
