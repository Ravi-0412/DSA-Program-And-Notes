# 1st method: Brute force, time: o(n^2)
# # just find using two loops 
# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         res=[]
#         for i in nums:
#             count=0
#             for j in nums:  
#                 if(j<i):
#                     count+=1
#             res.append(count)
#         return res



# 2nd  method:
# Logic: Store the 1st occurence of every distinct ele when they are sorted.
# Time: o(nlogn) , space : O(n)

# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         temp=list(nums)
#         nums.sort()
#         res= []
#         n= len(nums)
#         hashmap= {}
#         for i in range(n):
#             if nums[i] not in hashmap:
#                 hashmap[nums[i]]=i
#         for num in temp:
#                 smaller= hashmap.[num]
#                 res.append(smaller)
#         return res



#4th method:  Best one
# using Prefix sum method 

# Logic: see the constraint  i.e 0 <= nums[i] <= 100.

# So what can we do is :
# a) create an array of size '101' and init with '0' where index will represent nums[i] 
# b) whenever you see any num just incr value at that index = num .
# c) then for num , ans = sum of value till index 'num-1' .

# Directly incr value in prefix_sum only to save one more extra space of O(n).

# Time = space = O(n)

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        prefix_sum= [0 for i in range(101)]     # took n= 101 because max value of any ele can be 100 
        # count the occurence of each element and store the 
        # count at index equal to the number itself in the prefix_sum.
        for num in nums:
            prefix_sum[num]+=1
        #now caclculate the prefix sum for index each index.
        for i in range(1,101):
            prefix_sum[i]+= prefix_sum[i-1]   # prefix_sum[i] : now stores count of element <= 'i'
        #now the value at previous index in prefix_sum will give the no of smaller element for each ele of the original array
        res=[]
        for num in nums:
            if(num!=0):
                smaller = prefix_sum[num-1]
                res.append(smaller)
            else:  # if ele= 0 then append zero in the ans
                res.append(0)
        return res



