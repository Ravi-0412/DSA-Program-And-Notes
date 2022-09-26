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


# 2nd method- time: o(nlogn), space= o(n)
# just same logic of method 1
# when there is any q of sorting, try approach of sorting the array and find the solution from that
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n= len(nums)
        sorted_nums= sorted(nums)
        start, end= n-1,0
        # compare both list,whenever there will be 1st mistmatch that will the 'start' value
        # and last mismatch will give the value of 'end'
        # in case of any mismatch keep updating the start and end 
        for i in range(n):
            if(nums[i]!= sorted_nums[i]):
                start= min(start,i)
                end= max(end,i)            
        if end==0:  # means array is already sorted
            return 0
        else:
            return end-start+1


# 3rd method using stack , time:O(n), space: O(n)
# my mistake: for start index, i was just checking the first time it is violating theincreasing order sequence
# for end, i was checking 1st time it is violating the decreasing order sequence

# but this can be totally wrong e.g:
# [5,6,7,8,9,1,10,15,4], [1,2,2,2,2,0,5,7,4], [1,2,3,6,4,8,15,10,10,10,10,10], [1],[2,1](VVI), 

# logic:1) for start index , if elements are in order , push into the stack and once you find any ele out of order then
# keep on poping until you find any ele smaller than the current ele(out of order ele). we are simply finding the position of out of order ele and that will the 'start' index
# do the opposite for 'end' index 
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n= len(nums)
        stack = []   # used to store the index of start and end 
        start,end= n-1,0 

        # traverse left to right to finding the starting index
        # comapare the element at nums[peek] with current element
        # if current element is smaller then update 'start' value with min(top of stack,start)
        # else push the index of current element into the stack
        for i in range(n):
            # once you find any ele out of order from start then, search for its proper position in the array
            while stack and nums[stack[-1]]> nums[i]:
                start= min(start,stack.pop())
            # if ele is in order then push the curr index into the stack
            stack.append(i)
    
        # traverse right to left to finding the ending index
        # comapare the element at nums[peek] with current element
        # if current element is greater then update 'end' value with max(top of stack, end)
        # else push the index of current element into the stack  
        stack= []  
        for i in range(n-1,-1,-1):
            # once you find any ele out of order from end, search for its proper position in the array
            while stack and nums[stack[-1]]< nums[i]:
                end= max(end,stack.pop())
            # if ele is is in order, then push 
            stack.append(i)
        
        if end-start >0:  # means array is not already sorted, if array is already sorted then start= n-1 and end= 0
            return end-start+1   # this will give the final ans
        else:  # if array is already sorted
            return 0


# method 4:
# just reverse way of above logic, method 3
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) <2:
            return 0
        
        prev = nums[0]
        end = 0
		# find the largest index not in place from starting to find the 'end'
        for i in range(0, len(nums)):
            if nums[i] < prev:
                end = i
            else:
                prev = nums[i]

        start = len(nums) - 1
        prev = nums[start]
		# find the smallest index not in place from last to find the 'start'
        for i in range(len(nums)-1, -1, -1):
            if prev < nums[i]:
                start = i
            else:
                prev = nums[i]
        if end != 0:
            return end - start + 1
        else: 
            return 0