# first thing is how we will come to think that stack will be used here
# logic: since we have to take one ele from start and one from end 
# and this can only be done if we take a data structure on which we can operate from start and end in O(1)
# and this can be done by either a stack or a deque
# time:O(n), space:O(n)
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next== None:  # if there is only one ele present
            return head
        stack= []
        curr= head
        # 1st push all the element into stack
        while curr:
            stack.append(curr)
            curr= curr.next
        curr= head
        # now take the 1st ele of linked list and 1st ele of stack and join them one after the other till it reaches the mid
        while True:
            lastNode= stack.pop()  # storing the last ele
            nextNode= curr.next   # storing the next ele from first 
            curr.next= lastNode   # point the starting ele to the current last ele
            lastNode.next= nextNode  # and last ele will be point to the next starting ele
            curr= nextNode  # next starting node to be reordered
            # for stopping condition 
            if curr.next== lastNode:  # if it reaches till midddle in case of odd no of ele and next niddle in case of even no of elements
                curr.next= None
                break
        return head


# another method: better one, have to do only by this
# steps: 1) reverse the ele after middle to end 
# 2) now merge the two list 
# time:O(n), space:O(1)

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast= head, head
        # finding the middle element
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
            
        second= slow.next   # this will point to 1st ele after the middle
        slow.next= None

        # In case of even no of element last pair will be already in 1st part and get included automatically
        # in case of odd no of ele , extra ele will be 1st part and will get included automatically.
        
        # now reverse from 1st ele after middle to last
        pre= None
        while second:
            nextNode= second.next
            second.next= pre
            pre= second
            second= nextNode
            
        # now merge the two list
        curr1, curr2= head, pre
        while curr1 and curr2:
            temp1, temp2= curr1.next, curr2.next
            curr1.next, curr2.next= curr2, temp1
            curr1, curr2= temp1, temp2
        return head


# another way of doing the same logic.
# Just change in merging logic.
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next== None or head.next.next== None:
            return head
        slow, fast= head, head
        # finding the middle element. in case of even find the 1st middle instead of 2nd
        while fast and fast.next and fast.next.next:
            slow= slow.next
            fast= fast.next.next 
        second= slow.next   # this will point to 1st ele after the middle
        slow.next= None
        
        # now reverse from 1st ele after middle to last
        pre= None
        while second:
            nextNode= second.next
            second.next= pre
            pre= second
            second= nextNode
            
        # now merge the two list
        # curr1: will always contain the 1st node from which we have to start to connect
        # curr2: will always contain the 2nd node to which we have to connect curr1.   curr1 - > curr2
        curr1, curr2= head, pre
        while curr1 and curr2:
            temp = curr1.next
            curr1.next= curr2
            curr1, curr2= curr2, temp   # swap the pointer
        return head


# java
"""
class Solution {
    public void reorderList(ListNode head) {
        if (head == null) return;

        // Step 1: Find the middle of the list
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Step 2: Reverse the second half of the list
        ListNode second = slow.next;
        slow.next = null;
        ListNode pre = null;
        while (second != null) {
            ListNode nextNode = second.next;
            second.next = pre;
            pre = second;
            second = nextNode;
        }

        // Step 3: Merge the two halves
        ListNode curr1 = head, curr2 = pre;
        while (curr1 != null && curr2 != null) {
            ListNode temp1 = curr1.next, temp2 = curr2.next;
            curr1.next = curr2;
            curr2.next = temp1;
            curr1 = temp1;
            curr2 = temp2;
        }
    }
}
"""