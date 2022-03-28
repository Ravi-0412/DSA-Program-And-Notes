# submitted on leetcode

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head== None:
            return head
        temp= head  # temp will always point to the pre distinct ele
        current= head.next  # will point from the 2nd ele 
        while current!=None:
            if current.val== temp.val:  # if duplicates 
                temp.next= current.next  # skipping the duplicates
                # current.next= None
                current= temp.next   # in case of duplicates make current like this
            else:
                temp= current
                currrent= current.next  # simply incr curr if not duplicates
        return head
        