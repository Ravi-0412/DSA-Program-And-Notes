# method 1: find the length and again traverse till middle

# method 2: by storing node in the array
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # just traverse the list and go on keeping the node in the array till arr[-1].next is not None
        # after that just return the middle ele of array 
        # since in array we can retrieve each node by index
        arr= [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr)//2]


# method 3: better than all
# using double pointer slow and fast
# slow will incr by one and fast will incr by two step

# Note: # fast will point to last node or none after the loop will break
# slow will point to 'middle' node in case of odd no of element and '2nd middle' in case of even no of element.
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow= head, head
        while fast and fast.next:    # 'fast' will avoid checking for 'next' if 'fast' == None
            fast= fast.next.next
            slow= slow.next           
        return slow


# For getting the 1st middle in case of even no of elements.
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow= fast = head
        while fast and fast.next and fast.next.next:  
            slow, fast= slow.next, fast.next.next
        return slow

# Java Code 
"""
//Method 2
import java.util.ArrayList;

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

class Solution {
    public ListNode middleNode(ListNode head) {
        ArrayList<ListNode> arr = new ArrayList<>();
        arr.add(head);

        while (arr.get(arr.size() - 1).next != null) {
            arr.add(arr.get(arr.size() - 1).next);
        }

        return arr.get(arr.size() / 2); // Return middle node
    }
}
//Method 3
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) { // Move slow by one and fast by two
            slow = slow.next;
            fast = fast.next.next;
        }

        return slow; // Returns 2nd middle in case of even elements
    }
}
//Method to Get 1st Middle in Case of Even Nodes
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        return slow; // Returns 1st middle in case of even elements
    }
}
"""

# C++ Code 
"""
//Method 2
#include <vector>

class ListNode {
public:
    int val;
    ListNode* next;

    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        std::vector<ListNode*> arr;
        arr.push_back(head);

        while (arr.back()->next) {
            arr.push_back(arr.back()->next);
        }

        return arr[arr.size() / 2]; // Return middle node
    }
};
//Method 3
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast && fast->next) { // Move slow by one and fast by two
            slow = slow->next;
            fast = fast->next->next;
        }

        return slow; // Returns 2nd middle in case of even elements
    }
};
//Method to Get 1st Middle in Case of Even Nodes
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast && fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        return slow; // Returns 1st middle in case of even elements
    }
};
"""