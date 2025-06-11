# 1st method:
# if there will be any cycle then length of the linked will
# be more than the maximum no of elements according to the given constraint
# just find the length if >maximum length of the linked list then there 
# will be a loop otherwise not
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first= head
        length= 0
        while first:
            if(length>10001):
                return True
            else:
                first= first.next
                length+= 1
        return False

"""
Method 1 is not efficient because it checks the length of the linked list against a fixed maximum value (10001 in this case).
# This approach does not actually detect cycles; it only checks if the length exceeds a certain limit.
Method 1 Analysis:
Time Complexity: O(n), where n is the number of nodes in the linked list.
Space Complexity: O(1), as it uses a constant amount of space for the length variable.
# This method does not correctly identify cycles in the linked list.
"""

# 2nd method : storing the address into the hashmap or set
# why set came into mind: since we have to find cycle means same address can't repeat again while traversing and
# set only store the unique values
# time: o(n), space: o(n)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        add = {}
        temp = head
        # traverse the link list and when you see any node
        # for 1st time then store 'True' at the address of that node
        # and if that adress is alreay present then return true
        while temp:
            if temp in add: return True  # means we are visiting that address 
                                          # again means there is a loop
            else: add[temp]= True # at address of temp, making the value =True   , we are storing against the node 
            # so it will take the address of that node automatically as node conatains more than one object
            temp = temp.next
        return False

"""
Method 2 Analysis:
Time Complexity: O(n), where n is the number of nodes in the linked list.
Space Complexity: O(n), as it uses a hash map to store the addresses of nodes.
"""

# my mistake in method 2 
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first= head
        hashmap= {}
        while first:
            if id(first) not in hashmap: # error in this line 
                hashmap[first.val]= id(first) # error in this line
                # giving error because since we are storing address against the value and ele in the list can repeat with different add
                # so everytime it will change the address when repeating ele will come
                first= first.next
            else:
                return True
        if first== None:
            return False
        

# 3rd method
# time: o(n), space= o(1)
# mark the traversing node as 'visited'
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if head.val == 'visited':  # means we have seen this node before only
                return True
            head.val = 'visited'
            head = head.next
        return False

"""
Method 3 Analysis:
Time Complexity: O(n), where n is the number of nodes in the linked list.
Space Complexity: O(1), as it uses a constant amount of space by modifying the node values.
"""

# 4th method: Floyd's cycle detection algorithm(submitted on GFG)
# time: o(n), space= o(1)
# logic: move the slow pointer one step ahead and 'fast' pointer 
# two steps ahead. And if there will be any cycle then at some time 
# slow== fast means there exist a cycle  since 'fast' was ahead of slow and again they meet means there must be moving in a cycle

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow= head, head
        while fast and fast.next : # fast: for no node and fast.next for incr the fast two times
            slow= slow.next
            fast= fast.next.next
            if slow== fast:
                return True
        return False

"""
Method 4 Analysis:
Time Complexity: O(n), where n is the number of nodes in the linked list.
Space Complexity: O(1), as it uses a constant amount of space with two pointers (slow and fast).
NOTE : This method is efficient and widely used for cycle detection in linked lists.
"""

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
    public boolean hasCycle(ListNode head) {
        ListNode first = head;
        int length = 0;

        while (first != null) {
            if (length > 10001) {
                return true;
            }
            first = first.next;
            length++;
        }
        return false;
    }
}
//Method 2
import java.util.HashSet;

class Solution {
    public boolean hasCycle(ListNode head) {
        HashSet<ListNode> seenNodes = new HashSet<>();
        ListNode temp = head;

        while (temp != null) {
            if (seenNodes.contains(temp)) {
                return true; // Found repeating node, cycle exists
            }
            seenNodes.add(temp);
            temp = temp.next;
        }

        return false;
    }
}
//Method 3
class Solution {
    public boolean hasCycle(ListNode head) {
        while (head != null) {
            if (head.val == -1) { // Marking visited nodes uniquely
                return true;
            }
            head.val = -1; // Mark node as visited
            head = head.next;
        }
        return false;
    }
}
//Method 4
class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode slow = head, fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                return true; // Cycle detected
            }
        }

        return false;
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
    bool hasCycle(ListNode* head) {
        ListNode* first = head;
        int length = 0;

        while (first) {
            if (length > 10001) {
                return true;
            }
            first = first->next;
            length++;
        }
        return false;
    }
};
//Method 2
#include <iostream>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool hasCycle(ListNode* head) {
        unordered_set<ListNode*> seenNodes;
        ListNode* temp = head;

        while (temp) {
            if (seenNodes.find(temp) != seenNodes.end()) {
                return true; // Found repeating node, cycle exists
            }
            seenNodes.insert(temp);
            temp = temp->next;
        }

        return false;
    }
};
//Method 3
class Solution {
public:
    bool hasCycle(ListNode* head) {
        while (head) {
            if (head->val == -1) { // Marking visited nodes uniquely
                return true;
            }
            head->val = -1; // Mark node as visited
            head = head->next;
        }
        return false;
    }
};
//Method 4
class Solution {
public:
    bool hasCycle(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) {
                return true; // Cycle detected
            }
        }

        return false;
    }
};
"""