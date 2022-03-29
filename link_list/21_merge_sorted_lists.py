# just same method as merging in arrays
# made the dummy node to point to 1st ele of the result
# after that only we have to link the nodes based on condition


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode(0)
        temp= dummy
        curr1= list1
        curr2= list2
        while curr1!=None and curr2!= None:
            if curr1.val>= curr2.val:
                temp.next= curr2
                temp= curr2
                curr2= curr2.next
            if curr2!= None and curr2.val> curr1.val:
                temp.next= curr1
                temp= curr1
                curr1= curr1.next
        print(dummy.next)
        if curr1!= None:
            temp.next= curr1
            temp= curr1
        if curr2!= None:
            temp.next= curr2
            temp= curr2
        return dummy.next


# method2: By iteration but very concise
# the list which has minimum ele, dummy.next will point to that node
# after that just make the links based on conditions

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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


# method 3: recursive way

# just conversion of above iterative method
def mergeTwoLists2(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2


# method 4: Recursive way but very much concise

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if not list1 or list1 and list1.val> list2.val:   # make sure whether list1 has minimum ele or not
                                                              # i.e we can start from list1 or not
                                                              # if not minimum then exchange the pointers
                list1, list2= list2, list1                    # we were only exchanging the pointers(point to min) in all the above cases
                                                              # in iterative(exchanging temp) and in recursion above one exchanging the list pointer
            list1.next= self.mergeTwoLists(list1.next,list2)  # now whichever list will have min ele will become 1st ele
        return list1 or list2                                 # return the list which is not 'None' at last 
