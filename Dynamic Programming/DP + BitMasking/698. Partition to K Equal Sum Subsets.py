# method 1 :
# TLE

# Logic: Try to form 'k' subset one by one without sorting or with sorting.
# Both approach will give TLE

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
            # means have formed one more subset. form the new subset with all the elements.
            # So again call the bactrack
            if subsetSum== target:
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


# method 2: vvi
# logic: every element can go into any of the 'k' buckets.
# so just start putting each ele into each bucket one by one.

# Two game changer:
# 1. if sums[j] == 0: return False

# The key is, sums[j] == 0 means for all k > j, sums[k] == 0; 
# because this algorithm always fill the previous buckets before trying the next.
# So if by putting nums[i] in this empty bucket can't solve the game, 
# putting nums[i] on other empty buckets can't solve the game either.

# Kyonki agar dusre next partition me rakh denge nums[i] ko , then gain hmko yahi milega.

# If subsets[j] = 0, it means this is the first time adding values to that subset.
# If the backtrack search fails when adding the values to subSets[j] and subSets[j] remains 0, it will also fail for all subSets from subSets[j+1:].
# Because we are simply going through the previous recursive tree again for a different j+1 position.
# So we can effectively break from the for loop or directly return False.

# In the same level of DFS, if a bucket failed, then all other buckets of the same value should also fail.

# vvi: In simplest word.
# us condition ka matlab h ki us ele nums[i] ko hm empty subset 'j' me rakhe the but dalne ke bad ans nhi mila
# then, agar usko phli bar next empty subsets me dalenge tab bhi hmko ans nhi milega so simply return False and try to push diff ele in that subset.
# because this algorithm always fill the previous buckets before trying the next.

# time: O(k^n)

# 2. nums.sort(reverse=True)
# Always start from big numbers for this kind of problem, 
# just by doing it yourself for a few times you will find out that the big numbers are the easiest to place.

# Note vvi: if we will do by sorting in ascending order then above method will give TLE.
# Reason: when we sort in descending order then we will reach the base valid/invalid faster.
# Due to less no of function call.
# But in case if we sort in ascending order, we will reach the base case later because of more recursion call.

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
            # cur ele can go to any of the subset
            for j in range(k):
                # Try adding the current element to it
                sums[j] += nums[i]
                # If it's a valid placement and we correctly placed the next element, we're
                # done placing the current element.
                if sums[j] <= subsetSum and canPartition(i+1):
                    return True
                sums[j] -= nums[i]
				
                # This is an optimization that is not strictly necessary. 
                # If buckets[j] == 0, it means:
                #   - We put nums[i] into an empty bucket
                #   - We tried placing every other element after and failed.
                #   - We took nums[i] out of the bucket, making it empty again. 
                # So trying to put nums[i] into a _different_ empty bucket will not produce
                # a correct solution; we will just waste time (we place elements left to right,
                # so if this bucket is now empty, every one after it is too).
                if sums[j] == 0:  #  no need to try other empty bucket
                    return False
            # We couldn't place the current element anywhere that 
            # leads to a invalid solution, so we will need to backtrack
            # and try something else.
            return False        
        
        # Start by trying to place nums[0]
        return canPartition(0)


# Note: if number is negative also then do by this logic
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/solutions/108730/java-c-straightforward-dfs-solution/
    
# mehod 3: Better one
# using Bit Masking

# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/solutions/1494999/c-java-python-top-down-dp-bitmask-clean-concise/
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/solutions/905981/iterative-dp-deep-analysis-4-solutions-2-ways-of-bit-masking-1-backtracking-1-knapsack/
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/solutions/867956/python3-two-solutions-dp-with-bit-mask-48ms-dfs-backtracking-with-detailed-explanations/
