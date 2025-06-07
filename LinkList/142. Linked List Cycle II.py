# done the same thing in ' Q no: 287.Find Duplicates'
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


# concise way and doing in only one loop above logic
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
    public ListNode detectCycle(ListNode head) {
        ListNode slow = head, fast = head;
        boolean cycle = false; // This will check whether a cycle exists or not

        // Step 1: Check if cycle exists
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {
                cycle = true;
                break;
            }
        }

        if (!cycle) {
            System.out.println("No cycle");
            return null;
        }

        // Step 2: Find the start node of the cycle
        ListNode slow1 = head;
        while (slow1 != slow) {
            slow1 = slow1.next;
            slow = slow.next;
        }

        return slow;
    }
}
//Method 2
class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode slow = head, fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) { // Cycle detected, now find the start node
                slow = head;
                while (slow != fast) {
                    slow = slow.next;
                    fast = fast.next;
                }
                return slow;
            }
        }

        System.out.println("No cycle");
        return null;
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
    ListNode* detectCycle(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        bool cycle = false; // This will check whether a cycle exists or not

        // Step 1: Check if cycle exists
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;

            if (slow == fast) {
                cycle = true;
                break;
            }
        }

        if (!cycle) {
            cout << "No cycle" << endl;
            return nullptr;
        }

        // Step 2: Find the start node of the cycle
        ListNode* slow1 = head;
        while (slow1 != slow) {
            slow1 = slow1->next;
            slow = slow->next;
        }

        return slow;
    }
};
//Method 2
class Solution {
public:
    ListNode* detectCycle(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;

            if (slow == fast) { // Cycle detected, now find the start node
                slow = head;
                while (slow != fast) {
                    slow = slow->next;
                    fast = fast->next;
                }
                return slow;
            }
        }

        cout << "No cycle" << endl;
        return nullptr;
    }
};
"""