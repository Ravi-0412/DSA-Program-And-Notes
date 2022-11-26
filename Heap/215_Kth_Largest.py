# other two approaches are same as 'kth smallest ele'
# 1st one: sorting approach
def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]
    

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
                                         # in this way all the smallest ele except the k ele will get deleted
        # after this loop will end 'heap' will contain all the k largest ele and 
        # after this loop the topmost ele(1st index ele) will be the kth largest ele
        # as we have poped all the smallest ele and in max heap smallest ele get poped 
        # other k-1 ele will be greater or equal to this ele, since in min heap other ele than 1st index 
        # ele will be greater than or equal to the 1st ele
        return heap[0]

# to find the 'k' largest else:
# just return the heap. this will only contain the 'k' largest ele as we have poped all the smaller ele


# better one than all: Using Quick Select
# time: O(n)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k= len(nums)-k   # if array is alreay sorted then you will get the ans at this index only
        l,r= 0, len(nums)-1   # in range we want to traverse(partition) 
        index= self.QuickSelect(nums,k,l,r)
        return nums[index]
    
    def QuickSelect(self,nums,k,l,r):
        pivot= nums[r]   # selecting the last ele as pivot
        p= l   # position where we will place in case ele is smaller than or equal to pivot 
        #p will give the kth largest element
        # now find the proper position of pivot ele
        for i in range(l, r):   # will check from l to r-1(except pivot)
            if nums[i]<= pivot:  # means this ele should come before pivot index 
                nums[p], nums[i]= nums[i], nums[p]
                p+= 1    # next time if above condition follows then we will place the ele at this index
        # now every ele on left of p will less than or equal to the pivot
        # means 'p' will pointing to the ele greater than the pivot
        # so swap 'p' with 'r' for proper position of pivot
        nums[p], nums[r]= nums[r], nums[p]
        # now check the 'p' with 'k'
        if p== k:  # means you have got the kth largest ele
            return p
        elif p>k:  # means we have search on left side of p
            return self.QuickSelect(nums,k,l,p-1)
        else: #(p<k) means we have to search in right side of p
            return self.QuickSelect(nums,k,p+1,r)


