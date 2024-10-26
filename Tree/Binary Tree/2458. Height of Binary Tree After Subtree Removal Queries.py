# method 1:
# time: O(n^2)

# Logic: check for maxHeight after removing the cur node in queries.

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        def height(cur, nodeVal):
            if not cur:
                return 0
            if cur.val == nodeVal:
                return 0
            return 1 + max(height(cur.left, nodeVal), height(cur.right, nodeVal))

        ans = []       
        for nodeVal in queries:
            curHeight = height(root, nodeVal) - 1
            ans.append(curHeight)
        return ans
    

# Optimisation 
# Logic vvi: Max height without current node will be max height elsewhere in the tree or height of sibling node + curr depth
# And for getting the maxHeight , we need (curNode, curHeight, maxHeightPossible) as parameter in function.

# How to think?
# Because we can get maxHeight after deleting any node from 1) different subtree i.e max height elsewhere in the tree (maxHeight till now)
# 2) maxHeight from its sibling subtree

# Note : 'height' will repeat for same node value

# time: O(n*logn): we have to find the maxHeight we can get from sibling


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        heights = collections.defaultdict()
        def height(cur):
            if not cur:
                return 0
            if cur.val in heights:
                return heights[cur.val]
            h= 1 + max(height(cur.left), height(cur.right))
            heights[cur.val] = h
            return h

        ans = collections.defaultdict(int)   # [node : maxDepthAfterRemoving]
        def dfs(root, depth, maxDepth):
            if not root:
                return 
            ans[root.val] = maxDepth
            dfs(root.left , depth + 1 , max(maxDepth , depth + height(root.right)))   # for maxDepth taking prev 'depth' only so no need to add '+1' in maxDepth
                                # for 'left' we will find the maxHeight from its sibling i.e 'right' & same for 'right'.
            dfs(root.right , depth + 1 , max(maxDepth , depth + height(root.left)))
        
        dfs(root, 0, 0)
        # now max height that we will get after removing any node is stored in 'ans' i.e [node: maxDepth]
        return [ans[v] for v in queries]

# java
"""
class Solution {
    private Map<Integer, Integer> heights = new HashMap<>();
    private Map<Integer, Integer> maxDepthAfterRemoval = new HashMap<>();
    
    public int[] treeQueries(TreeNode root, int[] queries) {
        // Step 1: Calculate height of each node
        height(root);
        
        // Step 2: Perform DFS to calculate max depth after removing each node
        dfs(root, 0, 0);
        
        // Prepare answer based on the queries
        int[] answer = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            answer[i] = maxDepthAfterRemoval.getOrDefault(queries[i], 0);
        }
        
        return answer;
    }
    
    private int height(TreeNode node) {
        if (node == null) return 0;
        
        if (heights.containsKey(node.val)) {
            return heights.get(node.val);
        }
        
        int h = 1 + Math.max(height(node.left), height(node.right));
        heights.put(node.val, h);
        
        return h;
    }
    
    private void dfs(TreeNode node, int depth, int maxDepth) {
        if (node == null) return;
        
        // Store the max depth after "removing" the current node
        maxDepthAfterRemoval.put(node.val, maxDepth);
        
        // Traverse left and right children
        // For the left child, use the right child's height for max depth
        dfs(node.left, depth + 1, Math.max(maxDepth, depth + height(node.right)));
        
        // For the right child, use the left child's height for max depth
        dfs(node.right, depth + 1, Math.max(maxDepth, depth + height(node.left)));
    }
}
"""

# Try by other approaches also.
# https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/solutions/2757990/python-3-explanation-with-pictures-dfs/
