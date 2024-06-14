# first see 2nd distinct maximum
# Note: 2nd distinct maximum

# Code for 2nd maximum (submitted on gfg)
class Solution: 
	def print2largest(self,arr, n):
		firstMax, secondMax = -1, -1  
		for num in arr:
		    if num > firstMax:
		        # 'num' is greatest number till now
		        # so in this we will have to update both 'firstMax' and 'secondMax'
		        # Update 'secondMax' to 'firstMax' and then 'firstMax' to cur 'num'.
		        secondMax = firstMax
		        firstMax  =  num
		    elif num > secondMax and num != firstMax:  # checking num != firstMax to avoid duplicate
		        # in this case we only need to update 'secondMax' to 'num'
		        secondMax = num
		return secondMax  # if '-1' then all elements are equal and there is no 2nd maximum.

# if duplicate is also allowed then just change the 'elif' condition.
# just don't check 'num != firstMax' 
class Solution: 
	def print2largest(self,arr, n):
		firstMax, secondMax = -1, -1  
		for num in arr:
		    if num > firstMax:
		        # 'num' is greatest number till now
		        # so in this we will have to update both 'firstMax' and 'secondMax'
		        # Update 'secondMax' to 'firstMax' and then 'firstMax' to cur 'num'.
		        secondMax = firstMax
		        firstMax  =  num
		    elif num > secondMax :  # No need to check 'num != firstMax' to allow duplicate 
		        # in this case we only need to update 'secondMax' to 'num'
		        secondMax = num
		return secondMax  # if '-1' then all elements are equal and there is no 2nd maximum.


# for 1st and 2nd distinct minimum.
# for duplicate remove the 'num != firstMin' from 'elif' condition like above(maximum).
class Solution: 
	def print2largest(self,arr, n):
		firstMin, secondMin = 10**5 + 1, 10**5 + 1 
		for num in arr:
		    if num < firstMin:
		        secondMin = firstMin
		        firstMin  =  num
		    elif num < secondMin and num != firstMin:  # checking num != firstMax to avoid duplicate
		        # in this case we only need to update 'secondMax' to 'num'
		        secondMin = num
		return firstMin # if '-1' then all elements are equal and there is no 2nd maximum.


# Now come to this question

# Q) why can't use heap?
# Because heap gives kth smallest/largest that come in sequence assuming sorted array, not the kth distinct smallest/largest.

# method 1: sort and check from last and count the distinct number you have seen till now.
# time: O(n*logn)

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = len(nums)
        if n <=2:
            return max(nums)
        nums.sort()
        count= 1
        for i in range(n-1, 0, -1):
            if nums[i]  != nums[i-1]:
                count += 1
                if count == 3:
                    return nums[i-1]
        return max(nums)


# method 2: Just extension of '2nd largest number' logic.
# code of '2nd largest' you can see at the bottom.
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        firstMax, secondMax , thirdMax= float('-inf'), float('-inf'), float('-inf')
        for num in nums:
            if num > firstMax:
                # here we need to update all three
                thirdMax = secondMax
                secondMax = firstMax
                firstMax  =  num
            elif num > secondMax and num != firstMax:
                # here we need to update two i.e thirdMax and secondMax
                thirdMax = secondMax
                secondMax = num
            elif num > thirdMax and num != firstMax and num != secondMax:  
                # not writing the condition 'num != firstMax' will give error in case like: [1,2,2,5,3,5], [1,1,1,1,1] etc.
                # # here we need to update only thirdMax
                thirdMax = num
        return thirdMax if thirdMax != float('-inf') else max(nums)

# method 3:
# Just the shorter version of above logic.
# Updating the variable at same condition only but we don't need to check that much extra cases 

# Note: We need to handle that many cases under if-else to handle duplicate numbers in above method.
# In this we are only updating if we are getting distinct number.
# Logic of if-else condition will be same after seeing distinct no.

# keep track of first_max, 2nd_max, 3rd_max after you each ele you see any distinct number.

# Note: we can apply this logic to find '2nd largest number also' in similar way.

# time: O(3* n), space: O(3)

class Solution(object):
    def thirdMax(self, nums):
        v = [float('-inf'), float('-inf'), float('-inf')]   # [first_max, second_max, third_max]
        for num in nums:
            if num not in v:  # wil check only for distinct number
                if num > v[0]:   v = [num, v[0], v[1]]  # make first= num, second= pre_first, third= pre_2nd
                elif num > v[1]: v = [v[0], num, v[1]]  # keep first same, make  second= num &  third= pre_2nd
                elif num > v[2]: v = [v[0], v[1], num]  # keep first & second same, & make third= num
        # return max(nums) if float('-inf') in v else v[2]
        return v[2] if v[2] != float('-inf') else v[0]


# Related q:
# 1) 2706. Buy Two Chocolates
