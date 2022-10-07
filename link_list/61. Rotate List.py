# logic. 'K' right shift ka very basic meaning for any data structure like linklist or array:
#  last ke 'k' node ko aage lana h aur
# last node ko 1st node ke saath attach kar dena h and next node after 'n-k' ko 
# 1st_node after rotation bna dena h

# finally what we have to do:
# 1) find the last node ane length togetehr in one traversal 2) find the next node after 'n-k' node
# 3) store the next node after 'n-k' node say in 'head_node_after_rotation' and make next of 'n-k' as None and return 'the head_node_after_rotation' 
# time: O(n), space: O(1)
# very good one

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head== None:
            return head
        curr= head
        n= 0  # for length
        last_node= None  # storing the last ele as we have to connect this next to head of current linklist
        while curr:
            n+= 1
            last_node= curr
            curr= curr.next
        k= k% n
        if k==0:   # if 'k' is '0' or mutliple of length then we have to return the same linklist
            # this will be the corner case for this logic as we are making the next node after 'n-k' as 1st node and in this case last node will be the last node only
            return head
        # just we have bring nodes after 'n-k' position(1,2...) at start and attach the last node with the head 
        # anf after that make the node just after 'n-k' position as head
        count= 0  # will go till 'n-k'
        move_forward= n-k
        curr= head
        head_node_after_rotation= None
        while curr:
            count+= 1
            if count== move_forward:
                head_node_after_rotation= curr.next
                curr.next= None  # making the last_node_after_rotation.next= None as this will only the last node after rotation
                break
            curr= curr.next
        last_node.next= head
        return head_node_after_rotation


# 2nd method : like array
# step: 1) starting till 'n-k' tak reverse karo then
# 2) last ka 'k' node ko reverse karke phle wale ke saath attach kar do
# 3) finally jo linlist upper aaya hoga usko reverse kar do pura