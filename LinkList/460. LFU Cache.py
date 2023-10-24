class ListNode:
    def __init__(self, key , val):
        self.key = key
        self.val = val
        self.freq = 1   # New node will have freq= 1 automatically.
        self.prev = None
        self.next = None

# This we will pass as type inside 'freqTable'.
class DLL:
    def __init__(self):
        # Just same as 'LRU' because in case of same freq we have to remove 'least recently used'.
        self.Lru = ListNode(0, 0)
        self.Mru = ListNode(0, 0)
        self.Lru.next = self.Mru
        self.Mru.prev = self.Lru
        self.size = 0
    
    # same as 'LRU'. Key having same freq will be inserted at last i.e now will be most recently used.
    def insertAtLast(self, node):
        node_pre= self.Mru.prev   # storing the pre of mru
        self.Mru.prev.next= self.Mru.prev= node
        node.next, node.prev= self.Mru, node_pre
        self.size += 1

    # Remove any general node.  # same as 'LRU'
    def removeNode(self, node):
        node.prev.next= node.next
        node.next.prev= node.prev
        self.size -= 1
    
    def removeFirst(self):
        node_to_remove = self.Lru.next
        self.removeNode(node_to_remove)
        return node_to_remove

class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.freqTable = collections.defaultdict(DLL)  # will store (key, value) as linklist for each frequency.
        self.capacity = capacity 
        self.minFreq  = 0   # will keep track of minimum freq
    
    # will update the freq of given key and after that , it will remove cur node from prev freq and
    #  then will add the cur 'key-value' to new frequency.
    def updateCache(self, key, value):
        node = self.cache[key]
        node.val = value
        prevFreq = node.freq  # have to remove from this freq
        node.freq += 1       # will insert in this new_freq
        self.freqTable[prevFreq].removeNode(node)     # Removing from prevFreq
        self.freqTable[node.freq].insertAtLast(node)  # Inserting in new_freq. Will insert at last i.e most recently used for that freq. 
                                                      # because now it will be most recently used for that freq. same as 'LRU'
        if prevFreq == self.minFreq and self.freqTable[prevFreq].size == 0:
            # If 'minFreq' was = prevFreq and there was only 'key' for 'minFreq' then we have to update the minFreq = 1
            self.minFreq += 1
        return node.val
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        return self.updateCache(key, self.cache[key].val)
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # just update and return 
            self.updateCache(key, value)
        else:
            if len(self.cache) == self.capacity:
                # Remove the lru key having minimum frequency
                to_remove = self.freqTable[self.minFreq].removeFirst()
                # delete from cache also
                del self.cache[to_remove.key]
            # Now put this 'key' in freqTable with freq = 1 and in cache cache
            node = ListNode(key, value)
            self.freqTable[1].insertAtLast(node)
            self.cache[key] = node
            self.minFreq = 1  # Since inserting new node so minFreq = 1 only
