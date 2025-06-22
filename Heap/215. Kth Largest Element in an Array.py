# Method 1: 
# sorting approach
def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]

# Java Code 
"""
import java.util.Arrays;

public class Solution {
    public int findKthLargest(int[] nums, int k) {
        Arrays.sort(nums);
        return nums[nums.length - k];
    }
}
"""

# C++ Code 
"""
#include <algorithm>
#include <vector>

class Solution {
public:
    int findKthLargest(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        return nums[nums.size() - k];
    }
};
"""

# 2nd method: 
# make a max heap and delete the k-1 element
# after that return the top ele of the array, that will be the kth largest element

import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert to max heap by negating all elements
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        # Delete k - 1 largest elements
        for _ in range(k - 1):
            heapq.heappop(max_heap)

        # Top element is the kth largest (remember to negate it back)
        return -max_heap[0]

# Java Code 
"""
import java.util.*;

public class Solution {
    public int findKthLargest(int[] nums, int k) {
        // Convert to max heap by negating all elements
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>();
        for (int num : nums) {
            maxHeap.add(-num);
        }

        // Delete k - 1 largest elements
        for (int i = 0; i < k - 1; i++) {
            maxHeap.poll();
        }

        // Top element is the kth largest (remember to negate it back)
        return -maxHeap.peek();
    }
}
"""

# C++ Code 
"""
#include <queue>
#include <vector>

class Solution {
public:
    int findKthLargest(std::vector<int>& nums, int k) {
        // Convert to max heap by negating all elements
        std::priority_queue<int> maxHeap;
        for (int num : nums) {
            maxHeap.push(-num);
        }

        // Delete k - 1 largest elements
        for (int i = 0; i < k - 1; i++) {
            maxHeap.pop();
        }

        // Top element is the kth largest (remember to negate it back)
        return -maxHeap.top();
    }
};
"""

# methid 3: 
# Better one: using min Heap
"""
Note: for finding the 'k' largest element
just return the heap. this will only contain the 'k' largest ele as we have poped all the smaller ele.

Note vvi: Use opposite heap to find the kth largest/ smallest as it will save space since at any point of time
Heap won't contain more than 'k' element.
"""
# time complexity: O(nlogk)= O(k+(n-k)lgk)
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap= []   # creating max heap
        for num in nums:
            heapq.heappush(heap,num)     # since we are creating min heap so after pussing any ele
                                         # the smallest ele till now will be at the 1st index
            if len(heap)> k:             # we are only inserting k ele in the heap  
                heapq.heappop(heap)      # will delete the 1st index ele means the smallest ele till now
                                         # in this way all the smallest ele except the k largest ele will get deleted
        # after this loop will end 'heap' will contain all the k largest ele and 
        # Since this is min Heap so top ele will be smallest among 'k' ele i.e
        # Will be kth largest element only.
            
        return heap[0]

# Java Code 
"""
import java.util.*;

public class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();   // creating max heap
        for (int num : nums) {
            heap.add(num);     // since we are creating min heap so after pussing any ele
                               // the smallest ele till now will be at the 1st index
            if (heap.size() > k) {             // we are only inserting k ele in the heap  
                heap.poll();      // will delete the 1st index ele means the smallest ele till now
                                  // in this way all the smallest ele except the k largest ele will get deleted
            }
        }
        // after this loop will end 'heap' will contain all the k largest ele and  
        // Since this is min Heap so top ele will be smallest among 'k' ele i.e
        // Will be kth largest element only.
        return heap.peek();
    }
}
"""

# C++ Code 
"""
#include <queue>
#include <vector>

class Solution {
public:
    int findKthLargest(std::vector<int>& nums, int k) {
        std::priority_queue<int, std::vector<int>, std::greater<int>> heap;   // creating max heap
        for (int num : nums) {
            heap.push(num);     // since we are creating min heap so after pussing any ele
                                // the smallest ele till now will be at the 1st index
            if (heap.size() > k) {             // we are only inserting k ele in the heap  
                heap.pop();      // will delete the 1st index ele means the smallest ele till now
                                 // in this way all the smallest ele except the k largest ele will get deleted
            }
        }
        // after this loop will end 'heap' will contain all the k largest ele and  
        // Since this is min Heap so top ele will be smallest among 'k' ele i.e
        // Will be kth largest element only.
        return heap.top();
    }
};
"""

