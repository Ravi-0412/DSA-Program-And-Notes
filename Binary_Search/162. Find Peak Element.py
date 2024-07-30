# the best thing of this problem is we can apply binary search in this.

# 1st method : return index of max element. O(n)

# 2nd method: Binary Search
# logic: check if mid is 'peak ele' or not.
# if not then move into the direction of greater ele i.e due to which 'mid' didn't become the 'peak'.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)== 1:
            return 0
        n, start, end= len(nums), 0, len(nums)-1
        while start <= end:
            mid = start + (end-start)//2
            if mid > 0 and mid < n-1:  # if mid is not the first and last ele
                if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]: # peak ele will hold this condition
                    return mid
                # move to the side containing bigger ele i.e due to which 'mid' didn't become the 'peak' element.
                if nums[mid] <= nums[mid -1]:
                    end = mid- 1
                else: # nums[mid] <= nums[mid +1]
                    start= mid+ 1
            # now handle the edge cases
            elif mid== 0:  #if first ele
                if nums[0]> nums[1]:
                    return 0
                else:  # will handle the case when there is only two ele
                    return 1
            elif mid== n-1:  # if last ele
                if nums[n-1] > nums[n-2]:
                    return n-1

# Method 3: Better one
# same logic with Template 2
# ans will always lie in the decreasing part.
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start= 0
        end= len(nums)-1
        while start < end:
            mid= start+ (end-start)//2
            # in which direction  we should move 
            # will depend on the value of arr[mid] and arr[mid+1]
            if nums[mid] > nums[mid+1]: 
            # means we are in decr part of array i.e from mid it's decreasing
            # so our ans will lie on the left hand side of mid including 'mid'
                end= mid
            else:  #  peak(maximum ele) will be on right side of mid only excluding 'mid'
                start= mid +1
        return start

# Note: This same logic can  be used to find one of the peak ele(ele greater than neighbours) in any type of array.
# this doesn't mean you can find the max in any array using this approach. 
# only mean you can find any one of those ele following the property or array following this type of property.
    
# e.g:1)  '852. Peak Index in a Mountain Array'
# in this there will be only one peak ele
# other things are totally same as '162. find peak index'. 

# 2) 1095. Find in Mountain Array




