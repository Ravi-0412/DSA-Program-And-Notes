# method 1: try to understand all the methods properly later
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head== None or head.next==None:
            return head
        dummy= ListNode(0)  # need dummy node because 1st node can also have duplicates in this we will have to delete head also
        dummy.next= head     # need this to compare for first time
        pre= dummy  # pre will always point to the pre distinct ele having no duplicates.
        # and if no duplicates then it will always point to one node before current

        current= head
        while current!= None: 
            while current.next!= None and current.next.val== pre.next.val:  # if duplicates only update curr pointer
                current= current.next
            # after updating check whether temp and current adjacent or not
            # as this while loop can  break because of 1st condition also

            if pre.next == current:  # means no duplicates(if pre and curr are  adjacent)
                pre= current  
            else:  # means till current it is duplicates
                pre.next= current.next

            current= current.next   
        return dummy.next

# java
"""
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode dummy = new ListNode(0); // need dummy node because 1st node can also have duplicates in this we will have to delete head also
        dummy.next = head; // need this to compare for first time
        ListNode pre = dummy; // pre will always point to the pre distinct ele having no duplicates.
                              // and if no duplicates then it will always point to one node before current
        ListNode current = head;

        while (current != null) {
            while (current.next != null && current.next.val == pre.next.val) { // if duplicates only update current pointer
                current = current.next;
            }

            // after updating check whether pre and current are adjacent or not
            // as this while loop can break because of the 1st condition also

            if (pre.next == current) { // means no duplicates (if pre and current are adjacent)
                pre = current;
            } else { // means till current it is duplicates
                pre.next = current.next;
            }

            current = current.next;
        }

        return dummy.next;
    }
}
"""

# my mistake: I was trying to do using only one while loop 


# method 2: More easier
class Solution:
    def deleteDuplicates(self, head): 
        dummy = ListNode(0);  # construct a dummy node
        dummy.next = head 

        pre = dummy           # set up pre and cur pointers
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                # loop until cur point to the last duplicates
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                pre.next = cur.next  # make pre point to curr.next as curr.next will be the ditinct ele so far 
                                    # but this can also have dupliactes later and we are checking in below if condition
            else:  # if different make pre like this since pre.next will be already pointing to our one of the ans
                pre = pre.next   # to connect next ele after pre.next
            cur = cur.next
        return dummy.next