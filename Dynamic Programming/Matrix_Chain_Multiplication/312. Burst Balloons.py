# my mistakes: for cost i am simply taking just left and just right.
# but in case if its just left or right is already burst then that won't work.
# note: use common sense also according to the Q, don't start to solve simply.

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0,1)  # to get the left of  first balloons
        nums.append(1)    # to get the right of last  balloons
        print(nums)
        n= len(nums)
        i, j= 1, n-1
        return self.helper(nums, i, j)
    
    def helper(self, nums, i , j):
        if i== j:
            return 0
        mn= -9999999999
        for k in range(i, j):
            tempAns= self.helper(nums, i, k) + self.helper(nums, k+1, j) + nums[i-1]*nums[k]*nums[j]
            mn= max(mn, tempAns)
        return mn

# method 1: 
# logic: we have to divide the subproblem in such a way that both are independent to each other.
# by dividing like above, subproblem becomes dependent on each other to find the next left and right balloons which has not been burst yet.
# so to aolve that we will do by Bottom Up Approach. 

# main part: the kth picked balloon we will burst at last so that it's left and right balloons can get this 'k' easily.
# so when they will return the value, the next uburst left and right of 'kth' balloon will be 'i-1' and 'j+1' as all from 'i' to 'j' will get burst except 'k' in bottom up.
# so cost of bursting kth balloon will be : nums[i-1]*nums[k]*nums[j+1].
# Due to this post i solved this problem: https://leetcode.com/problems/burst-balloons/solutions/892552/for-those-who-are-not-able-to-understand-any-solution-with-diagram/
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0,1)  # to get the left of  first balloons
        nums.append(1)    # to get the right of last  balloons
        n= len(nums)
        i, j= 1, n-2  # j is passed as last valid so if i==j then still we have to call the rec fn. now both the end is valid
        return self.helper(nums, i, j)
    
    def helper(self, nums, i , j):
        if i> j:  # since 'j' was last valid instead of first invalid so base case will change like this(go one step further)
            return 0
        mx= -9999999999
        for k in range(i, j+1):  # 'j' in inclusive now(last valid)
            tempAns= self.helper(nums, i, k-1) + self.helper(nums, k+1, j) + nums[i-1]*nums[k]*nums[j+1]
            mx= max(mx, tempAns)
        return mx

# memoization:
# for dp size: 1) range of i: 'i' can go from 1 to 'n-1'(invalid one. jb 'i' , 'j' se bda hoga: base case). size= 'n-1'
# but 'k' is going till 'i+1'(till n). so finally size of 'i' should be 'n'(1 to n).
 
# 2) range of 'j': 'j' can go from 'n-2' to '0'(invalid one. jb 'j' , 'i' se chota hoga: base case), so size= 'n-1'.
# but 'k' is going to 'j-1'(to n-1 also). so finally size of 'j' should be 'n'(n-1 to 0).

# for memoization: 'n-1'*'n-1' will also work but will give error(out of index) in Tabulation.

# for bda and chota value of 'i' and 'j' (invalid one), see the value by which we made the first function call.
# time: O(n^3)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0,1)  # to get the left of  first balloons
        nums.append(1)    # to get the right of last  balloons
        n= len(nums)
        dp= [[-1 for j in range(n-1)] for i in range(n-1)]
        i, j= 1, n-2  # j is passed as last valid so if i==j then still we have to call the rec fn. now both the end is valid
        return self.helper(nums, i, j, dp)
    
    def helper(self, nums, i , j, dp):
        if i> j:  # since 'j' was last valid instead of first invalid so base case will change like this(go one step further)
            return 0
        if dp[i][j]!= -1:
            return dp[i][j]
        mx= -9999999999
        for k in range(i, j+1):  # 'j' in inclusive now(last valid)
            tempAns= self.helper(nums, i, k-1, dp) + self.helper(nums, k+1, j, dp) + nums[i-1]*nums[k]*nums[j+1]
            mx= max(mx, tempAns)
            dp[i][j]= mx
        return dp[i][j]

# Tabulation: Analyse properly
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0,1)  # to get the left of  first balloons
        nums.append(1)    # to get the right of last  balloons
        n= len(nums)
        dp= [[0 for j in range(n)] for i in range(n)]
        for i in range(n-2, 0, -1):  # from last valid one to first valid one
            for j in range(i, n-1):   # for valid one, 'j' should be >= 'i'. so for 'i'= 'n-2', j must be also equal to 'n-2;.
                mx= -9999999999
                for k in range(i, j+1):  # 'j' in inclusive now(last valid)
                    tempAns= dp[i][k-1] + dp[k+1][j] + nums[i-1]*nums[k]*nums[j+1]
                    mx= max(mx, tempAns)
                dp[i][j]= mx
        return dp[1][n-2]

