# Time: O(n), space: O(n)
# with the help of hashmap and doubly linked list
# Q: just we have to implement the LRU cache replacement Algo that we studied in OS.

# why hashmap + doubly linked list?
# Ans: we have to return the value of get function in O(1) => hashmap
# we have to put in O(1) and remove in O(1) by maintaing the property i.e we have to swap the nodes in O(1) => Doubly Linked List
# and all key-value pir should be connected also so using value as node pointer to itself and connecting all by linked list.


class Node:  # doubly Linked List with key-value pair.
    def __init__(self,key,val):
        self.key= key
        self.val= val
        self.Pre= None
        self.next= None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap= capacity
        self.cache= {}  # will map key to node. val will be node pointer containing key-value pair of itself.
        self.Lru= Node(0,0)  # Lru.next will always point to the least recently used Node. Keeping Lru left side of the list 
        self.Mru= Node(0,0)  # Mru.pre will always point to the most recently used Node. keeping Mru right side of the list
        self.Lru.next= self.Mru   # Lru will be leftmost side and mru will be on rightmost side.
        self.Mru.pre= self.Lru
        
    def Insert(self,node):
        # insertion will always happen at right side just before Mru as any inserted ele will become the Mru
        node_pre= self.Mru.pre   # storing the pre of mru
        self.Mru.pre.next= self.Mru.pre= node
        node.next, node.pre= self.Mru, node_pre

    # we will have to delete from any posistion like when put is called.
    def Delete(self, node):  
        # just we delete the middle node in doubly linked list.
        # first store the next and pre of node we want to delete.
        del_pre= node.pre
        del_nxt= node.next
        # now update the pointer like this to delete the node.
        del_pre.next= del_nxt
        del_nxt.pre= del_pre
        
    def get(self, key: int) -> int:
        # if key in cache, just delete from its position and keep it at the rightmost side as this is Mru now.
        # and return its val
        # if not present thn simply return -1
        if key in self.cache:
            self.Delete(self.cache[key])
            self.Insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        # if key in cache, just delete from its position and keep it at the rightmost side as this is Mru now.
        # after that insert it at the righmost side  as this is Mru now. we have to insert if not present also 
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