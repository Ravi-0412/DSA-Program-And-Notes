"""
with the help of hashmap and doubly linked list
Q: just we have to implement the LRU cache replacement Algo that we studied in OS.

why hashmap + doubly linked list?
Ans: we have to return the value of get function in O(1) => hashmap
The problem with dictionaries is that they usually don’t guarantee order in which they manage keys. 
So we don’t have a way to quickly remove least-recently-used items.
So we will connect all (key, val) pair with doubly linked list.
we have to put in O(1) and remove in O(1) by maintaing the property i.e 
we have to swap / delete the nodes in O(1) => Doubly Linked List

Note: After inserting if capacity got more than allowed one then , we need to remove the least recently used
and insert the current (key, value) as most recently used.
Both should be done in O(1) and only doubly linklist can perform any delete operation in O(1).
So we can't use singly linklist, it will take O(capacity) for delete operation.

Note: all key-value pair should be connected also in sequence they come 
so using value as node pointer to itself and connecting all by linked list.

Time: O(1) for each 'get' and 'put' , Space = O(Capacity) because maximum element can be this only at a time.
"""

class Node:  # doubly Linked List with key-value pair.
    def __init__(self,key,val):
        self.key= key
        self.val= val
        self.Prev= None
        self.next= None

class LRUCache:

    def __init__(self, capacity):
        self.cap= capacity
        self.cache= {}  # will map key to node. value will be node pointer containing key-value pair of itself.
                        # why storing ' node pointer ' in value?
                        # Because we will have to delete also the node corresonding to key while 'get' and 'put'.
                        # 
        self.Lru= Node(0,0)  # Lru.next will always point to the least recently used Node. Keeping Lru leftmost side of the list 
        self.Mru= Node(0,0)  # Mru.pre will always point to the most recently used Node. keeping Mru rightmost side of the list
        # connect 'Lru' and 'Mru' initially.
        # All nodes we will insert between these two nodes.
        self.Lru.next= self.Mru   
        self.Mru.prev= self.Lru
    
    # insertion will always happen at right side just before Mru as any inserted ele will become the Mru
    # Logic: Just we insert before a give node 'mru' in a doubly linklist.
    # Time : O(1)
    def Insert(self,node):
        # first connect the new_node to nodes on its next and prev.
        node.next, node.prev= self.Mru, self.Mru.prev
        # Now connect the existing nodes to new node.
        self.Mru.prev.next= self.Mru.prev= node

    # we will have to delete from any position like when put is called and capacity if full.
    # Time : O(1)
    def Delete(self, node):  
        # just like we delete the middle node in doubly linked list.
        # first store the next and pre of node we want to delete.
        # del_pre= node.pre
        # del_nxt= node.next
        # # now update the pointer like this to delete the node.
        # del_pre.next= del_nxt
        # del_nxt.pre= del_pre

        # In short
        node.prev.next, node.next.prev = node.next, node.prev
        
    def get(self, key):
        # if key in cache, just delete from its position and keep it at the rightmost side as this is Mru now.
        # and return its val
        # if not present then simply return -1
        if key in self.cache:
            self.Delete(self.cache[key])  # passing the node that we have to delete
            self.Insert(self.cache[key])
            return self.cache[key].val    # return the value of node associated with key.
        return -1
        
    def put(self, key, value):
        # if key in cache, just delete from its position.
        # after that insert it at the righmost side  as this is Mru now. 
        # we have to insert if not present also 
        # if not present then add in hashmap. 

        if key in self.cache:
            self.Delete(self.cache[key])
        self.cache[key]= Node(key,value)  
        self.Insert(self.cache[key])
        # after inserting check if capacity of cache is greater than given capacity.
        if len(self.cache) > self.cap:
            # delete the Lru from the list i.e node just after the Lru pointer
            lst_used= self.Lru.next  # storing the node that we have to delete. lst_used: least recently used
            self.Delete(lst_used)
            # now delete Lru from hashmap also
            del self.cache[lst_used.key]    # only in this case we need to delete from hashmap


    # other way of writing put but above one is more concise
    # def put(self, key, value): 
    #     if key in self.cache:
    #            self.Delete(self.cache[key])
    #         self.cache[key] = Node(key,value)
    #         self.Insert(self.cache[key])
    #     else:
    #         self.cache[key] = Node(key,value)
    #         if len(self.cache) > self.cap:
    #         # delete the Lru from the list i.e node just after the Lru pointer
    #         lst_used= self.Lru.next  # storing the node that we have to delete. lst_used: least recently used
    #         self.Delete(lst_used)
    #         # now delete Lru from hashmap also
    #         del self.cache[lst_used.key]    # only in this case we need to delete from hashmap
    #         self.Insert(self.cache[key])


