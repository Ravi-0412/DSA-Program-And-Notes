# method 1: Brute force
# make two linklist i.e odd and even 
# At last add join last_node_odd_list -> first_node_even_list

# time= space= O(n).

# method 2: vvi
# simple only
# just change the pointer and keep making the even list and odd list internally.

# The idea is to split the linked list into 2 : one containing all odd nodes and other containing all even nodes. 
# And finally, attach the even node linked list at the end of the odd node linked list.
# To split the linked list into even nodes & odd nodes, we traverse the linked list and
# keep connecting the consecutive odd nodes and even nodes (to maintain the order of nodes) and save the pointer to the first even node.

# Note: whenver Q says to do in O(1) space then :
# 1) for array: swapping the ele should come into mind. Think how we can swap elements.
# 2) for linklist: changing the pointer should come into mind (similar to swaping only)

# time: O(n), space= O(1)
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd, even= head, head.next   # odd will start from 1st node and even node will start from 2nd node.
        evenHead= even  # for merging last node of odd with 1st node of even. evenHead will point to the 1st node of even linklist
        # we need to point 'next.next' for odd and even so check next of both to avoid 'next' for 'None' node.
        while odd.next and even.next:  
            odd.next, even.next= odd.next.next, even.next.next
            odd, even= odd.next, even.next
        # at last join 1st node of even with last node of odd
        odd.next= evenHead
        return head

# Four conditions that may come in mind for the while-loop:

# 1) odd and odd.next -> wrong when 1->2->3->4->None ( even nodes ) because even.next is None, which has no attribute 'next'
# 2) odd and even.next -> wrong when 1->2->3->4->5->None ( odd nodes ) because even is None, which has no attribute 'next'
# 3) even and odd.next -> wrong when 1->2->3->4->None ( even nodes ) because even.next is None, which has no attribute 'next'
# 4) even and even.next -> correct
# 1. when 1->2->3->4->5->None ( odd nodes ) even will become None first and at the same time, odd points at the last node of the linked list; therefore, breaks from the while loop.
# 2. when 1->2->3->4->None ( even nodes ) even.next will become None first and at the same time, odd points at the last-2 node of the linked list and even points at the last node of the linked list; therefore, breaks from the while loop.


