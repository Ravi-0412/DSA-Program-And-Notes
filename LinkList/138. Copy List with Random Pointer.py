# method 1, time:O(n), space: O(n)
"""
Traversing the linked list and creating a copy of each node in a hashmap, storing the mapping of original node to copied node.
Traversing the linked list again to set the next and random pointers of the copied nodes using the hashmap.
Returning the head of the copied linked list from the hashmap.
"""
"""
Analysis:
Time Complexity: O(n), where n is the number of nodes in the linked list. Each node is visited twice, once for copying and once for connecting pointers.
Space Complexity: O(n), where n is the number of nodes in the linked list. The hashmap stores a copy of each node.
"""

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


# Java
"""
class Solution {
    public Node copyRandomList(Node head) {
        // storing each node in hashmap so that we can connect the random pointer if random is not adjacent to the already connected node
        Map<Node, Node> oldToCopy = new HashMap<>();
        oldToCopy.put(null, null); 
        // initializing with null because for getting node again while connecting for last node it will give error as
        // 'next' will be null and also in case if 'random' will be null for any node

        Node cur = head;
        while (cur != null) {
            // create the copy node for each node and store the copy node w.r.t to the cur node as we have to connect all the copied node only
            Node copy = new Node(cur.val); // next and random will be 'null' for each node
            oldToCopy.put(cur, copy);
            cur = cur.next;
        }

        // now connect all the nodes using hashmap
        cur = head;
        while (cur != null) {
            Node copy = oldToCopy.get(cur);
            copy.next = oldToCopy.get(cur.next);
            copy.random = oldToCopy.get(cur.random);
            cur = cur.next;
        }

        return oldToCopy.get(head); // as 1st node in hashmap will contain the 1st node of copy node only
    }
}


"""


# C++
"""
class Solution {
public:
    Node* copyRandomList(Node* head) {
        // storing each node in hashmap so that we can connect the random pointer if random is not adjacent to the already connected node
        unordered_map<Node*, Node*> oldToCopy;
        oldToCopy[nullptr] = nullptr; 
        // initializing with nullptr because for getting node again while connecting for last node it will give error as
        // 'next' will be nullptr and also in case if 'random' will be nullptr for any node

        Node* cur = head;
        while (cur) {
            // create the copy node for each node and store the copy node w.r.t to the cur node as we have to connect all the copied node only
            Node* copy = new Node(cur->val); // next and random will be 'nullptr' for each node
            oldToCopy[cur] = copy;
            cur = cur->next;
        }

        // now connect all the nodes using hashmap
        cur = head;
        while (cur) {
            Node* copy = oldToCopy[cur];
            copy->next = oldToCopy[cur->next];
            copy->random = oldToCopy[cur->random];
            cur = cur->next;
        }

        return oldToCopy[head]; // as 1st node in hashmap will contain the 1st node of copy node only
    }
};


"""