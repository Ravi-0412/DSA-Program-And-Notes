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


# Method 2: Recursive one
# for every ele we have two choices whether we can include the cur ele or not.
# 1) if there is option to consider the cur ele then again, we have to two choices: 1) take or not take
# 2) else not take 

# How to write the function?
# we need to keep tarck of pre ele we have included then only we can make decision whether to take cur ele or not.
# so we need one more parameter in function with cur index.

# Time: O(2^n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def solve(pre, cur):
            if cur == len(nums):
                return 0
            # If no problem in including the cur ele, then two choices
            # pre == -1 means no ele included till now.
            if pre == -1 or nums[cur] > nums[pre]:
                return max(1 + solve(cur, cur + 1), solve(pre, cur + 1))
            # else only option is to exclude the cur ele.
            return solve(pre, cur + 1)   # nums[pre] >= nums[cur]. so only option is exclude the cur one.
        return solve(-1, 0)
    
# memoising the above one.
# time: O(n^2). giving Tle don't know why.
# '+1' shift for 'pre'.
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def solve(pre, cur):
            if cur == len(nums):
                return 0
            if dp[pre + 1][cur] != -1:
                return dp[pre + 1][cur]
            if pre == -1 or nums[cur] > nums[pre]:
                dp[pre + 1][cur] = max(1 + solve(cur, cur + 1), solve(pre, cur + 1))
                return dp[pre + 1][cur]
            dp[pre + 1][cur]= solve(pre, cur + 1)
            return dp[pre + 1][cur]
            
        n = len(nums)
        dp = [[-1 for j in range(n + 1)] for i in range(n + 1)]
        return solve(-1, 0)
        
# Note: There is no need of taking 'ans' variable to take maximum out of all like this.
# Because there is more than one function call in 'if', so we can compare directly.
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def solve(pre, cur):
            if cur == len(nums):
                return 0
            ans = 0  # taking ans = 1 will give error because of the case when we are not allowed to take that.
            if pre == -1 or nums[cur] > nums[pre]:
                ans = max(ans, 1 + solve(cur, cur + 1), solve(pre, cur + 1))
                # return ans
            ans = max(ans, solve(pre, cur + 1))
            return ans              # returning only is fine but in case of above memoised one it will not work because their value will get updated again.
                                    # But here it is taking max of all possibility then returning so will work fine.
                                    # in above memoised one , we can do like this also if we compare 
                                    # i.e dp[pre + 1][cur]= max(dp[pre + 1][cur], solve(pre, cur + 1)). Then no need to return at both place.
        return solve(-1, 0) 

# method 3: Better one
# Just the same above logic only, different way to write.

# Note vvvi: This is better one template in case of 'take' and 'notTake'  which there is 'notTake' option always there.
# So just find the condition for 'take' and return the max(take, notTake)

# How?
# There is no need to check the possibility of 'taking' and 'not taking' in possible case.
# There is always one choice to 'not take' and we can only take if follows the sequence.

# in case of pick and non_pick always write the pick case and non_pick case separately 
# if there are some condition involved before including or not_including any ele.

# time: O(2^n)
# space: O(n)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.helper(0, -1, nums)
    def helper(self, ind, pre_ind, arr):
        if ind== len(arr):
            return 0
        take= 0
        notTake= self.helper(ind +1, pre_ind, arr)  # if we not include
        # when we include but we can only include in following condition only.
        if pre_ind== -1 or arr[ind] > arr[pre_ind]:  # when can only include if strictly increasing
            take= 1+ self.helper(ind +1, ind, arr)
        return max(take, notTake)


# memoizing the above method
# for matrix: we can't store -1 as pre_ind so we will do co-ordinate shift by +1 for pre_ind i.e for -1 we will write 0 and so on
# so in this range of pre_ind will be from [0, n] instead of '-1' to   and range of 'ind' from '0' to 'n-1'

# submitted on gfg but giving TLE on leetcode. have to ask someone
class Solution:
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        dp= [[-1 for j in range(n+1)] for i in range(n +1)]   # dp[i][j] denotes max LIS starting from i when 'j' is the index of previous picked element.
        return self.helper(0, -1, a, dp)
    def helper(self, ind, pre_ind, arr, dp):
        if ind== len(arr):
            return 0
        if dp[ind][pre_ind +1]!= -1:
            return dp[ind][pre_ind+1]
        take= 0
        notTake= self.helper(ind +1, pre_ind, arr, dp)
        if pre_ind== -1 or arr[ind] > arr[pre_ind]:
            take= 1+ self.helper(ind +1, ind, arr, dp)
        dp[ind][pre_ind+1]= max(take, notTake)
        return dp[ind][pre_ind+1]


