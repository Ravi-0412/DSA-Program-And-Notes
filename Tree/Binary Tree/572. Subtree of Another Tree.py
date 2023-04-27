# method 1: Brute Force
# just check at each node for subtree by calling the 'isIdentical(root)'
# time : O(n*m)

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if subRoot== None: return True  # null is always a valid subtree. No need of this line
        if root== None: return False    # simply return will also work
        # check if tree starting from root is same tree as subroot
        if self.isIdentical(root,subRoot)== True:
            return True
        # if root is not same then check for either of its children
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)  
    
    def isIdentical(self,root1, root2):
        # if any of them is None then both should be None for same tree
        if root1== None or root2== None:  # this will check that they are structurally same 
            return root1==root2    
        return (root1.val==root2.val) and self.isIdentical(root1.left, root2.left) and self.isIdentical(root1.right, root2.right)
                # this will check all nodes are value wise same

# method 2: 
# can also do like "Find Duplicate Subtree" using serialisation.
# Time: O(n*m)

# method 3: serialisation + kmp
# Time: O(m+ n)
# will do after learning KMP
# https://leetcode.com/problems/subtree-of-another-tree/solutions/474425/java-python-2-solutions-naive-serialize-in-preorder-then-kmp-o-m-n-clean-concise/


            