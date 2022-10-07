# very simple and straight
# time: O(n), space: O(1)
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head== None:
            return head
        remaining_child= None
        temp= head.next
        if head.child:
            remaining_child= self.flatten(head.child)
            head.next= remaining_child
            remaining_child.prev= head
        if temp!= None:
            remaining_nxt= self.flatten(temp)
            if remaining_child:
                curr= remaining_child
                while curr.next:
                    curr= curr.next
                curr.next= remaining_nxt
                remaining_nxt.prev= curr
            else:
                head.next= remaining_nxt
                remaining_nxt.prev= head
        head.child= None
        return head


# my mistake i was making but corrected by dry and run but took a lot of time

# i was writing 'pre' instead of 'prev'.. please go through the Q and syntax properly dont follow blindly as you were writing in other Q
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head== None:
            return head
        remaining_child= None
        temp= head.next
        if head.child:
            remaining_child= self.flatten(head.child)
            head.next= remaining_child
            remaining_child.prev= head
        if temp!= None:
            remaining_nxt= self.flatten(temp)
            if remaining_child:  
                # here i was making major mistake
                # i was connecting directly by this but we have to connect remaining_nxt by the last node of remaining_child
                remaining_child.next= remaining_nxt
                remaining_nxt.prev= remaining_child
            else:
                head.next= remaining_nxt
                remaining_nxt.prev= head
        head.child= None   # i was missing this so was getting error "not a valid doubly linked list"
        return head



# go through the other approaches in discussion and Neetcode video