# 1st method : 
# time: O(n)
# just compare the ele with its next ele
# in rotated and sorted array above condition will hold exactly once or zero time(in case array is already sorted in ascending order)
# so in case if holding true more than once then not sorted and rotated

# this logic will help in a lot of questions
class Solution:
    def check(self, nums: List[int]) -> bool:
        n= len(nums)
        count= 0
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:   
                count+= 1
        # if count>1:
        #     return False
        # return True
        return count<= 1