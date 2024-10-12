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
        
# Solution by taking 'k' as parameter and without ans as global variable
"""
Why are we returning root.val, k both , why are we not only returning root.val?
In each recursive call, k needs to be updated and passed to the next call
(because k decreases as we visit nodes). If we don't return the updated k, 
we won't know which node is the k-th smallest as the recursion unwinds.
Return Early (root.val): The value of the k-th smallest element can only be found at one point, 
and we need to pass that result up through the recursion without continuing the traversal once it's found.
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def findKthSmallest(root, k):
            if not root:
                return None, k
            
            # Explore the left subtree
            left, k = findKthSmallest(root.left, k)
            if left is not None:
                return left, k  # If k-th smallest is found in left subtree, return it
            
            # Decrement k as we process the current node
            k -= 1
            if k == 0:
                return root.val, k  # If the current node is the k-th smallest, return it
            
            # Explore the right subtree
            return findKthSmallest(root.right, k)

        result, _ = findKthSmallest(root, k)
        return result

# Related Q:
# 1) Kth largest element in BST
# Here first call for right then for left.


# Java
"""
// method 4:

class Solution {
    private int ans = -1;
    private int count;

    public int kthSmallest(TreeNode root, int k) {
        this.count = k;
        findKthSmallest(root);
        return ans;
    }

    private void findKthSmallest(TreeNode root) {
        if (root.left != null) {
            findKthSmallest(root.left);
        }

        count--;
        if (count == 0) {
            ans = root.val;
            return;
        }

        if (root.right != null) {
            findKthSmallest(root.right);
        }
    }
}

"""

