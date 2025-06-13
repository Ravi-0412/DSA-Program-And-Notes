# Method 1: 

"""
Floyd's Cycle Detection Algorithm= > using slow and fast pointer.

1) Detect the Cycle
i) use two pointers. slow: moves 1 step at a time, fast: moves 2 steps at a time.
ii) If there is no cycle, fast will eventually reach the end (null) — return None.
iii) If there is a cycle, slow and fast will meet inside the loop.

2) Find the Start of the Cycle
i) Once they meet, we confirm a cycle exists.
ii) Reset one pointer to the head of the list.
iii) Keep the other pointer at the meeting point.
iv) Move both pointers one step at a time.
v) The node where they meet is the start of the cycle.

🔍 Why This Works:
e.g: 
i) Distance from head to start of cycle = x
ii) Distance from start to meeting point = y
iii) Cycle length = C
iv) Then x == C - y (modulo the cycle), so they will meet at the cycle start when
moved step-by-step from head and meeting point.
"""
# time: 0(n), space: O(1)

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
            slow,fast= head, head
            cycle= False  # this will check whether there exist cycle or not 
            # first check whether cycle exist or not 
            while fast and fast.next:
                slow, fast= slow.next, fast.next.next
                if slow== fast:
                    cycle= True
                    break
            if cycle== False:
                print("no cycle")
                return
            # if cycle exist now find the starting point
            slow1= head
            while slow1!= slow:
                slow1, slow= slow1.next, slow.next
            return slow

# Method 2:
# concise way of doing Method 1, in only one loop.
# time: 0(n), space: O(1)

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
            slow,fast= head, head 
            while fast and fast.next:
                slow, fast= slow.next, fast.next.next
                if slow== fast: # we have found the cycle , now check the node.
                    slow= head
                    while slow!= fast:
                        slow, fast= slow.next, fast.next
                    return slow
            print("no cycle")

# Java Code 
"""
// Method 1

public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode slow = head, fast = head;
        boolean cycle = false;  // this will check whether there exist cycle or not 

        // first check whether cycle exist or not 
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                cycle = true;
                break;
            }
        }

        if (!cycle) {
            System.out.println("no cycle");
            return null;
        }

        // if cycle exist now find the starting point
        ListNode slow1 = head;
        while (slow1 != slow) {
            slow1 = slow1.next;
            slow = slow.next;
        }
        return slow;
    }
}


//Method 2

public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode slow = head, fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {  // we have found the cycle , now check the node.
                slow = head;
                while (slow != fast) {
                    slow = slow.next;
                    fast = fast.next;
                }
                return slow;
            }
        }

        System.out.println("no cycle");
        return null;
    }
}
"""

# C++ Code 
"""
// Method 1

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode* slow = head;
        ListNode* fast = head;
        bool cycle = false; // this will check whether there exist cycle or not 

        // first check whether cycle exist or not 
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) {
                cycle = true;
                break;
            }
        }

        if (!cycle) {
            cout << "no cycle" << endl;
            return nullptr;
        }

        // if cycle exist now find the starting point
        ListNode* slow1 = head;
        while (slow1 != slow) {
            slow1 = slow1->next;
            slow = slow->next;
        }
        return slow;
    }
};



// Method 2

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;

            if (slow == fast) { // we have found the cycle , now check the node.
                slow = head;
                while (slow != fast) {
                    slow = slow->next;
                    fast = fast->next;
                }
                return slow;
            }
        }

        cout << "no cycle" << endl;
        return nullptr;
    }
};
"""

