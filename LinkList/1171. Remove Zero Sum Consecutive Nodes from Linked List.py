# Logic:
# Assume the input is an array like 'count subarray having sum = k' etc.
# Do you know how to solve it?
# Scan from the left, and calculate the prefix sum.
# Whenever meet the seen prefix,
# remove all elements of the subarray between them.

# Implementation:
# Iterate for the first time,
# calculate the prefix sum.

# Iterate for the second time,
# calculate the prefix sum,
# and directly skip to last occurrence of this prefix

# time= space= O(n)

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


# Reason for my mistakes:
# we are updating the pointer of ans when we find any possible ans.
# Hmko same curSum aage bhi mil sakta h and size is samay subarray ka bda hoga.(isi ke chalte mera ans galat aa rha).
# agar aage mila to ans ke saath hm connect nhi payenge "other nodes ko remove karke".

# How to solve this?
# since we have to get max nodes for a curSum so in 1st iteration we will store the prefixSum with last node.
# Then in 2nd iteratin we will move our pointer to the value of prefixSum (all these nodes will be part of ans).
# kyonki hmko duplicate curSum milne pe beech wala nodes ko remove kar denge (sum== 0 ya k mil jayega beech wala ko remove karke).

# yhi hm upper wale solution me kiye h.


# my mistake:
# after removing there still can be such sequence.
# Because here storing only first node for each 'curSum' so we may get more sequence even after removing. 
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
    
