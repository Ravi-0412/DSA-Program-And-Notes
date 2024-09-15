# Note: if asked to move all zeroes at last without caring about order of non-zero ele then
# We can do like this.

# This logic wil work in Q like : '905. Sort Array By Parity'

# Logic: We have to move zero at last so focus on starting pointer
# Because we have to move from start to end if we find any zero at start.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l , r = 0, len(nums) -1
        while l < r:
            if nums[l] == 0:
                # swap 
                nums[l] , nums[r] = nums[r] , nums[l]
                r -= 1  # no need to incr 'l' as after swapping we can get '0' at 'l' because we are swapping without checking value at 'r'.
            else:
                # in correct position so simply move 'l'
                l += 1 
        return nums


# Now coming to actual Q.

# method 1:
# Similar as '26. Remove Duplicates from Sorted Array' logic.

# logic: whenever you see any '0', search for next non-zero and swap. else skip

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n= len(nums)
        i= 0  # i will denote where we have to keep next non-zero ele.
        while i < n :
            if nums[i]== 0:
                # search for next non-zero
                k=  i+ 1
                while k < n and nums[k]== 0:
                    k+= 1
                # means array is already in desired format.
                if k >= n: return nums
                # else swap  
                nums[i], nums[k]= nums[k], nums[i]
            i+= 1
        

# optimising the above method
# In above one we are always searching from 'i+ 1' even though we have already traverses more index than 'i + 1'.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n= len(nums)
        last= 0  # will tell from where we have to search for next non-zero ele. Till here we have alraedy traversed.
        i= 0   #  i will denote where we have to keep next non-zero ele.
        while i < n :
            if nums[i]== 0:
                k=  max(last + 1, i+ 1)  # We will start only from 'i+1' so taking maximum.
                while k < n and nums[k]== 0:
                    k+= 1
                if k >= n: return nums
                nums[i], nums[k]= nums[k], nums[i]
                last= k
            i+= 1
        

# New and very creative logic:
# logic: collect all consecutive zeroes and after finding any non-zero do replacement.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n= len(nums)
        snowBallSize= 0
        for i in range(n):
            if nums[i]== 0:
                snowBallSize+= 1   # tring to gather all the zeroes together.
            elif snowBallSize > 0:  # only update the value if we have encounter any zero till now.
                temp= nums[i]
                nums[i -snowBallSize]= temp   # moving the non-zero ele to the leftmost zero. 
                nums[i]= 0   # this should be zero only after replacement.
        

# Related Q: 
# 1) 26. Remove duplicates
# 2) 905. Sort Array By Parity
# 3) 75 sort colors
# 4) 926. Flip String to Monotone Increasing   => VVI
