# Logic: Similar to 'LRU cache'.
# But we need to  :
# 1) Keep track of frequency of key till now so for this we will need one more member in 'Node'
# i.e frequency.
# 2) We need to remove the least frequent element when size is more and in case of
# equal frequency we need to remove according to 'LRU' meaning.

# for this we will need one more hashmap for storing all the elements having same frequency in 'LRU' form.
# Because using single map of 'LRU' won't be able to handle the frequency case.

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
        self.minFreq  = 0   # will keep track of minimum freq. 
                            # in case of more item we have to remove lru from this frequency only.
                            # Also in case if frequency of any increase having minimum freq and single ele for that fre
                            # then we can update this
    
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


# Java
"""
import java.util.HashMap;
import java.util.Map;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Deque;

class ListNode {
    int key;
    int val;
    int freq;
    ListNode prev, next;

    public ListNode(int key, int val) {
        this.key = key;
        this.val = val;
        this.freq = 1;
    }
}

class DLL {
    ListNode Lru, Mru;
    int size;

    public DLL() {
        Lru = new ListNode(0, 0);
        Mru = new ListNode(0, 0);
        Lru.next = Mru;
        Mru.prev = Lru;
        size = 0;
    }

    public void insertAtLast(ListNode node) {
        ListNode nodePre = Mru.prev;
        nodePre.next = node;
        node.prev = nodePre;
        node.next = Mru;
        Mru.prev = node;
        size++;
    }

    public void removeNode(ListNode node) {
        ListNode pre = node.prev;
        ListNode next = node.next;
        pre.next = next;
        next.prev = pre;
        size--;
    }

    public ListNode removeFirst() {
        if (size == 0) {
            return null;
        }
        ListNode nodeToRemove = Lru.next;
        removeNode(nodeToRemove);
        return nodeToRemove;
    }
}

public class LFUCache {
    private int capacity;
    private int minFreq;
    private Map<Integer, ListNode> cache;
    private Map<Integer, DLL> freqTable;

    public LFUCache(int capacity) {
        this.capacity = capacity;
        this.minFreq = 0;
        this.cache = new HashMap<>();
        this.freqTable = new HashMap<>();
    }

    private int updateCache(int key, int value) {
        ListNode node = cache.get(key);
        node.val = value;
        int prevFreq = node.freq;
        node.freq++;
        freqTable.get(prevFreq).removeNode(node);

        if (!freqTable.containsKey(node.freq)) {
            freqTable.put(node.freq, new DLL());
        }
        freqTable.get(node.freq).insertAtLast(node);

        if (prevFreq == minFreq && freqTable.get(prevFreq).size == 0) {
            minFreq++;
        }
        return node.val;
    }

    public int get(int key) {
        if (!cache.containsKey(key)) {
            return -1;
        }
        return updateCache(key, cache.get(key).val);
    }

    public void put(int key, int value) {
        if (capacity == 0) {
            return;
        }
        if (cache.containsKey(key)) {
            updateCache(key, value);
        } else {
            if (cache.size() == capacity) {
                DLL minFreqList = freqTable.get(minFreq);
                ListNode toRemove = minFreqList.removeFirst();
                cache.remove(toRemove.key);
            }
            ListNode newNode = new ListNode(key, value);
            if (!freqTable.containsKey(1)) {
                freqTable.put(1, new DLL());
            }
            freqTable.get(1).insertAtLast(newNode);
            cache.put(key, newNode);
            minFreq = 1;
        }
    }
}
"""

# Try to do in more concise way later
# https://leetcode.com/problems/lfu-cache/solutions/166683/python-only-use-ordereddict-get-o-1-put-o-1-simple-and-brief-explained/
# https://leetcode.com/problems/lfu-cache/solutions/369104/python-two-dicts-explanation/