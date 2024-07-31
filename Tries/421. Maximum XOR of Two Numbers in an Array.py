# just same as 'Q. maxXor'. Treat the given arr 'nums' as both arr1 and arr2. 
# But giving Tle for last inputs.
# Time Complexity: O(N*32) + O(M*32)= space
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
            bit= (num>> i) & 1   # getting the bit at 'i'th position.
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
                max_xor = max_xor | (1<< i)
                cur= cur.children[1- bit]
            else:
                cur= cur.children[bit]
        return max_xor

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie= Trie()
        ans = 0
        for num in nums:
            trie.insert(num)
            ans= max(ans, trie.getMax(num))      
        return ans


# This same logic just we took two element to represent '0' and '1' at each node.
# do it this way only if you get tle in other questions as well involving bit + trie.
class TrieNode:
    def __init__(self):
        self.children = [None, None]

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        curr = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if curr.children[bit] is None:
                curr.children[bit] = TrieNode()
            curr = curr.children[bit]
    
    def get_max_xor(self, num):
        curr = self.root
        ans = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if curr.children[1 - bit]:
                ans |= (1 << i)
                curr = curr.children[1 - bit]
            else:
                curr = curr.children[bit]
        return ans

class Solution:
    def findMaximumXOR(self, nums):
        max_ans = 0
        trie = Trie()
        
        for num in nums:
            trie.insert(num)
            max_ans = max(max_ans, trie.get_max_xor(num))
        
        return max_ans


# java
"""
import java.util.*;

class TrieNode {
    TrieNode[] next;

    public TrieNode() {
        next = new TrieNode[2];
    }
}

class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    public void insert(int num) {
        TrieNode curr = root;
        for (int i = 31; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (curr.next[bit] == null) {
                curr.next[bit] = new TrieNode();
            }
            curr = curr.next[bit];
        }
    }

    public int getMaxXor(int num) {
        TrieNode curr = root;
        int ans = 0;
        for (int i = 31; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (curr.next[1 - bit] != null) {
                ans |= (1 << i);
                curr = curr.next[1 - bit];
            } else {
                curr = curr.next[bit];
            }
        }
        return ans;
    }
}

public class Solution {
    public int findMaximumXOR(int[] nums) {
        int maxAns = 0;
        int n = nums.length;
        Trie trie = new Trie();

        for (int i = 0; i < n; i++) {
            trie.insert(nums[i]);
            maxAns = Math.max(maxAns, trie.getMaxXor(nums[i]));
        }

        return maxAns;
    }
}

"""


# method 2: using bit

# for finding the max value, if we can get bit set(bit= 1) at rightmost sides then that will be our ans.
# so we are taking the help of masking to extract those number by 100....00, 1100...00, 11100..000  etc for leftmost bit.
# till every bit we have traversed, we are putting the 'mask&num' in a set.(we want '1' so doing '&')
# now we will fix our target to get the max ans and that will be acc to the ans we have got till now.

# later we will take num one by one from set and do will xor with 'target' and will check if it's xor is present in set then,
# we can get our target . so update ans= target in this case and break otherwise leave ans as it is(it means we can't set the ans bit at bit position)

# Reason behind working of above one.
# if (a^b= target) then (target ^ a= b) and (target ^ b= a).    

# just Two sum logic. 

# time= O(32*n)
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans, mask= 0, 0
        for i in range(31, -1, -1):
            mask= mask | (1<< i)  # '1' is the max we can get at any position. mask will conatin all '1' .
            found= set()
            for num in nums:
                found.add(mask & num)
            target= ans | (1<< i)  # maximum we can get '1' at the 'i'th position. so we are fixing the target to get '1' at that 'i'th position.
            # now do xor of num in 'found ' with target and check if 'target^num' is in found.
            # if it is in found then we can get our desired target by taking xor of two number. so update the ans and break
            for prefix in found:
                if target ^ prefix in found: 
                    ans= target
                    break
        return ans
