# # 1st method(myself) : time= o(n) ,space= o(n)
# class Solution:
#     def sortArrayByParity(self, nums: List[int]) -> List[int]:
#         n= len(nums)
#         even_list= []
#         odd_list=  []
#         for val in nums:
#             if(val%2==0):
#                 even_list.append(val)
#             else:
#                 odd_list.append(val)
#         even_list=even_list+odd_list
#         return even_list


# # 2nd method: very much concise and elegant way of 1st method
# class Solution:
#     def sortArrayByParity(self, nums: List[int]) -> List[int]:
#         return [val for val in nums if val%2==0] + [val for val in nums if val%2!=0]


# 3rd method: time= o(n) ,space= o(1)
# class Solution:
#     def sortArrayByParity(self, nums: List[int]) -> List[int]:
#         n= len(nums)
#         i,j=0,n-1
#         # if num[i] is odd swap it with num[j] and decrement j, else increment i
#         # to bring the even number to the front
#         while(i<j):
#             if(nums[i]%2!= 0):     
#                 temp= nums[i]
#                 nums[i]= nums[j]
#                 nums[j]= temp
#                 j-= 1
#             else: 
#                 i+= 1
#         return nums
            
            
        
        
        