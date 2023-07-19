# for finding len of LIS.
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS= [1]* len(nums)   # LIS[i] indicates that LIS that end at index 'i' from start. for each index at least ele at curr index will be get included so initialised with '1'
        for i in range(len(nums)):  # calculating for each index one by one
            for j in range(i):     # take the values from all the pre index till now 
                if nums[j] < nums[i]: # include the element. # checking whether this ele at 'j' can get added to LIS at 'i'.
                    LIS[i]= max(LIS[i], 1+ LIS[j])   # if follows the rule then incr the LIS by one 
        return max(LIS)

# in above Q, if we calculate the total no of max(LIS) then that will give the no of total LIS.
# But in above one, we were neglecting the LIS of same length , so here we will create another array to store the count of LIS.

# How to solve?
# If we encounter 'LIS[curr]== 1+ LIS[pre]' then, it means cur ele is already part of some seq having length = "LIS[CUR].
# so adding the pre one will give the different seq but of same length.
# But we need to calculate the no of LIS, we will add count of pre to cur i. : "count[curr]+= count[pre]".
# time: O(n^2)
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        LIS= [1]* len(nums) # LIS[i] indicates that LIS that end at index 'i' from start.
        count= [1]* len(nums)  # stores count of LIS of length 'LIS[i]'.
        for curr in range(len(nums)):   # i -> curr
            for pre in range(curr):      # j-> pre
                if nums[pre] < nums[curr]:
                    if LIS[curr] < 1+ LIS[pre]: 
                        # New greater length
                        LIS[curr] = 1+ LIS[pre]
                        # new one so count , it will inherit the count of 'pre'
                        count[curr]= count[pre]  # since we are adding the nums[pre] to the previous LIS only count of cur will be same as count of pre.
                    elif LIS[curr]== 1+ LIS[pre]:  # this means there are already more subsequences of same length ending at 'i'.
                        # just increase the count
                        count[curr]+= count[pre]
        max_LIS= max(LIS)
        # now add the no of occurence of max_LIS from count for final ans
    
        ans= 0
        for i in range(len(nums)):
            # Agar length max(LIS) ke equal h tb us index ka count ans me add kar do.
            if LIS[i]== max_LIS: 
                ans+= count[i]
        return ans


# Try to understand this way also.
# new Alo: Patience Sort
# https://leetcode.com/problems/longest-increasing-subsequence/solutions/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation/comments/206357/
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/solutions/916196/python-short-o-n-log-n-solution-beats-100-explained/