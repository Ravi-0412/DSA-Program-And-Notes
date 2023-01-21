# Brute force: find all the permuatation and store them in a list.
# after that sort that list and find the index of curr given num and return the next index num for the ans.

# My better approach.
# Time: O(n^2)

# i was doing by finding the permutation no of the given number by just finding the index of each num in the sorted arr of given number.
# say the permutaion no of given num is 'K' then we can find the 'k+1'th permutation to get the ans.
# if num given== sorted(num)[::-1], it means this is the last permutation so return the first sorted(num) as ans.
# But since it contains duplicate number also, it will not work.


# Best one: 
# Since we have to include all the given number in permutation.
# Logic: This Q reduces to 'Find the next greater number than the given number only using the digit of the given number'.
# and for finding this we can start from righmost side.

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
        print(nums,i-1, j)
        nums[j], nums[i-1]= nums[i-1], nums[j]
        print(nums,i)
        # 4) reverse the arr from index 'i' to last.
        # return nums[:i] + (nums[i+1:])[::-1]   # this will not work. because 'nums[:i]: create another array but nums[i:] modifies the same arr'.
        nums[i:]= nums[i:][::-1]
