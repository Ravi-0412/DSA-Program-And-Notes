
# time: O(n^2)
# space: O(1)
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode(0)
        pre= dummy  # it will point to the last node in sorted list till now. 
        # will tell the node from where we have to start checking for correct position. 
        # we will move 'pre' only to find the correct position and after finding the correct position 
        # we will insert node between 'pre' and 'pre.next'.
        while head:
            if pre.val > head.val:    # last sorted node agar bda (i.e pre) then hmko start se check karna hoga(dummy.next se). 
                                        # isliye pre= dummy kar do.
                pre= dummy            # otherwise we will start checking after the  last node in sorted list till now (i.e pre.next).
            # kyonki agar head >= pre.val se then head har ek node se >= till pre since till pre list already sorted h.
            # checking for correct position.
            while pre.next and pre.next.val < head.val:
                pre= pre.next
            # now we have found the correct position for 'head'. 
            temp= head.next    # to check for next node
            # insert the head between 'pre' and 'pre.next'.
            head.next= pre.next
            pre.next= head
            # update pre to last node of sorted list i.e head and head to 'temp'.
            pre= head
            head= temp
        return dummy.next
    
    