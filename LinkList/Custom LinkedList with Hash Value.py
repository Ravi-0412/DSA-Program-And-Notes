"""
Q) Create a custom LinkedList which would store three things:
value, pointer to next node and a string which contains hash of current value as well hash of next node's hash
If the next node doesn't exist, it would assume the next node has an empty string as hash.
Also write a function which would validate the linkedlist. If the hash value of a node is tampered, 
then I should return false otherwise if the hash of all nodes are good, then true.

Ans: 
This concept is very similar to how a Blockchain works, where each "block" (or node) contains a cryptographic link to the next. 
By storing a combined hash of the current value and the next node's hash, you create a chain that is extremely difficult to tamper with.

🧠 The Logic & Thought Process
1. Node Structure: Each node will have val, next, and a combined_hash field.
2.Hashing Strategy:
  To create the combined_hash, we take the hash of the current node's value and the hash of the next node.
  The Catch: In a standard LinkedList, you usually add nodes to the end. But here, a node's hash depends on the node that comes after it.
  The Solution: We must add nodes to the Head (prepend). This way, when we create a new node, we already know the hash of the "next" node.
3. Validation: We traverse the list. For every node, we re-calculate what the hash should be and compare it to the stored combined_hash. 
If someone changed a value or a pointer, the recalculation won't match.

Meaning of lines:
1. data = f"{current_val}{next_node_hash}"
say , value = 10 , hash = abc123... then, data = 10abc123....
2. return hashlib.sha256(data.encode()).hexdigest()
It consists of three steps internally:
a) .encode()
-> Computers don't "read" text; they read bytes (1s and 0s). encode() converts your string into a byte representation (usually UTF-8) so the hashing algorithm can process it.
b) hashlib.sha256(...)
This calls the SHA-256 (Secure Hash Algorithm 256-bit). It is a "one-way" cryptographic function.
Input: Any amount of data.
Output: A 256-bit signature.
Crucial Property: Even if you change one tiny letter in the input, the output signature will look completely different (this is called the Avalanche Effect).
c) .hexdigest()
-> The raw output of SHA-256 is a bunch of messy binary bytes. hexdigest() converts those bytes into a readable Hexadecimal string (using characters 0-9 and a-f).
Example Result: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

"""

import hashlib

class Node:
    def __init__(self, val, next_node=None):
        self.val = str(val)
        self.next = next_node
        # If next exists, use its hash; otherwise, use an empty string
        next_hash = next_node.combined_hash if next_node else ""
        
        # Create the hash: hash(current_val) + hash(next_node_hash)
        self.combined_hash = self._generate_hash(self.val, next_hash)

    def _generate_hash(self, current_val, next_node_hash):
        """Helper to create a SHA-256 hash string."""
        data = f"{current_val}{next_node_hash}"
        return hashlib.sha256(data.encode()).hexdigest()

class SecureLinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, val):
        """
        Adds a node to the front (Head) of the list.
        Prepending is necessary because a node's hash depends on the next node.
        """
        new_node = Node(val, self.head)
        self.head = new_node

    def validate(self):
        """
        Traverses the list and verifies if each node's hash is valid
        based on its current value and the next node's hash.
        """
        curr = self.head
        while curr:
            # Determine what the next hash should be for verification
            next_hash = curr.next.combined_hash if curr.next else ""
            
            # Recalculate the hash based on current state
            expected_hash = curr._generate_hash(curr.val, next_hash)
            
            # If the stored hash doesn't match the recalculated hash, it's tampered
            if curr.combined_hash != expected_hash:
                return False
            
            curr = curr.next
        return True

# Test cases
  def test_secure_list():
    sll = SecureLinkedList()
    
    # 1. Build a valid list: [30] -> [20] -> [10]
    sll.addNode(10)
    sll.addNode(20)
    sll.addNode(30)
    
    print(f"Initial Validation: {sll.validate()}") # Expected: True

    # 2. Tamper with a value
    print("\n--- Tampering with value in the middle ---")
    # Let's change the value of the second node (20 -> 99)
    sll.head.next.val = "99" 
    print(f"Validation after tampering: {sll.validate()}") # Expected: False

    # 3. Test tampering with the 'next' pointer
    sll2 = SecureLinkedList()
    sll2.addNode("A")
    sll2.addNode("B")
    print(f"\nNew List Validation: {sll2.validate()}") # Expected: True
    
    # Bypass next node
    sll2.head.next = None 
    print(f"Validation after pointer tampering: {sll2.validate()}") # Expected: False

if __name__ == "__main__":
    test_secure_list()
