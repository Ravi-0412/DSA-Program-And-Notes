"""
Note: First understand Why Dp won't work here?
Two points to consider here:
1. If the next building is on lower or equal height I can move on.

2. If the next building is higher than I have two choices 
I can use ladder or I can use no. of bricks of that height difference.  => From this we can think of DP.
But it will be 3D DP(index * bricks * ladder) and size will be very large that you will get Memory Limit Exceeded.

Here it's not like I have choice either I can pick ladder or brick, I also need to make sure I reach the maximum index.

"""


# Logic: Using Heap
"""
it's better to use ladder for larger difference and bricks for smaller difference you will waste too many bricks.

So here we know that we will use ladders for the highest climb and bricks for the remaining.

first try to use ladder only but in case we don't have sufficient ladder then we will use bricks.
But in that case difference should be smaller. For this we will maintain a MinHeap.

Q) How will you manage this, like for the highest climb you are using ladders and for other you are using bricks.

1) First of all as we climb one by one, we will use ladders till we are out of ladders.
2) Now when we have consumed our all ladders, now it's our turn to use bricks. Now let's say previously we have use 
ladders to climb [4, 10, 6] and now we have to climb 5, so now I know that for 5 I should use ladder, 
and the previously I have used ladder for 4 I will use brick there.
3) So now ladders will be used to climb [10, 6, 5] and bricks for [4].
4) Now let's say I have to climb 2, then obviously I can't use ladders because they are already being used to climb high. 
SO I will use bricks here. But let's say I have one 1 brick left then I won't be able to climb further.
We got to know that if the climb is lower or equal to the climb made by ladders then we can use brick.
but if we found high climb where previously we have used ladders for the lower climb, I will use ladders here and bricks there.

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
