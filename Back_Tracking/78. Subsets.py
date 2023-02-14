# Q: find all the subsets of given string
# logic: just make the recursion tree by including the first letetr 
# and 'not including' the 1st letter .
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

# leetcode Q:  returns  a list of list of all the subsets(leetcode Q) 
# very better one,just applied the above logic
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         return self.helper(0,nums,[])
#     def helper(self,ind,arr,ans):
#         if ind== len(arr):
#             return [ans]
#         left= self.helper(ind+1,arr,ans+ [arr[ind]])
#         right= self.helper(ind+1,arr,ans)
#         return left+right


# method 2: more concise and easier way of above logic
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res= []
        subset= []
        def dfs(i):
            if i>=len(nums):
                # res.append(subset)  # if you write this then will print very subset as empty only as we are updating the subset always i.e 
                # adding and poping so subset will be 'empty' only after the all calls end so getting all subset as empty
                res.append(subset.copy())     # so do deep copy
                return
            # when we include the curr ele in subset
            subset.append(nums[i])
            dfs(i+1)
            # when we don't include the curr ele in subset
            subset.pop()
            dfs(i+1)        
        # call the dfs with starting index '0'
        dfs(0)
        return res

# another way of writing the above code.
# very concise and useful way.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res= []
        
        def dfs(i, subset):   # just backtracking
            if i== len(nums):
                res.append(subset)
                return
            # when you include the curr index ele.
            dfs(i+1, subset + [nums[i]])
            # when you don't include the curr index ele.
            dfs(i+1, subset)

        dfs(0, [])  
        return res


# iterative way:

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

