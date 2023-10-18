# # 1st method:
#  time= o(n^2) ,space= o(n)
# class Solution:
#     def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
#         n= len(nums)
#         target=[]
#         for i in range(n):
#             target.insert(index[i],nums[i])  # O(n) each time
#         return target


# Method 3: Without insert
# Better one

# Time : O(n)
# Reason: Slicing a list in Python has a time complexity of O(k), where 'k' is the size of the resulting slice. 


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i , num in zip(index, nums):
            target[i : i] = [num]   # inserting at 'i'th index.
        return target


# Method 3: Can done by method of Q : "315. Count of Smaller Numbers After Self".
