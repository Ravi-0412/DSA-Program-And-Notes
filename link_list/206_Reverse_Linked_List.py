# method 1: Since we have to reverse, so stack should come into mind
# just push the node into the stack and then start poping
#  and keep making the updating the pointer

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head== None: return head
        stack= []
        curr= head
        while curr:
            stack.append(curr)
            curr= curr.next
        head= temp= stack.pop()
        while stack:
            temp.next= stack.pop()
            temp= temp.next
        # now temp will be pointing to the last node from reverse
        # so make temp.next= None
        temp.next= None
        return head


# method 2: Iterative(submitted on leetcode)
# time: o(n), space: o(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # first will point one step ahead of current, and current one step ahead of pre
        # what ever node we will pass in function, it will reverse all node from that node till end
        pre,current,first= None,head,head 
        while current:
            first= current.next  # you need to store current.next somewhere so that after reversing current ele , current point to his next to reverse that also
            current.next= pre    # change the direction of current ele i.e point to the ele before it
            pre= current        # we have to store current somewhere so that next time reversed ele point to this 
            current= first      # move current one step forward 
        return pre              # at last pre will point to the 1st node in reverse list
                                # and current and first will point to None

# Method 3: By recursion
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # at last current will point to None and
        # pre will point to last node
        # so make head point to pre
        # now it will start reversing the pointer like: current.next= pre
        # will execute in backward direction till first call
        def ReverseByRecursion(pre, current):  # whatever you will pass as current, from current
            if current== None:                 # it will reverse and at last will point to pre
                self.head= pre                  # which is None here since we have to reverse the whole
            else:
                ReverseByRecursion(current, current.next)
                current.next= pre
            return self.head
        return ReverseByRecursion(None, head)
