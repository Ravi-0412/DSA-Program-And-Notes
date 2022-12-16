# the same approach can be used to find the correct index of an element 
# if even ele is not in the sorted array like: Q) if element would be in the array what would be its index?
# we are just doing the same thing only i.e; finding the proper index of the given number

# 1st one 
def ceiling_number(arr,num):
    n= len(arr)
    low= 0
    high= n-1
    while(low<= high):
        mid= int(low+ (high- low)/2)
        if arr[mid]== num: 
            return arr[mid]
        elif arr[mid]< num: 
            low= mid+ 1
        else:
            high= mid-1
    return arr[low]


arr= [2,3,5,9,14,16,18]
print(ceiling_number(arr,14))
print(ceiling_number(arr,15))
print(ceiling_number(arr,4))
print(ceiling_number(arr,9))
print(ceiling_number(arr,8))


# 35. Search Insert Position
# index of ceil value will give the ans
# https://leetcode.com/problems/search-insert-position/

# if contains duplicate also then just change the if condition like "find the smallest no greater than target"
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n= len(nums)
        low= 0
        high= n-1
        while(low<= high):
            mid= int(low+ (high- low)/2)
            if nums[mid]== target: 
                return mid
            elif nums[mid]< target: 
                low= mid+ 1
            else:
                high= mid-1
        return low
    