# Logic: each index will store a singly linked list

# For avoiding collision and even distribution of keys 
# use a very simple multiplicative hashing function utilizing a large prime multiplier and then 
# modulo the result to the desired size (also a prime) of our hashmap array. 
# This should hopefully result in an even distribution of the entries throughout the hashmap array.

# Get()
# The get() method is fairly easy, then. We just hash() our key, access the corresponding bucket 
# in our hashmap array (data), and navigate through the linked list (if necessary) and return the
# correct val, or -1 if the key is not found.

# put()
# For the put() method, we should first remove() any earlier instance of that key to avoid chaining
# multiple versions of a key definition in our linked list. Then we simply form a new ListNode at the
# head of the proper hashmap bucket, pushing any others back.

# remove()
# The remove() method will be similar to the get() method, except that we need to find and stitch
# together the nodes on either side of the node that matches the key, removing it from the linked list entirely.

# why we took these primes numbers?
# static final int size = 19997;
# static final int mult = 12582917;

# Reason:
# No specific reason. For the size, I wanted something that was larger than the number of possible operations
# (10^4), but as small as possible without risking too many collisions, and preferably prime. 
# The other is just a random large multiplier, also preferably a prime.

# using Array
class MyHashMap:
    def __init__(self):
        self.data = [None] * 1000001
    def put(self, key: int, val: int) -> None:
        self.data[key] = val
    def get(self, key: int) -> int:
        val = self.data[key]
        return val if val != None else -1
    def remove(self, key: int) -> None:
        self.data[key] = None

# using linked list
class ListNode:
    def __init__(self, key, val, nxt):
        self.key = key
        self.val = val
        self.next = nxt
class MyHashMap:
    def __init__(self):
        self.size = 19997
        self.mult = 12582917
        self.data = [None for _ in range(self.size)]
    def hash(self, key):
        return key * self.mult % self.size
    def put(self, key, val):
        self.remove(key)
        h = self.hash(key)
        node = ListNode(key, val, self.data[h])
        self.data[h] = node
    def get(self, key):
        h = self.hash(key)
        node = self.data[h]
        while node:
            if node.key == key: return node.val
            node = node.next
        return -1
    def remove(self, key: int):
        h = self.hash(key)
        node = self.data[h]
        if not node: return
        if node.key == key:
            self.data[h] = node.next
            return
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next

# java
# using array
"""
class MyHashMap {
    int[] data;
    public MyHashMap() {
        data = new int[1000001];
        Arrays.fill(data, -1);
    }
    public void put(int key, int val) {
        data[key] = val;
    }
    public int get(int key) {
        return data[key];
    }
    public void remove(int key) {
        data[key] = -1;
    }
}
"""

# using linked list
""""
class ListNode {
    int key, val;
    ListNode next;
    public ListNode(int key, int val, ListNode next) {
        this.key = key;
        this.val = val;
        this.next = next;
    }
}

class MyHashMap {
    static final int size = 19997;
    static final int mult = 12582917;
    ListNode[] data;

    public MyHashMap() {
        this.data = new ListNode[size];
    }

    private int hash(int key) {
        return (int)((long)key * mult % size);
    }

    public void put(int key, int val) {
        remove(key);
        int h = hash(key);
        ListNode node = new ListNode(key, val, data[h]);
        data[h] = node;
    }

    public int get(int key) {
        int h = hash(key);
        ListNode node = data[h];
        while (node != null) {
            if (node.key == key) return node.val;
            node = node.next;
        }
        return -1;
    }

    public void remove(int key) {
        int h = hash(key);
        ListNode node = data[h];
        if (node == null) return;
        if (node.key == key) {
            data[h] = node.next;
        } else {
            while (node.next != null) {
                if (node.next.key == key) {
                    node.next = node.next.next;
                    return;
                }
                node = node.next;
            }
        }
    }
}

"""