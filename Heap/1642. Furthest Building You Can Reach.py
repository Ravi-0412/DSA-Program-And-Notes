# Logic
"""
it's better to use ladder for larger difference and bricks for smaller difference.

first try to use ladder only but in case we don't have sufficient ladder then we will use bricks.
But in that case difference should be smaller.
For this we will maintain a MinHeap.

We will add element in minHeap if difference(heights[i+ 1] - heights[i]) will be > 0.
Note: len(heap) will the number of ladder we have utilised.
In case len(heap) > ladders then it means we have utilised all ladders, so we will use bricks.
So just pop from minHeap to get minimum diff and subtract bricks from that.
"""

# Time: O(n*logn)

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minHeap = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(minHeap, diff)
            if len(minHeap) > ladders:
                # means we with help of ladder we can't go ahead, so we have to use bricks for one move. 
                bricks -= heapq.heappop(minHeap)
            if bricks < 0:
                # means we don't have sufficient bricks to go ahead
                return i 
        return len(heights) - 1
# java
"""
import java.util.PriorityQueue;

class Solution {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        // Min-heap to keep track of the smallest height differences where ladders are used
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        
        for (int i = 0; i < heights.length - 1; i++) {
            int diff = heights[i + 1] - heights[i];
            
            if (diff > 0) {
                minHeap.add(diff);
            }
            
            // If the number of ladders used exceeds the available ladders
            if (minHeap.size() > ladders) {
                // Use bricks for the smallest height difference in the minHeap
                bricks -= minHeap.poll();
            }
            
            // If bricks become negative, we can't move further
            if (bricks < 0) {
                return i;
            }
        }
        
        // If we can go through all the buildings
        return heights.length - 1;
    }
}
"""
