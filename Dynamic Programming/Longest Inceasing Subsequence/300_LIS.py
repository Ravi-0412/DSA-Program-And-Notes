# If we closely observe the problem then we can convert this problem to longest Common Subsequence Problem.
# Firstly we will create another array of unique elements of original array and sort it. 
# Now the longest increasing subsequence of our array must be present as a subsequence in our sorted array. 
# That’s why our problem is now reduced to finding the common subsequence between the two arrays.

# Time and Space: O(n^2)
# submited successfully on GFG but giving TLE on Leetcode

# write the logic in notes in detail
class Solution:
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        a1= sorted(list(set(a)))
        n1= len(a1)
        return self.lcs(a, a1, n, n1)
    def lcs(self, s1, s2, x, y):
        dp= [[0 for j in range(y+1)] for i in range(x+1)]
        for i in range(1,x+1):
            for j in range(1,y+1):
                if s1[i-1]== s2[j-1]:
                    dp[i][j]= 1+ dp[i-1][j-1]
                else:
                    dp[i][j]= max(dp[i-1][j], dp[i][j-1])
        return dp[x][y]


# other methods: good ones
# in this we are tracking the pre_ind also to which we are adding the curr ele if it follows the sequence
# pre_ind denotes the last index included in LIS
# in case of pick and non_pick always write the pick case and non_pick case separately if there are some condition involved before including or not_including any ele
# time: O(n^2)
# space: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.helper(0, -1, nums)
    def helper(self, ind, pre_ind, arr):
        if ind== len(arr):
            return 0
        # if we not include
        ans= 0+ self.helper(ind +1, pre_ind, arr)
        # when we include
        if pre_ind== -1 or arr[ind] > arr[pre_ind]: 
            ans= max(ans, 1+ self.helper(ind +1, ind, arr))
        return ans


# memoizing the above method
# for matrix: we can't store -1 as pre_ind so we will do co-ordinate shift by +1 for pre_ind i.e for -1 we will write 0 and so on
# so in this range of pre_ind will be from [0, n] instead of '-1' to   and range of 'ind' from '0' to 'n-1'

# submitted on gfg but giving TLE on leetcode. have to ask someone
class Solution:
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        dp= [[-1 for j in range(n+1)] for i in range(n)]   # ind*pre_ind
        return self.helper(0, -1, a, dp)
    def helper(self, ind, pre_ind, arr, dp):
        if ind== len(arr):
            return 0
        if dp[ind][pre_ind +1]!= -1:
            return dp[ind][pre_ind+1]
        ans= 0+ self.helper(ind +1, pre_ind, arr, dp)
        if pre_ind== -1 or arr[ind] > arr[pre_ind]:
            ans= max(ans, 1+ self.helper(ind +1, ind, arr, dp))
        dp[ind][pre_ind+1]= ans
        return dp[ind][pre_ind+1]


# converting to Tabulation: Top down 
# little twist here
# pre_ind will always start from 'ind+1' and will go till 'len(nums)'
# not able to convert above logic into tabulation.(not able to understand the striver logic, this time conversion is very diff as before) have to ask someone



# other way (neetcode): 
# method 2: submitted on leetcode
# logic: traverse the array from right to left 
# e.g: LIS[2] means nums[2] will get appened(+1) to the LIS of any of the previous LIS(i.e if all the ele of of any of the LIS will be grater than nums[2] then we will add +1)     
# very better one                                                       
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS= [1]* len(nums)   # LIS[i] indicates that LIS that end at index 'i' from last
        # traversing in reverse order and only storing 
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]: # LIS[i] will get updated each time
                    LIS[i]= max(LIS[i], 1+ LIS[j])
        # at last return the maximum in LIS
        return max(LIS)


# if you traverse from starting left to right
# write this logic in notes with printing the LIS, counting the number of LIS in detail
# for every ele, we have two choices either include that into 'subse' or not include to the pre_answers
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS= [1]* len(nums)   # LIS[i] indicates that LIS that end at index 'i' from start. for each index at least ele at curr index will be get included so initialised with '1'
        for i in range(len(nums)):  # calculating for each index one by one
            for j in range(i):     # take the values from all the pre index till now 
                if nums[j] < nums[i]: # include the element
                    LIS[i]= max(LIS[i], 1+ LIS[j])   # if follows the rule then incr the LIS by one 
        return max(LIS)

# another way of writing above code
class Solution:  
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS= [1]* len(nums)   
        for i in range(len(nums)):  # calculating for each index one by one
            for j in range(i):     # take the values from all the pre index till now 
                if nums[j] < nums[i] and LIS[i] < 1+ LIS[j]: # include the element # if follows the rule then incr the LIS by one
                    LIS[i]= 1+ LIS[j]    
        return max(LIS)


# better one: using binary search to find the proper position of curr index in case not follows the pattern and removing the curr ele at that index in 'sub'
# time: O(n*logn)
# space: O(n)
# bisect function: https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
# logic: https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326308/C%2B%2BPython-DP-Binary-Search-BIT-Solutions-Picture-explain-O(NlogN)
# here 'sub' will not give the one of the LIS but it will give the correct ans for LIS
import bisect
class Solution:  
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub= []
        for num in nums:
            if not sub or sub[-1] < num:
                sub.append(num)
            else: # find the position of num in sub and replace that ind with num
                idx= bisect.bisect_left(sub, num)  # simply bisect_left(sub,num)
                sub[idx]= num
        return len(sub)
