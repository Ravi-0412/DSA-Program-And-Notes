# using min heap
# time: O(nlogn)
# but not able to break the tie for equal fre elements
import heapq
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count= {}
        for num in nums:
            count[num]= 1+ count.get(num, 0)
        heap= []  
        # create a min heap with freq , key 
        for k,v in count.items():
            # add the num with negative sign to bring the num with larger value first in case of equal frequency
            heapq.heappush(heap,(v,-1*k))   
        # now add the ele into ans arr as many times they have occured(equal to their freq)
        ans= []
        while(len(heap)):
            temp = heapq.heappop(heap)
            for i in range(temp[0]):     # temp[0] will contain the fre of the ele
                ans.append(-1*temp[1])      # temp[1] will contain the ele
        return ans

# java
"""
class Solution {
    public int[] frequencySort(int[] nums) {
        // Step 1: Count the frequency of each number
        Map<Integer, Integer> count = new HashMap<>();
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        // Step 2: Create a priority queue (min-heap) with custom comparator
        PriorityQueue<int[]> heap = new PriorityQueue<>(
            (a, b) -> a[0] == b[0] ? b[1] - a[1] : a[0] - b[0]);

        // Step 3: Add entries to the heap
        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            heap.offer(new int[]{entry.getValue(), entry.getKey()});
        }

        // Step 4: Build the result array
        int[] result = new int[nums.length];
        int index = 0;
        while (!heap.isEmpty()) {
            int[] temp = heap.poll();
            int frequency = temp[0];
            int value = temp[1];
            for (int i = 0; i < frequency; i++) {
                result[index++] = value;
            }
        }
        return result;
    }
}
"""

# Shortcut of above method
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        # sorting nums
        # count[x] sorts by frequency, and if two values are equal, it will sort the keys in decreasing order.
        return sorted(nums, key=lambda x: (count[x], -x))  

# method 2: can be optimised to O(n) using bucket sort
# Try later

