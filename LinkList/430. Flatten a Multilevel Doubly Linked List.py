# Method 1: 
# Exactly sam logic as: "114. Flatten Binary Tree to Linked List".
# Here we need to take care of one more pointer 'prev' which is simple only.
"""
logic: 
i) First, recursively flatten child and next sublists.
ii) This ensures that when we come back to the current node, both the child and next parts are already in their final flattened form.
Only then can we safely connect them to the current node without breaking the structure.


Analogy to Tree problem and this problem.
a) root.right = left, 	     head.next = child
b) Stitch left -> right, 	child -> next
c) root.left = None,        head.child = None
"""
# Time: O(n), space: O(n) due to recursion depth

class Solution(object):
    def flatten(self, head):
        if not head:
            return None
        child_Node = self.flatten(head.child)
        next_Node = self.flatten(head.next)
        head.next = child_Node if child_Node else next_Node     # seeting next pointer
        # Take care of prev pointer for 'next' node.
        if child_Node:
            child_Node.prev = head
        elif next_Node:
            next_Node.prev = head

        if child_Node and next_Node:
            cur = child_Node
            while cur.next:
                cur = cur.next
            cur.next = next_Node
            next_Node.prev = cur
        head.child = None
        return head

# Java Code 
"""
class Node {
    int val;
    Node next, prev, child;

    Node(int x) {
        val = x;
        next = prev = child = null;
    }
}

class Solution {
    public Node flatten(Node head) {
        if (head == null) return null;

        Node child_Node = flatten(head.child);
        Node next_Node = flatten(head.next);

        head.next = (child_Node != null) ? child_Node : next_Node; // Setting next pointer

        // Take care of prev pointer
        if (child_Node != null) {
            child_Node.prev = head;
        } else if (next_Node != null) {
            next_Node.prev = head;
        }

        // If both child and next exist, connect them
        if (child_Node != null && next_Node != null) {
            Node cur = child_Node;
            while (cur.next != null) {
                cur = cur.next;
            }
            cur.next = next_Node;
            next_Node.prev = cur;
        }

        head.child = null; // Remove child reference
        return head;
    }
}
"""

# C++ Code 
"""
#include <iostream>

using namespace std;

class Node {
public:
    int val;
    Node* next;
    Node* prev;
    Node* child;

    Node(int x) : val(x), next(nullptr), prev(nullptr), child(nullptr) {}
};

class Solution {
public:
    Node* flatten(Node* head) {
        if (!head) return nullptr;

        Node* child_Node = flatten(head->child);
        Node* next_Node = flatten(head->next);

        head->next = child_Node ? child_Node : next_Node; // Setting next pointer

        // Take care of prev pointer
        if (child_Node) {
            child_Node->prev = head;
        } else if (next_Node) {
            next_Node->prev = head;
        }

        // If both child and next exist, connect them
        if (child_Node && next_Node) {
            Node* cur = child_Node;
            while (cur->next) {
                cur = cur->next;
            }
            cur->next = next_Node;
            next_Node->prev = cur;
        }

        head->child = nullptr; // Remove child reference
        return head;
    }
};
"""

# Method 2:
"""
1) Traverse next → child → node (reverse postorder).
2) On returning, connect current node.next = prev and fix prev.prev.
3) Set node.child = None after processing.
4) prev always tracks the already-flattened list.

Time Complexity: O(n), Every node visited once.
Space Complexity: O(n), (due to recursion stack)
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.prev = None

        def dfs(node):
            if not node:
                return
            dfs(node.next)
            dfs(node.child)

            node.next = self.prev
            if self.prev:
                self.prev.prev = node
            node.child = None
            self.prev = node

        dfs(head)
        return head


# java
"""
class Solution {
    Node prev = null;

    public Node flatten(Node head) {
        dfs(head);
        return head;
    }

    private void dfs(Node node) {
        if (node == null) return;

        dfs(node.next);
        dfs(node.child);

        node.next = prev;
        if (prev != null) prev.prev = node;
        node.child = null;
        prev = node;
    }
}
"""

# C++
"""
class Solution {
    Node* prev = nullptr;

public:
    Node* flatten(Node* head) {
        dfs(head);
        return head;
    }

    void dfs(Node* node) {
        if (!node) return;

        dfs(node->next);
        dfs(node->child);

        node->next = prev;
        if (prev) prev->prev = node;
        node->child = nullptr;
        prev = node;
    }
};
"""


# Method 3:
"""
1) Use a stack to simulate preorder (push next, then child).
2) At each step, attach current node to the flattened list (prev.next = curr).
3) Set curr.child = None after processing.

Time Complexity: O(n), Each node is pushed and popped once.
Space Complexity: O(n) (due to stack usage)
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        stack = [head]
        prev = None

        while stack:
            curr = stack.pop()
            if prev:
                prev.next = curr
                curr.prev = prev

            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None

            prev = curr

        return head


# Java
"""
class Solution {
    public Node flatten(Node head) {
        if (head == null) return head;

        Stack<Node> stack = new Stack<>();
        stack.push(head);
        Node prev = null;

        while (!stack.isEmpty()) {
            Node curr = stack.pop();

            if (prev != null) {
                prev.next = curr;
                curr.prev = prev;
            }

            if (curr.next != null) stack.push(curr.next);
            if (curr.child != null) {
                stack.push(curr.child);
                curr.child = null;
            }

            prev = curr;
        }

        return head;
    }
}
"""

# C++
"""
class Solution {
public:
    Node* flatten(Node* head) {
        if (!head) return head;

        stack<Node*> s;
        s.push(head);
        Node* prev = nullptr;

        while (!s.empty()) {
            Node* curr = s.top();
            s.pop();

            if (prev) {
                prev->next = curr;
                curr->prev = prev;
            }

            if (curr->next) s.push(curr->next);
            if (curr->child) {
                s.push(curr->child);
                curr->child = nullptr;
            }

            prev = curr;
        }

        return head;
    }
};
"""