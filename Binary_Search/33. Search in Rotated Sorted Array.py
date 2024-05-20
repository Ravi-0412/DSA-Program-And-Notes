# 1st method: first finding the index of min ele and calling the binary search on left side (before pivot) 
# and right side from pivot till end
# ele from index 0 till before index of  min ele will be sorted in ascending order and
# ele from index of min ele till last index will be sorted in ascending order
# so just apply binary search on both the parts after finding the index of pivot ele

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n= len(nums)
        # 1st find the index of minimum ele(here pivot index) 
        pivot_index= self.BinarySearchPivot(nums)
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
    
    def BinarySearchPivot(self, nums):              
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
    
            if nums[left] > nums[mid]:   # means array from 'left' to 'mid' is unsorted
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
#logic: just finding the sorted part and checking whether ele lies in that or not ..
# Reason: we can only applu binary search if array is sorted.

# time:O(logn)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end= 0, len(nums) -1 
        while start < end :
            mid= start + (end-start)//2
            # means array is sorted from start to mid
            if nums[mid] >= nums[start]: 
            # so we can check if target exist bw start and mid
                if nums[start] <=target<=nums[mid]:
                    end= mid
                else: # if not present then check in other part
                    start= mid + 1

            # if above part is not sorted then other part from mid+1 to end must be sorted        
            else: 
                # check if target lies in this range. 
                # note: comparing with 'mid' will give the wrong ans.
                if nums[mid+1] <=target<=nums[end]:  # if lies call binary search
                    start= mid + 1
                # if not lies from 'mid+1' to end then it must be before it
                else:
                    end= mid
        return start if nums[start]== target else -1


# Similar Q:
# 1) "81. Search in Rotated Sorted Array II".
# https://github.com/Ravi-0412/DSA-Program-And-Notes/blob/main/Binary_Search/81.%20Search%20in%20Rotated%20Sorted%20Array%20II.py


# Java
"""
# Method 2:

public class Solution {
    public int search(int[] nums, int target) {
        int start = 0, end = nums.length - 1;

        while (start < end) {
            int mid = start + (end - start) / 2;

            // Means array is sorted from start to mid
            if (nums[mid] >= nums[start]) {
                // Check if target exists between start and mid
                if (nums[start] <= target && target <= nums[mid]) {
                    end = mid;
                } else {
                    // If not present, then check in the other part
                    start = mid + 1;
                }
            } else {
                // If the above part is not sorted, then the other part from mid+1 to end must be sorted
                // Check if target lies in this range
                if (nums[mid + 1] <= target && target <= nums[end]) {
                    start = mid + 1;
                } else {
                    // If not lies from 'mid+1' to end, then it must be before it
                    end = mid;
                }
            }
        }

        // After loop ends, check if the start points to the target
        return nums[start] == target ? start : -1;
    }
}
"""