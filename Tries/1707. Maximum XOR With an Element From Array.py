# Method 1: 

# logic: for each query(xi, mi) we have to insert the num only having value <= mi. Since we have to take with num <= mi for each query.
# for this to check sort both the 'nums' and queries.

# Sort the query based on 'mi' then for next query, num inserted for query till now should also in Trie.
# so it will become easier.

class TrieNode:
    def __init__(self):
        self.children= {}

class Trie:
    def __init__(self):
        self.root= TrieNode()
    
    def insert(self, num):
        cur= self.root
        for i in range(31,-1,-1):
            bit= (num >> i) & 1    # will give the 'ith' bit.
            if bit not in cur.children:
                cur.children[bit]= TrieNode()
            cur= cur.children[bit]
    
    def getAns(self, num):
        # if not self.root:   # writing this will not return from here. root is an object so root must be assigned some address.
        #     return -1
        if not self.root.children:  # means all elements are larger than 'mi'.
            return -1
        max_xor= 0
        cur= self.root
        for i in range(31, -1, -1):
            bit= (num>> i) & 1      # getting the bit at 'i'th position.
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
        j= 0  # will tell the index till where we have inserted the num in tries.
        ans= [-1] *(len(queries))
        for i, (xi,mi) in queries:
            while j < len(nums) and nums[j] <= mi:
                trie.insert(nums[j])
                j+= 1
            ans[i]= trie.getAns(xi)
        return ans

# Java Code 
"""
import java.util.*;

class TrieNode {
    Map<Integer, TrieNode> children = new HashMap<>();  // will contain bits 0 and 1
}

class Trie {
    TrieNode root = new TrieNode();

    public void insert(int num) {
        TrieNode cur = root;
        for (int i = 31; i >= 0; i--) {
            int bit = (num >> i) & 1;  // will give the 'ith' bit
            cur.children.putIfAbsent(bit, new TrieNode());
            cur = cur.children.get(bit);
        }
    }

    public int getAns(int num) {
        if (root.children.isEmpty())  // means all elements are larger than 'mi'
            return -1;

        int max_xor = 0;
        TrieNode cur = root;

        for (int i = 31; i >= 0; i--) {
            int bit = (num >> i) & 1;  // getting the bit at 'i'th position
            // for maximum xor, we need the opposite of this 'bit'
            if (cur.children.containsKey(1 - bit)) {
                max_xor |= (1 << i);  // bring '1' at ith position in ans keeping all other bit same
                cur = cur.children.get(1 - bit);
            } else {
                cur = cur.children.get(bit);
            }
        }
        return max_xor;
    }
}

class Solution {
    public int[] maximizeXor(int[] nums, int[][] queries) {
        Arrays.sort(nums);  // to insert values less than equal to 'mi' for each query

        int[][] sortedQueries = new int[queries.length][3];
        for (int i = 0; i < queries.length; i++) {
            sortedQueries[i][0] = queries[i][0];  // xi
            sortedQueries[i][1] = queries[i][1];  // mi
            sortedQueries[i][2] = i;              // original index
        }

        Arrays.sort(sortedQueries, Comparator.comparingInt(a -> a[1]));  // sort based on 'mi'

        Trie trie = new Trie();
        int[] ans = new int[queries.length];
        int j = 0;

        // Now for each query insert the ele from the nums which are smaller than mi
        for (int[] q : sortedQueries) {
            int xi = q[0], mi = q[1], idx = q[2];
            while (j < nums.length && nums[j] <= mi) {
                trie.insert(nums[j]);
                j++;
            }
            ans[idx] = trie.getAns(xi);
        }

        return ans;
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class TrieNode {
public:
    unordered_map<int, TrieNode*> children;  // will contain bits 0 and 1
};

class Trie {
    TrieNode* root;

public:
    Trie() {
        root = new TrieNode();
    }

    void insert(int num) {
        TrieNode* cur = root;
        for (int i = 31; i >= 0; --i) {
            int bit = (num >> i) & 1;  // will give the 'ith' bit
            if (!cur->children.count(bit)) {
                cur->children[bit] = new TrieNode();
            }
            cur = cur->children[bit];
        }
    }

    int getAns(int num) {
        if (root->children.empty()) return -1;  // means all elements are larger than 'mi'

        TrieNode* cur = root;
        int max_xor = 0;
        for (int i = 31; i >= 0; --i) {
            int bit = (num >> i) & 1;  // getting the bit at 'i'th position
            // for maximum xor, we need the opposite of this 'bit'
            if (cur->children.count(1 - bit)) {
                max_xor |= (1 << i);  // bring '1' at ith position in ans keeping all other bit same
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
    vector<int> maximizeXor(vector<int>& nums, vector<vector<int>>& queries) {
        sort(nums.begin(), nums.end());  // to insert values less than equal to 'mi' for each query

        vector<tuple<int, int, int>> sortedQueries;
        for (int i = 0; i < queries.size(); ++i) {
            sortedQueries.emplace_back(queries[i][0], queries[i][1], i);  // xi, mi, index
        }

        sort(sortedQueries.begin(), sortedQueries.end(),
             [](const auto& a, const auto& b) { return get<1>(a) < get<1>(b); });  // sort based on 'mi'

        Trie trie;
        vector<int> ans(queries.size(), -1);
        int j = 0;

        // Now for each query insert the ele from the nums which are smaller than mi
        for (const auto& [xi, mi, idx] : sortedQueries) {
            while (j < nums.size() && nums[j] <= mi) {
                trie.insert(nums[j]);
                ++j;
            }
            ans[idx] = trie.getAns(xi);
        }

        return ans;
    }
};
"""