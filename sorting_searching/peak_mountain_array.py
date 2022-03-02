#  method1: brute force 
# just find the index of maximum element in the array


# method 2: Binary search
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start= 0
        end= len(arr)-1
        while(start<= end):
            mid= start+ (end-start)//2
            # if mid ele will be greater than the ele
            # on its left and right side then
            # that will be the peak element
            if arr[mid-1] < arr[mid]> arr[mid+1]:
                return mid
            # if ele at 'mid+1'is greater than at 'mid' 
            # and greater than ele at 'mid-1' means still increasig only
            elif arr[mid]< arr[mid+1]: #  peak will be on right side of mid
                start= mid +1
            # if ele at 'mid'is greater than at 'mid+1' 
            # and lesser than ele at 'mid-1' means its decreasing
            elif arr[mid] > arr[mid+1]: # means peak will be on left side of mid
                end= mid-1
        # these three condition will cover all conditions    


# method 3: Using binary search to find the largest element
# beacuse indirectly we have to find the index of maximum ele(peak ele)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start= 0
        end= len(arr)-1
        while(start<end):
            mid= start+ (end-start)//2
            if arr[mid]< arr[mid+1]: 
            # means we are in incr part of array
            # this might be the ans, but look at left 
            # because end!= mid-1 may be 
            # so peak(maximum ele) will be on right side of mid
                start= mid +1
            else:  #  peak(maximum ele) will be on left side of mid including mid
                end= mid
        # after loop will fail then start= end and both will be
        # pointing to the maximum ele in the array
        # both are always trying to find max element in the array
        # which is our ans
        return start