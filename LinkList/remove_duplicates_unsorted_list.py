# this giving time out(on gfg) ,but correct only
# time: O(n^2)
# logic: Just take each element one by one and search for its duplicates in the remaining list, just like we do for array(brute force)

# method 1: 
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
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

class Solution {
    public ListNode removeDuplicates(ListNode head) {
        ListNode current = head;

        while (current != null && current.next != null) {
            ListNode current1 = current;

            while (current1.next != null) {
                if (current.val == current1.next.val) {
                    current1.next = current1.next.next; // Skipping duplicates
                } else {
                    current1 = current1.next;
                }
            }

            current = current.next; // Move to next distinct element
        }

        return head;
    }
}
//Method 2
import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public ListNode removeDuplicates(ListNode head) {
        if (head == null) return null;

        ArrayList<Integer> values = new ArrayList<>();
        ListNode current = head;

        while (current != null) {
            values.add(current.val);
            current = current.next;
        }

        Collections.sort(values);

        ListNode newHead = new ListNode(values.get(0));
        ListNode temp = newHead;

        for (int i = 1; i < values.size(); i++) {
            if (!values.get(i).equals(values.get(i - 1))) {
                temp.next = new ListNode(values.get(i));
                temp = temp.next;
            }
        }

        return newHead;
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
    ListNode* removeDuplicates(ListNode* head) {
        ListNode* current = head;

        while (current && current->next) {
            ListNode* current1 = current;

            while (current1->next) {
                if (current->val == current1->next->val) {
                    current1->next = current1->next->next; // Skipping duplicates
                } else {
                    current1 = current1->next;
                }
            }
            
            current = current->next; // Move to next distinct element
        }

        return head;
    }
};
//Method 2
#include <algorithm>
#include <vector>

class Solution {
public:
    ListNode* removeDuplicates(ListNode* head) {
        if (!head) return nullptr;

        vector<int> values;
        ListNode* current = head;

        while (current) {
            values.push_back(current->val);
            current = current->next;
        }

        sort(values.begin(), values.end());

        ListNode* newHead = new ListNode(values[0]);
        ListNode* temp = newHead;

        for (size_t i = 1; i < values.size(); i++) {
            if (values[i] != values[i - 1]) {
                temp->next = new ListNode(values[i]);
                temp = temp->next;
            }
        }

        return newHead;
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