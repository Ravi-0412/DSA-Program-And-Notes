# Method 1:
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n*(n+ 1))//2 - sum(nums)  # sum of natural number till n - sum(nums)
        


# 2nd method : using XOR operation
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


# Other way of writing above code:
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n= len(nums)
        x1=0
        for i in range(n+1):
            x1= x1^i
        for i in range(n):
            x1= x1^nums[i]
        return x1

# METHOD 3: Sort the number in store in another aray now compare the sorted array with original array
# index at which there will be mismatch return that number from the original array 
# and if no mismatch means last number is missing so simply return 'n'

    







