# logic: If we can get the ele in sorted order then our ans = 'min difference between consecutive ele'

# And in BST, we can get ele in sorted order in o(N) time.

# time: O(n)

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        pre = float('-inf')
        stack = []
        ans = float('inf')
        while stack or root:
            while root:  # keep going left 
                stack.append(root)
                root= root.left
            curr= stack.pop()
            ans = min(ans, curr.val - pre)   # just finding diff between two consecutive ele in sorted array.
            pre = curr.val
            root= curr.right  # move the pointer to check the right child.
        return ans

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
