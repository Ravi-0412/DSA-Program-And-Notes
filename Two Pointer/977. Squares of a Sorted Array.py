# Method 1: generalised solution for both sorted and unsorted array
# LOGIC: square of both "-x" and "+x" will be same, so just count the occurrence of both "-x" and "+x" and store at same index "x".
# then traverse the array from left to right and add the square of that number having count= count at that index.

# using counting sort
# time: O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square= [0]* (10**4 + 1)   # [(count, square)]
        for n in nums:
            n= abs(n)
            square[n]+= 1
        ans= []
        for i, n in enumerate(square):
            if n!= 0:
                for j in range(n):
                    ans.append(i*i)
        return ans


# method 2: using Two pointer
# time: O(N)

# logic: The crux over here is that the array is already sorted.
# We are comparing the first and last elements because after square these have the possibility of being the highest element.
# Both the extremes contain the max element (after square ofc), so we are inserting these elements to the last of the new array to make it sorted.
# jo bda hoga uska index update kar denge.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n= len(nums)
        ans= [0]*n
        i, j= 0, n-1   # will point to start and end of array. 'j' tells the remaining index to fill.
        for index in range(n-1,-1,-1):  # we can do from left to right also.
            if abs(nums[i]) > abs(nums[j]):
                ans[index]= nums[i] * nums[i]
                i+= 1
            else:
                ans[index]= nums[j] * nums[j]
                j-= 1
        return ans

# Note: where you see array is sorted then once must think about "Two Pointer" or "Binary Search".



# tried to do in-place
# But it won't work if all number is negative
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n= len(nums)
        for i in range(n-1, -1, -1):
            if abs(nums[0]) > abs(nums[i]):
                nums[0], nums[i]= nums[i], nums[0]
            nums[i]= nums[i] * nums[i]
        return nums
    