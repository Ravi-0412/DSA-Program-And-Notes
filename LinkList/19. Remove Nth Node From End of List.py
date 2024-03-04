
# 1st method: traversing the linked list two times.
# one for finding the length and 2nd for deleting the element
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int):      
        #create a dummy node at start and make it(dummy.next=head)           
        #point to the head to handle #the corner cases(like list             
        # containing only one element ii: when we are deleting the          
        #first element itself)
        # and at last retrun dummy.next
        dummy = ListNode(0)
        dummy.next= head
        # now find the length of link list
        current= head
        length= 0
        while current:
            length+= 1
            current= current.next
        # now initialise current = dummy
        # traverse till 'length-n'
        # after this current.next will point to the element we 
        # have to delete

        length=length-n
        first = dummy
        while length>0:
            length-= 1
            first= first.next

        # now change the pointer to delete the element
        first.next= first.next.next 
        return dummy.next 

# 2nd method(best one): in one travesal
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #create a dummy node at start and make it(dummy.next=head) to handle the corner cases like:
        # 1) when there is only one ele 2) when 1st ele is the nth from the last
        
        dummy = ListNode(0)
        dummy.next= head
        first = dummy
        second= dummy   
        # move the first n step ahead then start moving the second
        for i in range(n):
            first= first.next
        # now start incr the 'second' to maintain the difference bw first-second= n always
        # when first will reach the end, second will be pointing to the one node before the node that we have to delete                           
        while first.next:
            first= first.next
            second= second.next
        # now update the pointers
        second.next= second.next.next
        return dummy.next  

# just same logic as method 2
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy= ListNode()
        dummy.next= head
        slow, fast, count= dummy, head, 0
        # slow pointing to dummy to handle corner cases
        while fast.next:
            fast= fast.next
            count+= 1
            if count >=n:
                slow= slow.next
        slow.next= slow.next.next
        return dummy.next
        