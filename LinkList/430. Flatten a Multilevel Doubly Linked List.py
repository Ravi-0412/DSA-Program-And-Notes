# simple and straight
# time: O(n), space: O(1)
# bottom up
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head== None:
            return head
        remaining_child= None
        temp= head.next
        if head.child:  # first we have to add the child node. after head then child then next
            remaining_child= self.flatten(head.child)
            head.next= remaining_child   # we have to add with 'next' pointer for ans always
            remaining_child.prev= head
        if temp!= None:  # check for next node 
            remaining_nxt= self.flatten(temp)
            if remaining_child:  # add the remaining next after the last node of child node if child is not None
                curr= remaining_child
                while curr.next:   # we are traversing in ans and in ans there is only 'next' pointer
                    curr= curr.next
                curr.next= remaining_nxt
                remaining_nxt.prev= curr
            else:  # if empty then directly add the next to head
                head.next= remaining_nxt
                remaining_nxt.prev= head
        head.child= None  #while backtrack make child pointer as 'None' 
        return head


# try by this also and other approaches as well later.
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/solutions/150321/easy-understanding-java-beat-95-7-with-explanation/