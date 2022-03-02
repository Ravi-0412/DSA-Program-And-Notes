# 1st method: Time: o(n), space: o(1)
# just traverse the array from left to right wherever 
# you will find the currnet ele greater than next element that 
# index will be the index of maximum ele and next will be the index 
# of minimum ele
# use '%' with next ele to compare because largest ele can be at 'n-1'
# then smallest will be at '(n-1+1)%n'
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n= len(nums)
        if n==1:
            return nums[0]
        for i in range(0,n):
            if nums[i]>nums[(i+1)%n]:
                return nums[(i+1)%n]


        