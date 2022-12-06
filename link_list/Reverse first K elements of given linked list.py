# check this in Q: 206.reverse linklist 2

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.successor= None

        def ReverseN(head, n):
            if n==1 :
                self.successor= head.next   # storing the first node after 'n' into successor
                return head
            reverseHead= ReverseN(head.next, n-1)
            head.next.next= head
            head.next= self.successor   # at last first node(head) will point to the first node after 'n'
            return reverseHead
        
        return ReverseN(head, 7)

# method 2: Recursive
# not working: have to ask someone
# error: ReverseN is not adding the nodes after the range
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left== 1:  # now just reverse the first n 'right' nodes. only we have to reverse the node count= right-left
            return self.ReverseN(head, right, None)  # not able to globally declare the succesor so passed like this
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head
    
    def ReverseN(self,head, n, successor):
        if n==1 :
            successor= head.next   # storing the first node after 'n' into successor
            return head
        reverseHead= self.ReverseN(head.next, n-1, successor)
        head.next.next= head
        head.next= successor   # at last first node(head) will point to the first node after 'n'
        return reverseHead

        