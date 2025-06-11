
# method 1: 
# time: O(n^2)
# logic: Just take each element one by one and search for its duplicates in the remaining list, just like we do for array(brute force)

class Solution:
    def removeDuplicates(self, head):
        current= head
        while current and current.next: # have to check till 'n-1'
            current1= current
            while current1.next:  # this will go till end
                if current.data== current1.next.data:
                    current1.next= current1.next.next   # assuming the next node after that we checked may be distinct
                else:
                    # here current1 already be pointing to the distinct node than 'current' so simply we have to current1 one step ahead
                    current1 = current1.next
            # now current.next will point to the next distinct ele 
            current = current.next
        return head


# my mistakes for same approach above
class Solution:
    def removeDuplicates(self, head):
        current= head
        while current and current.next: 
            current1= current.next
            while current1:  
                if current.data== current1.data:
                    current1.next= current1.next.next   # this will give error like 'None type object has no attribute next'
                                                        # as we are blindly pointing to 'next.next' 
                                                        # we can blindly only point to one node ahead from the node we are sure
                                                        # so to avoid this use the above logic (method 1)
                else:
                    current1= current1.next
            # now current.next will point to the next distinct ele 
            current= current.next
        return head

# method 2:
# sort the list and apply the concept of removing duplicates from the sorted list
# time: O(nlogn)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeDuplicates(self, head):
        # Step 1: Sort the list using merge sort
        head = self.sortList(head)

        # Step 2: Remove duplicates from sorted list
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

    def sortList(self, head):
        if not head or not head.next:
            return head
        # Split list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        # Recursive sort
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge sorted halves
        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next


# method 3:
# store the visited ele in set and for each ele whether that is present in set or not
# time: O(n), space: O(n)

def removeDuplicates(self, head):
        # Base case of empty list or
        # list with only one element
        if self.head is None or self.head.next is None:
            return head
        # Hash to store seen values
        hash = set()
        current = head
        hash.add(self.head.data)
        while current.next is not None:

            if current.next.data in hash:
                current.next = current.next.next
            else:
                hash.add(current.next.data)
                current = current.next

        return head

# Java Code 
"""
//Method 1
class ListNode {
    int data;
    ListNode next;
    ListNode(int data) {
        this.data = data;
    }
}

class Solution {
    public ListNode removeDuplicates(ListNode head) {
        ListNode current = head;

        while (current != null && current.next != null) {  // have to check till 'n-1'
            ListNode current1 = current;

            while (current1.next != null) {  // this will go till end
                if (current.data == current1.next.data) {
                    current1.next = current1.next.next;  // assuming the next node after that we checked may be distinct
                } else {
                    // here current1 already be pointing to the distinct node than 'current' so simply we have to current1 one step ahead
                    current1 = current1.next;
                }
            }

            // now current.next will point to the next distinct ele 
            current = current.next;
        }

        return head;
    }
}


//Method 2
class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public ListNode removeDuplicates(ListNode head) {
        // Step 1: Sort the list
        head = sortList(head);

        // Step 2: Remove duplicates from sorted list
        ListNode curr = head;
        while (curr != null && curr.next != null) {
            if (curr.val == curr.next.val) {
                curr.next = curr.next.next;
            } else {
                curr = curr.next;
            }
        }
        return head;
    }

    private ListNode sortList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode slow = head, fast = head.next;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode mid = slow.next;
        slow.next = null;
        ListNode left = sortList(head);
        ListNode right = sortList(mid);
        return merge(left, right);
    }

    private ListNode merge(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0), tail = dummy;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                tail.next = l1;
                l1 = l1.next;
            } else {
                tail.next = l2;
                l2 = l2.next;
            }
            tail = tail.next;
        }
        tail.next = (l1 != null) ? l1 : l2;
        return dummy.next;
    }
}



//Method 3
import java.util.HashSet;

class Solution {
    public ListNode removeDuplicates(ListNode head) {
        if (head == null || head.next == null) return head;

        HashSet<Integer> seen = new HashSet<>();
        ListNode current = head;
        seen.add(current.val);

        while (current.next != null) {
            if (seen.contains(current.next.val)) {
                current.next = current.next.next; // Removing duplicate
            } else {
                seen.add(current.next.val);
                current = current.next;
            }
        }

        return head;
    }
}
"""

# C++ Code 
"""
//Method 1
struct ListNode {
    int data;
    ListNode* next;
    ListNode(int x) : data(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* removeDuplicates(ListNode* head) {
        ListNode* current = head;

        while (current && current->next) {  // have to check till 'n-1'
            ListNode* current1 = current;

            while (current1->next) {  // this will go till end
                if (current->data == current1->next->data) {
                    current1->next = current1->next->next;  // assuming the next node after that we checked may be distinct
                } else {
                    // here current1 already be pointing to the distinct node than 'current' so simply we have to current1 one step ahead
                    current1 = current1->next;
                }
            }

            // now current->next will point to the next distinct ele 
            current = current->next;
        }

        return head;
    }
};


//Method 2
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int val) : val(val), next(nullptr) {}
};

class Solution {
public:
    ListNode* removeDuplicates(ListNode* head) {
        // Step 1: Sort the list
        head = sortList(head);

        // Step 2: Remove duplicates
        ListNode* curr = head;
        while (curr && curr->next) {
            if (curr->val == curr->next->val) {
                curr->next = curr->next->next;
            } else {
                curr = curr->next;
            }
        }
        return head;
    }

    ListNode* sortList(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode* slow = head, *fast = head->next;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* mid = slow->next;
        slow->next = nullptr;
        ListNode* left = sortList(head);
        ListNode* right = sortList(mid);
        return merge(left, right);
    }

    ListNode* merge(ListNode* l1, ListNode* l2) {
        ListNode dummy(0), *tail = &dummy;
        while (l1 && l2) {
            if (l1->val < l2->val) {
                tail->next = l1;
                l1 = l1->next;
            } else {
                tail->next = l2;
                l2 = l2->next;
            }
            tail = tail->next;
        }
        tail->next = l1 ? l1 : l2;
        return dummy.next;
    }
};


//Method 3
#include <unordered_set>

class Solution {
public:
    ListNode* removeDuplicates(ListNode* head) {
        if (!head || !head->next) return head;

        unordered_set<int> seen;
        ListNode* current = head;
        seen.insert(current->val);

        while (current->next) {
            if (seen.find(current->next->val) != seen.end()) {
                current->next = current->next->next; // Removing duplicate
            } else {
                seen.insert(current->next->val);
                current = current->next;
            }
        }

        return head;
    }
};
"""