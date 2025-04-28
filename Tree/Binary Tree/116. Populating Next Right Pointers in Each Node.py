# They are telling to connect all nodes at same elevel by right pointer.
# and whenenver we have to do something levelwise, first thing should come into mind is 'Level Order Traversal'(MultiSource Bfs)

# we need to point the cur visited node to the right of pre node at each level,
# so we will keep a varible 'pre' to keep track of last visited node in current level.

# Time = space = O(n)

from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root== None:
            return root
        q= deque([root])
        while q:
            pre= None
            for i in range(len(q)):  # we have to print level by level in a list
                curr= q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                if pre:  # not None
                    pre.next= curr
                pre= curr  # update pre to curr always
        return root

# Java
"""
class Solution {
    public Node connect(Node root) {
        if (root == null) {
            return root;
        }
        
        Queue<Node> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            Node pre = null;
            int size = q.size();
            
            for (int i = 0; i < size; i++) {
                Node curr = q.poll();
                
                if (curr.left != null) {
                    q.add(curr.left);
                }
                if (curr.right != null) {
                    q.add(curr.right);
                }
                if (pre != null) {
                    pre.next = curr;
                }
                pre = curr;
            }
        }
        
        return root;
    }
}
"""

# method 2:
# In O(1) space
# Using the property of a perfect binary tree:  perfect binary tree where all leaves are on the same level, and every parent has two children.
class Solution(object):
    def connect(self, root):
        # if root == None or if 'leaf' node is None. Perfect binary tree so checking only child for leaf is also fine
        if root == None or root.left == None:
            return root
        self.connectNodes(root.left, root.right)   # it will connect these two nodes & wil call function again to join four adjacent node at next level
        return root
    
    def connectNodes(self,node1, node2):
        node1.next = node2
        # Now join nodes at next level. if node at next level then only call the function
        if node1.left:
            # just join the nodes at next level that you can join using these two nodes. (call the function for those nodes)
            self.connectNodes(node1.left, node1.right)
            self.connectNodes(node1.right, node2.left)
            self.connectNodes(node2.left, node2.right)

# Java
"""
class Solution {
    public Node connect(Node root) {
        // If root is null or it's a leaf node (no left child), return root
        if (root == null || root.left == null) {
            return root;
        }
        
        connectNodes(root.left, root.right);
        return root;
    }
    
    private void connectNodes(Node node1, Node node2) {
        // Connect node1 to node2
        node1.next = node2;
        
        // If there's a next level (node1 has a left child), continue connecting
        if (node1.left != null) {
            connectNodes(node1.left, node1.right);
            connectNodes(node1.right, node2.left);
            connectNodes(node2.left, node2.right);
        }
    }
}
"""
# Try by other approaches alo later

