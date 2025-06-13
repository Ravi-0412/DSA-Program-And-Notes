
# 1st method: 
# traversing the linked list two times.
# one for finding the length and 2nd for deleting the element

"""
Analysis:
Time Complexity: O(m+n) where m is the length of the linked list and n is the position from the end.
Space Complexity: O(1) as we are not using any extra space.
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int):      
        #create a dummy node at start and make it(dummy.next=head)           
        #point to the head to handle the corner cases like i): list             
        # containing only one element ii): when we are deleting the          
        #first element itself) and at last retrun dummy.next
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

        length = length-n
        first = dummy
        while length > 0:
            length-= 1
            first= first.next

        # now change the pointer to delete the element
        first.next= first.next.next 
        return dummy.next 
    

# 2nd method
# Best one : in one travesal
"""
Analysis:
Time Complexity: O(m+n) where m is the length of the linked list and n is the position from the end.
Space Complexity: O(1) as we are not using any extra space.
"""

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


# Method 3: 
# just same logic as method 2 but in one pass.
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy= ListNode()
        dummy.next= head
        slow, fast, count= dummy, dummy, 0
        # slow pointing to dummy to handle corner cases
        while fast.next:
            fast= fast.next
            count += 1
            if count > n:
                slow= slow.next
        slow.next= slow.next.next
        return dummy.next
    


# Java

"""
// method 1: 
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // create a dummy node at start and make it (dummy.next = head)
        // to handle corner cases like:
        // 1) list containing only one element
        // 2) when we are deleting the first element itself
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        // find the length of linked list
        ListNode current = head;
        int length = 0;
        while (current != null) {
            length++;
            current = current.next;
        }

        // set current = dummy and traverse till (length - n)
        current = dummy;
        length = length - n;
        while (length > 0) {
            length--;
            current = current.next;
        }

        // now change the pointer to delete the element
        current.next = current.next.next;
        return dummy.next;
    }
}

// method 2:
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // create a dummy node at start and make it (dummy.next = head)
        // to handle corner cases like:
        // 1) when there's only one element
        // 2) when the 1st element is the nth from the last
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode first = dummy;
        ListNode second = dummy;

        // move the first pointer n steps ahead
        for (int i = 0; i < n; i++) {
            first = first.next;
        }

        // now move both pointers until first reaches end
        while (first.next != null) {
            first = first.next;
            second = second.next;
        }

        // remove the nth node from end
        second.next = second.next.next;
        return dummy.next;
    }
}


// method 3:
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // create a dummy node at start to handle corner cases
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode slow = dummy;
        ListNode fast = dummy;
        int count = 0;

        // move fast pointer and update count
        while (fast.next != null) {
            fast = fast.next;
            count++;
            if (count > n) {
                slow = slow.next;
            }
        }

        // remove the nth node from end
        slow.next = slow.next.next;
        return dummy.next;
    }
}

"""
        
# C++ Code 
"""
//Method 1
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // create a dummy node at start and make it (dummy->next = head)
        // to handle corner cases like:
        // 1) list containing only one element
        // 2) when we are deleting the first element itself
        ListNode* dummy = new ListNode(0);
        dummy->next = head;

        // find the length of linked list
        ListNode* current = head;
        int length = 0;
        while (current != nullptr) {
            length++;
            current = current->next;
        }

        // set current = dummy and traverse till (length - n)
        current = dummy;
        length = length - n;
        while (length > 0) {
            length--;
            current = current->next;
        }

        // now change the pointer to delete the element
        current->next = current->next->next;
        return dummy->next;
    }
};


//Method 2
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // create a dummy node at start and make it (dummy->next = head)
        // to handle corner cases like:
        // 1) when there's only one element
        // 2) when the 1st element is the nth from the last
        ListNode* dummy = new ListNode(0);
        dummy->next = head;

        ListNode* first = dummy;
        ListNode* second = dummy;

        // move the first pointer n steps ahead
        for (int i = 0; i < n; i++) {
            first = first->next;
        }

        // now move both pointers until first reaches end
        while (first->next != nullptr) {
            first = first->next;
            second = second->next;
        }

        // remove the nth node from end
        second->next = second->next->next;
        return dummy->next;
    }
};

// Method 3
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // create a dummy node at start to handle corner cases
        ListNode* dummy = new ListNode(0);
        dummy->next = head;

        ListNode* slow = dummy;
        ListNode* fast = dummy;
        int count = 0;

        // move fast pointer and update count
        while (fast->next != nullptr) {
            fast = fast->next;
            count++;
            if (count > n) {
                slow = slow->next;
            }
        }

        // remove the nth node from end
        slow->next = slow->next->next;
        return dummy->next;
    }
};

"""