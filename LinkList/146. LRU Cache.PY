# Time: O(n), space: O(n)
# with the help of hashmap and doubly linked list
# Q: just we have to implement the LRU cache replacement Algo that we studied in OS.

# why hashmap + doubly linked list?
# Ans: we have to return the value of get function in O(1) => hashmap
# The problem with dictionaries is that they usually don’t guarantee order in which they manage keys. 
# So we don’t have a way to quickly remove least-recently-used items.
# So we will connect all (key, val) pair with doubly linked list.
# we have to put in O(1) and remove in O(1) by maintaing the property i.e 
# we have to swap / delete the nodes in O(1) => Doubly Linked List

# Note: After inserting if capacity got more than allowed one then , we need to remove the least recently used
# and insert the current (key, value) as most recently used.
# Both should be done in O(1) and only doubly linklist can perform any delete operation in O(1).
# So we can't use singly linklist, it will take O(capacity) for delete operation.

# Note: all key-value pair should be connected also in sequence they come 
# so using value as node pointer to itself and connecting all by linked list.


class Node:  # doubly Linked List with key-value pair.
    def __init__(self,key,val):
        self.key= key
        self.val= val
        self.Prev= None
        self.next= None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap= capacity
        self.cache= {}  # will map key to node. val will be node pointer containing key-value pair of itself.
        self.Lru= Node(0,0)  # Lru.next will always point to the least recently used Node. Keeping Lru leftmost side of the list 
        self.Mru= Node(0,0)  # Mru.pre will always point to the most recently used Node. keeping Mru rightmost side of the list
        # connect 'Lru' and 'Mru' initially.
        # All nodes we will insert between these two nodes.
        self.Lru.next= self.Mru   
        self.Mru.prev= self.Lru
    
    # insertion will always happen at right side just before Mru as any inserted ele will become the Mru
    # Time : O(1)
    def Insert(self,node):
        node_prev= self.Mru.prev   # storing the pre of mru
        self.Mru.prev.next= self.Mru.prev= node
        node.next, node.prev= self.Mru, node_prev

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
        node.prev.next= node.next
        node.next.prev= node.prev
        
    def get(self, key: int) -> int:
        # if key in cache, just delete from its position and keep it at the rightmost side as this is Mru now.
        # and return its val
        # if not present then simply return -1
        if key in self.cache:
            self.Delete(self.cache[key])  # passing the node that we have to delete
            self.Insert(self.cache[key])
            return self.cache[key].val    # return the value of node associated with key.
        return -1
        
    def put(self, key: int, value: int) -> None:
        # if key in cache, just delete from its position.
        # after that insert it at the righmost side  as this is Mru now. 
        # we have to insert if not present also 
        # if not present then add in hashmap. 

        if key in self.cache:
            self.Delete(self.cache[key])
        self.cache[key]= Node(key,value)  # Adding into cache. no need to write inside if because dictionary doesn't store duplicates key,val pair.
        self.Insert(self.cache[key])
        # after inserting check if capacity of cache is greater than given capacity.
        if len(self.cache) >self.cap:
            # delete the Lru from the list i.e node just after the Lru pointer
            lst_used= self.Lru.next  # storing the node that we have to delete. lst_used: least recently used
            self.Delete(lst_used)
            # now delete Lru from hashmap also
            del self.cache[lst_used.key]
