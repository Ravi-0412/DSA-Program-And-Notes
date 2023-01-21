# just same as 'Q. maxXor'. Treat the given arr 'nums' as both arr1 and arr2. 
# But giving Tle for last input.

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

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie= Trie()
        for num in nums:
            trie.insert(num)

        ans= 0
        for num in nums:
            ans= max(ans, trie.getMax(num))
        return ans

# same logic is getting submitted in c++ and java.
# also there are solutions which are short and based on same logic and also getting submitted.


# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/solutions/171747/python-o-n-solution-easily-explained/?orderBy=most_votes