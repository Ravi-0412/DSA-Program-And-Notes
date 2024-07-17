# just go through element of descriptions one by one and form tree.
# Two things kep in mind:
# 1) if any of node is already created then we have to join with created node only else create new node and join.
# 2) update the indegree

# Note: Node having indegree = 0 will be our root.

# Method 1:

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        indegree = collections.defaultdict(int)
        node_created = collections.defaultdict(TreeNode)
        for p, c , isLeft in descriptions:
            indegree[p] += 0   # just to get 'p' as key in hashmap.
            indegree[c] += 1
            parent = node_created.get(p, TreeNode(p))
            child = node_created.get(c, TreeNode(c))
            # update/create node for p and c
            node_created[p] = parent
            node_created[c] = child
            if isLeft== 1:
                parent.left = child
            else:
                parent.right = child

        # return the node having indegree = 0
        for k, v in indegree.items():
            if v == 0:
                return node_created[k]

# java
"""
public class Solution {
    public TreeNode createBinaryTree(int[][] descriptions) {
        Map<Integer, Integer> indegree = new HashMap<>();
        Map<Integer, TreeNode> nodeCreated = new HashMap<>();

        for (int[] description : descriptions) {
            int parentVal = description[0];
            int childVal = description[1];
            int isLeft = description[2];

            indegree.put(parentVal, indegree.getOrDefault(parentVal, 0));
            indegree.put(childVal, indegree.getOrDefault(childVal, 0) + 1);

            TreeNode parent = nodeCreated.getOrDefault(parentVal, new TreeNode(parentVal));
            TreeNode child = nodeCreated.getOrDefault(childVal, new TreeNode(childVal));

            nodeCreated.put(parentVal, parent);
            nodeCreated.put(childVal, child);

            if (isLeft == 1) {
                parent.left = child;
            } else {
                parent.right = child;
            }
        }

        for (Map.Entry<Integer, Integer> entry : indegree.entrySet()) {
            if (entry.getValue() == 0) {
                return nodeCreated.get(entry.getKey());
            }
        }

        return null; // Should never reach here if input is valid
    }
}

"""


