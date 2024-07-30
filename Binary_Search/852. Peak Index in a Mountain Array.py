
# Note: exact same as '162. FindPeakIndex'. in this there will be only one peak ele
# other things are totally same as '162. find peak index'. 

# method 2: 

class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        start= 0
        end= len(nums)-1
        while start < end:
            mid= start+ (end-start)//2
            # in which direction  we should move 
            # will depend on the value of arr[mid] and arr[mid+1]
            if nums[mid] > nums[mid+1]: 
            # means we are in decr part of array
            # so our ans will lie on the left hand side of mid including 'mid'
                end= mid
            else:  #  peak(maximum ele) will be on left side of mid including mid
                start= mid +1
        return start


# Later learn and do by 'Golden-section search'.
# Last solution of link : https://leetcode.com/problems/peak-index-in-a-mountain-array/solutions/139848/c-java-python-better-than-binary-search/