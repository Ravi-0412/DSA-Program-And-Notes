# method 1: swapping the values(submitted on Leetcode)
# swapping type of q you can do by swapping the values but it's not a good method, good comapnies will not accept in interview
# not a good method.. Do by swapping nodes
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        beg,end, curr=head,head,head
        # beg point to kth element from beg 
        # end point to kth element from end
        count= 0
        while curr.next:
            curr= curr.next
            count+= 1
            if count< k:
                beg= beg.next
            if count>= k:
                end= end.next
        beg.val, end.val= end.val, beg.val
        return head


# 2nd method : found from submissions
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/discuss/1054370/Python-3-or-Swapping-NODES-or-Swapping-Values-or-One-Pass-or-Fully-explained
# very good one
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        left= right= head
        dummy= ListNode()
        dummy.next= head
        pre_left= pre_right= dummy  # initialisng with dummy as if we initailse with None, it won't work for k=1
        for i in range(1,k):  # should run k-1 times to point left to kth node from start
            pre_left= left
            left= left.next
        null_checker= left
        while null_checker.next:
            null_checker= null_checker.next
            pre_right= right
            right= right.next
        if left== right:
            return dummy.next
        pre_left.next, pre_right.next= right, left
        left.next, right.next= right.next, left.next
        return dummy.next

