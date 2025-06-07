
# method 1:
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


# method 2 : concise way of method 1
# Better one
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr= head   # cur will point to last distinct ele.
        while curr: 
            while curr.next and curr.next.val== curr.val:
                curr.next= curr.next.next
            curr= curr.next
        return head
    
# my mistake: i was missing 1st while loop



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


# Java Code 
"""
//Method 1
class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) return head;

        ListNode temp = head;
        ListNode current = head.next;

        while (current != null) {
            if (current.val == temp.val) { // If duplicate
                temp.next = current.next; // Skip duplicate node
            } else {
                temp = temp.next; // Move to next distinct node
            }
            current = current.next;
        }

        return head;
    }
}
//Method 2
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode curr = head;

        while (curr != null) {
            while (curr.next != null && curr.next.val == curr.val) {
                curr.next = curr.next.next; // Skip duplicates
            }
            curr = curr.next;
        }

        return head;
    }
}
//Method 3
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head != null && head.next != null) {
            head.next = deleteDuplicates(head.next);
            return (head.next.val == head.val) ? head.next : head;
        }
        return head;
    }
}
"""

# C++ Code 
"""
//Method 1
#include <iostream>

using namespace std;

class ListNode {
public:
    int val;
    ListNode* next;

    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head) return head;

        ListNode* temp = head;  // temp will always point to last distinct node
        ListNode* current = head->next; // start from second node

        while (current) {
            if (current->val == temp->val) {  // If duplicate
                temp->next = current->next;  // Skip duplicate node
            } else {
                temp = temp->next; // Move to next distinct node
            }
            current = current->next;
        }

        return head;
    }
};
//Method 2
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* curr = head;

        while (curr) {
            while (curr->next && curr->next->val == curr->val) {
                curr->next = curr->next->next; // Skip duplicates
            }
            curr = curr->next;
        }

        return head;
    }
};
//Method 3
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (head && head->next) {
            head->next = deleteDuplicates(head->next);
            return (head->next->val == head->val) ? head->next : head;
        }
        return head;
    }
};
"""