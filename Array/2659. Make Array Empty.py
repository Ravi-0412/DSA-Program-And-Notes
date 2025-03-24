# used heap to find the minimum ele after each deletion but giving Tle in last few test cases.
# Time: O(n* logn)

class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n= len(nums)
        q= collections.deque(nums)
        heap= nums.copy()
        heapq.heapify(heap)
        # print(q, heap)
        count= 0
        while q:
            if q[0]== heap[0]:
                q.popleft()
                heapq.heappop(heap)
            else:
                temp= q[0]
                q.popleft()
                q.append(temp)
            count+= 1   
        return count

# Method 2: can be done using simple sorting 
from typing import List

class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Store original indices along with values
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        
        # Lambda comparator function to sort based on values
        indexed_nums.sort(key=lambda x: x[0])  # Sort by number value
        
        count = n  # At minimum, n removals are needed
        prev_index = -1  # Track last processed index
        
        for i in range(n):
            curr_index = indexed_nums[i][1]
            
            # If the current index moves backward, additional operations are required
            if curr_index < prev_index:
                count += (n - i)
            
            prev_index = curr_index
        
        return count

# java
"""
import java.util.*;

class Solution {
    public int countOperationsToEmptyArray(int[] nums) {
        int n = nums.length;
        int[][] indexedNums = new int[n][2];

        // Store original indices along with values
        for (int i = 0; i < n; i++) {
            indexedNums[i][0] = nums[i]; // Value
            indexedNums[i][1] = i;       // Original index
        }

        // Sort using a lambda expression
        Arrays.sort(indexedNums, (a, b) -> Integer.compare(a[0], b[0]));
        // OR
        // Arrays.sort(indexedNums, Comparator.comparingInt(a -> a[0]));

        int count = n; // At minimum, n removals are needed
        int prevIndex = -1; // Tracks the last processed index

        for (int i = 0; i < n; i++) {
            int currIndex = indexedNums[i][1];

            // If the current index is smaller than the previous index,
            // it means a rotation would be needed
            if (currIndex < prevIndex) {
                count += (n - i);
            }

            prevIndex = currIndex;
        }

        return count;
    }
}

"""
