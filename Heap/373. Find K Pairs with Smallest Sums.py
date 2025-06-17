# Method 1: 

# smallest ele will be at the start only. 
# So we will push (nums1[0] + nums1[0] ,0, 0) => (sum, index1, index2).
# But next minimum can be at index (0, 1) or (1, 0).

# Explanation:

# Logic: When we will pop any ele say at index (i, j) then 
# next minimum sum we will get at (i+1, j) or (j+1, i) only.

# We will push both possibility in heap and will pop pair having minimum sum using min heap.

# Note: Since there are two possibility to get same pair of indices 
# e.g: (2,2) -> (1,2) or (2, 1) so we will use visited set to keep track of visited indices.

# Note: Add visited at 1st time only otherwise you will get duplicate in answer 
# i.e if you mark visited after poping.

# time: O(k*log(m+n))

import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        visited= set()
        visited.add((0,0))
        heap, ans= [], []
        heapq.heappush(heap,(nums1[0]+ nums2[0],0,0))   # (sum, i, j)  # i, j index of nums1 and nums2.

        while len(ans) < k and heap:
            sum,i,j= heapq.heappop(heap)
            ans.append([nums1[i],nums2[j]])
            if j+1 < len(nums2) and (i,j+1) not in visited:
                visited.add((i,j+1))
                heapq.heappush(heap,(nums1[i]+ nums2[j+1],i,j+1))
            if i+1 < len(nums1) and (i+1,j) not in visited:
                visited.add((i+1,j))
                heapq.heappush(heap,(nums1[i+1]+ nums2[j], i+1, j))

        return ans
    
# Java Code 
"""
import java.util.*;

class Solution {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        Set<String> visited = new HashSet<>();
        List<List<Integer>> ans = new ArrayList<>();

        minHeap.offer(new int[]{nums1[0] + nums2[0], 0, 0});
        visited.add("0,0");

        while (ans.size() < k && !minHeap.isEmpty()) {
            int[] top = minHeap.poll();
            int i = top[1], j = top[2];
            ans.add(Arrays.asList(nums1[i], nums2[j]));

            if (j + 1 < nums2.length && !visited.contains(i + "," + (j + 1))) {
                visited.add(i + "," + (j + 1));
                minHeap.offer(new int[]{nums1[i] + nums2[j + 1], i, j + 1});
            }

            if (i + 1 < nums1.length && !visited.contains((i + 1) + "," + j)) {
                visited.add((i + 1) + "," + j);
                minHeap.offer(new int[]{nums1[i + 1] + nums2[j], i + 1, j});
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
#include <queue>
#include <set>

using namespace std;

class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> minHeap;
        set<pair<int, int>> visited;
        vector<vector<int>> ans;

        visited.insert({0, 0});
        minHeap.push({nums1[0] + nums2[0], 0, 0}); // (sum, i, j)

        while (ans.size() < k && !minHeap.empty()) {
            auto [sum, i, j] = minHeap.top();
            minHeap.pop();
            ans.push_back({nums1[i], nums2[j]});

            if (j + 1 < nums2.size() && visited.find({i, j + 1}) == visited.end()) {
                visited.insert({i, j + 1});
                minHeap.push({nums1[i] + nums2[j + 1], i, j + 1});
            }

            if (i + 1 < nums1.size() && visited.find({i + 1, j}) == visited.end()) {
                visited.insert({i + 1, j});
                minHeap.push({nums1[i + 1] + nums2[j], i + 1, j});
            }
        }

        return ans;
    }
};
"""

# Extension:  

# 1) Maximum Sum Combinations

# 2) Merge k sorted arrays
# This is also an wider extension of this approach only.