# Method 4: 

# better one than all: Using Quick Select
# Exactly same as quick sort.
    
# Logic: If pivot of an element is 'n-k' then this means this ele is our ans i.e kth largest ele.
# So just find the pivot and check if it is ans or not.
# If not then check which side our ans lie i.e either left side of pivot or right side of pivot and call quick_select on that side.

# time: O(n) average, worst: O(n^2)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k = n- k  # if array is alreay sorted then you will get the ans at this index only
        return self.quick_select(nums, 0, n-1,  k)
    
    def quick_select(self, arr, low, high, k):
        if low <= high:  # if arr contain at least one element
            q= self.partition(arr, low, high)
            if q == k: # pivot index element is equal to 'k' from start
                return arr[q]
            if q > k:  # element lies on left side of pivot index
                return self.quick_select(arr, low, q-1, k)
            else:    # element lies on right side of pivot index
                return self.quick_select(arr, q+1, high, k)

    def partition(self, arr, low, high):
        pivot= arr[low]
        i,j= low,high
        while i < j:
            while arr[j] > pivot:
                j-= 1
            while i < j and arr[i] <= pivot:
                i+= 1
            if i < j:
                arr[i], arr[j]= arr[j], arr[i]
        arr[j], arr[low]= arr[low], arr[j]
        return j

# Java Code 
"""
public class Solution {
    public int findKthLargest(int[] nums, int k) {
        int n = nums.length;
        k = n - k;  // if array is alreay sorted then you will get the ans at this index only
        return quickSelect(nums, 0, n - 1, k);
    }

    private int quickSelect(int[] arr, int low, int high, int k) {
        if (low <= high) {  // if arr contain at least one element
            int q = partition(arr, low, high);
            if (q == k) // pivot index element is equal to 'k' from start
                return arr[q];
            if (q > k)  // element lies on left side of pivot index
                return quickSelect(arr, low, q - 1, k);
            else    // element lies on right side of pivot index
                return quickSelect(arr, q + 1, high, k);
        }
        return -1; // unreachable if input is valid
    }

    private int partition(int[] arr, int low, int high) {
        int pivot = arr[low];
        int i = low, j = high;
        while (i < j) {
            while (arr[j] > pivot)
                j--;
            while (i < j && arr[i] <= pivot)
                i++;
            if (i < j) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[j];
        arr[j] = arr[low];
        arr[low] = temp;
        return j;
    }
}
"""

# C++ Code 
"""
#include <vector>

class Solution {
public:
    int findKthLargest(std::vector<int>& nums, int k) {
        int n = nums.size();
        k = n - k;  // if array is alreay sorted then you will get the ans at this index only
        return quickSelect(nums, 0, n - 1, k);
    }

private:
    int quickSelect(std::vector<int>& arr, int low, int high, int k) {
        if (low <= high) {  // if arr contain at least one element
            int q = partition(arr, low, high);
            if (q == k) // pivot index element is equal to 'k' from start
                return arr[q];
            if (q > k)  // element lies on left side of pivot index
                return quickSelect(arr, low, q - 1, k);
            else    // element lies on right side of pivot index
                return quickSelect(arr, q + 1, high, k);
        }
        return -1; // unreachable if input is valid
    }

    int partition(std::vector<int>& arr, int low, int high) {
        int pivot = arr[low];
        int i = low, j = high;
        while (i < j) {
            while (arr[j] > pivot)
                j--;
            while (i < j && arr[i] <= pivot)
                i++;
            if (i < j)
                std::swap(arr[i], arr[j]);
        }
        std::swap(arr[j], arr[low]);
        return j;
    }
};
"""