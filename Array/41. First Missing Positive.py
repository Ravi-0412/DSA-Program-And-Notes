# more clarity for Q: if all numbers in the array is negative then return smallest positive i.e '1'.
# if all number in range are present then return the greatest of all number beyond array i.e maxNo +1 


# method 1:
# logic: first find the range of number i.e min no in arr and max no in array.
# now check for positive number which is not present in the array.

# Not good because it is taking extra space :O(n)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minNo, maxNo = min(nums), max(nums)
        if maxNo <= 0:  # all number in array is negative
            return 1
        numSet= set(nums)   # to check whether a num is present or not in O(1).
        for num in range(1, maxNo):
            if num not in numSet: 
                return num
        # means all no in range are present.
        return maxNo + 1

# Method 2:

# Observation: the missing integer must be in the range [1..n + 1]. (n = length of array)
# So, If an integer is missing it must be in the range [1..n], if an integer is not missing then the answer is n+1.

# How to solve?

# Ignore all numbers <=0 and > n since they are outside the range of possible answers (which we proved was [1..n]). 
# We do this by replacing them with the value n+1.
# For all other integers < n+1, mark their bucket (cell) to indicate the integer exists. (*see below)
# Find the first cell not marked, that is the first missing integer. If you did not find an unmarked cell, 
# there was no missing integer, so return n+1.

# Time = O(n), space : O(1)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # 1) mark numbers (num <= 0) and (num > n) with a special marker number (n+1) 
        # (we can ignore those because if all number are > n then we'll simply return 1)
        for i in range(n):
            if nums[i] <=0 or nums[i] > n:
                nums[i] = n + 1
        # note: all number in the array are now positive, and in the range 1..n+1
        # 2. mark each cell appearing in the array, by converting the index for that number to negative
        for i in range(n):
            num = abs(nums[i]) # since modifying in place so might be -ve also
                    #But we have to take index
            if num > n:
                continue
            # 'num' will correspond to index 'num-1'
            if nums[num - 1] > 0:  # prevents double negative
                nums[num -1] = -1*nums[num -1]  # it means 'num' is present in array
        # 3. find the first cell which isn't negative (doesn't appear in the array)
        for i in range(n):
            if nums[i] >= 0:
                return i + 1
        # 4. no positive numbers were found, which means the array contains all numbers 1..n
        return n + 1


# Try by this approach also in python.
# https://leetcode.com/problems/first-missing-positive/solutions/17071/my-short-c-solution-o-1-space-and-o-n-time/
# Tried but not working.

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n= len(nums)
        for i in range(n):
            while nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[i], nums[nums[i] -1]= nums[nums[i] -1], nums[i]
        
        for i in range(n):
            if nums[i]!= i+1:
                return i +1
        return n + 1