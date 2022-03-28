

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head== None or head.next==None:
            return head
        dummy= ListNode(0)
        dummy.next= head
        temp= dummy  # temp will always point to the distinct ele
        # and if no duplicates then it will always point to one node before current

        current= head
        while current!= None:
            while current.next!= None and current.next.val== temp.next.val:  # if duplicates 
                current= current.next
            # after updating check whether temp and current adjacent or not
            # as this while loop and break because of 1st condition also

            if temp.next==current:  # means no duplicates(adjacent)
                temp= current
            else:  # means till current it is duplicates
                temp.next= current.next

            current= current.next   
        return dummy.next

# my mistake: I was trying to do using only one while loop 