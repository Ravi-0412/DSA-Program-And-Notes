# Logic: it's always better to increment the smaller ele to increase the multiplication.
# e.g: just take fe examples and compare i.e (3, 6), (5, 6), (10, 4) etc.

# so just run loop 'k' time and take minimum number each time and increment by '1' and 
# repeat the same thing.

# Note: wherever you have to apply any operation on min/max element always
# and same number can be reused again then think of heap.

# use minHeap, take minimum ele and increment by '1' and again push in heap.
# Repeat this step.

# giving tle in 2nd last test case but correct only.
# in java, it's getting accepted.

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        heapq.heapify(nums)
        for i in range(k):
            num = heapq.heappop(nums)
            heapq.heappush(nums, num + 1)
        ans = 1
        for num in nums:
            ans *= num
        return ans % mod

# Note vvi: It is always better to do 'modulus' while updating the ans also inside loop.
# because it will avoid overflow . 
# VVI: So it's always better to use 'mod' while calculating also. 

# Java
"""
class Solution {
    public int maximumProduct(int[] nums, int k) {
        int mod = 1000000007;
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        
        // Add all numbers to the min-heap
        for (int num : nums) {
            minHeap.offer(num);
        }
        
        // Increment the smallest number k times
        for (int i = 0; i < k; i++) {
            int num = minHeap.poll();
            minHeap.offer(num + 1);
        }
        
        // Calculate the product of all numbers in the min-heap
        long ans = 1;
        while (!minHeap.isEmpty()) {
            ans = (ans * minHeap.poll()) % mod;
        }
        
        return (int) ans;
    }
}
"""