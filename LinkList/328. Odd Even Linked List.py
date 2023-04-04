# method 1: Brute force
# make two linklist i.e odd and even 
# Tarverse th elist and if len is odd then add that node to odd list, else add to even list.
# store the first node of even list
# At last add join 1st node of even list to last node of odd list.

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
# 2) for linklist: changing the pointer should come into mind (similar to swaaping only)

# time: O(n), space= O(1)
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd, even= head, head.next   
        evenHead= even  # for merging last node of odd with 1st node of even. evenHead will point to the 1st node of even linklist
        # odd will point to even.next and even will point to even.next.next. so we have to check like this in while loop
        while even and even.next:  # while odd.next and even.next:   # this will also work
            odd.next, even.next= odd.next.next, even.next.next
            odd, even= odd.next, even.next
        # at last join 1st node of even with last node of odd
        odd.next= evenHead
        return head




