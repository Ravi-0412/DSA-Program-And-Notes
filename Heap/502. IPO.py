# Method 1: 

# just similar to "2402. Meeting Rooms III"

# logic: we need to keep track of all projects we can complete using curr 'w'.
# for this we will maintain a  minHeap.
# We need to store (capital , profit) pair to get maxProfit among all possible project.

# And from the all possible projects we have to take the most profitable project, so we will maintain a maxHeap for this.

# time: O(k* 2*logn), space= O(n)
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit= []   # stores the profit of projects we can afford with current 'w'. creating maxHeap to get the maxProfit project 
        minCapital= [(c, p) for c, p in zip(capital, profits)]   # creating minHeap for pair (c, p)
        heapq.heapify(minCapital)
        print(minCapital)

        for i in range(k):
            # add all the profits of projects that we can afford into maxProfit with current capital 'w'. 
            while minCapital and minCapital[0][0] <= w:
                c, p= heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -1* p)
            # check if maxProfit is empty. if empty means we can't add any project so simply break  or return
            if not maxProfit:
                return w
            # Add the maxProfit project that we can afford with 'w'.
            w+= -1* heapq.heappop(maxProfit)
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