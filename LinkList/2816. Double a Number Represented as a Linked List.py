# just same as: "445. Add Two Numbers II"

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def addToFront(value, node):
            new = ListNode(value)
            new.next = node
            return new

        # make a linklist combine values(actual value, without carry) of both from left to right.
        res= None
        cur = head
        while cur:
            curSum = cur.val *2
            cur= cur.next
            res= addToFront(curSum, res)   # to reverse the direction just like above one

        # now propagate the carry from LSB to MSB if value of node in above formed linklist is >= 10 and update the node value.
        # And we have to reverse the direction also since we have to return ans MSB-->LSB.
        cur= res
        res, carry = None, 0
        while cur or carry:
            sumValue = carry
            if cur:
                sumValue += cur.val
                cur = cur.next
            carry, nodeValue= divmod(sumValue, 10)
            res = addToFront(nodeValue, res)
        return res


# Metho2: In single traversal
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val > 4:
            # Make a new node with value = 0 and make new node as 'head' and next of it = 'head'
            # just we are adding node at front with value = 0
            head = ListNode(0, head)
        node = head
        while node:
            node.val = (node.val * 2) % 10
            if node.next and node.next.val > 4:
                node.val += 1
            node = node.next
        return head
