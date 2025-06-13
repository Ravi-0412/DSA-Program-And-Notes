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
This is not efficient because it checks the length of the linked list against a fixed maximum value (10001 in this case).
# This approach does not actually detect cycles; it only checks if the length exceeds a certain limit.

Analysis:
Time Complexity: O(n), where n is the number of nodes in the linked list.
Space Complexity: O(1), as it uses a constant amount of space for the length variable.
# This method does not correctly identify cycles in the linked list.
"""

# 2nd method : storing the address into the hashmap or set
# why set came into mind: since we have to find cycle means same address can't repeat again while traversing and
# set only store the unique values

"""
Analysis:
Time Complexity: O(n), where n is the number of nodes in the linked list.
Space Complexity: O(n), as it uses a hash map to store the addresses of nodes.
"""

# my mistake
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
        
# Correct solution 
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


# 3rd method
# mark the traversing node as 'visited'

"""
Analysis:
Time Complexity: O(n), where n is the number of nodes in the linked list.
Space Complexity: O(1), as it uses a constant amount of space by modifying the node values.
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if head.val == 'visited':  # means we have seen this node before only
                return True
            head.val = 'visited'
            head = head.next
        return False


# 4th method: Floyd's cycle detection algorithm(submitted on GFG)
# time: o(n), space= o(1)
# logic: move the slow pointer one step ahead and 'fast' pointer 
# two steps ahead. And if there will be any cycle then at some time 
# slow== fast means there exist a cycle  since 'fast' was ahead of slow and again they meet means there must be moving in a cycle
"""
Analysis:
Time Complexity: O(n), where n is the number of nodes in the linked list.
Space Complexity: O(1), as it uses a constant amount of space with two pointers (slow and fast).
NOTE : This method is efficient and widely used for cycle detection in linked lists.
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow= head, head
        while fast and fast.next : # fast: for no node and fast.next for incr the fast two times
            slow= slow.next
            fast= fast.next.next
            if slow== fast:
                return True
        return False


# java
"""
// Method 1:
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode first = head;
        int length = 0;

        while (first != null) {
            if (length > 10001) {
                return true;
            } else {
                first = first.next;
                length++;
            }
        }
        return false;
    }
}

// Method 2:
import java.util.HashSet;

public class Solution {
    public boolean hasCycle(ListNode head) {
        HashSet<ListNode> visited = new HashSet<>();
        ListNode temp = head;

        // traverse the linked list and track visited nodes using address
        while (temp != null) {
            if (visited.contains(temp)) {
                return true;  // means we are visiting that address again — loop detected
            } else {
                visited.add(temp);  // mark this node as visited
            }
            temp = temp.next;
        }
        return false;
    }
}


// Method 3:
public class Solution {
    public boolean hasCycle(ListNode head) {
        while (head != null) {
            if (head.val == Integer.MIN_VALUE) {  // means we have seen this node before
                return true;
            }
            head.val = Integer.MIN_VALUE;  // mark it visited
            head = head.next;
        }
        return false;
    }
}


// Method 4:
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode slow = head, fast = head;

        // fast: for null node check and fast.next to increment fast by two steps
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {
                return true;
            }
        }
        return false;
    }
}

"""


# C++
"""
// Method 1:
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* first = head;
        int length = 0;

        while (first != nullptr) {
            if (length > 10001) {
                return true;
            } else {
                first = first->next;
                length++;
            }
        }
        return false;
    }
};


// Method 2:
#include <unordered_set>

class Solution {
public:
    bool hasCycle(ListNode *head) {
        std::unordered_set<ListNode*> visited;
        ListNode* temp = head;

        // traverse the linked list and track visited nodes using address
        while (temp != nullptr) {
            if (visited.count(temp)) {
                return true;  // visiting this address again means a loop exists
            } else {
                visited.insert(temp);  // mark this node as visited
            }
            temp = temp->next;
        }
        return false;
    }
};


// Method 3:
#include <climits>

class Solution {
public:
    bool hasCycle(ListNode *head) {
        while (head != nullptr) {
            if (head->val == INT_MIN) {  // already visited
                return true;
            }
            head->val = INT_MIN;  // mark as visited
            head = head->next;
        }
        return false;
    }
};


// Method 4:
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* slow = head;
        ListNode* fast = head;

        // fast: for null node check and fast->next to increment fast by two steps
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;

            if (slow == fast) {
                return true;
            }
        }
        return false;
    }
};


"""