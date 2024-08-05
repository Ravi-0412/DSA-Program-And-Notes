# Method 1:
# Brute force
# O(N^2 logN) time & O(N^2) space
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ans = []
        for i in range(len(nums)):
            prefix = 0
            for ii in range(i, len(nums)):
                prefix += nums[ii]
                ans.append(prefix)
        ans.sort()
        return sum(ans[left-1:right]) % 1_000_000_007


# Method 2: Using minHeap
# Logic: Similar as 'Merge k sorted arrays'.

# Time: O(right * logn)), space = O(n)

"""
1) check if step has reached left, add x to ans;
2) extend the range sum x (currently ending at i) by adding nums[i+1] and in the meantime update the ending index to i+1.

"""

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # our ans can start from any index, so put all nums[i] with it's index in heap.
        h = [(x, i) for i, x in enumerate(nums)] #min-heap 
        heapify(h)
        
        ans = 0  # will denote the ans when we have included 'k' subarray_sum_element.
        for k in range(1, right+1): #1-indexed
            x, i = heappop(h)
            if k >= left: ans += x
            if i+1 < len(nums): 
                heappush(h, (x + nums[i+1], i+1))
                
        return ans % 1_000_000_007
    
# Java
"""
import java.util.PriorityQueue;

class Solution {
    public int rangeSum(int[] nums, int n, int left, int right) {
        // A min-heap to store pairs of (sum, index)
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        
        // Initialize the heap with the initial sums (each individual number in the array)
        for (int i = 0; i < nums.length; i++) {
            heap.add(new int[]{nums[i], i});
        }

        long ans = 0;
        for (int k = 1; k <= right; k++) {
            int[] current = heap.poll();
            int sum = current[0];
            int index = current[1];
            
            // Only add the sum to the answer if k is within the specified range
            if (k >= left) {
                ans += sum;
                ans %= 1_000_000_007; // Prevent overflow by taking modulo at each step
            }

            // If there are more elements to the right, push the next possible sum into the heap
            if (index + 1 < nums.length) {
                heap.add(new int[]{sum + nums[index + 1], index + 1});
            }
        }

        return (int) ans;
    }
}
"""