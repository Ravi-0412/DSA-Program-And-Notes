# method 1: just sort and store ele in set then in list.
# time: O(n*logn)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinct_ele= sorted(list(set(nums)))
        print(distinct_ele)
        if len(nums)== 0: return 0
        ans= 1
        count= 1
        i= 0
        while (i +1) < len(distinct_ele):
            if distinct_ele[i+1]!= distinct_ele[i] + 1:
                # ans= max(ans, count)    # updating here only will give the incorrect ans as when your ans lies at last
                #  e.g: [1,2,3,4] then our ans won't get updated singlee time.
                count= 1
            elif distinct_ele[i+1]== distinct_ele[i] + 1:
                count+= 1
                ans= max(count, ans)
            i+= 1
        return ans

# another way of writing
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinct_ele= sorted(list(set(nums)))
        print(distinct_ele)
        if len(nums)== 0: return 0
        ans= 1
        count= 1
        i= 0
        while (i +1) < len(distinct_ele):
            if distinct_ele[i+1]!= distinct_ele[i] + 1:
                ans= max(ans, count)
                count= 1
            elif distinct_ele[i+1]== distinct_ele[i] + 1:
                count+= 1
            i+= 1
        ans= max(ans, count)
        return ans
    

# method 2:
# Just above logic only.
# For cur ele if 'cur -1' is not present then, new sequence will start from 'cur ele'.
# else cur ele is already got included in some sequence.

# time: O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet= set(nums)   # can use hashmap also, in both we can search in O(1)
        ans= 0
        for n in numSet:
            # check if this no is start of the sequence
            if n-1 not in numSet: # means 'n' is the start of the sequence
                # calculate the longest sequence from 'n'
                long= 0
                while n + long in numSet:
                    long+= 1
                # now we have got the longest sequence acc to the 'n'
                ans= max(ans, long)
            # otherwise 'n' is simply part of a sequence so simply skip, they will automatically get included.
        return ans


# method 3: using DSU
# Logic: we will try to merge(union) a cur ele with its adjacent ele if already merged(present in hashamp) into one component.
# At alst we will return the largest size of distinct component.

class DSU:
    def __init__(self, n):
        self.parent= [i for i in range(n)]
        self.size=   [1 for i in range(n)]
    
    def findParent(self, n):
        if n== self.parent[n]:
            return n
        self.parent[n]= self.findParent(self.parent[n])
        return self.parent[n]
    
    def union(self, n1, n2):
        p1, p2= self.findParent(n1), self.findParent(n2)
        if self.size[p1] < self.size[p2]:
            self.parent[p1]= p2
            self.size[p2]+= self.size[p1]
        else:
            self.parent[p2]= p1
            self.size[p1]+= self.size[p2]

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n= len(nums)
        dsu= DSU(n)
        # to avoid repetition we have to keep distinct value of num and to do union we need index of already added ele.
        numToIndex= collections.defaultdict(int) # [num: index]
        for i, num in enumerate(nums):
            if num in numToIndex:  # means we have alreay added this to a component
                continue
            # Try to merge(union) 'num' with any of the adjacent number which is already included i.e 'num+1' and 'num-1'
            # we will do union with the index value.
            if num + 1 in numToIndex:
                dsu.union(i, numToIndex[num + 1])
            if num - 1 in numToIndex:
                dsu.union(i, numToIndex[num - 1])
            # Add this curr num in hashmap
            numToIndex[num]= i  # since we have to do union with already included element that's why including at last.
            
        # find the size of the largest component (distinct parent)

        # return dsu.getLongestSequence() if nums else 0
        return max(dsu.size) if nums else 0  # shortcut



