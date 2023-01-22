# logic: for each query(xi, mi) we have to insert the num only having value <= mi.
# for this to check sort both the 'nums' and queries.

# reason for sorting the queries based on 'xi': for next query, num inserted for query till now should also in Trie.
# so it will become easier.
# reason

class TrieNode:
    def __init__(self):
        self.children= {}

class Trie:
    def __init__(self):
        self.root= TrieNode()
    
    def insert(self, num):
        cur= self.root
        for i in range(31,-1,-1):
            bit= (num>> i) & 1    # will give the 'ith' bit.
            if bit not in cur.children:
                cur.children[bit]= TrieNode()
            cur= cur.children[bit]
    
    def getAns(self, num):
        # if not self.root:   # writing this will not return from here. root is an object so root must be assigned some address.
        #     return -1
        if not self.root.children:
            return -1
        max_xor= 0
        cur= self.root
        for i in range(31, -1, -1):
            bit= (num>> i) & 1
            # for maximum xor, we need the opposite of this 'bit'.
            if (1-bit) in cur.children:
                max_xor= max_xor | (1<< i)   # bring '1' at ith position in ans keeping all other bit same.
                cur= cur.children[1- bit]
            else:
                cur= cur.children[bit]
        return max_xor


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()    # to insert values less than equal to 'mi' for each query.
        queries= sorted(enumerate(queries), key= lambda x: x[1][1])   # To sort based on 'mi' as we only need to insert values in tries <='mi'.
        # using emumerate to maintain the index of original since we have to return ans according to that only.

        # Now for each query insert the ele from the nums which are smaller than mi.
        trie= Trie()
        j= 0
        ans= [-1] *(len(queries))
        for i, (xi,mi) in queries:
            while j < len(nums) and nums[j] <= mi:
                trie.insert(nums[j])
                j+= 1
            ans[i]= trie.getAns(xi)
        return ans