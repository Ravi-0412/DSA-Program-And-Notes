# Time: O(n*logn)

# Logic: we have to get minimum from a set of ele so heap should come into mind.

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        minHeap = []   # Will push (cost[i], i)
        l, r = 0, n - 1

        # push the 'candidates' ele from left side
        while l < candidates :
            heapq.heappush(minHeap, (costs[l] , l))
            l += 1
        
        # push the 'candidates' ele from right side. But we may left with less no of ele than candidates so using 2nd case
        while r >= n - candidates and r >= l:
            heapq.heappush(minHeap, (costs[r] , r))
            r -= 1
        # Now 'l' will represent 1st ele from left that we need to add if we pop element from left.
        # r: will represent 1st ele from right that we need to add if we pop element from right.
        
        ans = 0
        # we need to get k ele from heap for min cost
        for i in range(k):
            cost , ind = heapq.heappop(minHeap)
            ans += cost

            # Now we have to put ele in heap from that side from which we poped the cur ele i.e either left or right
            if ind < l :
                # Means cur poped ele id from left. so we will push next  ele from left only
                if l <= r:  # then only we can push
                    heapq.heappush(minHeap, (costs[l] , l))
                    l += 1

            else:
                # Means cur poped ele id from right. so we will push next  ele from right only
                if l <= r:  # then only we can push
                    heapq.heappush(minHeap, (costs[r] , r))
                    r -= 1
        return ans

# Java Code 
"""
import java.util.PriorityQueue;

class Solution {
    public int totalCost(int[] costs, int k, int candidates) {
        int n = costs.length;
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]); // Min heap for cost, index
        int l = 0, r = n - 1;
        int ans = 0;

        // Push 'candidates' elements from the left side
        while (l < candidates) {
            minHeap.offer(new int[]{costs[l], l});
            l++;
        }

        // Push 'candidates' elements from the right side (ensuring l ≤ r)
        while (r >= n - candidates && r >= l) {
            minHeap.offer(new int[]{costs[r], r});
            r--;
        }

        // Extract 'k' elements for the minimum cost
        for (int i = 0; i < k; i++) {
            int[] top = minHeap.poll();
            int cost = top[0], ind = top[1];
            ans += cost;

            // Determine where to push the next element
            if (ind < l) { // Element was taken from the left side
                if (l <= r) {
                    minHeap.offer(new int[]{costs[l], l});
                    l++;
                }
            } else { // Element was taken from the right side
                if (l <= r) {
                    minHeap.offer(new int[]{costs[r], r});
                    r--;
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
#include <queue>

using namespace std;

class Solution {
public:
    int totalCost(vector<int>& costs, int k, int candidates) {
        int n = costs.size();
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap; // Min heap for cost, index
        int l = 0, r = n - 1;
        int ans = 0;

        // Push 'candidates' elements from the left side
        while (l < candidates) {
            minHeap.push({costs[l], l});
            l++;
        }

        // Push 'candidates' elements from the right side (ensuring l ≤ r)
        while (r >= n - candidates && r >= l) {
            minHeap.push({costs[r], r});
            r--;
        }

        // Extract 'k' elements for the minimum cost
        for (int i = 0; i < k; i++) {
            auto [cost, ind] = minHeap.top();
            minHeap.pop();
            ans += cost;

            // Determine where to push the next element
            if (ind < l) { // Element was taken from the left side
                if (l <= r) {
                    minHeap.push({costs[l], l});
                    l++;
                }
            } else { // Element was taken from the right side
                if (l <= r) {
                    minHeap.push({costs[r], r});
                    r--;
                }
            }
        }

        return ans;
    }
};
"""