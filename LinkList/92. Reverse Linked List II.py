# Method 1: Most simplest
# Just same as reverse linklist

# Logic: just divide the list into three parts:
# 1) before start  2) given sublist  3) right of sublist
# e.g: head = [1,2,3,4,5, 6, 7], left = 3, right = 5
# divide like : [1, 2] , [3, 4, 5] , [6, 7]

# Now reverse the sublist.
# After reversing : [1, 2] , [5, 4, 3] , [6, 7]

# Now combine all three to get ans.

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        def reverseList(head) :
            if not head: return head 
            pre,current= None,head 
            while current:  
                temp= current.next  
                current.next= pre    
                pre= current        
                current= temp     
            return pre  


        dummy= ListNode(0)  # will help to handle the case when we will reverse from head also
        dummy.next= head
        pre = dummy 
        # first finding the start position of sublist which we have to reverse
        pos = 0
        while pos < left - 1:
            pre= pre.next
            pos+= 1
        # pre will point to one node before the sublist
        start = pre.next   # storing the first node of the sublist 
        # Now find the last node till where we have to reverse
        cur = pre
        while pos < right:   # you can also go from '0' to right-1' but to save extra O(n), we did like this.
            cur = cur.next
            pos += 1
        end = cur
        temp = end.next   # storing the 1st ele right of sublist
        end.next = None  # so that it only reverse till 'end' starting from 'start' node.  

        reversedList = reverseList(start)  # this will reverse the list starting from node 'start'.
                     # Since we have made 'end.next = None', it will reverse from [start, end]
        # Now combine three lists
        pre.next = reversedList   # pre.next pointing to 1st node in reversedList
        start.next = temp         # last node in reversedList (i.e start.next) poiting to 1st node to right of sublist.

        return dummy.next
        
        

# method 2: 
# Here just changing the pointer internally

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy= ListNode(0)  # will help to handle the case when we will reverse from head also
        dummy.next= head
        # We need a pointer before sublist say 'pre'
        pre = dummy
        for i in range(left -1):
            pre = pre.next
        
        start = pre.next   #  a pointer to the beginning of a sub-list that will be reversed
        # Note: We won't change 'pre' and 'start' pointer. Will only change its 'next'.
        then = start.next  # node from which we will change the direction (2nd node of sublist)

        # 1 - 2 -3 - 4 - 5 ; m=2; n =4 ---> pre = 1, start = 2, then = 3
        # dummy-> 1 -> 2 -> 3 -> 4 -> 5

        # 'pre.next'     will always point to the 1st node that we got after reversing till now.
        # 'start.next' : will point the node from which we have to reverse in next iteration
        
        for i in range(right - left):  # We need to range direction 'right - left'(length_sublist - 1) time.
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next   # will point the node from which we have to reverse in next iteration
        # first reversing : dummy->1 - 3 - 2 - 4 - 5; pre = 1, start = 2, then = 4
        # second reversing: dummy->1 - 4 - 3 - 2 - 5; pre = 1, start = 2, then = 5 (finish)
        return dummy.next


# method 2: Recursive

            