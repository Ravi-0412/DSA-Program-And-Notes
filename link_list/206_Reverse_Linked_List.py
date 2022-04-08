# method 1: Iterative(submitted on leetcode)
# time: o(n), space: o(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # first will point one step ahead of current, and current one step ahead of pre
        # what ever node we will pass in function, it will reverse all node from that node till end
        pre,current,first= None,head,head 
        while current:
            first= current.next  # storing the value of current.next to initialise(incr) current with first later
            current.next= pre    # chnaging the direction of current.next
            pre= current        # initi to change the direction of current in next step
            current= first      # move current one step forward
        return pre              # at last pre will point to the 1st node in reverse list
                                # and current and first will point to None

# Method 2: By recursion
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
