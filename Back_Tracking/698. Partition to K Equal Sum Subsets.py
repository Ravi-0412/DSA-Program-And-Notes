# method 1 :
# TLE

# Logic: Try to form 'k' subset one by one.

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n= len(nums)
        if sum(nums) % k != 0:
            return False
        nums.sort(reverse= True)
        target= sum(nums)//k  # sum of each subset will be this only
        used= [False]*n  # will tell whether index 'i' has been used or not.

        def backtrack(ind, k, subsetSum):
            if k== 0:
                # means we have formed all the 'k' subsets with equal sum
                return True
            if subsetSum== target:
                # means have formed one more subset. form the new subset with all the elements.
                return backtrack(0, k-1, 0)
            # form the subset with the help of numbers which has not been used yet.
            for j in range(ind, n):
                # after adding any num subset sum must be <= target.
                if not used[j] and subsetSum + nums[j] <= target:
                    used[j]= True
                    if backtrack(j+1, k, subsetSum + nums[j]):
                        return True
                    used[j]= False  # backtarcking
            return False
        
        return backtrack(0, k, 0)

# Note: if number is negative also then do by this logic
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/solutions/108730/java-c-straightforward-dfs-solution/


# method 2:
# logic: every element can go into any of the 'k' buckets.
# so just start putting each ele into eaach bucket one by one.

# Two game changer:
# 1. if sums[j] == 0: break

# The key is, sums[j] == 0 means for all k > j, sum[k] == 0; because this algorithm always fill the previous buckets before trying the next.
# So if by putting nums[i] in this empty bucket can't solve the game, putting nums[i] on other empty buckets can't solve the game either.
# i.e "buck[i]==0 break" is actually a kind of hashing of failure pattern "all zero". You can use a hash to record all failed patterns in the same way, not just "all zero". 
# In the same level of DFS, if a bucket failed, then all other buckets of the same value should also fail.

# 2. nums.sort(reverse=True)
# Always start from big numbers for this kind of problem, just by doing it yourself for a few times you will find out that the big numbers are the easiest to place.

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        if sum(nums) % k:
            return False
        sums = [0]*k  # will store the partition of each sum.
        subsetSum = sum(nums) // k
        nums.sort(reverse=True)
        n = len(nums)
        
        # function determines which bucket to put the 'current element' (nums[id] ) into
        def canPartition(i):
            # If we've placed all of the items, we're done;
            # check if we correctly made k equal subsets of 
            # size sum(nums) // k
            if i == n:
                return len(set(sums)) == 1
            for j in range(k):
                # Try adding the current element to it
                sums[j] += nums[i]
                # If it's a valid placement and we correctly placed the next element, we're
                # done placing the current element.
                if sums[j] <= subsetSum and canPartition(i+1):
                    return True
                sums[j] -= nums[i]
                # This is an optimization that is not strictly necessary. 
                # If buckets[i] == 0, it means:
                #   - We put nums[idx] into an empty bucket
                #   - We tried placing every other element after and failed.
                #   - We took nums[idx] out of the bucket, making it empty again. 
                # So trying to put nums[idx] into a _different_ empty bucket will not produce
                # a correct solution; we will just waste time (we place elements left to right,
                # so if this bucket is now empty, every one after it is too).
                #
                # Otherwise (bucket[i] > 0), we just go to the next bucket and 
                # try placing nums[idx] there. If none of them work out, we wind up
                # breaking out of the loop when range(k) ends and returning False.
                if sums[j] == 0:  #  no need to try other empty bucket
                    break
            # We couldn't place the current element anywhere that 
            # leads to a valid solution, so we will need to backtrack
            # and try something else.
            return False        
        
        # Start by trying to place nums[0]
        return canPartition(0)