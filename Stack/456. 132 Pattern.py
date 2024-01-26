# QUESTION: To search for a subsequence (s1,s2,s3) i.e (nums[i], nums[j], nums[k]) such that s1 < s3 < s2. 

# Method 1:

# Brute force:
# simply check every (i, j, k) combination using three loops to see if there is any 132 pattern.

# Time: O(n^3)

# Method 2:
# optimising to O(n^2)

# just combined the first two loop into one.
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n= len(nums)
        s1 = float('inf')   # will store minium we have seend so far on left of 'j'.
                            # More smaller will be 'nums[i]' , there will be more chances of getting the ans.
        
        # for s2 as 'nums[j]' find if we can find nums[k] keeping track of s1.
        for j in range(n):
            s1 = min(nums[j], s1)
            # if nums[j] is s1 i.e minimum till now then no need to continue for this 'j'.
            if s1 == nums[j]:
                continue
            # Now it's sure that nums[j] > s1 (any ele on it'e left)
            # Now check if there exist any nums[k] to right of 'j' following 132 pattern.
            for k in range(j+ 1, n):
                if s1 < nums[k] and nums[k] < nums[j]:
                    return True
        return False

# Method 2:
# Optimising to O(n) with help of stack.

# Logic: First think how we can track s2 and s3 i.e make sure that s3 < s2 exist.
# 's3' must be the largest number smaller than 's2' to get a valid s1 candidate to the left.

# Note: For getting largest smaller we can use stack.

# Once we encounter any number on the left(s1) that is smaller than the largest s3 we have seen so far,
# we know we found a valid sequence, since s1 < s3 and already s3 < s2.

# How to do this?
# for getting the largest 's2' i.e to search for valid (s2,s3) we can traverse right to left.
# A number becomes a candidate for s3 if there is any number on the left bigger than it.

# And largest s3 for 'nums'[i]' is always the recently popped number from the stack because :
# Stack will maintain the element in descending order only because we are popping the smaller number after each nums[i].

# Note: Hence, each time we compare nums[i] with the largest candidate for s3 within the interval nums[i+1]...nums[n-1],
#  we are effectively asking the question: Is there any 132 sequence with s1 = nums[i]? 

# Implementation:
# Have a stack, each time we store a new number, we first pop out all numbers that are smaller than that number. 
# The numbers that are popped out becomes candidate for s3.

# We keep track of the maximum of such s3 (which is always the most recently popped number from the stack).
# Once we encounter any number smaller than s3, we know we found a valid sequence since s1 < s3 implies s1 < s2.

# Time : O(n)

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        stack = []   # will store ele in descending order to get largest 's3'
        s3 = float('-inf')
        for i in range(n-1 , -1, -1):
            if nums[i] < s3:
                # Here nums[i] is behaving as s1 i.e index 'j'.
                # means we have found one pattern
                # since while loop is taking care of s2 > s3 and here we found s1 < s3
                # so finally we found pattern s1s2s3 such that s1 < s3 < s2
                return True
            # Now nums[i] will behave as 's2' i.e nums[j] .
            while stack and nums[i] > stack[-1]:
                # means we have found s2 > s3 (nums[j] > nums[k])
                # i.e there exist an element on right of 'i' which is smaller than 'nums[i]'.
                s3 = stack.pop()  # last poped will be only the largest possible condidate for s3
            stack.append(nums[i])
        return False

