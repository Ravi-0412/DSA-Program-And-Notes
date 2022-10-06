# Time: O(n), space: O(n)
# with the help of hashmap and doubly linked list

class Node:
    def __init__(self,key,val):
        self.key= key
        self.val= val
        self.Pre= None
        self.next= None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap= capacity
        self.cache= {}  # will map the key to node. val will be node pointer
        self.Lru= Node(0,0)  # Lru.next will always point to the least recently used Node. Keeping Lru left side of the list 
        self.Mru= Node(0,0)  # Mru.pre will always point to the most recently used Node. keeping Mru right side of the list
        self.Lru.next= self.Mru
        self.Mru.pre= self.Lru
        
    def Insert(self,node):
        # insertion will always happen at right side just before Mru as any inserted ele will become the Mru
        node_pre= self.Mru.pre
        self.Mru.pre.next= self.Mru.pre= node
        node.next, node.pre= self.Mru, node_pre

    def Delete(self, node):
        del_pre= node.pre
        del_nxt= node.next
        del_pre.next= del_nxt
        del_nxt.pre= del_pre
        
    def get(self, key: int) -> int:
        # if key in cache, just delete from its position and keep it at the rightmost side as this is Mru now
        # and return its val
        # if not present thn simply return -1
        if key in self.cache:
            self.Delete(self.cache[key])
            self.Insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        # if key in cache, just delete from its position and keep it at the rightmost side as this is Mru now
        # after that insert it at the righmost side  as this is Mru now. we have to insert if not present also 
        # if not present then add in hashmap 
        if key in self.cache:
            self.Delete(self.cache[key])
        self.cache[key]= Node(key,value)  # no need to write inside if because dictionary doesn't store duplicates key,val pair
        self.Insert(self.cache[key])
        if len(self.cache) >self.cap:
            # delete the Lru from the list i.e node just after the Lru pointer
            lst_used= self.Lru.next  # storing the node that we have to delete. lst_used: least recently used
            self.Delete(lst_used)
            # now delete Lru from hashmap also
            del self.cache[lst_used.key]