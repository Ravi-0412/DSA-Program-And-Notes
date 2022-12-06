
# very basic approach.. this can be modified to two pointer only curr_odd and pre
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode(0)
        dummy.next= head
        if head== None or head.next== None:
            return head
        # curr_even will point to the position from where we have to swap each time
        # curr_odd will point to one position before curr_even
        # pre will point to one position before curr_odd 
        curr_even, curr_odd, pre= head, dummy,dummy
        len= 1
        while curr_even.next:
            pre= curr_odd
            curr_odd= curr_even
            curr_even= curr_even.next
            len+= 1
            if len%2== 0:  # if len is even means we have to swap
                # changing the links to swap the pair
                pre.next= curr_even
                curr_odd.next= curr_even.next
                curr_even.next= curr_odd
                # now change the even and odd pointer to the rightmost swapped ele till now, to check for next pair
                curr_even= curr_odd
                curr_odd= curr_even
        return dummy.next



# 2nd method(better one):
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

        # if curr.next is not None it means we have seen the two nodes so swap.  
        # it basically confirming that remaining node is at least two
        while curr and curr.next: 
            pre.next= curr.next
            curr.next= pre.next.next
            pre.next.next= curr
            
            # now update the pre to current and current to next node 
            # Just change the pointer such that curr just point to the 1st ele of next swapa and pre just before that
            pre= curr
            curr= curr.next
        return dummy.next
