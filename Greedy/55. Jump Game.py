# tried a lot with dp, optimisng from two variable change(n^3) to one variable  change(n^2) but got TLE.

# with two variable, changing the target also.
# memoised this but TLE only
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n= len(nums)
        return self.helper(0, n-1, nums)
    
    def helper(self, ind, target, nums):
        if target>0 and ind>= len(nums)-1:
            return False
        if target== 0 and ind== len(nums)-1:
            return True
        if nums[ind]== 0 and target > 0:  
            return False
        ans= False
        # if any of ways return True then return True
        for i in range(1, nums[ind] + 1):
            ans= ans or self.helper(ind + i, target- i, nums)
        return ans


# with one variable change
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n= len(nums)
        dp= [-1 for i in range(n)]
        return self.helper(0, n-1, nums, dp)
    
    def helper(self, ind, target, nums, dp):
        if nums[ind]>= target- ind:   # if diff of nums[ind] and target is <=0.
            return True
        if nums[ind]== 0 and target > 0:
            return False
        if dp[ind]!= -1:
            return dp[ind]
        ans= False
        for i in range(1, nums[ind] + 1):
            ans= ans or self.helper(ind + i, target, nums, dp)
        dp[ind]= ans
        return dp[ind]

# now by greedy
# in case when we have to reach the goal then try to start just before goal only,
#  as seeing only next cell we can make a decision or we can reduce our problem && try to reach the starting point.
# this we used to do in graph.
# time: O(N)

# we are checking from index 'n-2' like we can reach the target from here or not.
# if we can reach the target then make the curr index as target otherwise target will be same only.
# at last check if our target is equal to '0' or not.

# Greedy at making the decision and reducing the target.
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n= len(nums)
        target= n-1
        for i in range(n-2, -1, -1):
            if i+ nums[i]>= target:  # if we can reach the target from index 'i' then make 'i' as target.
                target= i
        return target== 0

