# method 1: Iterative
# https://leetcode.com/problems/reverse-linked-list-ii/solutions/30666/simple-java-solution-with-clear-explanation/
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy= ListNode(0)  # will help to handle the case when we will reverse from head also
        dummy.next= head
        pre, curr= None, dummy
        # first finding the start position of sublist which we have to reverse
        pos= 0
        while pos< left:
            pre= curr
            curr= curr.next
            pos+= 1
        
        # pre will point to one node before the sublist
        first= curr   # storing the first node of the sublist
        next= curr.next  # node from which we will change the direction
        # now reverse the list
        while pos< right:
            temp= next.next
            next.next= curr
            curr= next
            next= temp
            pos+= 1
        
        # now just make the pointer in order
        first.next= next
        pre.next=  curr
        return dummy.next


# method 2: Recursive

            