# time: O(n), space: O(1)
# did myself
# logic: just go on incrementing the count, when you see count== k reverse the node node k in group 
# by storing the head of th enode that has not beem reversed till now  thats all
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        reverse_count= 0  # to handle the corner case when we will reverse 1st time
        reversed_till_now= head            # will point to last nodes of reversed list that are already reversed till now before checking for next cycle
                                           # after 1st reverse it should point to head only so better initialise with 'head' itself
                                            # my mistake:  i initialsied reversed_till_now with 'None'
        remaining_node_to_reverse= head    # will point to head of nodes that are remaining to reverse
        curr_reversed_head= None       # will point to head of node that has been  reversed in current cycle
        count= 0
        curr= head       
        while curr:
            count+= 1
            if count== k:
                count= 0   # to check again in next cycle
                temp= curr.next
                curr.next= None
                reverse_count+= 1
                curr_reversed_head= self.reverseList(remaining_node_to_reverse)
                if reverse_count== 1:
                    # reverse_till_now= head   # no need to write this here as already initialised with 'head'
                    head= curr_reversed_head
                    
                else:
                    reversed_till_now.next= curr_reversed_head
                    reversed_till_now= remaining_node_to_reverse   
                remaining_node_to_reverse= temp   # to check for next cycle
                curr= temp 
            else:
                curr= curr.next
        # at last if count is less than k then simply add the remaining node to the already reversed node
        if count< k: 
            reversed_till_now.next= remaining_node_to_reverse
        return head    
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp,pre,current= None,None,head 
        while current:  
            temp= current.next 
            current.next= pre    
            pre= current 
            current= temp
        return pre          



# my mistakes and still don't know why giving error. have to ask someone
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        reverse_count= 0  # to handle the corner case when we will reverse 1st time
        reversed_till_now= None            # last nodes that are already reversed before checking for next cycle       
        remaining_node_to_reverse= head    # will point to head of nodes that are remaining to reverse
        pre_last_reversed_head= None       # will point to head of node that has been in  reversed in current cycle
        count= 0
        curr= head       
        while curr:
            count+= 1
            if count== k:
                count= 0   # to check again in next cycle
                temp= curr.next
                curr.next= None
                reverse_count+= 1
                pre_last_reversed_head= self.reverseList(remaining_node_to_reverse)  # 
                if reverse_count== 1:
                    print(head.val)
                    reverse_till_now= head   # for 1st time make reverse_till_now = head
                    print("rev: ", reverse_till_now.val)
                    head= pre_last_reversed_head                
                else:
                    print("rev1: ", reverse_till_now.val)
                    reversed_till_now.next= pre_last_reversed_head  # here giving error 'None type object has no attribute next' 
                                                                    # when initialisng Reverded_till_now with None but printing the val .. totally confused what's happening internally
                                                                    # giving correct result when initialsing with 'head
                        
                    reversed_till_now= remaining_node_to_reverse  
                remaining_node_to_reverse= temp   # to check for next cycle
                curr= temp 
            else:
                curr= curr.next
        if count< k:
            reversed_till_now.next= remaining_node_to_reverse
        return head
                    
                    
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp,pre,current= None,None,head 
        while current:  
            temp= current.next 
            current.next= pre    
            pre= current 
            current= temp
        return pre  


