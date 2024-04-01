# Intitution: They aretelling to find a path between every pair means all ele should be connected together into single component.
# so if we can connect all element together into single component using given condition
# then True else False.

# method 1:
# Try by making graph
# Two solution link in sheet, lst one is with video.




# method 2: 
# https://leetcode.com/problems/greatest-common-divisor-traversal/solutions/3573057/math-without-union-find-with-explanation/

# We need to find a more direct approach to seeing if there are separate groups.

# Starting with one number x, compare it through the list until we find a number y that has a common factor. 
# (If there are none we can end here and return False.)
# Replace the number y with y*x//gcd(x,y). 
# This way we have a number in the list that has both x and y's unique factors (and only one copy of their common factors to keep the size down).
# Move on from x to the next number and do the same thing.
# Eventually we either find a number with no common factors to any other number or get to the last number in the list which tells us all numbers are in the same group.

# time: O(n^2)  # will not till n^2 that's why get accepted.


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        length=len(nums)
        if length==1:
            return True

        nums.sort()
        if nums[0]==1:
            return False

        for idx in range(length-1,0,-1):

            found=False
            
            for j in range(idx-1,-1,-1):
                if gcd(nums[idx],nums[j])>1:
                    # make nums[j]= lcm of (nums[idx], nums[j])
                    # index 'idx' and 'j' is getting connected.
                    nums[j]*=nums[idx]//(gcd(nums[idx],nums[j]))
                    found=True
                    break

            if not found:
                return False
        
        return True


# Note: Starting from start will give TLE because we are moving from lower to higher 
# updating higher also and in most of case higher will because greater only after updating.
# so time for finding gcd will be more.

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        length=len(nums)
        if length==1:
            return True

        nums.sort()
        if nums[0]==1:   # if there is '1' in the array then not possible.
            return False

        for idx in range(length- 1):

            found=False
            
            for j in range(idx + 1, length):
                if gcd(nums[idx],nums[j])>1:
                    # make nums[j]= lcm of (nums[idx], nums[j])
                    nums[j]*=nums[idx]//(gcd(nums[idx],nums[j]))
                    found=True
                    break
 
            if not found:
                return False
        
        return True

# My doubt: I am not getting why we are sorting and why after sorting it is giving corret ans.

# 