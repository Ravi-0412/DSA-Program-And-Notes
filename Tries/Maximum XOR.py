# why Tries?
# ans: if we see the binary form of every number then all are  made from '0' or '1' only like all words is formed from letters 'a-z' only.

# logic: insert all element of first array into Trie.
# After that take each number one by one from 2nd array and keep updating the ans.

# Time Complexity: O(N*32) + O(M*32)
# Reason: For inserting all the elements of arr1 into the trie take O(N*32) [32 Bit] 
# and O(M*32) for finding the maxXOR for every element of arr2.

# Space Complexity: O(N*32)
# Reason: Since we are inserting all the elements of arr1 into trie where every element is of size 32 bit
#  but the space complexity will be less than O(N*32) because they might have overlapped.

# Note vvi: for insertion , we will insert from leftmost side because for maximum xor we will try to get
# '1' from leftmost side as soon as possible. 

class TrieNode:
    def __init__(self):
        self.children= {}   # will contains two num max i.e bit '0' and bit '1'.

class Trie:
    def __init__(self):
        self.root= TrieNode()
    
    # will insert in binary from leftmost side(most significant bit) and each num is stored in '32' bit binary.
    # 1st node will contain most significant bit and so on.
    def insert(self, num):
        cur= self.root
        for i in range(31,-1,-1):
            bit= (num>> i) & 1    # getting ith most significant digit.for this we need to do right shift 'i' times
            if bit not in cur.children:
                cur.children[bit]= TrieNode()
            cur= cur.children[bit]
    
    # will give the maximum xor of this number with all the number inserted in the Trie.
    def getMax(self, num):
        max_xor= 0
        cur= self.root
        # first node of Trie has most significant bit so 1st we will find the most significant bit and  take the xor.
        for i in range(31, -1, -1):
            bit= (num>> i) & 1
            # for maximum xor, we need the opposite of this 'bit'.
            # if present then at this position, we will make bit= 1 for this position keeping all other bit same.
            # for this, bring 1 at this position by doing left shift by 'i' and take OR with max_xor.
            if (1-bit) in cur.children:
                max_xor= max_xor | (1<< i)
                cur= cur.children[1- bit]     # will follow node with '1-bit' here.
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
    







