
# method 1:
# as you can see clearly that we have to print the last node at each level i.e we have to print only the rightmost node at each level
# so applied the exactly same logic of "level order traversal" and for each level put only the last ele at that level that's it

# why ? Because all other nodes at same level won't be visible.

# Method 1: 
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root== None:
            return root
        ans= []
        q= deque([root])
        while q:
            ans += [q[-1].val]   # appending the last node value at each level
            for i in range(len(q)):  # we have to print level by level in a list
                curr= q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return ans


# Recursive way
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans= []
        # just preorder traversal only. just we are traversing first right before left because
        #  we have to add right node first if exist
        def dfs(root, level): 
            if root== None:
                return
            if level== len(ans):  # means at that level no node has been added.  
                # this is the first node from the right at that level so add in the ans
                ans.append(root.val)
            dfs(root.right, level+1)
            dfs(root.left,  level+1)
    
        dfs(root, 0)
        return ans



# Method 2:
# this can also be done by the vertical order approaches 
# here key= vertical_level and value will be a pair of (hori_level, node.val)
# and we have to traverse from min depth i.e= 0 to max depth(range of vertical level)
# after that print the value with max horizonatl level that's it 
# but time complexity of this will go O(n*logn)

# java
# Method 1:
"""
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        if (root == null) {
            return ans;
        }
        
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        
        while (!q.isEmpty()) {
            int levelSize = q.size();
            for (int i = 0; i < levelSize; i++) {
                TreeNode curr = q.poll();
                if (i == levelSize - 1) {
                    ans.add(curr.val); // add the last node value at each level
                }
                if (curr.left != null) {
                    q.add(curr.left);
                }
                if (curr.right != null) {
                    q.add(curr.right);
                }
            }
        }
        
        return ans;
    }
}

"""