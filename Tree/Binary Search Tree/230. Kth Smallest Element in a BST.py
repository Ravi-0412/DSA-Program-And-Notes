# method 1: do any traversal and then sort the ans and then return the kth ele from start
# time: O(n*logn), space: O(n)

# method 2: just find the inorder traversal of the tree and return the kth element from the start
# inorder always give the ans in sorted form for BST
# time: O(n), space: O(n) for ans + recursion depth

# method 3: rather than storing the ans in any array just keep a count for method 2
# and increment the count when you add any ele to the ans 
# and when count reaches 'k' just print the value of that node
# time: O(n), space: O(n) recursion depth

# to avoid the space complexity in method 3
# use the morris inorder traversal


# Note: All above method is taking O(n) space

# Method 4: 

# Optimsing to O(1) space

# Logic: Smallest node will be the leftmost node.
# so once you find '.left' of any node = None then that will be the smallest node as of now.
# And to get the next smaller node , move to its right.

# If it's right is also None then it will do backtrack function call to previous node and calculate in same way.

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def findKthSmallest(root):
            if root.left:
                findKthSmallest(root.left)
            self.count -= 1
            if self.count == 0:
                self.ans = root.val
                return
            # next smaller we will get from right side of root
            if root.right:
                findKthSmallest(root.right)

        self.ans = -1
        self.count = k
        findKthSmallest(root)
        return self.ans

# My mistake
# Note: if we do taking 'k' in function call only then we will get wrong ans
# because after backtarck value of 'k' will be won't change for that function.
# but it should change globally like above.

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def findKthSmallest(root, k):
            if root.left:
                findKthSmallest(root.left, k)
            k -= 1
            if k == 0:
                self.ans = root.val
                return
            # next smaller we will get from right side of root
            if root.right:
                findKthSmallest(root.right, k)

        self.ans = -1
        findKthSmallest(root, k)
        return self.ans


# Related Q:
# 1) Kth largest element in BST

