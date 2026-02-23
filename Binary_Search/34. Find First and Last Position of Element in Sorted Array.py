
# 1st method: Best one
# Time: o(logn), space:o(1)   
def search(nums,target,findStartIndex):
    ans= -1
    start= 0
    end= len(nums)-1
    while(start<= end):
        mid= start+ (end-start)//2
        if nums[mid]> target:
            end= mid-1
        elif nums[mid]< target:
            start= mid+1
        else:
            # potential ans has been found means
            # the target ele exist now we have to find 
            # its first and last index
            ans= mid  # updating the ans since we have got the target ele
            if(findStartIndex==1):  # this will execute to find the first position
                end= mid-1  # since we are finding the first index so we are updating
                            # the 'end' keeping 'start' constant because we have to find on left side of mid
            else:
                start= mid+1       # this will execute to find the last position
                                # since we are finding the last index so we are updating
                            # the 'start' keeping 'end' constant because we have to find on right side of the mid
    return ans  # will return first or last index depending upon 
                # the third parameter 'findStartIndex'

    
def searchRange(nums, target):
    ans= [-1,-1]  # initialising the result , nothing target will not be 
                  # there then it will retrun this only
    ans[0]= search(nums,target, 1) # will give the first position of target ele
    ans[1]= search(nums,target, 0)  # will give the last position of target ele
    return ans

nums= [5,7,7,8,8,10]
print(searchRange(nums,8))
print(searchRange(nums,6))
nums1= []
print(searchRange(nums1,0))



# method 2: 
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans= [-1,-1]
        start= self.search(nums,target, 1)  # was missing 'self' before search
                                            # and due to this was getting error again and again
        end=   self.search(nums,target, 0)       
        ans[0]= start
        ans[1]= end
        return ans
    
    def search(self,nums,target,findStartIndex):
        #   if findStartIndex== 1, it means we are finding the first position if '0' means we are finding the last position
        ans= -1
        start= 0
        end= len(nums)-1
        while(start<= end):
            mid= start+ (end-start)//2
            if nums[mid]> target:
                end= mid-1
            elif nums[mid]< target:
                start= mid+1
            else:
                # potential ans has been found
                ans= mid
                if(findStartIndex==1):
                    end= mid-1
                else:
                    start= mid+1
        return ans


# Java Code 
"""
//Method 1
import java.util.*;

class Solution {
    private int search(int[] nums, int target, boolean findStartIndex) {
        int ans = -1;
        int start = 0, end = nums.length - 1;

        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (nums[mid] > target) {
                end = mid - 1;
            } else if (nums[mid] < target) {
                start = mid + 1;
            } else {
                ans = mid;
                if (findStartIndex) {
                    end = mid - 1; // Find first occurrence
                } else {
                    start = mid + 1; // Find last occurrence
                }
            }
        }
        return ans;
    }

    public int[] searchRange(int[] nums, int target) {
        int[] ans = {-1, -1};
        ans[0] = search(nums, target, true);  // First occurrence
        ans[1] = search(nums, target, false); // Last occurrence
        return ans;
    }
}

//Method 2
class Solution {
    private int search(int[] nums, int target, int left, int right, boolean findStartIndex) {
        if (left > right) return -1;

        int mid = left + (right - left) / 2;
        if (nums[mid] > target) {
            return search(nums, target, left, mid - 1, findStartIndex);
        } else if (nums[mid] < target) {
            return search(nums, target, mid + 1, right, findStartIndex);
        } else {
            if (findStartIndex) {
                int leftSearch = search(nums, target, left, mid - 1, findStartIndex);
                return leftSearch != -1 ? leftSearch : mid;
            } else {
                int rightSearch = search(nums, target, mid + 1, right, findStartIndex);
                return rightSearch != -1 ? rightSearch : mid;
            }
        }
    }

    public int[] searchRange(int[] nums, int target) {
        int[] ans = {-1, -1};
        ans[0] = search(nums, target, 0, nums.length - 1, true);  // First occurrence
        ans[1] = search(nums, target, 0, nums.length - 1, false); // Last occurrence
        return ans;
    }
}
"""

# C++ Code 
"""
//Method 1
#include <vector>

using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target, bool findStartIndex) {
        int ans = -1;
        int start = 0, end = nums.size() - 1;

        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (nums[mid] > target) {
                end = mid - 1;
            } else if (nums[mid] < target) {
                start = mid + 1;
            } else {
                ans = mid;
                if (findStartIndex) {
                    end = mid - 1; // Find first occurrence
                } else {
                    start = mid + 1; // Find last occurrence
                }
            }
        }
        return ans;
    }

    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> ans = {-1, -1};
        ans[0] = search(nums, target, true);  // First occurrence
        ans[1] = search(nums, target, false); // Last occurrence
        return ans;
    }
};

//Method 2
class Solution {
public:
    int search(vector<int>& nums, int target, int left, int right, bool findStartIndex) {
        if (left > right) return -1;

        int mid = left + (right - left) / 2;
        if (nums[mid] > target) {
            return search(nums, target, left, mid - 1, findStartIndex);
        } else if (nums[mid] < target) {
            return search(nums, target, mid + 1, right, findStartIndex);
        } else {
            if (findStartIndex) {
                int leftSearch = search(nums, target, left, mid - 1, findStartIndex);
                return leftSearch != -1 ? leftSearch : mid;
            } else {
                int rightSearch = search(nums, target, mid + 1, right, findStartIndex);
                return rightSearch != -1 ? rightSearch : mid;
            }
        }
    }

    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> ans = {-1, -1};
        ans[0] = search(nums, target, 0, nums.size() - 1, true);  // First occurrence
        ans[1] = search(nums, target, 0, nums.size() - 1, false); // Last occurrence
        return ans;
    }
};
"""
