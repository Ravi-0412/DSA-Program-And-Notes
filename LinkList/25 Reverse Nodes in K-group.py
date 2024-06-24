# time: O(n), space: O(1)
# did myself
# logic: just go on incrementing the count, when you see count== k reverse the node node k in group 
# by storing the head of th enode that has not beem reversed till now  thats all

class Solution:
    def reverseKGroup(self, head, k) :
        dummy = ListNode(0)
        reversed_till_now= dummy            # will point to last nodes of reversed list that are already reversed till now  
        remaining_node_to_reverse= head    # will point to head of nodes that are remaining to reverse
        count= 0
        curr= head       
        while curr:
            count+= 1
            if count == k:
                temp= curr.next   # head for next cycle
                curr.next= None
                reversed_till_now.next = self.reverseList(remaining_node_to_reverse)
                reversed_till_now = remaining_node_to_reverse   
                remaining_node_to_reverse= temp   # to check for next cycle
                curr= temp
                count= 0   # to check again in next cycle
            else:
                curr= curr.next
        # at last add the remaining node
        reversed_till_now.next = remaining_node_to_reverse
        return dummy.next
    
    def reverseList(self, head):
        pre,current= None,head 
        while current:  
            temp= current.next 
            current.next= pre    
            pre= current 
            current= temp
        return pre  


# go through the other approaches in discussion and Neetcode video


# Java
"""
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode(0);
        ListNode reversedTillNow = dummy;            // will point to last nodes of reversed list that are already reversed till now  
        ListNode remainingNodeToReverse = head;    // will point to head of nodes that are remaining to reverse
        int count = 0;
        ListNode curr = head;       
        while (curr != null) {
            count++;
            if (count == k) {
                ListNode temp = curr.next;   // head for next cycle
                curr.next = null;
                reversedTillNow.next = reverseList(remainingNodeToReverse);
                reversedTillNow = remainingNodeToReverse;   
                remainingNodeToReverse = temp;   // to check for next cycle
                curr = temp;
                count = 0;   // to check again in next cycle
            } else {
                curr = curr.next;
            }
        }
        // at last add the remaining node
        reversedTillNow.next = remainingNodeToReverse;
        return dummy.next;
    }
    
    private ListNode reverseList(ListNode head) {
        ListNode pre = null, current = head; 
        while (current != null) {  
            ListNode temp = current.next; 
            current.next = pre;    
            pre = current; 
            current = temp;
        }
        return pre;
    }
}


"""