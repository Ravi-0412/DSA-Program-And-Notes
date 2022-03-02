# method 1: swapping the values(submitted on Leetcode)
# not a good method.. Do by swapping nodes
# class Solution:
#     def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         curr_x,curr_y, first=head,head,head
#         # x point to kth element from beg 
#         # y point to kth element from end
#         count= 0
#         while first.next:
#             first= first.next
#             count+= 1
#             if count<=k-1:
#                 curr_x= curr_x.next
#             if count>= k:
#                 curr_y= curr_y.next
#         curr_x.val, curr_y.val= curr_y.val, curr_x.val
#         return dummy.next


# method 2: by making dummy node but missing few corner cases
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy= ListNode(0)
        dummy.next= head
        pre_x,curr_x, pre_y, curr_y, first= dummy,head,dummy,head,head
        # x point to kth element from beg 
        # y point to kth element from end
        count= 0
        while first.next:
            first= first.next
            count+= 1
            if count<=k-1:
                pre_x= curr_x
                curr_x= curr_x.next
            if count>= k:
                pre_y= curr_y
                curr_y= curr_y.next
        #dummy node will remove all the corner cases except 
        #when there will be two elements only
        if (curr_x== head and curr_y.next== None):
            dummy.next= curr_y
            curr_y.next= curr_x
            curr_x.next= None
            return dummy.next
        if (curr_y== head and curr_x.next== None):
            dummy.next= curr_x
            curr_x.next= curr_y
            curr_y.next= None
            return dummy.next
        else:
            temp = curr_y.next
            pre_x.next= curr_y
            pre_y.next= curr_x
            curr_x.next= temp
            curr_y.next= curr_x.next
            
            
            return dummy.next
        temp = curr_y.next
        pre_x.next= curr_y
        curr_y.next= curr_x.next
        curr_x.next= temp
        pre_y.next= curr_x
        return dummy.next