# converting to Tabulation VVI: Top down 
# little twist here: different from general pattern.
# Rules: 1) write the base case
# 2) convert the indices into for loop by seeing the starting and ending point of indices.
# Here 'ind' will go from 'n-1' to '0'. 
# And 'pre_ind' will go from 'n-1' to '-1' but it can't be equal to ind , it will be always less than the 'ind'..So it will from 'ind-1' to '-1'.
# 3) copy paste the recurrence do coordinate shift of '1' in case of 'pre_ind'. That's it.
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n= len(nums)
        dp= [[0 for j in range(n+1)] for i in range(n +1)]   
        for ind in range(n-1, -1, -1):
            for pre_ind in range(ind -1, -2, -1):
                take= 0
                notTake= dp[ind +1][pre_ind +1]
                if pre_ind== -1 or nums[ind] > nums[pre_ind]:
                    take= 1+ dp[ind+ 1][ind +1]
                dp[ind][pre_ind +1]= max(take, notTake)
        return dp[0][0]   # return the dp for which you had called the recursive function. 


# Method 4:  (neetcode): 
# method 2: submitted on leetcode
# logic: traverse the array from right to left . just the conversion of above logic and optimising the space to O(n).
# e.g: LIS[2] means nums[2] will get appened(+1) to any of the LIS ahead of it,
# (i.e if all the ele of of any of the LIS will be grater than nums[2] then we will add +1).     
# very better one    
# # time: O(n^2)                                                   
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS= [1]* len(nums)   # LIS[i] indicates that LIS that end at index 'i' from last
                                #  for each index at least ele at curr index will be get included so initialised with '1'
        for i in range(len(nums)-1, -1, -1):
            # for 'i'th index we have to merge this ele with any of the ans(LIS) after it. so we will check for all ele after this.
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]: # checking whether this ele at 'j' can get added to LIS at 'i'.
                    LIS[i]= max(LIS[i], 1+ LIS[j])  # Have to take max of all LIS ahead of it.
        # at last return the maximum in LIS
        return max(LIS)


# if you traverse from starting left to right
# write this logic in notes with printing the LIS, counting the number of LIS in detail
# for every ele, we have two choices either include that into 'subse' or not include to the pre_answers
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS= [1]* len(nums)   # LIS[i] indicates that LIS that end at index 'i' from start. 
        for i in range(len(nums)):  # calculating for each index one by one
            for j in range(i):     # take the values from all the pre index till now 
                if nums[j] < nums[i]: # include the element. # checking whether this ele at 'j' can get added to LIS at 'i'.
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


# best one: using binary search to find the proper position of curr index in case not follows the pattern 
# and removing the curr ele at that index in 'subsequence'.

# How Binary search?
# Since LIS will be in strictly sorted order only.
# if cur ele follows the sequence i.e > pre added one then, we will add this directly i.e
# If 'num' is bigger than last ele of sub, we just extend our list 
# Otherwise, we will simply apply binary search to find the smallest element >= num and replace it.

# why this logic is giving correct ans?
# Ans: Replace karenge tb length to wahi rhega but smaller ele se replace karne pe next ele ka append hone ka chance increase kar jayega.
# kyonki chota se replace kar rhe. e.g: [2, 8] next ele is '3'. 
# after replacing => [2,3] ab agar next elements '3' se large hua to append kar denge directly,
#  but agar [2,8] hota tb sirf '8' se bda wale ko hi append kar pate. 
# Append kitna jayda ho rha last me wahi mera length ko increase karega..

# Note: if we will use 'bisect_right' then we get duplicates also if 'num' is already  in 'sub' so using 'bisect_left'
#  since we need to replace with smallest ele in sub >= num.
# If we use 'bisect_right' then, it will replace with next greater ele than 'num', so we may get duplicate like pre and num will be same only.

# Note vvi: 'sub' will give one of the 'LIS' .

# time: O(n*logn)
# space: O(n)

# bisect function: https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
# logic: https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326308/C%2B%2BPython-DP-Binary-Search-BIT-Solutions-Picture-explain-O(NlogN).
# vvi: https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326552/optimization-from-brute-force-to-dynamic-programming-explained/

import bisect
class Solution:  
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub= []  # will store the ele in strictly increasing order only.
        for num in nums:
            if not sub or sub[-1] < num:
                # if following the pattern.
                sub.append(num)
            else: # find the position of num in sub and replace that ind with num
                idx= bisect.bisect_left(sub, num)  # simply bisect_left(sub,num). 
                sub[idx]= num  # no need to check if idx >= len(sub) because if like this then must be greatest of all and this case is already covered above.
        return len(sub)


# Note: when trying to do by "1235. Maximum Profit in Job Scheduling".
# And same q of this method is not working in '1235. Maximum Profit in Job Scheduling'.

# I am getting error . Have to ask someone
# nums = [4,10,4,3,8,9] , getting : 4 but exp = 3

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def solve(i):
            if i >= len(nums):
                return 0
            j = i + 1
            while j < len(nums):
                if nums[j] > nums[i]:
                    break
                j += 1
            return max(solve(i + 1), 1 + solve(j))
        
        return solve(0)