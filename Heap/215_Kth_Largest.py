# other two approaches are same as 'kth smallest ele'
# 1st one: sorting approach
def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]
    

# 2nd method: make a min heap and delete the k-1 element
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



