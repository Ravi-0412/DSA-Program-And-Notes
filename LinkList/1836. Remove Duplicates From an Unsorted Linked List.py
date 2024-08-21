class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        # Dictionary to store the frequency of each node value
        repeated_nodes = {}
        
        # Count the frequency of each value in the list
        curr = head
        while curr is not None:
            repeated_nodes[curr.val] = repeated_nodes.get(curr.val, 0) + 1
            curr = curr.next
        
        # Create a temporary dummy node to handle edge cases (e.g., if head needs to be deleted)
        temp_head = ListNode(0)
        temp_head.next = head
        
        prev = temp_head
        curr = head
        
        # Remove nodes that have a frequency greater than 1
        while curr is not None:
            if repeated_nodes[curr.val] > 1:
                prev.next = curr.next  # Skip the current node
                curr.next = None  # Remove the current node by setting its next pointer to None
            else:
                prev = curr  # Move prev only if the current node is not deleted
            curr = prev.next  # Move to the next node
        
        return temp_head.next  # Return the next node of the temporary head (actual head of the modified list)


# java
"""
import java.util.HashMap;

class Solution {
    public ListNode deleteDuplicatesUnsorted(ListNode head) {
        HashMap<Integer, Integer> repeatedNodes = new HashMap<>();
        
        // First pass: Count the frequency of each node's value
        ListNode curr = head;
        while (curr != null) {
            repeatedNodes.put(curr.val, repeatedNodes.getOrDefault(curr.val, 0) + 1);
            curr = curr.next;
        }
        
        // Create a dummy node to handle edge cases
        ListNode tempHead = new ListNode(0);
        tempHead.next = head;
        
        ListNode prev = tempHead;
        curr = head;
        
        // Second pass: Remove nodes with a frequency greater than 1
        while (curr != null) {
            if (repeatedNodes.get(curr.val) > 1) {
                prev.next = curr.next; // Skip the current node
            } else {
                prev = curr; // Move prev only if the current node is not deleted
            }
            curr = prev.next; // Move to the next node
        }
        
        return tempHead.next; // Return the head of the modified list
    }
}
"""

