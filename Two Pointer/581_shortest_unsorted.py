# # Brute force(not accepted on leetcode), time: o(n^2), space: o(1)
# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         n= len(nums)
#         #start,end will give the starting and last index index of subarray respectively
#         start, end= n,0
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
# my mistake: for start index, i was just checking the first time it is violating the increasing order sequence and 
# for end, i was checking 1st time it is violating the decreasing order sequence

# but this can be totally wrong e.g:
# [1,2,11,12,13,14,10,7,8,9],  [5,6,7,8,9,1,10,15,4], [1,2,2,2,2,0,5,7,4], [1,2,3,6,4,8,15,10,10,10,10,10], [1],[2,1] etc.

# Why it is violating take 1st example: [1,2,11,12,13,14,10,7,8,9]
# from start we are getting out of sequence at index '2' and from last at index '6'
# But sorting fromindex '2' to '6' will give wrong ans.
# As '7,8,9' also needs to be included.

# How to solve this issue?
# For each index we need to find the index where that ele can fit.
# for this we need to find the next smaller or equal to left and here idea of stack comes.

# Note: Since we can't get track of length so we have to check this also for 'end' using another loop.

# time: o(n), space= o(n)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n= len(nums)
        stack = []   # used to store the index of start and end 
        start,end= n-1,0 

        # For each ele, search for its proper position in the array
        for i in range(n):
            while stack and nums[stack[-1]]> nums[i]:
                # out of order means 'stack' top may be the possible index from we have to start sorting.
                start= min(start,stack.pop())
            stack.append(i)
    
        stack= []  
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]]< nums[i]:
                end= max(end,stack.pop())
            stack.append(i)
        
        # if array is not sorted then start will be somewhere before end. so 'end-start' will be greater than zero
        if end-start >0:  # means array is not already sorted, if array is already sorted then start= n-1 and end= 0
            return end-start+1   # this will give the final ans
        else:  # if array is already sorted
            return 0


# method 4: optimising the space complexity
# just reverse way of above logic, method 3
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) <2:
            return 0
        
        prev_max = nums[0]   # it will store the largest pre ele till now
        end = 0  # maximum till where we need to sort.
		# find the largest index not in place from starting to find the 'end'
        for i in range(1,len(nums)):
            if nums[i] < prev_max:  
                # if inordered . nums[i] bda hona chahiye tha
                end = i
            else:  # means in order
                # max_seen (prev_max) se bhi bda then order me h
                prev_max = nums[i]

        start = len(nums) - 1
        prev = nums[start]   # min index from where we need to sort
        for i in range(len(nums)-2, -1, -1):
            if prev < nums[i]:
                start = i
            else:
                prev = nums[i]
        if end != 0:
            return end - start + 1
        else: # means array is sorted
            return 0