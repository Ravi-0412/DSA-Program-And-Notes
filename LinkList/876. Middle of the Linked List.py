# method 1: find the length and again traverse till middle
"""
Traverse the entire linked list to find its length.
Calculate the middle index as length // 2.
Traverse the list again to the middle index.
Return the node at that position.
"""
# Python
class Solution:
    def middleNode(self, head):
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        mid = length // 2
        temp = head
        for _ in range(mid):
            temp = temp.next
        
        return temp

"""
# Java
class Solution {
    public ListNode middleNode(ListNode head) {
        int length = 0;
        ListNode temp = head;
        while (temp != null) {
            length++;
            temp = temp.next;
        }
        
        int mid = length / 2;
        temp = head;
        for (int i = 0; i < mid; i++) {
            temp = temp.next;
        }
        
        return temp;
    }
}

# C++
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        int length = 0;
        ListNode* temp = head;
        while (temp != nullptr) {
            length++;
            temp = temp->next;
        }
        
        int mid = length / 2;
        temp = head;
        for (int i = 0; i < mid; i++) {
            temp = temp->next;
        }
        
        return temp;
    }
};
METHOD 1 Analysis:
Time Complexity: O(N) — first pass to calculate length + second pass to reach middle
Space Complexity: O(1) — only a few pointers and counters used
"""



# method 2: by storing node in the array
"""
just traverse the list and go on keeping the node in the array till arr[-1].next is not None
after that just return the middle ele of array 
since in array we can retrieve each node by index
Method 2 Analysis:
Time Complexity: O(N) — traverse list once
Space Complexity: O(N) — extra array/list to store all nodes
"""

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr= [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr)//2]

"""
# Java
class Solution {
    public ListNode middleNode(ListNode head) {
        List<ListNode> arr = new ArrayList<>();
        arr.add(head);
        while (arr.get(arr.size() - 1).next != null) {
            arr.add(arr.get(arr.size() - 1).next);
        }
        return arr.get(arr.size() / 2);
    }
}

# C++
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        vector<ListNode*> arr;
        arr.push_back(head);
        while (arr.back()->next != nullptr) {
            arr.push_back(arr.back()->next);
        }
        return arr[arr.size() / 2];
    }
};


"""

# method 3: better than all
"""
using double pointer slow and fast
slow will incr by one and fast will incr by two step

Note: # fast will point to last node or none after the loop will break
slow will point to 'middle' node in case of odd no of element and '2nd middle' in case of even no of element.

Method 3 Analysis:
Time Complexity: O(N) — one pass through the list
# Space Complexity: O(1) — only two pointers used
"""
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

"""
# Java
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}

// For getting the 1st middle in case of even no of elements.
class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}


# C++
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode *slow = head, *fast = head;
        while (fast != nullptr && fast->next != nullptr && fast->next->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
};

// For getting the 1st middle in case of even no of elements.
class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}
"""