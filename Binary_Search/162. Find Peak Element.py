# 1st method: 
# Binary Search
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

# Java Code 
"""
public class Solution {
    public int findPeakElement(int[] nums) {
        if (nums.length == 1) {
            return 0;
        }
        int n = nums.length, start = 0, end = nums.length - 1;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (mid > 0 && mid < n - 1) {  // if mid is not the first and last ele
                if (nums[mid] > nums[mid - 1] && nums[mid] > nums[mid + 1]) { // peak ele will hold this condition
                    return mid;
                }
                // move to the side containing bigger ele i.e due to which 'mid' didn't become the 'peak' element.
                if (nums[mid] <= nums[mid - 1]) {
                    end = mid - 1;
                } else { // nums[mid] <= nums[mid +1]
                    start = mid + 1;
                }
            }
            // now handle the edge cases
            else if (mid == 0) {  // if first ele
                if (nums[0] > nums[1]) {
                    return 0;
                } else {  // will handle the case when there is only two ele
                    return 1;
                }
            } else if (mid == n - 1) {  // if last ele
                if (nums[n - 1] > nums[n - 2]) {
                    return n - 1;
                }
            }
        }
        return -1;
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int findPeakElement(const std::vector<int>& nums) {
        if (nums.size() == 1) {
            return 0;
        }
        int n = nums.size(), start = 0, end = n - 1;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (mid > 0 && mid < n - 1) {  // if mid is not the first and last ele
                if (nums[mid] > nums[mid - 1] && nums[mid] > nums[mid + 1]) { // peak ele will hold this condition
                    return mid;
                }
                // move to the side containing bigger ele i.e due to which 'mid' didn't become the 'peak' element.
                if (nums[mid] <= nums[mid - 1]) {
                    end = mid - 1;
                } else { // nums[mid] <= nums[mid +1]
                    start = mid + 1;
                }
            }
            // now handle the edge cases
            else if (mid == 0) {  // if first ele
                if (nums[0] > nums[1]) {
                    return 0;
                } else {  // will handle the case when there is only two ele
                    return 1;
                }
            } else if (mid == n - 1) {  // if last ele
                if (nums[n - 1] > nums[n - 2]) {
                    return n - 1;
                }
            }
        }
        return -1;
    }
};

"""
# Method 2: Better one
# same logic with Template 2
# ans will always lie in the decreasing part.

"""
Using : "Signal-Following" or "Uphill" logic.

Logic:
1. The Slope Test: By comparing nums[mid] and nums[mid+1], you are determining the local direction of the array.
2. Uphill Rule: If nums[mid] < nums[mid+1], you are currently on an ascending slope. 
Since a peak must exist somewhere to your right (even if it's just the very last element), you move start = mid + 1.
3. Downhill Rule: If nums[mid] > nums[mid+1], you are either at the peak itself or on a descending slope. 
Therefore, a peak must exist at mid or somewhere to your left. You move end = mid.
4. Template 2 Benefit: Using while start < end ensures that mid + 1 is always a valid index to check, preventing "Index Out of Bounds" errors.

Note: This same logic can  be used to find one of the peak ele(ele greater than neighbours) in any type of array.
This doesn't mean you can find the max in any array using this approach. 
only mean you can find any one of those ele following the property or array following this type of property.
    
e.g:1)  '852. Peak Index in a Mountain Array' => in this there will be only one peak ele
Other things are totally same as '162. find peak index'. 

2) 1095. Find in Mountain Array

Time : O(logn)
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        
        while start < end:
            mid = start + (end - start) // 2
            
            # If current element is greater than the next, 
            # we are in a decreasing sequence. 
            # The peak is to the left (including mid).
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                # If current element is smaller than the next,
                # we are in an increasing sequence.
                # The peak is strictly to the right.
                start = mid + 1
        
        # When start == end, they point to the peak element.
        return start
        

# Java Code 
"""
public class Solution {
    public int findPeakElement(int[] nums) {
        int start = 0;
        int end = nums.length - 1;
        while (start < end) {
            int mid = start + (end - start) / 2;
            // in which direction  we should move 
            // will depend on the value of arr[mid] and arr[mid+1]
            if (nums[mid] > nums[mid + 1]) {
            // means we are in decr part of array i.e from mid it's decreasing
            // so our ans will lie on the left hand side of mid including 'mid'
                end = mid;
            } else {  //  peak(maximum ele) will be on right side of mid only excluding 'mid'
                start = mid + 1;
            }
        }
        return start;
    }
}
"""

# C++ Code 
"""
class Solution {
public:
    int findPeakElement(const std::vector<int>& nums) {
        int start = 0;
        int end = nums.size() - 1;
        while (start < end) {
            int mid = start + (end - start) / 2;
            // in which direction  we should move 
            // will depend on the value of arr[mid] and arr[mid+1]
            if (nums[mid] > nums[mid + 1]) {
            // means we are in decr part of array i.e from mid it's decreasing
            // so our ans will lie on the left hand side of mid including 'mid'
                end = mid;
            } else {  //  peak(maximum ele) will be on right side of mid only excluding 'mid'
                start = mid + 1;
            }
        }
        return start;
    }
};
"""
