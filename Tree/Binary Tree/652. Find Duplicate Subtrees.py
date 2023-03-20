# Brute force: O(n^3)
# for every node (O(n)) check for every subtree (O(n)) whether they are same or not (O(n))= O(n^3)

# method 2:
# for each node find the serialisation and store that serialisation as key with node as "val" in a hashmap.
# there will be 'n' node and for finding serialisation for each node O(n). so
# time: O(n^2).

# why we went with serialisation not by simply storing the node values using preorder?
# Ans: Since two different subtree can have same preorder. so we will get incorrect ans.
# we are doing serialisation just same as "Q 297. Serialise and Deserialise Binary Tree".

# bottom up
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtree= defaultdict(list)  # {serialisation_node: node}

        def dfs(root):
            if not root:
                return "null"
            s= ",".join([str(root.val) , dfs(root.left) , dfs(root.right)])   # serialisation for curr node
            # now check if this serialisation is already present in 'subtree' means duplicate subtree
            if len(subtree[s]) == 1:  # means duplicate subtree starting from 'root.. checking length to add duplicate tree only first time.
                ans.append(root)
            subtree[s].append(root)  # add the serialisation of curr node into subtree
            return s
        
        ans= []
        dfs(root)
        return ans
    



# try to do in O(n) also later(link in sheet. 4th link)