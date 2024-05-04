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


# try by this also and other approaches as well later.
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/solutions/150321/easy-understanding-java-beat-95-7-with-explanation/