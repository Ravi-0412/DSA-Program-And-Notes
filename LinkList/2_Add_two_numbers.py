# logic: Just we do the sum of two number given on paper.
# we keep on doing the sum either 1) first no has some ele remaining 2) second no has some ele remaining  3) carry is non zero
# here doing the same thing we are calculating the cursum of each position of l1 and l2, and adding with carry.

# Note: Here given LSB on left side, so we are calculating from left side only because in simple addition also we start from LSB only.
# We are exactly doing what we do in simple addition. we always start from LSB and go to MSB


# time: O(m+n)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans= None  # head for ans linklist
        cur= None  # for traversing into ans
        cur1= l1   # for traversing into l1
        cur2= l2   # for traversing into l2
        carry= 0   # will store the carry for next node
        while cur1 or cur2 or carry:
            curSum= carry
            if cur1:
                curSum+= cur1.val
                cur1= cur1.next
            if cur2:
                curSum+= cur2.val
                cur2= cur2.next
            carry= curSum // 10
            # now update the ans
            if ans:
                cur.next= ListNode(curSum % 10)
                cur= cur.next
            else:
                ans= ListNode(curSum % 10)
                cur= ans
        return ans


# very concise way of writing above code
# logic is same only but too concise

def addTwoNumbers(self, l1,l2):
        ans=curr= ListNode(0)  # creating a dummy node to handle inserting at first
        carry= 0
        while l1 or l2 or carry:  # we have to do addition till either first linklist 
                                # or 2nd linklist or carry is not None(or zero)
            v1,v2= 0,0  # to store the val of linklist1 and linklist2
            if l1: # if linklist1 is not None
                v1= l1.val
                l1= l1.next
            if l2:  # if linklist2 is not None
                v2= l2.val
                l2= l2.next
            # now we have push sum(v1+v2+carry)%10 into the new linklist
            # and carry will be equal to= sum(v1+v2+carry)//10 
            # we can update the values in one lines using divmod
            # https://www.tutorialsteacher.com/python/divmod-method
            carry, sum= divmod(v1+v2+carry,10)   # this will handle the case when both linklist or any of them will become None or zero
                                                 # and also when carry not equal to zero and both the linklist list is None
                                                 # since we are pushing modulo in ans linklist       
            curr.next= ListNode(sum)
            curr= curr.next
        return ans.next
