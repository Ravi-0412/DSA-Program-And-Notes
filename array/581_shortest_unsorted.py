# # Brute force(not accepted on leetcode), time: o(n^2), space: o(1)
# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         n= len(nums)
#         #start,end will give the starting and last index index of subarray respectively
#         start, end= n,0
#         # start will be equal to: when we find any element(i) greater than the any upcoming next element
#         # end will be equal to: max index till we can find any smaller element than the any previous element
#         for i in range(n-1):
#             for j in range(i+1,n):
#                 if nums[i]> nums[j]:
#                     start= min(start,i)
#                     end=   max(end,j)
#         if(end==0):  # for already sorted array
#             return 0
#         else:
#             return  end-start+1


# 2nd method- time: o(n), space= o(n)
# def findUnsortedSubarray(self, nums: List[int]) -> int:
#         n= len(nums)
#         # copying the sorted 'nums' into another list temp
#         temp= sorted(nums)
#         start, end= n-1,0
# # compare both list,whenever there will be 1st mistmatch that will the 'start' value
# # and last mismatch will give the value of 'end'
#         for i in range(n):
#             if(nums[i]!= temp[i]):
#                 start= min(start,i)
#                 end= max(end,i)            
#         if(end==0):
#             return 0
#         else:
#             return end-start+1


# 3rd method using stack 
nums = [2,6,4,8,10,9,15]
n= len(nums)
stack = []   # used to store the inndex of start and end 
start,end= n-1,0 

# traverse left to right to finding the starting index
# comapare the element at nums[peek] with current element
# if current element is smaller then update 'start' value with min(top of stack,start)
# else push the index of current element into the stack
for i in range(n):
    while stack and nums[stack[-1]]> nums[i]:
        start= min(start,stack.pop())
    stack.append(i)
    
# traverse right to right to finding the ending index
# comapare the element at nums[peek] with current element
# if current element is greater then update 'end' value with max(top of stack, end)
# else push the index of current element into the stack  
stack= []  
for i in range(n-1,-1,-1):
    while stack and nums[stack[-1]]< nums[i]:
        end= max(end,stack.pop())
    stack.append(i)

if(end!=0):
    print(end-start+1)
else:
    print(0) 
