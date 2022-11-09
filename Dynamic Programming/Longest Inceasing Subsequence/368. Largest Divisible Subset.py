# same logic as LIS
# logic: just sort the array and change the condition that's it
# After sorting the array if any next ele will satisfy the condition then that will be automatically divisible by all for sure 


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n= len(nums)
        LDS= [1]*n   # LIS[i] indicates that 'Largest Divisible Subset' that ends at index 'i'
        nums.sort()
        pre_included_ind= [i for i in range(n)]
        for curr in range(len(nums)):  # checking each index one by one
            for pre in range(curr):     # take the values from all the pre index till now 
                if nums[curr] % nums[pre]==0  and LDS[curr] < 1+ LDS[pre]: # include the element # if follows the rule then incr the LIS by one 
                    LDS[curr]= 1+ LDS[pre]
                    pre_included_ind[curr]= pre
        ans= []
        start= LDS.index(max(LDS))  # starting in reverse order
        ans.append(nums[start])
        # now traverse back from the index with max LDS till you reach pre_ind become same because when it will matxh means LDS has started from here only
        # this will store the ans in reverse order
        while start!= pre_included_ind[start]:
            start= pre_included_ind[start]
            ans.append(nums[start])            
        return ans[::-1]