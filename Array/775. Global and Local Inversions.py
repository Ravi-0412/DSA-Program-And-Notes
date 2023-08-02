# Note: we are able to do this by these methods since no are only from '0' to 'n-1' and 
# there is only 'n' element each exactly occuring once(permutation).

# method 1:
# The problem asks us to find whether the number of global inversions are equal to local inversion.
# And we know all local inversion are global. Why? .Because local inversions are basically gobal with
# a distance as one between them.So if we can find at least one global inversion which is not local 
# our job is done and we can eliminate by returning false.
# And since we are maintaining the maximum value all the cases will be covered in it because we only need one case for False.

# logic: if curr_max is greater than any of the non-adjacent element, then simply return False.
# At last return True

# time: O(n)

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        curr_max= nums[0]
        for i in range(len(nums)- 2):
            curr_max= max(curr_max, nums[i])
            if curr_max > nums[i+2]:  # if greater than any one of the non-adjacent ele.
                return False
        return True


# method 2:
# Explanation: 
# Q reduce to :
# Suppose you have a sorted array [1, 2, 3, 4, 5], and each element differ by one. 
# How can you create a new array with same local inversion and global inversion by swap elements?

# The answer is simply swap the current element with its neighbor.

# you can switch A[i] with A[i+1], which turns to be [1, 3, 2, 4, 5] if i=1
# you can switch A[i] with A[i-1], which turns to be [2, 1, 3, 4, 5] if i=1
# Switch to any other position would break the promise. That's quite intuitive, 
# because switch i to i+2 would create a non-local global inversion.

# Original explain works quite similar way. If i is not in A[i], A[i+1] and A[i-1], 
# that means there must be a swap between A[i+/-k] swap with A[i] (k>=2),
# since they are not neighbor at sorted array, you immediately create a non-local global inversion.

# time: O(n)
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if abs(nums[i]- i) > 1 :
                return False
        return True

# VVI: method 3
# Generalize to any integer array (not necessarily a 0->N permutation)
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n= len(nums)
        # check if local inversion is enough to sort the array.
        i= 1
        while i < n:
            # swap if we find any local inversion.
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i]= nums[i], nums[i-1]
                # the recently swapped ele should not be swapped anymore otherwise, we will get global inversion.
                i+=  1  # so incr 'i'. if inversion then we are incr 'i' by '2' in total.
            i+= 1   
        # Now check if array is sorted or not afterward.  (Here array might not be sorted for last input)
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                return False
        return True


# this will not work in Python since we can't incr the iterating variable we are using in for loop(here 'i') manually.
# it will always start checking from the next value only.
# so used while loop instead of for loop.
# Read this : https://stackoverflow.com/questions/15363138/scope-of-python-variable-in-for-loop#comment21706302_15363138
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n= len(nums)
        # check if local inversion is enough to sort the array.
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i]= nums[i], nums[i-1]
                # the recently swapped ele should not be swapped anymore otherwise, we will get global inversion.
                i+=  1  # so incr 'i'.   # This doesn't work in python
        # Now check if array is sorted or not afterward.  (Here array might not be sorted for last input)
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                return False
        return True

