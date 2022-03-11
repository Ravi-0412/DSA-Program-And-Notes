# Q: find all the subsets of given string
# logic: just make the recursioin tree by including the first letetr 
# and 'not including' the 1st letter 
# and whenever you will find the given string empty then that will be
# our one of the subset
# must draw recursion tree, it very easy to understand and the basic of DP

# def subset(str1,ans):
#     if not str1:  # if empty then that will be one of the subset so,print it
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


# 3rd method: iteration
# Q: returns  a list of list of all the subsets 

# logic: While iterating through all numbers, for each new number, 
# we can either pick it or not pick it. 
# 1, if pick, just add current number to every existing subset.
# 2, if not pick, just leave all existing subsets as they are.
# We just combine both into our result.

# For example, {1,2,3} intially we have an emtpy set as result [ [ ] ]
# Considering 1, if not use it, still [ ], if use 1, add it to [ ], so we have [1] now
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
# created subsets not to the existing subsets also like above
# and for this to work properly duplicate elements must be together
# beacuse in case duplicates doesn't come together then you will not find 
# at what level that ele had come before 

# so solve the duplicates appearing more than once at different positions
# just sort the array then apply the this method


# code: if set conatins duplicates

def subset(arr):
    outer= [[]]
    start,end= 0,0  
    # 'start' will tell from where we have to start coping 
    # 'end' will contain the index of last subset that was already in the outer 
    # so if we add '1' to end then we will know that from where we have to start copying 
    # and adding if duplicate comes otherwise we will copy from '0' till n-1

    arr.sort()   # first sort the array so that all duplicates come together
    for i in range(len(arr)):
        start=0  # will start copy from index '0' only in case no duplicates 
        if(i>0 and arr[i-1]==arr[i]):  # if duplicates
            start= end+1              # will copy from previous newly added set
        end= len(outer) -1     # will be equal to 
        for j in range(start,len(outer)):
            internal= outer[j].copy()  
            internal.append(arr[i])       
            outer.append(internal)   
    return outer

# arr= [1,2,3,2]
arr= [1,2,2]
print(subset(arr))




