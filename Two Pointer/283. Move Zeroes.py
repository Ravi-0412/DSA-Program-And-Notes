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
        i= 0  # will denote the till before which we have done the operation.
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

# method 2: simple one
# logic: whenever you see any '0', search for next non-zero and swap. else skip

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n= len(nums)
        i= 0
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
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n= len(nums)
        last= 0  # will tell from where we have to search for non-zero ele.(till where we have made array in proper format)
        i= 0
        while i < n :
            if nums[i]== 0:
                k=  max(last + 1, i+ 1)  # to handle the case when there is many non-zero ele at start, in this case we have to search from 'i+1'.
                while k < n and nums[k]== 0:
                    k+= 1
                if k >= n: return nums
                nums[i], nums[k]= nums[k], nums[i]
                last= k
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
        
        