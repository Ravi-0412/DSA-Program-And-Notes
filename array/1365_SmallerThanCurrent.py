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


# 2nd method: usinng sorting.  Time: O(nlogn), space:O(n)
# whenever you have find smaller(or smallest), gretater(or greatest) sorting may be always a solution
# logic: 1st sort the elements then find the index of each ele of nums in sorted one
# and that index will give the no of ele smaller than the current ele of original array


# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:            
#             sorted_nums= sorted(nums) 
#             res=[]
#             for num in nums:
#                 smaller= sorted_nums.index(num)
#                 res.append(smaller)
#             return res


# 3rd method: using hashmmap after sorting the array,  Time: o(nlogn)
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



#4th method: using Prefix sum method Time: o(n), space:O (n)
# https://www.youtube.com/watch?v=pVS3yhlzrlQ 
# prefix sum means calculating the sum of all elemenst till that index(included)
# for calculating this we can start from index 1 and add the value at pre index+ current index and so on
# like: prefix_Sum[i]= prefix_Sum[i] + prefix_Sum[i-1]; i!= 0 and prefix_Sum[i]= a[i]; i= 0 ; 'a' is the original array
# ele at every index in prefix sum indicates the sum of all ele till that index 

# using above logic,  prefix sum method can also be used to find the sum of all elements in a given range
# like: a[i,j]= prefix_sum[j]- prefix_sum[i-1]


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        prefix_sum= [0 for i in range(101)]     # took n= 101 because max value of any ele can be 100 
        # count the occurence of each element and store the 
        # count at index equal to the number itself in the prefix_sum
        for num in nums:
            prefix_sum[num]+=1
        #now caclculate the prefix sum and for index 0 put value= 0 which is automatically assigned here 
        # as no of ele smaller than zero will be zero only
        for i in range(1,101):
            prefix_sum[i]+= prefix_sum[i-1]
        #now the value at previous index in prefix_sum will give the no of smaller element for each ele of the original array
        res=[]
        for num in nums:
            if(num!=0):
                smaller= prefix_sum[num-1]
            else:  # if ele= 0 then append zero in the ans
                smaller=0
            res.append(smaller)
        return res
            


