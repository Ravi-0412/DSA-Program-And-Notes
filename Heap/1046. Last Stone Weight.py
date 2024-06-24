# do stone ko smash karne ke bad jo aayega result usko phir se add karna hoga
# And ye step repeat karte rhna h.

# Note: Jahan bhi aisa kuch dikhe ki har ek operation me(ya bad) hmko min/max chahiye then
# think about heap.

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]= -stones[i]  # to make max heap we hav eto switch the sign of every ele
        heapq.heapify(stones)
        while len(stones)>1:
            y= -heapq.heappop(stones)
            x= -heapq.heappop(stones)
            if x!= y:
                y= y-x
            else:  # to handle the case if there only two ele at any point and both of them are equal
                y= 0
            heapq.heappush(stones,-y)
        return -stones[0]

# Another way.
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


# java
""""

import java.util.PriorityQueue;

class Solution {
    public int lastStoneWeight(int[] stones) {
        // Use a max-heap with a custom comparator using a lambda expression
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);

        // PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());  this will also work 
        
        // Add all stones to the max-heap
        for (int stone : stones) {
            maxHeap.add(stone);
        }
        
        // Simulate the process of smashing stones
        while (maxHeap.size() > 1) {
            int y = maxHeap.poll(); // largest stone
            int x = maxHeap.poll(); // second largest stone
            if (x != y) {
                maxHeap.add(y - x); // push the remaining weight back to the heap
            }
        }
        
        // Return the weight of the last stone, or 0 if no stones are left
        return maxHeap.isEmpty() ? 0 : maxHeap.poll();
    }
}

"""