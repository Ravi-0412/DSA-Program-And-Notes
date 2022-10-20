# Q: find all the subsets of given string
# logic: just make the recursion tree by including the first letetr 
# and 'not including' the 1st letter 
# and whenever you will find the given string empty then that will be our one of the subset
# must draw recursion tree, it very easy to understand and the basic of DP

# def subset(str1,ans):
#     if not str1:  # if empty then that will be one of the subset and that will be in 'ans'
#         print(ans)
#         return
#     subset(str1[1:], ans + str1[0])  # when you include the current character
#     subset(str1[1:], ans)   # when you don't include the current character

# str1= input("enter any string: ")
# ans= ""
# print("all the subsets of given string are: ") 
# subset(str1,ans)
# # subset("abc",ans)


# 2nd method: to store the result into an list
# you have to pass the list inside the function not as parameter

# def subset(str1,ans):
#     if not str1:  # if empty then that will be one of the subset so,print it
#         new_ans= []
#         new_ans.append(ans)
#         return new_ans
#     leftAns= subset(str1[1:], ans + str1[0])  # when you include the current character
#     rightAns= subset(str1[1:], ans)   # when you don't include the current character
#     return leftAns + rightAns     # both are type of list so just add them and return

# # str1= input("enter any string: ")
# ans= ""
# # print("all the subsets of given string are: ")
# # subset(str1,ans)
# print(subset("abc",ans))



# leetcode Q:  returns  a list of list of all the subsets(leetcode Q) 
# very better one,just applied the above logic
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         return self.helper(0,nums,[])
#     def helper(self,ind,arr,ans):
#         if ind== len(arr):
#             local= [ans]   # since we have to in list of list
#             return local
#         left= self.helper(ind+1,arr,ans+ [arr[ind]])
#         right= self.helper(ind+1,arr,ans)
#         return left+right


# logic: Accept and reject is happening with 'ans so far'
# for each new number, 
# we can either pick it or not pick it. 
# 1, if pick, just add current number to every existing subset.
# 2, if not pick, just leave all existing subsets as they are.
# We just combine both into our result.

# For example, {1,2,3} intially we have an emtpy set as result [ [ ] ]
# Considering 1, if not use it, still [], if use 1, add it to [ ], so we have [1] now
# Combine them, now we have [ [ ], [1] ] as all possible subset

# Next considering 2, if not use it, we still have [ [ ], [1] ], 
# if use 2, just add 2 to each previous subset, we have [2], [1,2]
# Combine them, now we have [ [ ], [1], [2], [1,2] ]

# Next considering 3, if not use it, we still have [ [ ], [1], [2], [1,2] ], 
# if use 3, just add 3 to each previous subset, we have [ [3], [1,3], [2,3], [1,2,3] ]
# Combine them, now we have [ [ ], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3] ]

# time: O(n*2^n), where 2^n is the total no of subsets and 
# we are copying the number to n subsets each time we encounter a num of the array

# space- O(n*2^n), where 2^n is the total no of subsets and 
# n is the space taken by each subset

# def subset(arr):
#     outer= [[]]   # our final ans will contain list of list
#     for num in arr:   # for each number in the array
#         n= len(outer) 
#         for i in range(n):
#             internal= outer[i].copy()  # copy the internal list of outer list one by one
#             internal.append(num)       # and append the number to all the existing list
#             outer.append(internal)    # and at alst append the internal created list to the outer list
#     return outer
# arr= [1,2,3]
# print(subset(arr))


# my mistake but got later
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         ans= [[]]
#         for i in range(len(nums)):
#             for j in range(len(ans)):
#                 local= ans[j].copy()
#                 local.append(nums[i])
#                 ans.append(local)
#             # ans.append(local)       # this i was writing outside the inside for loop
#         return ans

# my mistake
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         ans= [[]]
#         for i in range(len(nums)):
#             local= ans.copy()      # copying like this is creating the reference for all 1D list inside the 2D array
#                                    # so changing the value inside any 1D array in local will change the same 1D array in ans also
#             for j in range(len(local)):
#                 # print(num," num")
#                 local[j].append(nums[i])
#             ans+= local
#         return ans


# concise way of writing above code:
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         outer= [[]]   # our final ans will contain list of list
#         for num in nums:
#             outer+= [items+ [num] for items in outer]
#         return outer



# the above method won't work if list contain duplicate elements
# if duplicates are there then there will be also duplicate subsets

# in case of duplicates elements,add the element only to the newly 
# created subsets of previous step also because pre_ele  were already added to the old subsets

# and for this to work properly duplicate elements must be together then only we can know which is newly created subsets for pre ele
# beacuse in case duplicates doesn't come together then you will not find 
# at what level that ele had come before 

# so solve the duplicates appearing more than once at different positions and to bring all duplicates together
# just sort the array then apply this method

# code: if set conatins duplicates

def subset(arr):
    outer= [[]]
    start,end= 0,0  
    # 'start' will tell from where we have to start copying i.e start index of pre newly created subset
    # 'end' will contain the last index of pre newly created subset i.e till where we have to copy and it will be always 'len(outer)-1'
    # so if we add '1' to end then we will know that from where we have to start copying if duplicates comes
    # otherwise we will copy from '0' till n-1

    arr.sort()   # first sort the array so that all duplicates come together
    for i in range(len(arr)):
        start=0  # will start copy from index '0' only in case of no duplicates 
        if(i>0 and arr[i-1]==arr[i]):  # if duplicates comes then we have to add duplicate from end+=1
            start= end+1            
        end= len(outer) -1   # it will be always this only    
        for j in range(start,len(outer)):
            internal= outer[j].copy()  
            internal.append(arr[i])       
            outer.append(internal)   
    return outer

# arr= [1,2,3,2]
# arr= [1,2,2]
arr= [1,1,2,2]
# arr= [10,1,2,7,6,1,5]
print(subset(arr))




