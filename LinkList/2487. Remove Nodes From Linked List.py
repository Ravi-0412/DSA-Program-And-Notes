# Logic: Reverse node and check.
# keep track of last node having greater value.

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverseLinkList(head):
            pre, current = None, head 
            while current:  
                temp = current.next  
                current.next = pre    
                pre = current        
                current = temp    
            return pre 

        head = reverseLinkList(head)
        last = head
        cur = head.next
        while cur:
            while cur and cur.val < last.val:
                cur = cur.next
            last.next = cur
            last = cur
            if cur:
                # cur might be null so first check then only update.
                cur = cur.next
        return reverseLinkList(head)


# Other way
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverseLinkList(head):
            pre, current = None, head 
            while current:  
                temp = current.next  
                current.next = pre    
                pre = current        
                current = temp    
            return pre 

        head = reverseLinkList(head)
        last = head
        cur = head
        while cur and cur.next:
            while cur.next and cur.next.val < last.val:
                cur = cur.next
            last.next = cur.next
            last = cur.next
            cur = cur.next

        return reverseLinkList(head)

        