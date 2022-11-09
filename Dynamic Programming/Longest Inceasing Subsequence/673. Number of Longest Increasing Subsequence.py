# write the logic in notes

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        LIS= [1]* len(nums)
        count= [1]* len(nums)
        for curr in range(len(nums)):
            for pre in range(curr):
                if nums[pre] < nums[curr]:
                    if LIS[curr] < 1+ LIS[pre]: 
                        LIS[curr] = 1+ LIS[pre]
                        # inherit
                        count[curr]= count[pre]
                    elif LIS[curr]== 1+ LIS[pre]:  # got many more subquence of max_length till now 
                        # just increase the count
                        count[curr]+= count[pre]
        max_LIS= max(LIS)
        # now add the no of occurence of max_LIS from count for final ans
        ans= 0
        for i in range(len(nums)):
            if LIS[i]== max_LIS:
                ans+= count[i]
        return ans