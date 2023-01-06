#  method1: brute force 
# just find the index of maximum element in the array

# in this there will be only one peak ele. other things are totally same as '162. find peak index'. 

# mountain array

# method 2: 
# exact same solution of '162. FindPeakIndex'.
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start= 0
        end= len(arr)-1
        while start< end:
            mid= start+ (end-start)//2
            # in which direction  we should move 
            # will depend on the value of arr[mid] and arr[mid+1]
            if arr[mid]> arr[mid+1]: 
            # means we are in incr part of array
            # so our ans will lie on the right hand side of mid
                end= mid
            else:  #  peak(maximum ele) will be on left side of mid including mid
                start= mid +1
        return start

