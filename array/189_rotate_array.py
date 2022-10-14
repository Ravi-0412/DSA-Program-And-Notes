# 1st method: time o(n),space o(n) 
#
# gfg accepted for left rotation just after modifyingh the program

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n= len(nums)
#         k=k%n  #this '%' i was missing thats why leetcode was not accepting . will have to bring k in range of n thats why % is necessary 
#         temp= nums.copy()
#         for i in range(n):
#             position= i+k
#             if(position<n):
#                 nums[position]= temp[i]
#             else:
#                 nums[position-n]= temp[i]


# very concise way of writing the above code
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        temp,n= nums.copy(), len(nums)
        k= k%n
        for i in range(n):
            nums[(i+k)%n]= temp[i]
        return nums

# 2nd method: very concise one
# time= space= O(n)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n= len(nums)
        k= k%n
        # print(nums[(n-k):] + nums[:(n-k)])  # will print correct one only but at return time it will return the original array only   
        # return nums[(n-k):] + nums[:(n-k)]   # this one will return the original array only, because this is not changing the values in original array
    
        # nums[:]= nums[(n-k):] + nums[:(n-k)]  # or use negative slicing 
        nums[:] = nums[-k:] + nums[:-k]   # better one
        
         # nums[:]= nums[-k:] + nums[:n-k]  # this will incorrect ans in case of one ele and k=0, it will just add that array two times
        return nums

# Note:
# 1) nums[:] = nums[n-k:] + nums[:n-k] 
# 2) nums = nums[n-k:] + nums[:n-k]
# The previous one can truly change the value of old nums
# but the following one(2nd one) just changes its reference to a new nums not the value of old nums


# 3rd method: optimising the space complexity to O(1) for right rotation
# logic: 1)Reverse the first 'n-k' elements 
# 2) Reverse the remaining ele 'k' ele i.e from index 'n-k' to 'n-1' i.e 'k' ele from end
# 3) and finally reverse the whole array 
# Time: o(n),space: o(1)


# for left rotation : this for this like above
# logic: 1)Reverse the first 'k' elements 
# 2) Reverse the remaining ele 'n-k' i.e from index 'k+1' to 'n-1'
# 3) and finally reverse the whole array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n= len(nums) 
        k=k%n
        def reverse(a,l,h):
            i,j=l,h
            while(i<j):
                nums[i],nums[j]= nums[j],nums[i]
                i+= 1
                j-= 1
        reverse(nums,0,n-k-1)
        reverse(nums,n-k,n-1)
        reverse(nums,0,n-1)
