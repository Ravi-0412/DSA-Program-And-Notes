# just similar as "2. Add Two numbers"

# Difference ?
# Ans: Here MSB on left side and LSB on right side.
# We always start to add number from LSB, so we have to start from right side only.

# Approach 1:
# Just reverse both the linklist then this Q get reduced to "2. Add Two numbers".

# Approach 2: Without reversing the input
# Since we have start from right side so one data structure which can help is stack.

# so put all ele value of l1 and l2 in two different stack.
# Then we can apply the same logi c as "2. Add Two numbers".

# But here we will reverse the direction of newNode since we have bring the MSB first.

# time= space= O(n + m)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans= None  # head of ans. first time newNode will be point to None only
        stackL1= []   # will store the node val of l1
        stackL2= []   # will store the node val of l2
        while l1:
            stackL1.append(l1.val)
            l1= l1.next
        while l2:
            stackL2.append(l2.val)
            l2= l2.next
        
        carry= 0
        while stackL1 or stackL2 or carry:
            curSum= carry
            if stackL1:
                curSum+= stackL1.pop()
            if stackL2:
                curSum+= stackL2.pop()
            # here changing the direction. LSB should go at last and MSB should come at first.
            # Just adding the new formed node to front. same as we reverse string by concatenating.
            newNode= ListNode(curSum % 10)
            newNode.next= ans
            ans= newNode
            carry= curSum //10
        return ans

# optimising space complexity to O(1)
# time: O(n+m)
# space= O(1)

# very good approach. 
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def size(cur):
            n= 0
            while cur:
                n+= 1
                cur= cur.next
            return n
        
        def addToFront(value, node):
            new= ListNode(value)
            new.next= node
            return new

        cur1, cur2= l1, l2
        s1, s2= size(cur1), size(cur2)

        # make a linklist combine values(actual value, without carry) of both from left to right but in reverse order.
        # Since we have to propagate the carry from LSB to MSB. so direction of linklist should from LSB--> MSB.
        res= None
        cur1, cur2= l1, l2
        while s1 and s2:    # or while cur1 and cur2:
            curSum= 0   # making the linklist from actual value 
            if s1 >= s2:
                curSum+= cur1.val
                cur1= cur1.next
                s1-= 1
            if s2 > s1:   # We will only add at the position and for this n2>n1 in case if we have decremented 'n1' above
                curSum+= cur2.val
                cur2= cur2.next
                s2-= 1
            res= addToFront(curSum, res)   # to reverse the direction

        # now propagate the carry from LSB to MSB if value of node in above formed linklist is >= 10 and update the node value.
        # And we have to reverse the direction also since we have to return ans MSB-->LSB.
        cur= res
        res, carry= None, 0
        while cur:
            sumValue= carry + cur.val
            carry, nodeValue= divmod(sumValue, 10)
            res= addToFront(nodeValue, res)
            cur= cur.next
        
        # at last carry can be non-zero(1) so for that we have to make one extra node
        if carry:
            res= addToFront(carry, res)
        return res