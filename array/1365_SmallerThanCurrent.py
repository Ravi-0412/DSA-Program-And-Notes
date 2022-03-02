# 1st method: Brute force, time: o(n^2) 
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


# 2nd method: o(nlogn)
# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:            
#             sorted_nums= sorted(nums)
#             res=[]
#             for num in nums:
#                 smaller= sorted_nums.index(num)
#                 res.append(smaller)
#             return res


# 3rd method: using hashmmap Time: o(nlogn)
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



#4th method: using Prefix sum method Time: o(n)
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # count= [0 for i in range(101)]
        count1= [0]*101
        # count the occurence of each element and store the 
        # count at index equal to the number itself in the count1 array
        for num in nums:
            count1[num]+=1
        #now caclculate the prefix sum for the list: count1
        for i in range(1,101):
            count1[i]+= count1[i-1]
        #now traverse the original list to get the output
        res=[]
        for num in nums:
            if(num!=0):
                smaller= count1[num-1]
            else:
                smaller=0
            res.append(smaller)
        return res
            


