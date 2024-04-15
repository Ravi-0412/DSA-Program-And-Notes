# method 1:
# just like we print all paths from root to leaf.

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans= 0

        def dfs(root, num):
            if root== None:
                return 
            num= num * 10 + root.val
            if root.left== None and root.right== None:
                self.ans+= num
                return
            dfs(root.left, num)
            dfs(root.right, num)

        dfs(root, 0)
        return self.ans


# Method 2: 
# Concise version of above

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def sumOfPaths(root, total):
            if not root:
                return 0
            if root.left == None and root.right == None:
                # Add the current leaf node val
                return total* 10 + root.val
            return sumOfPaths(root.left, total*10 + root.val) + sumOfPaths(root.right, total*10 + root.val)

        return sumOfPaths(root, 0)
    
# My Mistake
# Here returning only after seeing 'root = None'
# so same total will return from both left and right side.
# So ans will get doubled.

# Note vvi: In case of question related to leaf, put one base condition for leaf also with 'not root'
# and return ans from here.

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def sumOfPaths(root, total):
            if not root:
                return total
            return sumOfPaths(root.left, total*10 + root.val) + sumOfPaths(root.right, total*10 + root.val)

        return sumOfPaths(root, 0)

# Java code

# class Solution {
#     public int sumNumbers(TreeNode root) {
#         return sumOfPath(root, 0);
#     }
#     public int sumOfPath(TreeNode root, int total){
#         if(root == null)
#             return 0;
#         if(root.left == null && root.right == null)
#             return total *10 + root.val ;
#         return sumOfPath(root.left, total *10 + root.val) + sumOfPath(root.right, total *10 + root.val);
#     }
# }