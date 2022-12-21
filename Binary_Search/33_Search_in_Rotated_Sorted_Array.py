# 1st method: first finding the index of min ele and calling the binary search on left side (before pivot) 
# and right side from pivot till end
# ele from index 0 till before index of  min ele will be sorted in ascending order and
# ele from index of min ele till last index will be sorted in ascending order
# so just apply binary search on both the parts after finding the index of pivot ele

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n= len(nums)
        # 1st find the index of minimum ele(here pivot index) 
        pivot_index= self.BinarySearchPivot(nums,0,n-1)
        # now apply binry search from index 0 before index of minimum ele
        left= self.BinarySearch(nums,target,0,pivot_index-1)
        if left== -1:
            # if not found in left side 
            # apply binary search from index of min ele till last index
            right= self.BinarySearch(nums,target,pivot_index,n-1)
            if right== -1:
                return -1
            else:
                return right
        return left
    
    def BinarySearchPivot(nums):              
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
    
            if nums[left] >nums[mid]:   # means array from 'left' to 'mid' is unsorted
                right = mid-1            # so max will lie before mid 

            else:      # here it will guarantee that array from left to mid is sorted and 
            # mid to right is unsorted and mid can also be the max
            # so max will lie in this range only 
                left= mid
        # after loop will fail , start and end will point to 
        # the same ele and that will be the maximum ele
        # because both are merging towards the index of max ele in each iteration
    
        return nums[left]
            
    def BinarySearch(self,arr,target,low,high):
        start,end= low,high
        while(start<= end):
            mid= start + (end-start)//2
            if arr[mid]== target:
                return mid
            elif arr[mid]<target:
                start= mid+1
            else:
                end= mid-1
        return -1


# method2: By recursion(Template 2)
#logic: just finding the sorted part and checking whether ele lies 
# in this or not .. if lies then call the binary search  as we can directly apply binary search in sorted part only.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.search1(nums,target,0,len(nums)-1)
    
    def search1(self,arr, target, low, high):
        start, end= low, high
        while start<end:
            mid= start + (end-start)//2
            if arr[start] <= arr[mid]: # means array is sorted from start to mid
            # so we can check if target exist bw start and mid
            # if it exists then we can apply binary search directly

                if arr[start] <=target<=arr[mid]:
                    return self.search1(arr, target,start, mid)
                else: # if not present then check in other part
                    return self.search1(arr, target,mid+1,end)

            # if above part is not sorted then it other part from mid+1 to end must be sorted
            # check if target lies in this range        
            else: 
                if arr[mid+1] <=target<=arr[end]:  # if lies call binary search
                    return self.search1(arr, target,mid+1,end)
                # if not lies from 'mid+1' to end then it must be before it
                else:
                    return self.search1(arr, target,start,mid)
        return start if arr[start]== target else -1







        

        