# Method 2:
"""
Very concise code
Using Python inbuilt : OrderedDict (HashMap + DoublyLinkedList)

About: OrderedDict
from collections import OrderedDict

Internal Implementation
OrderedDict is essentially a Hybrid Data Structure. It combines:
1. A Hash Table (Standard Dict): For O(1) key-based lookups.
2. A Doubly Linked List: To maintain the order of insertion.

Internally, it keeps a "circular" doubly linked list. Each entry in the dictionary points to a node in the list. 
When you add a new key, it's appended to the end of the list. When you delete a key, the list pointers are "stitched" together to remove that node.

Key Inbuilt Functions & Complexity :
Function	                                        Description	                                                Time Complexity
1. d[key] = val	                            Inserts or updates a key.	                                            O(1)
2. d.popitem(last=True)	                Pops the last (MRU) or first (LRU) item.	                                O(1)
3. d.move_to_end(key, last=True)	        Moves an existing key to either end of the dict.	                    O(1)
4. reversed(d)	                        Iterates through the keys in reverse order.	                               O(1) (to start)
5. == (Equality)	            Checks if two OrderedDicts have the same content AND same order.	                 O(N)
"""

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        """
        Thought Process:
        OrderedDict maintains the order of insertion.
        We will treat the 'end' of the dict as Most Recently Used (MRU)
        and the 'beginning' as Least Recently Used (LRU).
        """
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        """
        Logic:
        1. If key not present, return -1.
        2. If present, move it to the end to mark it as 'Most Recently Used'.
        3. Return the value.
        """
        if key not in self.cache:
            return -1
        
        # move_to_end(key, last=True) sends the key to the rightmost side
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        """
        Logic:
        1. If key exists, update value and move to end (MRU).
        2. If new key, add it to the end.
        3. If we exceed capacity, pop from the beginning (LRU).
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        
        # Update or insert the value
        self.cache[key] = value
        
        # Check capacity
        if len(self.cache) > self.cap:
            # popitem(last=False) removes the first (leftmost) item
            self.cache.popitem(last=False)

# follow ups:
"""
Part 2: Extend the cache to support time-based expiration.
Each entry should expire after a fixed time window, for example 5 minutes.

Updated API:

class LRUCache:
    def __init__(self, capacity: int, expirationTime: int):
        pass
    def get(self, key: int) -> int:
        pass
    def put(self, key: int, value: int) -> None:
        pass

"""

import time

class Node:
    """
    Doubly Linked List node storing key-value pairs and a timestamp.
    """
    def __init__(self, key, val, timestamp):
        self.key = key
        self.val = val
        self.ts = timestamp
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int, expirationTime: int):
        """
        capacity: Maximum number of items allowed.
        expirationTime: Time in seconds before an item becomes stale.
        """
        self.cap = capacity
        self.ttl = expirationTime
        self.cache = {} # Map for O(1) access: {key: Node}
        
        # Dummy head (LRU) and tail (MRU) to simplify pointer logic
        self.Lru = Node(0, 0, 0)
        self.Mru = Node(0, 0, 0)
        self.Lru.next = self.Mru
        self.Mru.prev = self.Lru

    def _is_expired(self, node: Node) -> bool:
        """Logic: Check if current time is beyond the allowed window."""
        return (time.time() - node.ts) > self.ttl

    def get(self, key: int) -> int:
        """
        Logic:
        1. If key exists:
           a. Check if it's expired. If so, delete and return -1.
           b. If fresh, update its timestamp (Sliding Expiry).
           c. Move it to the MRU position (right side).
        2. Return value or -1.
        """
        if key in self.cache:
            node = self.cache[key]
            
            if self._is_expired(node):
                # Lazy eviction
                self._remove(node)
                del self.cache[key]
                return -1
            
            # Update timestamp to extend life (Sliding Expiration) . If fixed then we can remove this line
            node.ts = time.time()
            
            # Refresh position in LRU list
            self._remove(node)
            self._insert_mru(node)
            return node.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Logic:
        1. If key exists, remove the old node.
        2. Create and insert new node at MRU with current timestamp.
        3. If over capacity, remove the oldest (Lru.next).
        """
        if key in self.cache:
            self._remove(self.cache[key])
            
        # Create node with 'now' as the birthday
        new_node = Node(key, value, time.time())
        self.cache[key] = new_node
        self._insert_mru(new_node)
        
        # Evict based on capacity if necessary
        if len(self.cache) > self.cap:
            oldest_node = self.Lru.next
            self._remove(oldest_node)
            del self.cache[oldest_node.key]

    # --- DLL Internal Operations ---

    def _remove(self, node: Node):
        """Logic: Bypass the node by connecting its neighbors to each other."""
        p, n = node.prev, node.next
        p.next, n.prev = n, p

    def _insert_mru(self, node: Node):
        """Logic: Place node at the 'hot' end (just before the dummy Mru)."""
        # Current most-recent node
        prev_node = self.Mru.prev
        
        # Connect new node to Mru and the previous most-recent
        node.next = self.Mru
        node.prev = prev_node
        
        # Update neighbors to point back to the new node
        self.Mru.prev = node
        prev_node.next = node


