# o(n): 1st method

n= int(input("enter the value of n \n"))
lst= []
for i in range(n-1):
    x=int(input("enter the number \n"))
    lst.append(x)
print(lst)
# y=sum(lst)
# def missing(n):
#     sum1=(n*(n+1))/2
#     x= sum1-y
#     for i in range(1,n+1):
#         if x==i:
#             break
#     print("missing number is: ",i)
def missing(n):
    sum1=(n*(n+1))/2
    print("mising no is:",sum1-sum(lst))
# print(sum(lst))
missing(n)



#leetcode solution(2nd method) : using XOR operation
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n= len(nums)
#         x1=0
#         for i in range(n+1):
#             x1= x1^i
        
#         x2=0
#         for i in range(n):
#             x2= x2^nums[i]
        
#         num=x1^x2
#         return num






