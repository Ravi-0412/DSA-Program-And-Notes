# o(n): 1st method
# but this can overflow 
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


# leetcode solution(2nd method) : using XOR operation
# time: O(n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n= len(nums)
        x1=0      # 1st time xor will happen with zero and this will
                    # give that number itself no problem in init x1=0

        # 1st find the xor of all numbers in that range
        for i in range(n+1):
            x1= x1^i          
        x2=0
        for i in range(n):
            x2= x2^nums[i]
# now take xor of x1 and x2, no occuring two times will get wiped out and we will 
# get the missing number since it will occur only one time including both traversal
        num=x1^x2   # for ans take the cumulative xor not one by one
        return num


# my mikstake 
# note: always take xor as a whole for final ans , don't take xor one by one
# but this logic is giving the incorrect ans after finding x1 don't know why
# x2=0
# while taking xor one by one, it is giving incorrect ans
# for i in range(n):
#     x2^= x1^nums[i]
# return x2

# METHOD 3: Sort the number in store in another aray now compare the sorted array with original array
# index at which there will be mismatch return that number from the original array 
# and if no mismatch means last number is missing so simply return 'n'

    







