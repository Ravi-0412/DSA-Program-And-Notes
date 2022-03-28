# 2nd method(best one): in one travesal

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        #create a dummy node at start and make it(dummy.next=head)           
        # containing only one element ii: when we are deleting the          
        #point to the head to handle #the corner cases(like list             
        #first element itself
        # move the pointer 'first' to n step after beginning(like 1->4 for n=3)
        dummy = ListNode(0)
        dummy.next= head
        first = dummy
        second= dummy   
        # move the pointer 'first' to n step after beginning(1->4 for n=3) without incr 'second'
        for i in range(n+1):
            first= first.next
        # now start incr the 'second' to maintain the difference bw first-second= n always
        # after reaching the end , second.next will be= nth node from last
        # first will point to None 
        while first:
            first= first.next
            second= second.next
        # now update the pointers
        second.next= second.next.next
        return dummy.next     

        

# 1st method: traversing the linked list two times(leetcode accepted)
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

        length-= n
        first = dummy
        while length>0:
            length-= 1
            first= first.next

        # now change the pointer to delete the element
        first.next= first.next.next 
        return dummy.next 
