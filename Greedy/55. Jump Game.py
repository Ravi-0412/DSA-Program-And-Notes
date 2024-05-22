# Method 1:
# memoising :
# time: O(n^2)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n= len(nums)
        dp= [-1 for i in range(n)]
        return self.helper(0, n-1, nums, dp)
    
    def helper(self, ind, target, nums, dp):
        if ind + nums[ind]>= target:  # if we are able to reach the target using the steps at that index.
            return True
        if nums[ind]== 0 and target > 0:  # we can't move any step
            return False
        if dp[ind]!= -1:
            return dp[ind]
        ans= False
        for i in range(1, nums[ind] + 1):
            ans= ans or self.helper(ind + i, target, nums, dp)
        dp[ind]= ans
        return dp[ind]

# now by greedy
# Method 2:
# in case when we have to reach the goal then try to start just before goal only,
#  as seeing only next cell we can make a decision and try to reach the starting point.
# this we used to do in graph.
# time: O(N)

# we are checking from index 'n-2' and checking from each index whether we can reach the target from here or not.
# if we can reach the target then make the curr index as target otherwise target will be same only.
# at last check if our target is equal to '0' or not.

# Greedy at making the decision and reducing the target.
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n= len(nums)
        target = n-1
        for i in range(n-2, -1, -1):
            if i+ nums[i]>= target:  # if we can reach the target from index 'i' then make 'i' as target.
                target= i
        return target== 0

# Method 3:
# more better:
# logic: tmko bs last point pe pahunch jana h steps leke.
# bs step lene se phle dhyan me rakhna h ki at least us index tak pahunche h ki nhi jahan se hm next step lenge.
# agar us index pe pahunch chuke h then reached= i + nums[i] ho jayega agar pre reached se bda hua to nhi to pre reached hi rah jayega.

# time: O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, target= len(nums), len(nums) -1
        reached= 0
        for i in range(len(nums)):
            if reached < i:  # frog must be at least at 'i' th position to utilise the step of next index 'i'th index
                return False
            reached= max(i + nums[i], reached)   # max we have reached till now
            if reached >= target:  # we have reached the target
                return True
