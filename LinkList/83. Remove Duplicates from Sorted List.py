
# method 1:
"""
As the list is sorted, we can use a two-pointer technique to remove duplicates.
We will traverse the list and compare each node with the next one. 
If they are the same, we skip the next node by changing the link. If they are different, we move to the next node.
Continue this until we reach the end of the list.
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head== None:
            return head
        # we are joining distinct node with the help of temp
        temp= head  # temp will always point to the pre distinct ele
        current= head.next  # will point from the 2nd ele 
        while current != None:
            if current.val == temp.val:  # if duplicates 
                temp.next = current.next  # skipping the duplicates, thinking next node might be distinct
            else:
                # here temp.next already be pointing to the distinct node than 'temp' so simply make temp = temp.next
                temp = temp.next
            current = current.next 
        return head
"""
Time Complexity: O(n) where n is the number of nodes in the linked list.
Space Complexity: O(1) as we are not using any extra space.
"""

# method 2 : concise and better way of method 1
# my mistake: i was missing 1st while loop


"""
What's make it concise and better?
This method is more concise because it uses a single pointer (curr) to traverse the list and remove duplicates in one pass.
It removes duplicates immediately by checking the next node's value against the current node's value, and if they match, it skips the next node.
It removes all duplicates immediately by skipping all consecutive nodes with the same value right away inside a nested loop.
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr= head   # cur will point to last distinct ele.
        while curr: 
            while curr.next and curr.next.val== curr.val:
                curr.next= curr.next.next
            curr= curr.next
        return head
"""
Time Complexity: O(n) where n is the number of nodes in the linked list.
Space Complexity: O(1) as we are not using any extra space.
"""



# method 3: By recursion 

# better one to understand:
# agar aage wala node ka value same h to hm apne aap ko usme include nhi kar sakte isliye 'head.next' return kar denge
# agar aage wala node ka value different h to hm apne aap ko usme include kar sakte isliye apna value include karke return kar denge, 
# isliye 'head' return kar rhe.

# Note: Har distinct element ka last node store hoga internally answer me.
# Only last distinct element will get added for each node.

def deleteDuplicates(self, head):
        if head and head.next:
            head.next = self.deleteDuplicates(head.next)
            return head.next if head.next.val == head.val else head
        return head   # will act as base case also

"""
Time Complexity: O(n) where n is the number of nodes in the linked list.
Space Complexity: O(n) due to the recursion stack.
"""


# java
"""
// Method 1 :
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return head;
        }
        // we are joining distinct node with the help of temp
        ListNode temp = head;        // temp will always point to the pre distinct ele
        ListNode current = head.next; // will point from the 2nd ele 
        while (current != null) {
            if (current.val == temp.val) {  // if duplicates
                temp.next = current.next;  // skipping the duplicates, thinking next node might be distinct
            } else {
                // here temp.next already be pointing to the distinct node than 'temp' so simply make temp = temp.next
                temp = temp.next;
            }
            current = current.next;
        }
        return head;
    }
}

// method 2
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode curr = head; // curr will point to last distinct ele.
        while (curr != null) {
            while (curr.next != null && curr.next.val == curr.val) {
                curr.next = curr.next.next;
            }
            curr = curr.next;
        }
        return head;
    }
}

// Method 3
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head != null && head.next != null) {
            head.next = deleteDuplicates(head.next);
            // agar aage wala node ka value same h to hm apne aap ko usme include nhi kar sakte isliye 'head.next' return kar denge
            // agar aage wala node ka value different h to hm apne aap ko usme include kar sakte isliye apna value include karke return kar denge,
            // isliye 'head' return kar rhe.
            return (head.next.val == head.val) ? head.next : head;
        }
        return head;   // will act as base case also
    }
}

"""

# C++
"""
// Method 1:

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == nullptr) {
            return head;
        }
        // we are joining distinct node with the help of temp
        ListNode* temp = head;         // temp will always point to the pre distinct ele
        ListNode* current = head->next; // will point from the 2nd ele 
        while (current != nullptr) {
            if (current->val == temp->val) {  // if duplicates
                temp->next = current->next;  // skipping the duplicates, thinking next node might be distinct
            } else {
                // here temp->next already be pointing to the distinct node than 'temp' so simply make temp = temp.next
                temp = temp->next;
            }
            current = current->next;
        }
        return head;
    }
};


// Method 2:
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* curr = head; // curr will point to last distinct ele.
        while (curr != nullptr) {
            while (curr->next != nullptr && curr->next->val == curr->val) {
                curr->next = curr->next->next;
            }
            curr = curr->next;
        }
        return head;
    }
};

// Method 3:
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (head != nullptr && head->next != nullptr) {
            head->next = deleteDuplicates(head->next);
            // agar aage wala node ka value same h to hm apne aap ko usme include nhi kar sakte isliye 'head.next' return kar denge
            // agar aage wala node ka value different h to hm apne aap ko usme include kar sakte isliye apna value include karke return kar denge,
            // isliye 'head' return kar rhe.
            return (head->next->val == head->val) ? head->next : head;
        }
        return head;  // will act as base case also
    }
};


"""