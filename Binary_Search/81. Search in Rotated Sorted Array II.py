# Exact solution of q : "33. Search in Rotated Sorted Array" won't work.
# Where it will fail?
# Ans: will fail in test cases like =>
# Given a size n and two integers 'a' != 'b', we can always construct n different arrays of size n 
# such that there is a single 'a' while the rest are 'b', and clearly they are all valid rotated sorted arrays. 
# In other words, even if 'a' exists, it can be at any location; so in the worst case where the input array only contains 'b',
# an algorithm must access all n locations of such array to determine whether a exists.

# i.e when there is only two ele then we will get wrong ans based on their arrangements. like:
# [1,0,1,1,1] (target = 0), [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1] (target = 2)

# why part1 ans giving wrong?
# Because when we are checking the sorted part then we are comparing only 'mid' with start
#  without taking care of elements that are coming in middle of 'start' and 'mid'.
# e.g: [1,0,1,1,1] . mid = 2 then according to our 'if' condition array from index '0' to '2' is sorted 
# but its not because '0' in between.
# That's why getting wrong ans.

# There is no way to get ans in logn for such cases. will go in O(n)

# How to solve?
# Just skip duplicates before finding the 'mid' and after that apply the exact solution of '"33. Search in Rotated Sorted Array"'.
# Note: skipping dupliactes may go in O(n) for those cases.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1 
        while left < right:

            # shifting to remove duplicate elements. we have to break this loop before condition of outer while loop only.
            # Otherwise we will get wrong ans. so left is going till -> 'right -1' instead of 'right'.
            while left < right - 1 and nums[left] == nums[left+1]:
                left += 1
            while left < right -1  and nums[right] == nums[right-1]:
                right -= 1

            # from here exactly same as "33. Search in Rotated Sorted Array"  
            mid=(left+right)//2

            if nums[mid] >= nums[left] :
                if nums[left] <= target <= nums[mid] :
                    right= mid
                else:
                    left= mid + 1

            else:
                if nums[mid + 1] <= target <= nums[right]:
                    left= mid + 1
                else:
                    right= mid

        return nums[left] == target