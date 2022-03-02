# 1st method(best one):
# logic: just create a dummy node to handle the corner cases like :
# i) if there is only two elements
# ii)if there is more than two elements and we are swapping first two
# iii) if we are swapping last two elements
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if contains no or only one element
        if head== None or head.next== None: return head
        dummy = ListNode()
        dummy.next= head
        pre,curr= dummy,head
# just after seeing two elements we are swapping
# current will point to 1st element of swap and
# pre will follow the current 
        while curr and curr.next:
            # update the pointers to show 
            # after below three lines node will get swapped
            pre.next= curr.next
            curr.next= pre.next.next
            pre.next.next= curr
            
            # now update the pre to current and current to next node
            pre= curr
            curr= curr.next
        return dummy.next
