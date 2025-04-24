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

# java
"""
import java.util.*;

class TrieNode {
    Map<Integer, TrieNode> children = new HashMap<>();
}

class Trie {
    TrieNode root = new TrieNode();

    public void insert(int num) {
        TrieNode cur = root;
        for (int i = 31; i >= 0; i--) {
            int bit = (num >> i) & 1;
            cur.children.putIfAbsent(bit, new TrieNode());
            cur = cur.children.get(bit);
        }
    }

    public int getMaxXor(int num) {
        if (root.children.isEmpty()) return -1;

        TrieNode cur = root;
        int maxXor = 0;
        for (int i = 31; i >= 0; i--) {
            int bit = (num >> i) & 1;
            int toggledBit = 1 - bit;
            if (cur.children.containsKey(toggledBit)) {
                maxXor |= (1 << i);
                cur = cur.children.get(toggledBit);
            } else {
                cur = cur.children.getOrDefault(bit, null);
            }
        }
        return maxXor;
    }
}

class Solution {
    public int[] maximizeXor(int[] nums, int[][] queries) {
        Arrays.sort(nums);
        int n = queries.length;
        int[] result = new int[n];

        // Create a combined list with index
        int[][] extendedQueries = new int[n][3];
        for (int i = 0; i < n; i++) {
            extendedQueries[i][0] = queries[i][0]; // xi
            extendedQueries[i][1] = queries[i][1]; // mi
            extendedQueries[i][2] = i;             // original index
        }

        Arrays.sort(extendedQueries, Comparator.comparingInt(a -> a[1]));  // sort by mi

        Trie trie = new Trie();
        int index = 0;
        for (int[] query : extendedQueries) {
            int xi = query[0], mi = query[1], originalIdx = query[2];

            while (index < nums.length && nums[index] <= mi) {
                trie.insert(nums[index]);
                index++;
            }
            result[originalIdx] = trie.getMaxXor(xi);
        }

        return result;
    }
}
"""
