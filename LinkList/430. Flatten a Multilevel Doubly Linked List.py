# Exactly sam elogic as: "114. Flatten Binary Tree to Linked List".
# Here we need to take care of one more pointer 'prev' which is simple only.

class Solution(object):
    def flatten(self, head):
        if not head:
            return None
        child_Node = self.flatten(head.child)
        next_Node = self.flatten(head.next)
        head.next = child_Node if child_Node else next_Node     # writing this only won't work because we have to take care of 'prev' also.
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
# try by this also and other approaches as well later.
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/solutions/150321/easy-understanding-java-beat-95-7-with-explanation/