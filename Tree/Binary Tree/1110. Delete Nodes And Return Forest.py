# Logic : If any node is in 'to_delete' then its children must be part of ans because it will be connected components.

# Note vvi: we have to return ans after deleting all the given nodes in 'to_delete' so if we traverse from top-bottom then we will get wrong ans
# because we don't know which all nodes will get deleted later.

# So we will go bottom-top (postorder) , this will make sure that we are doing operation on updated subtree for current node.
# and we will keep updating tree also.

# Time : O(n)

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        ans = []

        def dfs(root):
            if not root:
                return None
            root.left = dfs(root.left)
            root.right = dfs(root. right)
            # if root in 'to_delete' then its children must be in ans. so first add them then, make root as None as we are deleting
            if root.val in to_delete:           
                if root.left: 
                    ans.append(root.left)
                if root.right:
                    ans.append(root.right)
                return None # make 'None' since we are deleting
            # if root not in 'to_delete' then simply return root
            return root  
        
        dfs(root)
        # since we are doing a postorder traversal we will not be able to process root if it's not in toDelete in our recursive function
        # Add root if not in 'to_delete' otherwise simply return the ans.

        # Just one more connected we can get starting from root.
        if root.val not in to_delete:
            ans.append(root)
        return ans


# Note: Do by bfs and other approaches also later
# https://leetcode.com/problems/delete-nodes-and-return-forest/solutions/345009/python-bfs-solution/
# https://leetcode.com/problems/delete-nodes-and-return-forest/solutions/328854/python-recursion-with-explanation-question-seen-in-a-2016-interview/

# If Q ask :"to get the ans after deleting each given node" given tree returns to its initial state after each deletion.
# then our solution will:

# Simply we have to disconnect all node of the subtree starting from 'node_to_delete'.
# for this just return 'None' when we will see the 'node_to_delete' or null node.

# And keep including all the nodes by creating new_node just like we make 'Binary Search Tree'.

# Time : O(n^2)

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        def forest(cur, nodeVal):
            if not cur or cur.val == nodeVal:
                return None
            ans = TreeNode(cur.val)
            ans.left = forest(cur.left, nodeVal)
            ans.right = forest(cur.right, nodeVal)
            return ans

        ans = []
        for nodeVal in to_delete:
            subtree = forest(root, nodeVal)
            ans.append(subtree)
        return ans