# method 1, time:O(n), space: O(n)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # storing each node in hashmap so that we can connect the random pointer if random is not adjacent to the already connected node
        OldToCopy= {None:None}    # [curNode: curNode_copy]
                    # initilasing with None because for geeting node again while connecting for last node it will give error as
                    # 'next' will be None and also in case if 'random' will be None for any node
        cur= head
        while cur:
            # create the copy node for each node and store the copy node w.r.t to the cur node as we have to connect all the copied node only
            copy= Node(cur.val)   # next and random will be 'none' for each node
            OldToCopy[cur]= copy  
            cur= cur.next
    
        # now connect all the nodes using hashmap
        cur= head
        while cur:
            copy= OldToCopy[cur]
            copy.next= OldToCopy[cur.next]
            copy.random= OldToCopy[cur.random]
            cur= cur.next
        return OldToCopy[head]  # as 1st node in hashmap will conatin the 1st node of copy node only

# Java Code 
"""
import java.util.HashMap;

class Node {
    int val;
    Node next, random;

    Node(int x) {
        val = x;
        next = random = null;
    }
}

class Solution {
    public Node copyRandomList(Node head) {
        HashMap<Node, Node> oldToCopy = new HashMap<>();
        oldToCopy.put(null, null); // Initialize to handle null cases

        Node cur = head;
        
        // First pass: Create copies of nodes and store in hashmap
        while (cur != null) {
            Node copy = new Node(cur.val);
            oldToCopy.put(cur, copy);
            cur = cur.next;
        }

        // Second pass: Connect next and random pointers
        cur = head;
        while (cur != null) {
            Node copy = oldToCopy.get(cur);
            copy.next = oldToCopy.get(cur.next);
            copy.random = oldToCopy.get(cur.random);
            cur = cur.next;
        }

        return oldToCopy.get(head); // Return copied head node
    }
}
"""

# C++ Code 
"""
#include <iostream>
#include <unordered_map>

using namespace std;

class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node(int x) : val(x), next(nullptr), random(nullptr) {}
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*, Node*> OldToCopy;
        OldToCopy[nullptr] = nullptr; // Initialize to handle 'nullptr' cases

        Node* cur = head;
        
        // First pass: Create copies of nodes and store in hashmap
        while (cur) {
            Node* copy = new Node(cur->val);
            OldToCopy[cur] = copy;
            cur = cur->next;
        }

        // Second pass: Connect next and random pointers
        cur = head;
        while (cur) {
            Node* copy = OldToCopy[cur];
            copy->next = OldToCopy[cur->next];
            copy->random = OldToCopy[cur->random];
            cur = cur->next;
        }

        return OldToCopy[head]; // Return copied head node
    }
};
"""
# my mistake : didn't understand the Q properly at all

# have to understand these solutions
# https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43484/C%2B%2B-6-lines-recursive-solution-using-memoization
# https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43491/A-solution-with-constant-space-complexity-O(1)-and-linear-time-complexity-O(N)

# java