# java
"""
class Node {
    int key, val;
    Node prev, next;

    public Node(int key, int val) {
        this.key = key;
        this.val = val;
    }
}

class LRUCache {
    int cap;
    Map<Integer, Node> cache;
    Node Lru, Mru;

    public LRUCache(int capacity) {
        this.cap = capacity;
        this.cache = new HashMap<>();
        // doubly Linked List with key-value pair.
        this.Lru = new Node(0, 0);  // Lru.next will always point to the least recently used Node. Keeping Lru leftmost side of the list 
        this.Mru = new Node(0, 0);  // Mru.pre will always point to the most recently used Node. keeping Mru rightmost side of the list
        this.Lru.next = this.Mru;
        this.Mru.prev = this.Lru;
    }

    // insertion will always happen at right side just before Mru as any inserted ele will become the Mru
    // Logic: Just we insert before a give node 'mru' in a doubly linklist.
    // Time : O(1)
    private void insert(Node node) {
        // first connect the new_node to nodes on its next and prev.
        node.next = Mru;
        node.prev = Mru.prev;
        // Now connect the existing nodes to new node.
        Mru.prev.next = node;
        Mru.prev = node;
    }

    // we will have to delete from any position like when put is called and capacity if full.
    // Time : O(1)
    private void delete(Node node) {
        // just like we delete the middle node in doubly linked list.
        // In short
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    public int get(int key) {
        // if key in cache, just delete from its position and keep it at the rightmost side as this is Mru now.
        // and return its val
        // if not present then simply return -1
        if (cache.containsKey(key)) {
            delete(cache.get(key)); // passing the node that we have to delete
            insert(cache.get(key));
            return cache.get(key).val; // return the value of node associated with key.
        }
        return -1;
    }

    public void put(int key, int value) {
        // if key in cache, just delete from its position.
        // after that insert it at the righmost side  as this is Mru now. 
        // we have to insert if not present also 
        // if not present then add in hashmap. 

        if (cache.containsKey(key)) {
            delete(cache.get(key));
        }
        cache.put(key, new Node(key, value));
        insert(cache.get(key));

        // after inserting check if capacity of cache is greater than given capacity.
        if (cache.size() > cap) {
            // delete the Lru from the list i.e node just after the Lru pointer
            Node lstUsed = Lru.next;  // storing the node that we have to delete. lst_used: least recently used
            delete(lstUsed);
            // now delete Lru from hashmap also
            cache.remove(lstUsed.key); // only in this case we need to delete from hashmap
        }
    }
}
"""


# C++
"""
class Node {
public:
    int key, val;
    Node* prev;
    Node* next;

    Node(int k, int v) {
        key = k;
        val = v;
        prev = nullptr;
        next = nullptr;
    }
};

class LRUCache {
private:
    int cap;
    unordered_map<int, Node*> cache;
    Node* Lru;
    Node* Mru;

public:
    LRUCache(int capacity) {
        cap = capacity;
        // doubly Linked List with key-value pair.
        Lru = new Node(0, 0); // Lru->next will always point to the least recently used Node. Keeping Lru leftmost side of the list 
        Mru = new Node(0, 0); // Mru->prev will always point to the most recently used Node. keeping Mru rightmost side of the list
        Lru->next = Mru;
        Mru->prev = Lru;
    }

    // insertion will always happen at right side just before Mru as any inserted ele will become the Mru
    // Logic: Just we insert before a give node 'mru' in a doubly linklist.
    // Time : O(1)
    void insert(Node* node) {
        // first connect the new_node to nodes on its next and prev.
        node->next = Mru;
        node->prev = Mru->prev;
        // Now connect the existing nodes to new node.
        Mru->prev->next = node;
        Mru->prev = node;
    }

    // we will have to delete from any position like when put is called and capacity if full.
    // Time : O(1)
    void deleteNode(Node* node) {
        // just like we delete the middle node in doubly linked list.
        // In short
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

    int get(int key) {
        // if key in cache, just delete from its position and keep it at the rightmost side as this is Mru now.
        // and return its val
        // if not present then simply return -1
        if (cache.find(key) != cache.end()) {
            deleteNode(cache[key]);
            insert(cache[key]);
            return cache[key]->val;
        }
        return -1;
    }

    void put(int key, int value) {
        // if key in cache, just delete from its position.
        // after that insert it at the righmost side  as this is Mru now. 
        // we have to insert if not present also 
        // if not present then add in hashmap. 

        if (cache.find(key) != cache.end()) {
            deleteNode(cache[key]);
        }
        cache[key] = new Node(key, value);
        insert(cache[key]);

        // after inserting check if capacity of cache is greater than given capacity.
        if (cache.size() > cap) {
            // delete the Lru from the list i.e node just after the Lru pointer
            Node* lstUsed = Lru->next;  // storing the node that we have to delete. lst_used: least recently used
            deleteNode(lstUsed);
            // now delete Lru from hashmap also
            cache.erase(lstUsed->key); // only in this case we need to delete from hashmap
        }
    }
};
"""
