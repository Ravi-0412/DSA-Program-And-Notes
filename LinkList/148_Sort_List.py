# exactly same as merge sort of array just think how we can convert it for linklist

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:   
            return head
        middle_head= self.FindMiddle(head)
        # print(middle_head.val, middle_next_head.val)
        newHead1= self.sortList(head)      # i was not storing the returned value thats why took some time 
        newHead2= self.sortList(middle_head)
        # now use the concept of merging two sorted lists
        After_merging= self.mergeTwoLists(newHead1, newHead2)
        return After_merging
    
    def FindMiddle(self,head):
        slow, fast= head, head
        while fast.next and fast.next.next:
            slow= slow.next
            fast= fast.next.next
        # slow will point to the middle ele. In case of even no of ele it will point to 1st middle
        temp= slow.next
        slow.next= None   # Next of last node of 1st half as 'None'.
        return temp
    
#     def MergeList(self,list1,list2):     # recursion depth was exceeding so used iterative one
#         if not list1 or list2 and list1.val> list2.val:
#             list1, list2= list2, list2
#         list1.next= self.MergeList(list1.next, list2)
#         return list1 or list2

    def mergeTwoLists(self, list1,list2):
        dummy= temp= ListNode(0)
        while list1 and list2:
            if list1.val>=list2.val:   # will check the 1st ele in each list to which it is pointing
                temp.next= list2
                list2= list2.next
            else:
                temp.next= list1
                list1= list1.next
            # after each iteration make temp point to the list which has executed the 'if' statement
            temp= temp.next
        
        # if l1 is not none means remaining ele in l1 is greater than or equal
        # to all the elements of l2. so just make temp.next point to l1 or l2
        # whichever is not none
        
        temp.next= list1 or list2  
        return dummy.next