# other two approaches are same as 'kth smallest ele'
# 1st one: sorting approach
def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]
    

# 2nd method: make a max heap and delete the k-1 element
# after that return the top ele of the array, that will be the kth largest element

# methid 3: using min Heap
# better method:
# time complexity: O(nlogk)= O(k+(n-k)lgk) time
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

# Note: for finding the 'k' largest element
# just return the heap. this will only contain the 'k' largest ele as we have poped all the smaller ele.

# Note vvi: Use opposite heap to find the kth largest/ smallest as it will save space since at any point of time
# Heap won't contain more than 'k' element.

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
//Method 1
import java.util.Arrays;

class Solution {
    public int findKthLargest(int[] nums, int k) {
        Arrays.sort(nums);
        return nums[nums.length - k];
    }
}
//Method 2
import java.util.PriorityQueue;

class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
        
        // Insert all elements into maxHeap
        for (int num : nums) {
            maxHeap.offer(num);
        }
        
        // Remove k-1 elements to get the kth largest element
        for (int i = 0; i < k - 1; i++) {
            maxHeap.poll();
        }
        
        return maxHeap.peek();
    }
}
//Method 3
import java.util.PriorityQueue;

class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        
        for (int num : nums) {
            minHeap.offer(num);
            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }

        return minHeap.peek();
    }
}
//Method 4
import java.util.Random;

class Solution {
    public int findKthLargest(int[] nums, int k) {
        int n = nums.length;
        k = n - k;
        return quickSelect(nums, 0, n - 1, k);
    }

    private int quickSelect(int[] arr, int low, int high, int k) {
        if (low <= high) {
            int q = partition(arr, low, high);
            if (q == k) return arr[q];
            if (q > k) return quickSelect(arr, low, q - 1, k);
            else return quickSelect(arr, q + 1, high, k);
        }
        return -1;
    }

    private int partition(int[] arr, int low, int high) {
        int pivot = arr[low];
        int i = low, j = high;
        
        while (i < j) {
            while (arr[j] > pivot) j--;
            while (i < j && arr[i] <= pivot) i++;
            if (i < j) swap(arr, i, j);
        }
        swap(arr, j, low);
        return j;
    }

    private void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
"""

# C++ Code 
"""
//Method 1
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        return nums[nums.size() - k];
    }
};
//Method 2
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int> maxHeap;
        
        // Insert all elements into maxHeap
        for (int num : nums) {
            maxHeap.push(num);
        }
        
        // Remove k-1 elements to get the kth largest element
        for (int i = 0; i < k - 1; i++) {
            maxHeap.pop();
        }
        
        return maxHeap.top();
    }
};
//Method 3
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> minHeap;
        
        for (int num : nums) {
            minHeap.push(num);
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }

        return minHeap.top();
    }
};
//Method 4
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int n = nums.size();
        k = n - k;
        return quickSelect(nums, 0, n - 1, k);
    }

private:
    int quickSelect(vector<int>& arr, int low, int high, int k) {
        if (low <= high) {
            int q = partition(arr, low, high);
            if (q == k) return arr[q];
            if (q > k) return quickSelect(arr, low, q - 1, k);
            else return quickSelect(arr, q + 1, high, k);
        }
        return -1;
    }

    int partition(vector<int>& arr, int low, int high) {
        int pivot = arr[low];
        int i = low, j = high;
        
        while (i < j) {
            while (arr[j] > pivot) j--;
            while (i < j && arr[i] <= pivot) i++;
            if (i < j) swap(arr[i], arr[j]);
        }
        swap(arr[j], arr[low]);
        return j;
    }
};
"""