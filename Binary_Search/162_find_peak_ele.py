# the best thing of this problem is we can apply binary search in this.

# 1st method : return index of max elemet. O(n)

# 2nd method: Binary Search
# logic: check if mid is 'peak ele' or not.
# if not then move into the direction of greater ele i.e due to which 'mid' didn't become the 'mid'.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)== 1:
            return 0
        n,start, end= len(nums), 0, len(nums)-1
        while start<= end:
            mid= start + (end-start)//2
            if mid >0 and mid < n-1:  # if mid is not the first and last ele
                if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]: # peak ele will hold this condition
                    return mid
                # move to the side containing bigger ele i.e due to which 'mid' didn't become the 'peak' element.
                elif nums[mid-1] > nums[mid]:
                    end= mid- 1
                else: # nums[mid+1] > nums[mid]
                    start= mid+ 1
            # now handle the edge cases
            elif mid== 0:  #if first ele
                if nums[0]> nums[1]:
                    return 0
                else:  # will handle the case when there is only two ele
                    return 1
            elif mid== n-1:  # if last ele
                if nums[n-1]>nums[n-2]:
                    return n-1


# same logic with Template 2
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start= 0
        end= len(nums)-1
        while start< end:
            mid= start+ (end-start)//2
            # in which direction  we should move 
            # will depend on the value of arr[mid] and arr[mid+1]
            if nums[mid]< nums[mid+1]: 
                start= mid +1
            else:  #  peak(maximum ele) will be on left side of mid including mid because we have to find the max.
                end= mid
        return start
