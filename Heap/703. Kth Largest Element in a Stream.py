# add will give ans in O(1) only

import heapq
class KthLargest:   
    def __init__(self, k: int, nums: List[int]):
        self.k= k
        self.nums= nums
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:  # will run 'n-k' times only as there will be only one extra ele in heap always
            heapq.heappop(self.nums)
        return self.nums[0]

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