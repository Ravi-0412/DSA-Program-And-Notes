# in simple way: if we reach any node then that node should be the max till now.

# so we need to keep track of maxVal seen till now then only we will able to decide whether that node is a good node or not.
# if it's val >=maxSeen then it is good node else not. 

# just start from root and store the maxValue seen till now.
# And if current node has value>= max_seen_till now then incr the count and update the max_seen

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count, ans= 0, []
        def dfs(root, maxSeen):
            if root== None:
                return
            if root.val>= maxSeen:
                ans.append(root.val)
                self.count+= 1
                maxSeen= root.val
            dfs(root.left, maxSeen)
            dfs(root.right, maxSeen)
        
        dfs(root,root.val)
        return self.count

# Java
"""
class Solution {
    private int count;

    public int goodNodes(TreeNode root) {
        count = 0;
        dfs(root, root.val);
        return count;
    }

    private void dfs(TreeNode node, int maxSeen) {
        if (node == null) {
            return;
        }
        if (node.val >= maxSeen) {
            count++;
            maxSeen = node.val;
        }
        dfs(node.left, maxSeen);
        dfs(node.right, maxSeen);
    }
}
"""