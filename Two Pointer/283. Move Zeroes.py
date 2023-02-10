# time: O(n)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n= len(nums)
        # find the index of first zero.
        i= 0
        while i < n and nums[i]!= 0:
            i+= 1
        if i== n:  # means no zero is present
            return
        # find the first non-zero number after 'i' to swap.
        j= i +1
        while j < n and nums[j]== 0:
            j+= 1
        if j== n:  # means no non-zero ele is present
            return 
        # apply two pointer from 'i' to 'n-1' and swap the zero with non-zero element.
        while i< n and j < n:
            # swap(nums[i], nums[j])
            nums[i], nums[j]= nums[j], nums[i]
            # move 'i' to index where next zero is present.
            i+= 1
            while i < n and nums[i]!= 0:
                i+= 1
            # move 'j' to index where next non-zero ele is present.
            j+= 1
            while j < n and nums[j]== 0:
                j+= 1


# little concise way of writing the above same logic.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n= len(nums)
        # find the index of first zero.
        i= 0
        while i < n and nums[i]!= 0:
            i+= 1
        if i== n:  # means no zero is present
            return
        for j in range(i+1, n):
            if nums[j]!= 0:
                nums[i], nums[j]= nums[j], nums[i]
            # now move 'i' to find the next zero
            while i < n and nums[i]!= 0:
                i+= 1


# New and very creative logic:
# From discussion section
# https://leetcode.com/problems/move-zeroes/solutions/172432/the-easiest-but-unusual-snowball-java-solution-beats-100-o-n-clear-explanation/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n= len(nums)
        snowBallSize= 0
        for i in range(n):
            if nums[i]== 0:
                snowBallSize+= 1   # tring to gather all the zeroes together.
            elif snowBallSize >0:  # only update the value if we have encounter any zero till now.
                temp= nums[i]
                nums[i]= 0
                nums[i -snowBallSize]= temp   # moving the non-zero ele to the leftmost zero.  
        
        