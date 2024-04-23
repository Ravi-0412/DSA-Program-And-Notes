# logic. 'K' right shift ka very basic meaning for any data structure like linklist or array:
#  last ke 'k' node ko aage lana h and
# last node ko 1st node ke saath attach kar dena h and next node after 'n-k' ko 
# 1st_node after rotation bna dena h.

# For left shift first 'k' node ko last me rakh dena h.

# finally what we have to do:
# 1) find the last node and length together in one traversal 
# 2) find the next node after 'n-k' node
# 3) store the next node after 'n-k' node say in 'head_node_after_rotation' 
# and make next of 'n-k' as None and make last_node.next = 1st node && return 'the head_node_after_rotation'. 
# time: O(n), space: O(1)
# very good one

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head== None:
            return head
        curr = head
        n= 0  # for length
        last_node= None  # storing the last ele as we have to connect this next to head of current linklist
        while curr:
            n+= 1
            last_node= curr
            curr= curr.next
        k = k % n
        if k == 0:   # if 'k' is '0' or mutliple of length then we have to return the same linklist
            return head
        count =  1  # will go till 'n-k'
        cur = head
        while count < n- k :
            cur = cur.next
            count += 1

        head_node_after_rotation = cur.next
        cur.next = None
        last_node.next= head
        return head_node_after_rotation


# VVI: Another simpler way of doing above logic
# just find the kth node from end like we used to find.  this will be the head of the linklist after rotation 
# keep a pointer 'pre' that will point to one node before kth node from end. (just like finding kth and k+1 th node from end)
# make pre.next= None and last.next = head and make head = kth node from end and return head

# Must do code by above mentioned way later and by other approaches also.

# 2nd method : like array
# step: 1) starting till 'n-k' tak reverse karo then
# 2) last ka 'k' node ko reverse karke phle wale ke saath attach kar do
# 3) finally jo linlist upper aaya hoga usko reverse kar do pura