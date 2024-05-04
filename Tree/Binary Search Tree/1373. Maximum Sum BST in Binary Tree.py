# Just applied 2nd method of Q: "98. Validate Binary Search Tree"
# Only one difference: just return 'sum' also with minimum and maximum value


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0    # Taken '0' instead of 'float('-inf') because in case of all negative values we have to return '0' only(empty bst)

        def check(root):
            if not root:
                return [float('inf'), float('-inf'), 0]  # [minimum, maximum, sum]. For base case return such value which will be valid always
            min1, max1, sum1 = check(root.left)
            min2, max2, sum2 = check(root.right)
            if root.val <= max1 or root.val >= min2:
                # not valid so return such values which will be invalid always
                return [float('-inf'), float('inf'), 0]
            self.ans = max(self.ans, sum1 + sum2 + root.val)
            return [min(min1, root.val), max(root.val, max2), sum1 + sum2 + root.val]

        check(root)
        return self.ans