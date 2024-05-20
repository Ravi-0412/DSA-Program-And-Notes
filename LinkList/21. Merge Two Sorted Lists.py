# just same method as merging in arrays
# made the dummy node to point to 1st ele of the result
# after that only we have to link the nodes based on condition

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
            else:
                temp.next= curr1
                temp= curr1
                curr1= curr1.next
            temp = temp.next
        # Connect the node which is still remaining
        # if curr1!= None:
        #     temp.next= curr1
        # if curr2!= None:
        #     temp.next= curr2
        temp.next = curr1 or curr2  # shortcut
        return dummy.next


# method 2: recursive way

# just conversion of above iterative method
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # base condition.. Both list can't be None at the same time
        # if l1 if None then return 'l2' and if 'l2' is None then return 'l1'. (This condition is short form of this meaning)
        if not l1 or not l2:   
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            # in this case starting node will be from 'l1' so return 'l1'
            return l1  
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            # in this case starting node will be from 'l1' so return 'l1'
            return l2


# method 3: Recursive way but very much concise
# just the above logic only 

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            # make sure whether list1 has minimum ele or not
            # i.e we can start from list1 or not
            # if not minimum then exchange the pointers
            # we were only exchanging the pointers(point to min) in all the above cases

            if list1.val> list2.val:
                # in iterative(exchanging temp) and in recursion above one exchanging the list pointer 
                # based on condition and exactly same here                       
                list1, list2= list2, list1                                                                                  
            list1.next= self.mergeTwoLists(list1.next,list2)  # now whichever list will have min ele will become 1st ele
        
        # if any of the list is None then return the list which is not 'None' at last 
        return list1 or list2                              


# Java
"""
// method 1: 

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(0);
        ListNode temp = dummy;
        ListNode curr1 = list1;
        ListNode curr2 = list2;

        while (curr1 != null && curr2 != null) {
            if (curr1.val >= curr2.val) {
                temp.next = curr2;
                curr2 = curr2.next;
            } else {
                temp.next = curr1;
                curr1 = curr1.next;
            }
            temp = temp.next;
        }

        // Connect the remaining nodes
        temp.next = (curr1 != null) ? curr1 : curr2;

        return dummy.next;
    }
}


// method 2: 
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        // Base condition: if either list is null, return the other list
        if (l1 == null) {
            return l2;
        } 
        if (l2 == null) {
            return l1;
        }

        // Recursive case: choose the smaller value node and recurse
        if (l1.val < l2.val) {
            l1.next = mergeTwoLists(l1.next, l2);
            return l1;
        } else {
            l2.next = mergeTwoLists(l1, l2.next);
            return l2;
        }
    }
}


// method 3:
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 != null && list2 != null) {
            // Ensure that list1 has the smaller element or swap pointers
            if (list1.val > list2.val) {
                ListNode temp = list1;
                list1 = list2;
                list2 = temp;
            }
            list1.next = mergeTwoLists(list1.next, list2);
        }
        
        // If either list is null, return the non-null list
        return list1 != null ? list1 : list2;
    }
}
"""