# # 1st method(mysefl): time= o(n) ,space= o(n)
# class Solution:
#     def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
#         n= len(nums)
#         target=[]
#         for i in range(n):
#             target.insert(index[i],nums[i])
#         return target
            