# logic: insert all element of first array into Trie.
# After that take each number one by one from 2nd array and keep updating the ans.

class TrieNode:
    def __init__(self):
        self.children= {}   # will contains two num max i.e bit '0' and bit '1'.

class Trie:
    def __init__(self):
        self.root= TrieNode()
    
    # will insert in binary from leftmost side and each num is stored in '32' bit binary.
    def insert(self, num):
        cur= self.root
        for i in range(31,-1,-1):
            bit= (num>> i) & 1    # will give the bit from the letmost side.
            if bit not in cur.children:
                cur.children[bit]= TrieNode()
            cur= cur.children[bit]
    
    # will give the maximum xor of this number with all the number inserted in the Trie.
    def getMax(self, num):
        max_xor= 0
        cur= self.root
        for i in range(31, -1, -1):
            bit= (num>> i) & 1
            # for maximum xor, we need the opposite of this 'bit'.
            if (1-bit) in cur.children:
                max_xor= max_xor | (1<< i)
                cur= cur.children[1- bit]
            else:
                cur= cur.children[bit]
        return max_xor

def maxXOR(n, m, arr1, arr2):
    trie= Trie()
    # first insert all the element of first array into the Trie.
    for num in arr1:
        trie.insert(num)
    
    # now take number one by one from arr2 and calculate the max_xor of this num from all the num of arr1.
    ans= 0
    for num in arr2:
        ans= max(ans, trie.getMax(num))
    return ans
    







