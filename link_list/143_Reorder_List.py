# first thing is how we will come to think that stack will be used here
# logic: since we have to take one ele from start and one from end 
# and this can only be done if we take a data structure on which we can operate from start and end in O(1)
# and this can be done by either a stack or a deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next== None:  # if there is only one ele present
            return head
        stack= []
        curr= head
        # 1st push all the element into stack
        while curr:
            stack.append(curr)
            curr= curr.next
        # now reorder the list just like we had thought for 'reverse list' 
        curr= head
        while True:
            lastNode= stack.pop()  # storing the last ele
            nextNode= curr.next   # storing the next ele from first 
            curr.next= lastNode   # point the starting ele to the current last ele
            lastNode.next= nextNode  # and last ele will be point to the next starting ele
            curr= nextNode  # next starting node to be reordered
            # for stopping condition 
            if curr.next== lastNode:  
                curr.next= None
                break
        return head


# Do by Deque later 
# Also try by two pointer without any extra space