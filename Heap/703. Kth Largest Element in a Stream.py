# add will give ans in O(1) only

import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        """
        We initialize the heap and ensure it only stores 
        the 'k' largest elements right from the start.
        """
        self.k = k
        self.heap = []
        
        # We process the initial list using our add logic
        for val in nums:
            self.add(val)

    def add(self, val: int) -> int:
        """
        1. Push the new value into the min-heap.
        2. If the size exceeds k, pop the smallest element.
        3. The root (heap[0]) is now the kth largest.
        """
        # Always add the new value first
        heapq.heappush(self.heap, val)   
        # If we have more than k elements, remove the smallest
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # The smallest of the 'k' largest elements is the kth largest
        return self.heap[0]

# java
"""
import java.util.PriorityQueue;

class KthLargest {
    private int k;
    private PriorityQueue<Integer> heap;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.heap = new PriorityQueue<>();
        for (int num : nums) {
            add(num);
        }
    }

    public int add(int val) {
        heap.offer(val);
        if (heap.size() > k) {
            heap.poll();
        }
        return heap.peek();
    }
}

"""
