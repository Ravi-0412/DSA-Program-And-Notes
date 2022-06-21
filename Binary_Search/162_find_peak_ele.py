# the best thing of thing of this problem is we can apply binary search in this

# 1st method (better one): 
# Excatly same solution of 'index of peak ele in mountain array' will work as in this q 
# there can be many mountain and we have to return index of any of the peak ele


# other method
# this method can work in 'index of peak ele in mountain array also' 
def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        n,start, end= len(nums), 0, len(nums)-1
        while start<= end:
            mid= start + (end-start)//2
            if mid >0 and mid < n-1:
                if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]: # peak ele will hold this condition
                    return mid
                # move to the side containing bigger ele
                elif nums[mid-1] > nums[mid]:
                    end= mid- 1
                else: # nums[mid+1] > nums[mid]
                    start= mid+ 1
            # now handle the edge cases
            elif mid== 0:
                if nums[0]> nums[1]:
                    return 0
                else:
                    return 1
            elif mid== n-1:
                if nums[n-1]>nums[n-2]:
                    return n-1
                else:
                    return n-2
