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
            # If 'minFreq' was = prevFreq and there was only 'key' for 'minFreq' then we have to update the minFreq += 1
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


# Java Code 
"""
import java.util.HashMap;

class ListNode {
    int key, val, freq;
    ListNode prev, next;

    ListNode(int k, int v) {
        key = k;
        val = v;
        freq = 1;
        prev = next = null;
    }
}

// Doubly Linked List (DLL) for Frequency Table
class DLL {
    ListNode Lru;  // Least Recently Used
    ListNode Mru;  // Most Recently Used
    int size;

    DLL() {
        Lru = new ListNode(0, 0);
        Mru = new ListNode(0, 0);
        Lru.next = Mru;
        Mru.prev = Lru;
        size = 0;
    }

    // Insert node at last (Most Recently Used)
    void insertAtLast(ListNode node) {
        ListNode prevNode = Mru.prev;
        prevNode.next = Mru.prev = node;
        node.next = Mru;
        node.prev = prevNode;
        size++;
    }

    // Remove given node
    void removeNode(ListNode node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
        size--;
    }

    // Remove Least Recently Used node
    ListNode removeFirst() {
        ListNode node_to_remove = Lru.next;
        removeNode(node_to_remove);
        return node_to_remove;
    }
}

// LFU Cache Implementation
class LFUCache {
    private int capacity, minFreq;
    private HashMap<Integer, ListNode> cache;
    private HashMap<Integer, DLL> freqTable;

    public LFUCache(int cap) {
        this.capacity = cap;
        this.minFreq = 0;
        this.cache = new HashMap<>();
        this.freqTable = new HashMap<>();
    }

    private void updateCache(int key, int value) {
        ListNode node = cache.get(key);
        node.val = value;
        int prevFreq = node.freq;
        node.freq++;

        freqTable.get(prevFreq).removeNode(node);
        freqTable.computeIfAbsent(node.freq, k -> new DLL()).insertAtLast(node);

        if (prevFreq == minFreq && freqTable.get(prevFreq).size == 0) {
            minFreq++;
        }
    }

    public int get(int key) {
        if (!cache.containsKey(key)) return -1;
        updateCache(key, cache.get(key).val);
        return cache.get(key).val;
    }

    public void put(int key, int value) {
        if (capacity == 0) return;

        if (cache.containsKey(key)) {
            updateCache(key, value);
        } else {
            if (cache.size() == capacity) {
                ListNode to_remove = freqTable.get(minFreq).removeFirst();
                cache.remove(to_remove.key);
            }

            ListNode node = new ListNode(key, value);
            freqTable.computeIfAbsent(1, k -> new DLL()).insertAtLast(node);
            cache.put(key, node);
            minFreq = 1;
        }
    }
}
"""

# C++ Code
"""
#include <iostream>
#include <unordered_map>
#include <map>

using namespace std;

// Definition for a node in the doubly linked list
class ListNode {
public:
    int key, val, freq;
    ListNode* prev;
    ListNode* next;

    ListNode(int k, int v) : key(k), val(v), freq(1), prev(nullptr), next(nullptr) {}
};

// Doubly Linked List (DLL) for Frequency Table
class DLL {
public:
    ListNode* Lru;  // Least Recently Used
    ListNode* Mru;  // Most Recently Used
    int size;

    DLL() {
        Lru = new ListNode(0, 0);
        Mru = new ListNode(0, 0);
        Lru->next = Mru;
        Mru->prev = Lru;
        size = 0;
    }

    // Insert node at last (Most Recently Used)
    void insertAtLast(ListNode* node) {
        ListNode* prevNode = Mru->prev;
        prevNode->next = Mru->prev = node;
        node->next = Mru;
        node->prev = prevNode;
        size++;
    }

    // Remove given node
    void removeNode(ListNode* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
        size--;
    }

    // Remove Least Recently Used node
    ListNode* removeFirst() {
        ListNode* node_to_remove = Lru->next;
        removeNode(node_to_remove);
        return node_to_remove;
    }
};

// LFU Cache Implementation
class LFUCache {
private:
    int capacity;
    int minFreq;
    unordered_map<int, ListNode*> cache;
    unordered_map<int, DLL> freqTable;

    void updateCache(int key, int value) {
        ListNode* node = cache[key];
        node->val = value;
        int prevFreq = node->freq;
        node->freq += 1;

        freqTable[prevFreq].removeNode(node);
        freqTable[node->freq].insertAtLast(node);

        if (prevFreq == minFreq && freqTable[prevFreq].size == 0) {
            minFreq++;
        }
    }

public:
    LFUCache(int cap) : capacity(cap), minFreq(0) {}

    int get(int key) {
        if (cache.find(key) == cache.end()) return -1;
        updateCache(key, cache[key]->val);
        return cache[key]->val;
    }

    void put(int key, int value) {
        if (capacity == 0) return;

        if (cache.find(key) != cache.end()) {
            updateCache(key, value);
        } else {
            if (cache.size() == capacity) {
                ListNode* to_remove = freqTable[minFreq].removeFirst();
                cache.erase(to_remove->key);
            }
            
            ListNode* node = new ListNode(key, value);
            freqTable[1].insertAtLast(node);
            cache[key] = node;
            minFreq = 1;
        }
    }
};
"""

# Try to do in more concise way later
# https://leetcode.com/problems/lfu-cache/solutions/166683/python-only-use-ordereddict-get-o-1-put-o-1-simple-and-brief-explained/
# https://leetcode.com/problems/lfu-cache/solutions/369104/python-two-dicts-explanation/


# Related Question
"""
1) Asked in FAANG. Exact same as LFU

Imagine you're building an online music streaming app that allows users to store a playlist of their favorite songs. 
The app has a feature that shows the most popular songs based on how often they’ve been played.


However, the playlist can only hold a limited number of songs. 
If the user tries to add more songs than the playlist can hold, the app needs to remove some songs to make room 
for the new ones. 
But the app has specific rules on which songs to remove:

Least Played Songs: The song that has been played the least will be removed first.

Tie-breaker: If multiple songs have been played the same number of times, the song that was added to the playlist 
the longest time ago will be removed.

Your Task
Design a data structure called PlaylistManager to manage the playlist with the following operations:

class PlaylistManager:
    def __init__(self, capacity: int)
    def get_song(self, song_id: int) -> int
    def add_song(self, song_id: int, song_details: int) -> None
**/


Sample 1:
const manager = new PlaylistManager(2);
manager.add_song(1, 100); // Add song 1
manager.add_song(2, 200); // Add song 2

console.log(manager.get_song(1)); // Output: 1
console.log(manager.get_song(2)); // Output: 2
console.log(manager.get_song(3)); // Output: -1 (not present)

Sample 2:
const manager = new PlaylistManager(2);
manager.add_song(1, 100); // song 1, freq 1      
manager.add_song(2, 200); // song 2, freq 1
manager.get_song(1);      // song 1, freq 2

manager.add_song(3, 300); // should evict song 2 

console.log(manager.get_song(1)); // Output: 1
console.log(manager.get_song(2)); // Output: -1 (evicted)
console.log(manager.get_song(3)); // Output: 3

const manager = new PlaylistManager(2);
manager.add_song(1, 100);
manager.add_song(2, 200);
manager.add_song(1, 150); // Updates freq of song 1

manager.add_song(3, 300); // song 2 should be evicted

console.log(manager.get_song(1)); // Output: 1
console.log(manager.get_song(2)); // Output: -1
console.log(manager.get_song(3)); // Output: 3
"""
