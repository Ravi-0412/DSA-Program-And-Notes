# Logic: 1st minimum can be 1st ele of any of the arrays.
# For getting this we can put 1st ele from all the arrays and select the minimum one.
# For this we can use min Heap.

# But next minimum can come from same array.
# So we need to put the array number with index as well so that we can insert next ele of this array in heap.

# time: O(n*logk), n= total no of elements

import heapq
class Solution:
    def mergeKArrays(self, arr, K):
        heap, ans= [], []
        # put the 1st ele of all the arrays in the heap with the array number and index
        for i in range(len(arr)):
            heapq.heappush(heap,(arr[i][0], i, 0))  # pushing the 1st ele of 'i'th arr
        
        # now to merge the array, just pop one ele from the heap and that will be minium at present
        while heap:
            val, arr_num, ind= heapq.heappop(heap)
            ans.append(val)
            # now add the next ele of the curr arr
            if ind+ 1 < len(arr[arr_num]):
                heapq.heappush(heap, (arr[arr_num][ind+1], arr_num, ind+1))
        return ans

# Java Code 
"""
import java.util.PriorityQueue;

class Solution {
    public int[] mergeKArrays(int[][] arr, int K) {
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        int[] ans = new int[K * arr.length];
        int index = 0;

        // Push the first element of each array into the heap with the array number and index
        for (int i = 0; i < arr.length; i++) {
            if (arr[i].length > 0) {
                minHeap.offer(new int[]{arr[i][0], i, 0});
            }
        }

        // Merge the arrays by always popping the minimum element
        while (!minHeap.isEmpty()) {
            int[] top = minHeap.poll();
            int val = top[0], arr_num = top[1], ind = top[2];
            ans[index++] = val;

            // Add the next element from the current array
            if (ind + 1 < arr[arr_num].length) {
                minHeap.offer(new int[]{arr[arr_num][ind + 1], arr_num, ind + 1});
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

using namespace std;

class Solution {
public:
    vector<int> mergeKArrays(vector<vector<int>>& arr, int K) {
        priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> minHeap;
        vector<int> ans;

        // Push the first element of each array into the heap with the array number and index
        for (int i = 0; i < arr.size(); i++) {
            if (!arr[i].empty()) {
                minHeap.push({arr[i][0], {i, 0}});
            }
        }

        // Merge the arrays by always popping the minimum element
        while (!minHeap.empty()) {
            auto [val, pos] = minHeap.top();
            minHeap.pop();
            ans.push_back(val);

            int arr_num = pos.first;
            int ind = pos.second;

            // Add the next element from the current array
            if (ind + 1 < arr[arr_num].size()) {
                minHeap.push({arr[arr_num][ind + 1], {arr_num, ind + 1}});
            }
        }

        return ans;
    }
};
"""

# Related Q:
# 355. Design Twitter