# Java Code
"""
    // Method 1: Sorting and Iterating

import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;

        TreeSet<Integer> distinct_ele = new TreeSet<>();
        for (int num : nums) distinct_ele.add(num);

        int ans = 1, count = 1;
        Integer prev = null;
        for (Integer num : distinct_ele) {
            if (prev != null && num == prev + 1) {
                count++;
                ans = Math.max(ans, count);
            } else {
                count = 1;
            }
            prev = num;
        }
        return ans;
    }
}

// Alternative writing of sorting approach
class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;

        TreeSet<Integer> distinct_ele = new TreeSet<>();
        for (int num : nums) distinct_ele.add(num);

        int ans = 1, count = 1;
        Integer prev = null;
        for (Integer num : distinct_ele) {
            if (prev != null && num == prev + 1) {
                count++;
            } else {
                ans = Math.max(ans, count);
                count = 1;
            }
            prev = num;
        }
        ans = Math.max(ans, count);
        return ans;
    }
}

// Method 2: Using HashSet (Optimized O(N))
class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) numSet.add(num);
        
        int ans = 0;
        for (int n : numSet) {
            if (!numSet.contains(n - 1)) { // Start of a new sequence
                int longSeq = 0;
                while (numSet.contains(n + longSeq)) {
                    longSeq++;
                }
                ans = Math.max(ans, longSeq);
            }
        }
        return ans;
    }
}

// Method 3: Using Disjoint Set Union (DSU)
class DSU {
    private int[] parent, size;
    
    public DSU(int n) {
        parent = new int[n];
        size = new int[n];
        Arrays.fill(size, 1);
        for (int i = 0; i < n; i++) parent[i] = i;
    }

    public int findParent(int n) {
        if (n == parent[n]) return n;
        return parent[n] = findParent(parent[n]);
    }

    public void union(int n1, int n2) {
        int p1 = findParent(n1), p2 = findParent(n2);
        if (size[p1] < size[p2]) {
            parent[p1] = p2;
            size[p2] += size[p1];
        } else {
            parent[p2] = p1;
            size[p1] += size[p2];
        }
    }

    public int getLargestComponentSize() {
        int maxSize = 1;
        for (int i = 0; i < parent.length; i++) {
            if (i == parent[i]) { // Root of a component
                maxSize = Math.max(maxSize, size[i]);
            }
        }
        return maxSize;
    }
}

class Solution {
    public int longestConsecutive(int[] nums) {
        int n = nums.length;
        if (n == 0) return 0;

        DSU dsu = new DSU(n);
        Map<Integer, Integer> numToIndex = new HashMap<>();

        for (int i = 0; i < n; i++) {
            int num = nums[i];
            if (numToIndex.containsKey(num)) continue;

            if (numToIndex.containsKey(num + 1)) dsu.union(i, numToIndex.get(num + 1));
            if (numToIndex.containsKey(num - 1)) dsu.union(i, numToIndex.get(num - 1));

            numToIndex.put(num, i);
        }

        return dsu.getLargestComponentSize();
    }
}
"""

# C++ Code 
"""
 // Method 1: Sorting and Iterating

#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:

    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;

        vector<int> distinct_ele(nums.begin(), nums.end());
        sort(distinct_ele.begin(), distinct_ele.end());

        int ans = 1, count = 1;
        for (size_t i = 0; i + 1 < distinct_ele.size(); ++i) {
            if (distinct_ele[i + 1] != distinct_ele[i] + 1) {
                count = 1;
            } else {
                count++;
                ans = max(ans, count);
            }
        }
        return ans;
    }
};

// Alternative writing of sorting approach
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;

        vector<int> distinct_ele(nums.begin(), nums.end());
        sort(distinct_ele.begin(), distinct_ele.end());

        int ans = 1, count = 1;
        for (size_t i = 0; i + 1 < distinct_ele.size(); ++i) {
            if (distinct_ele[i + 1] != distinct_ele[i] + 1) {
                ans = max(ans, count);
                count = 1;
            } else {
                count++;
            }
        }
        ans = max(ans, count);
        return ans;
    }
};

// Method 2: Using HashSet (Optimized O(N))
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int ans = 0;

        for (int n : numSet) {
            if (numSet.find(n - 1) == numSet.end()) { // Start of a new sequence
                int longSeq = 0;
                while (numSet.find(n + longSeq) != numSet.end()) {
                    longSeq++;
                }
                ans = max(ans, longSeq);
            }
        }
        return ans;
    }
};

// Method 3: Using Disjoint Set Union (DSU)
class DSU {
public:
    vector<int> parent, size;
    DSU(int n) : parent(n), size(n, 1) {
        for (int i = 0; i < n; i++) parent[i] = i;
    }

    int findParent(int n) {
        if (n == parent[n]) return n;
        return parent[n] = findParent(parent[n]);
    }

    void unionSets(int n1, int n2) {
        int p1 = findParent(n1), p2 = findParent(n2);
        if (size[p1] < size[p2]) {
            parent[p1] = p2;
            size[p2] += size[p1];
        } else {
            parent[p2] = p1;
            size[p1] += size[p2];
        }
    }
};

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;

        DSU dsu(n);
        unordered_map<int, int> numToIndex;

        for (int i = 0; i < n; i++) {
            int num = nums[i];
            if (numToIndex.count(num)) continue;

            if (numToIndex.count(num + 1)) dsu.unionSets(i, numToIndex[num + 1]);
            if (numToIndex.count(num - 1)) dsu.unionSets(i, numToIndex[num - 1]);

            numToIndex[num] = i;
        }

        return *max_element(dsu.size.begin(), dsu.size.end());
    }
};
"""
