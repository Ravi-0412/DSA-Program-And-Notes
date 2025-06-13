# Method 1:

"""
logic. 'K' right shift ka very basic meaning for any data structure like linklist or array:
 last ke 'k' node ko aage lana h and
last node ko 1st node ke saath attach kar dena h and next node after 'n-k' ko 
1st_node after rotation bna dena h.

For left shift first 'k' node ko last me rakh dena h.

finally what we have to do:
1) find the last node and length together in one traversal 
2) find the next node after 'n-k' node
3) store the next node after 'n-k' node say in 'head_node_after_rotation' 
and make next of 'n-k' as None and make last_node.next = 1st node && return 'the head_node_after_rotation'. 


Another simpler way of doing Method 1
just find the kth node from end like we used to find.  this will be the head of the linklist after rotation 
keep a pointer 'pre' that will point to one node before kth node from end. (just like finding kth and k+1 th node from end)
make pre.next= None and last.next = head and make head = kth node from end and return head

You can try this on your own.
"""
"""
Analysis:
Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse the list once to find the length and once more to find the new head.
Space Complexity: O(1), as we are not using any extra space for data structures.
"""

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head== None:
            return head
        curr = head
        n= 0  # for length
        last_node= None  # storing the last ele as we have to connect this next to head of current linklist
        while curr:
            n+= 1
            last_node= curr
            curr= curr.next
        k = k % n
        if k == 0:   # if 'k' is '0' or mutliple of length then we have to return the same linklist
            return head
        count =  1  # will go till 'n-k'
        cur = head
        while count < n- k :
            cur = cur.next
            count += 1

        head_node_after_rotation = cur.next
        cur.next = None
        last_node.next= head
        return head_node_after_rotation


# 2nd method : 
# just like array
# step: 1) starting till 'n-k' tak reverse karo then
# 2) last ka 'k' node ko reverse karke phle wale ke saath attach kar do
# 3) finally jo linlist upper aaya hoga usko reverse kar do pura
"""
Analysis:
Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse the list to find the length and then to find the new tail.
Space Complexity: O(1), as we are not using any extra space for data structures.
"""

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find the length of the list and the last node
        length = 1
        last_node = head
        while last_node.next:
            last_node = last_node.next
            length += 1
        
        # Step 2: Calculate effective rotations
        k = k % length
        if k == 0:
            return head
        
        # Step 3: Find the new tail (n-k) and new head (n-k+1)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        
        # Step 4: Rotate the list
        new_tail.next = None
        last_node.next = head
        
        return new_head


# Java
"""
// Method 1:
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null) return head;

        ListNode curr = head;
        int n = 0; // for length
        ListNode last_node = null; // storing the last ele as we have to connect this next to head of current linklist

        while (curr != null) {
            n++;
            last_node = curr;
            curr = curr.next;
        }

        k = k % n;
        if (k == 0) return head;  // if 'k' is '0' or multiple of length then we have to return the same list

        int count = 1; // will go till 'n-k'
        ListNode cur = head;
        while (count < n - k) {
            cur = cur.next;
            count++;
        }

        ListNode head_node_after_rotation = cur.next;
        cur.next = null;
        last_node.next = head;

        return head_node_after_rotation;
    }
}


// Method 2:
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null || k == 0) return head;

        // Step 1: Find the length of the list and the last node
        int length = 1;
        ListNode last_node = head;
        while (last_node.next != null) {
            last_node = last_node.next;
            length++;
        }

        // Step 2: Calculate effective rotations
        k = k % length;
        if (k == 0) return head;

        // Step 3: Find the new tail (n-k) and new head (n-k+1)
        ListNode new_tail = head;
        for (int i = 0; i < length - k - 1; i++) {
            new_tail = new_tail.next;
        }

        ListNode new_head = new_tail.next;

        // Step 4: Rotate the list
        new_tail.next = null;
        last_node.next = head;

        return new_head;
    }
}



"""

# C++
"""
// Method 1:
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head) return head;

        ListNode* curr = head;
        int n = 0; // for length
        ListNode* last_node = nullptr; // storing the last ele as we have to connect this next to head of current linklist

        while (curr) {
            n++;
            last_node = curr;
            curr = curr->next;
        }

        k = k % n;
        if (k == 0) return head;  // if 'k' is '0' or multiple of length then we have to return the same list

        int count = 1; // will go till 'n-k'
        ListNode* cur = head;
        while (count < n - k) {
            cur = cur->next;
            count++;
        }

        ListNode* head_node_after_rotation = cur->next;
        cur->next = nullptr;
        last_node->next = head;

        return head_node_after_rotation;
    }
};

// Method 2:
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || !head->next || k == 0) return head;

        // Step 1: Find the length of the list and the last node
        int length = 1;
        ListNode* last_node = head;
        while (last_node->next) {
            last_node = last_node->next;
            length++;
        }

        // Step 2: Calculate effective rotations
        k = k % length;
        if (k == 0) return head;

        // Step 3: Find the new tail (n-k) and new head (n-k+1)
        ListNode* new_tail = head;
        for (int i = 0; i < length - k - 1; i++) {
            new_tail = new_tail->next;
        }

        ListNode* new_head = new_tail->next;

        // Step 4: Rotate the list
        new_tail->next = nullptr;
        last_node->next = head;

        return new_head;
    }
};


"""