# time= space= O(n)
# Analyse very properly and write the logic in notes.

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode(0)
        dummy.next= head
        cur= head
        prefixSum= {0: dummy}  # [presum: cur]. prefix calculates the prefix sum from the first node to the current cur node.
                        # if we remove this extra sum(cursum- k),k= 0 here. then we can get sum= 0 from 'node.next' in hashmap  till cur.
        curSum= 0
        while cur:
            curSum+= cur.val
            # generalising from sum= 0 to sum= 'k'(here k= 0 only). storing only the last node for same 'curSum'. 
            # if same curSum i.e (curSum- k) is found then we can get sum== 'k' after last occurence of curSum til cur node.
            prefixSum[(curSum- 0)]= cur
            cur= cur.next
        
        curSum= 0
        # Go from the dummy node again to set the next node to be the last node for a prefix sum 
        head= dummy  # we will start connecting node from dummy only after removing
        while head:
            curSum+= head.val
            head.next= prefixSum[curSum].next   # remove the nodes 
            head= head.next
        return dummy.next


# my mistake:
# after removing there still can be such sequence 
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy= pre= ListNode(0)
        dummy.next= head
        cur= head
        prefixSum= {0: dummy}  # sum-> till node. if we remove this extra sum(cursum- k),k= 0 here. then we can get sum= 0 from 'node.next' in hashmap  till cur.
        curSum= 0
        while cur:
            curSum+= cur.val
            if (curSum- 0) in prefixSum:  # just generalise from sum= 0 to 'k'. 
                prefixSum[(curSum- 0)].next= cur.next   # we can get sum= 0. so just remove that zero sum part.
            if curSum not in prefixSum:
                prefixSum[curSum]= cur
            cur= cur.next
        return dummy.next
    

# tried to update the cursum with latest node but now diff type of error.
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode(0)
        dummy.next= head
        cur= head
        prefixSum= {0: dummy}  # sum-> till node. if we remove this extra sum(cursum- k),k= 0 here. then we can get sum= 0 from 'node.next' in hashmap  till cur.
        curSum= 0
        while cur:
            curSum+= cur.val
            if (curSum- 0) in prefixSum:  # just generalise from sum= 0 to 'k'. 
                prefixSum[(curSum- 0)].next= cur.next   # we can get sum= 0. so just remove that zero sum part.
            # if curSum not in prefixSum:
            #     prefixSum[curSum]= cur
            prefixSum[curSum]= cur
            cur= cur.next
        return dummy.next