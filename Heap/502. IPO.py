# Method 1: 

# just similar to "2402. Meeting Rooms III"

"""
logic: we need to keep track of all projects we can complete using curr capital 'w', for this: 
1. Get all the projects which we can execute using current capital => Sort all projects based on capital required
2 . Take the maximum profit project from all available one => maxHeap

Sorting  + maxHeap

Time : O(N * logN + K * logN)
"""

import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        # 1. Combine and sort projects by their required capital (ascending)
        # Time: O(N log N)
        projects = sorted(zip(capital, profits))
        
        # max_profit_heap will store profits of projects we can afford
        # We use negative values for Max-Heap behavior in Python
        max_profit_heap = []
        
        project_idx = 0
        n = len(projects)
        
        # 2. Pick up to k projects
        # Time: O(k log N)
        for _ in range(k):
            # Add all projects we can now afford into the Max-Heap
            while project_idx < n and projects[project_idx][0] <= w:
                # We only care about the profit now, the capital constraint is met
                heapq.heappush(max_profit_heap, -projects[project_idx][1])
                project_idx += 1
            
            # If no affordable projects are available, we can't do anything more
            if not max_profit_heap:
                break
            
            # Greedily pick the project with the highest profit
            w += -heapq.heappop(max_profit_heap)
            
        return w
        


# Java Code 
"""
import java.util.PriorityQueue;

class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        PriorityQueue<Integer> maxProfit = new PriorityQueue<>((a, b) -> b - a); // Max heap for profits
        PriorityQueue<int[]> minCapital = new PriorityQueue<>((a, b) -> a[0] - b[0]); // Min heap for (capital, profit) pairs

        // Populate minCapital with (capital, profit) pairs
        for (int i = 0; i < capital.length; i++) {
            minCapital.offer(new int[]{capital[i], profits[i]});
        }

        for (int i = 0; i < k; i++) {
            // Add all affordable projects to maxProfit heap
            while (!minCapital.isEmpty() && minCapital.peek()[0] <= w) {
                maxProfit.offer(minCapital.poll()[1]);
            }

            // If no affordable project remains, return current capital
            if (maxProfit.isEmpty()) return w;

            // Select the most profitable affordable project and increase capital
            w += maxProfit.poll();
        }
        return w;
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
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        priority_queue<int> maxProfit;  // Max heap for profits of affordable projects
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minCapital; // Min heap for (capital, profit) pairs

        // Populate minCapital with (capital, profit) pairs
        for (int i = 0; i < capital.size(); i++) {
            minCapital.push({capital[i], profits[i]});
        }

        for (int i = 0; i < k; i++) {
            // Add all affordable projects to maxProfit heap
            while (!minCapital.empty() && minCapital.top().first <= w) {
                maxProfit.push(minCapital.top().second);
                minCapital.pop();
            }

            // If no affordable project remains, return current capital
            if (maxProfit.empty()) return w;

            // Select the most profitable affordable project and increase capital
            w += maxProfit.top();
            maxProfit.pop();
        }
        return w;
    }
};
"""
