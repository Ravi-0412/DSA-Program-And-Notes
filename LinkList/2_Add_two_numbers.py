# just read the input from left to right
# find the sum of val of both the link list at same position + quotient of pre sum
# take remainder of above, remainder will be the new node
# quotient will be the new quotient for next node

# time: O(m+n)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2, pre, remainder, quotient= l1, l2, None, 0, 0
        ans= None # to return the ans
        # till any of one becomes None
        while curr1 and curr2:
            temp= curr1.val + curr2.val + quotient
            remainder= temp%10
            curr= ListNode(remainder)
            quotient= temp//10
            if ans== None:
                ans= curr
                pre= curr
            else:
                pre.next= curr
                pre= curr
            curr1= curr1.next
            curr2= curr2.next
        # if first linklist is not None
        while curr1:
            temp= curr1.val + quotient
            remainder= temp%10
            curr= ListNode(remainder)
            quotient= temp//10
            print(quotient)
            pre.next= curr
            pre= curr
            curr1= curr1.next
        # if second linklist is not None
        while curr2:
            temp= curr2.val + quotient
            remainder= temp%10
            curr= ListNode(remainder)
            quotient= temp//10
            pre.next= curr
            pre= curr
            curr2= curr2.next
        # at last check for quotient== 1
        # corner case if there is quotient at the end and both link point to the None
        if quotient== 1:
            curr= ListNode(1)
            pre.next= curr
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
