# find the LIS from both left side and right side 

# submitted on GFG
class Solution:
    def LongestBitonicSequence(self, nums):
	    LIS_left= self.lengthOfLIS1(nums)
	    LIS_right= self.lengthOfLIS2(nums)
	    ans= 0
	    for i in range(len(nums)):
	        ans= max(ans,LIS_left[i] + LIS_right[i] -1)   # '-' because common ele will get added two times i.w ele where function will change its monotonocity
	    return ans
	
    def lengthOfLIS1(self, nums):
        LIS= [1]* len(nums)   
        for i in range(len(nums)):  # calculating for each index one by one
            for j in range(i):     # take the values from all the pre index till now 
                if nums[j] < nums[i] and LIS[i] < 1+ LIS[j]: # include the element # if follows the rule then incr the LIS by one
                    LIS[i]= 1+ LIS[j]    
        return LIS
    def lengthOfLIS2(self, nums):
        n= len(nums)
        LIS= [1]* n   
        for i in range(n-1,-1,-1):  # calculating for each index one by one
            for j in range(n-1,i,-1):     # take the values from all the pre index till now 
                if nums[j] < nums[i] and LIS[i] < 1+ LIS[j]: # include the element # if follows the rule then incr the LIS by one
                    LIS[i]= 1+ LIS[j]    
        return LIS