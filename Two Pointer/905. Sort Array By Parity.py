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
# logic: try to bring the even ele at first and odd ele at last
# traverse the array and if you find odd ele then from last find the position of 1st even ele
# and then swap nums[start] and nums[end] and so on

# Note in this order of ele doesn't matter like '283. Move Zeroes' and '26. Remove Duplicates from Sorted Array'.
# So this method is working .

# Apply this method in this type of questioj if order is not mattering.

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n= len(nums)
        start, end= 0, n-1
        # start will denote the curr index and after 'end' index all the elements will be odd only
        while(start <end):
            if(nums[start]%2!= 0):      # if odd swap ele at start and end index
                nums[start], nums[end]= nums[end], nums[start]
                end-= 1  # in this case don't incr 'start' as after swapping 'start' because 
                        # we may get the odd also at start as we are swapping without checking the ele at 'end'
            else:
                start+= 1   # in this case don't decr 'end ' 
        return nums
            

# just another way of writing the above logic
# class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n= len(nums)
        start, end= 0, n-1
        # start will denote the curr index and from 'end' index all the elements will be odd only
        # in this case you always have to incr start by '1' as after each iteration one ele from start is getting placed at proper position
        while(start <end):
            if(nums[start]%2!= 0): # if odd find the position of 1st even index from last
                while start <end and nums[end]%2 != 0 :
                    end-= 1
                nums[start], nums[end]= nums[end], nums[start]
                start+= 1
            else: 
                start+= 1   # in this case don't decr 'end '

            # since we have to incr start always so we can write start+= 1 outside the if-else statement like: 
            
            # while(start <end):
            #     if(nums[start]%2!= 0): # if odd swap ele at start and end index
            #       while start <end and nums[end]%2 != 0 :
            #         end-= 1
            #     nums[start], nums[end]= nums[end], nums[start]
            # start+= 1   # in this case don't decr 'end '
        return nums     
        
        
        