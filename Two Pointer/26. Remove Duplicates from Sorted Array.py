# method 1:
# 'l' , 'r' will point to the different indices of current ele . so will compare num[l] and nums[r] to check duplicates.
# lastDistinct will point to the index where last distinct ele was put.

# time: o(n), space: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n= len(nums)
        l, r, lastDistinct= 0, 1, 0  
        while r < n:
            while r < n and nums[l]== nums[r]:
                r+= 1
            if r < n:
                nums[lastDistinct + 1]= nums[r]
                lastDistinct+= 1
            l, r= r, r + 1
        return lastDistinct + 1
    

# method 2:
# no need to take lastDistinct variable 'l' we can use like that.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l= 0 # denote till where we have put elements. next we will put at 'i+ 1'.
        for r in range(len(nums)):
            if nums[l]== nums[r]:
                # agar cur ele and last distinct ele same h
                r+= 1
            else:
                nums[l+ 1]= nums[r]
                l+= 1
                r+= 1
        return l + 1
    

# method 3:
# concise way of writing above code. 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lastDistinct= 0
        for num in nums:
            if lastDistinct== 0 or num > nums[lastDistinct -1]:
                nums[lastDistinct]= num
                lastDistinct+= 1
        return lastDistinct


# Note vvi: Jahan order maintain karna ho and O(1) space me karna ho
# Wahan ek pointer chahiye jo btaye ki next ele kahan rakhna h.


