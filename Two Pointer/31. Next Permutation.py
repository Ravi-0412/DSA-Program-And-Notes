
# Best one: 
# Since we have to include all the given number in permutation.
# Logic: This Q reduces to 'Find the next greater number than the given number only using the digit of the given number'.
# and for finding this we can start from righmost side.

# for next smallest number,
# 1) first find 'i' from last such that  nums[i] > nums[i - 1]  then ,
# (from index 'i' to last ele, element will be in descending order.

# 2)  We have to bring 'i-1' to its correct position in right side.
# For bringing at rigth position , we have to search j' such that nums[j] > nums[i-1] then, swap(i-1, j) .
# just finding the position of nums[i-1] in a descending array i.e from index 'i' to last.

# After swapping number from index 'i' to last will be in descending order only
# So to get minimum number value from index 'i' to last, we will have to reverse array from index 'i' to last.

# For visualisation take e.g : [9, 4, 8, 3, 6, 5, 2, 1]
# i = 4, j = 5

# Steps: wrote in solution itself.
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n= len(nums)
        i= n- 1  # will point to the index such that nums[i] < nums[i-1] from the right.
        # more later you will find 'i' it means more bigger the number is & if i== 0 then num are in decreasing order. 
        j= n- 1  # will point to the index such that nums[j] > nums[i] from the right.

        # 1) first find 'i'.
        while i> 0 and nums[i-1] >= nums[i]:
            i-= 1
        if i== 0:  # no is in descending order.
            return nums.reverse()
        # 2)  find 'j'.
        while nums[j] <= nums[i-1]:
            j-= 1
        # 3) now swap the 'j' and 'i-1'.
        nums[j], nums[i-1]= nums[i-1], nums[j]
        # 4) reverse the arr from index 'i' to last.
        # return nums[:i] + (nums[i+1:])[::-1]   # this will not work. because 'nums[:i]: create another array but nums[i:] modifies the same arr'.
        nums[i:]= nums[i:][::-1]
