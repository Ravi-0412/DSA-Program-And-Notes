# Method 1:

# just same as 'Q. maxXor'. Treat the given arr 'nums' as both arr1 and arr2. 
# Will give TLE for last inputs.
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

# Java Code 
"""
import java.util.*;

class TrieNode {
    Map<Integer, TrieNode> children = new HashMap<>();  // will contain two num max i.e bit '0' and bit '1'
}

class Trie {
    TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    // will insert in binary from leftmost side and each num is stored in '32' bit binary
    public void insert(int num) {
        TrieNode cur = root;
        for (int i = 31; i >= 0; i--) {
            int bit = (num >> i) & 1;  // getting the bit at 'i'th position
            cur.children.putIfAbsent(bit, new TrieNode());
            cur = cur.children.get(bit);
        }
    }

    // will give the maximum xor of this number with all the number inserted in the Trie
    public int getMax(int num) {
        TrieNode cur = root;
        int max_xor = 0;

        for (int i = 31; i >= 0; i--) {
            int bit = (num >> i) & 1;
            // for maximum xor, we need the opposite of this 'bit'
            if (cur.children.containsKey(1 - bit)) {
                max_xor |= (1 << i);
                cur = cur.children.get(1 - bit);
            } else {
                cur = cur.children.get(bit);
            }
        }

        return max_xor;
    }
}

class Solution {
    public int findMaximumXOR(int[] nums) {
        Trie trie = new Trie();
        int ans = 0;
        for (int num : nums) {
            trie.insert(num);
            ans = Math.max(ans, trie.getMax(num));
        }
        return ans;
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class TrieNode {
public:
    unordered_map<int, TrieNode*> children;  // will contain two num max i.e bit '0' and bit '1'
};

class Trie {
    TrieNode* root;

public:
    Trie() {
        root = new TrieNode();
    }

    // will insert in binary from leftmost side and each num is stored in '32' bit binary
    void insert(int num) {
        TrieNode* cur = root;
        for (int i = 31; i >= 0; i--) {
            int bit = (num >> i) & 1;  // getting the bit at 'i'th position
            if (cur->children.find(bit) == cur->children.end()) {
                cur->children[bit] = new TrieNode();
            }
            cur = cur->children[bit];
        }
    }

    // will give the maximum xor of this number with all the number inserted in the Trie
    int getMax(int num) {
        TrieNode* cur = root;
        int max_xor = 0;
        for (int i = 31; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (cur->children.find(1 - bit) != cur->children.end()) {
                max_xor |= (1 << i);
                cur = cur->children[1 - bit];
            } else {
                cur = cur->children[bit];
            }
        }
        return max_xor;
    }
};

class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        Trie trie;
        int ans = 0;
        for (int num : nums) {
            trie.insert(num);
            ans = max(ans, trie.getMax(num));
        }
        return ans;
    }
};
"""

# Method 2: 
# In this logic just we took two element to represent '0' and '1' at each node.
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


# Java Code 
"""
class TrieNode {
    TrieNode[] children = new TrieNode[2];
}

class Trie {
    TrieNode root = new TrieNode();

    public void insert(int num) {
        TrieNode curr = root;
        for (int i = 31; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (curr.children[bit] == null) {
                curr.children[bit] = new TrieNode();
            }
            curr = curr.children[bit];
        }
    }

    public int getMaxXOR(int num) {
        TrieNode curr = root;
        int ans = 0;
        for (int i = 31; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (curr.children[1 - bit] != null) {
                ans |= (1 << i);
                curr = curr.children[1 - bit];
            } else {
                curr = curr.children[bit];
            }
        }
        return ans;
    }
}

class Solution {
    public int findMaximumXOR(int[] nums) {
        Trie trie = new Trie();
        int maxAns = 0;

        for (int num : nums) {
            trie.insert(num);
            maxAns = Math.max(maxAns, trie.getMaxXOR(num));
        }

        return maxAns;
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <vector>
using namespace std;

class TrieNode {
public:
    TrieNode* children[2] = {nullptr, nullptr};  // will contain two nodes: for bit 0 and bit 1
};

class Trie {
    TrieNode* root;

public:
    Trie() {
        root = new TrieNode();
    }

    void insert(int num) {
        TrieNode* curr = root;
        for (int i = 31; i >= 0; --i) {
            int bit = (num >> i) & 1;
            if (curr->children[bit] == nullptr) {
                curr->children[bit] = new TrieNode();
            }
            curr = curr->children[bit];
        }
    }

    int getMaxXOR(int num) {
        TrieNode* curr = root;
        int ans = 0;
        for (int i = 31; i >= 0; --i) {
            int bit = (num >> i) & 1;
            if (curr->children[1 - bit]) {
                ans |= (1 << i);
                curr = curr->children[1 - bit];
            } else {
                curr = curr->children[bit];
            }
        }
        return ans;
    }
};

class Solution {
public:
    int findMaximumXOR(const vector<int>& nums) {
        Trie trie;
        int maxAns = 0;

        for (int num : nums) {
            trie.insert(num);
            maxAns = max(maxAns, trie.getMaxXOR(num));
        }

        return maxAns;
    }
};
"""


# method 3: 
# using bit

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


# Java Code 
"""
import java.util.*;

class Solution {
    public int findMaximumXOR(int[] nums) {
        int ans = 0, mask = 0;

        for (int i = 31; i >= 0; i--) {
            mask = mask | (1 << i);  // '1' is the max we can get at any position. mask will contain all '1'.
            Set<Integer> found = new HashSet<>();

            for (int num : nums) {
                found.add(num & mask);
            }

            int target = ans | (1 << i);  // trying to fix '1' at the 'i'th position.

            // now do xor of num in 'found' with target and check if 'target ^ num' is in found
            // if it is, then we can get our desired target
            for (int prefix : found) {
                if (found.contains(prefix ^ target)) {
                    ans = target;
                    break;
                }
            }
        }

        return ans;
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        int ans = 0, mask = 0;

        for (int i = 31; i >= 0; --i) {
            mask = mask | (1 << i);  // '1' is the max we can get at any position. mask will contain all '1'.
            unordered_set<int> found;

            for (int num : nums) {
                found.insert(num & mask);
            }

            int target = ans | (1 << i);  // maximum we can get '1' at the 'i'th position.

            // now do xor of num in 'found' with target and check if 'target ^ num' is in found.
            for (int prefix : found) {
                if (found.count(prefix ^ target)) {
                    ans = target;
                    break;
                }
            }
        }

        return ans;
    }
};
"""
