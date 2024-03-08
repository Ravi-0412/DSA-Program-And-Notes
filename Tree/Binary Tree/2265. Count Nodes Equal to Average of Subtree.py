# method 1: Brute Force
# logic: for each node, find the sum of subtree and no of nodes in that subtree.

# time: (n^2)

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans= 0

        # finding the sum of nodes in subtree starting with node 'root'.
        def dfs(root):
            if not root:
                return 0
            self.count+= 1
            l= dfs(root.left)
            r= dfs(root.right)
            return root.val + l + r
            
        def preorder(root):
            if not root:
                return
            self.count= 0   # here i was writing without self so was getting error.
            average= dfs(root) // self.count
            if average== root.val:
                self.ans+= 1

            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        return self.ans


# method 2: optimising the above using bottom up dp.

# logic: for each subtree we need "sum of subtree" and "count of node in that subtree".

# how to do?
# just similar method as "1372. Longest ZigZag Path in a Binary Tree", or "House Robber 3". we will return 2 thing in this.

#  For each node return [sum, no_nodes]

# time: O(n)
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans= 0

        # same as we find the the sum of a subtree or count nodes.
        # only diff "we are returning both sum and node_count".
        def dfs(root):
            if not root:
                return [0, 0]   # [sum, node_count]
            left_sum, left_count=   dfs(root.left)
            right_sum, right_count= dfs(root.right)
            sum=   root.val + left_sum + right_sum
            count= 1 + left_count + right_count
            if root.val== sum// count:
                self.ans+= 1
            return [sum, count]
        
        dfs(root)
        return self.ans



