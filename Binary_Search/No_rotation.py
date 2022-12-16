# no of rotation will be equal to index of minimum element in the array
# so just we have to find the minimum element index
# minimum/max ele will always exist in the unsorted part
class Solution:
    def findKRotation(self,nums,  n):
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:   # means array from 'mid' to 'right' is unsorted
                left = mid + 1            # so minimum will lie in this part only i.e beyond mid

            else:      
            # here it will guarantee that array from 
            # mid to right is sorted and start to mid is unsorted and mid can also be minimum
                right = mid
        return left   # returning the index of minimum ele 