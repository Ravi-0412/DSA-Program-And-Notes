# 1st method: time o(n),space o(n) 
#
# gfg accepted for left rotation just after modifyingh the program

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n= len(nums)
#         k=k%n  #this '%' i was missing thats why leetcode was not accepting . will have to bring k in range of n thats why % is necessary 
#         temp= nums.copy()
#         for i in range(n):
#             position= i+k
#             if(position<n):
#                 nums[position]= temp[i]
#             else:
#                 nums[position-n]= temp[i]




# 2nd method: optimising the space complexity to O(1)
# logic: 1st reverse the array till k, then reverse the array from k+1 to n-1 (index) internally 
#  and finally revrse the whole array
# Time: o(n),space: o(1)
a = [1,2,3,4,5,6,7]
print(a)
# a.reverse()  # for reversing
# # for i in range(n,2,-1): #another way of reversing for specific elements
# #     print(i,end=" ")
n=len(a)
k=int(input("enter the number of time you want to rotate: "))
k=k%n

def reverse(a,l,h):
    i,j= l,h
    while(i<j):
        temp=a[i]
        a[i]= a[j]
        a[j]= temp
        i+=1
        j-=1

reverse(a,0,k)
print(a)
reverse(a,k+1,n-1)
print(a)
reverse(a,0,n-1)
print(a)
