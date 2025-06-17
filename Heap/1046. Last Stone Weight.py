# Method 1: 

# do stone ko smash karne ke bad jo aayega result usko phir se add karna hoga
# And ye step repeat karte rhna h.

# Note: Jahan bhi aisa kuch dikhe ki har ek operation me(ya bad) hmko min/max chahiye then
# think about heap.

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]= -stones[i]  # to make max heap we have to switch the sign of every ele.
        heapq.heapify(stones)
        while len(stones)>1:
            y= -heapq.heappop(stones)
            x= -heapq.heappop(stones)
            if x!= y:
                y= y-x
                heapq.heappush(stones,-y)
        return -1*stones[0] if stones else 0


# Java Code 
"""
import java.util.PriorityQueue;

class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);

        // Convert into max heap by pushing elements
        for (int stone : stones) {
            maxHeap.offer(stone);
        }

        while (maxHeap.size() > 1) {
            int y = maxHeap.poll();
            int x = maxHeap.poll();

            if (x != y) {
                maxHeap.offer(y - x);
            }
        }

        return maxHeap.isEmpty() ? 0 : maxHeap.peek();
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
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> maxHeap;

        // Convert into max heap by pushing elements
        for (int stone : stones) {
            maxHeap.push(stone);
        }

        while (maxHeap.size() > 1) {
            int y = maxHeap.top(); maxHeap.pop();
            int x = maxHeap.top(); maxHeap.pop();

            if (x != y) {
                maxHeap.push(y - x);
            }
        }

        return maxHeap.empty() ? 0 : maxHeap.top();
    }
};
"""