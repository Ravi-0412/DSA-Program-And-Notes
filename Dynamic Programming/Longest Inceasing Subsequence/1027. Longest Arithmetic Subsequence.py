# This problem is similar to Longest Increasing Subsequence problem.
# The difference is that we need to consider the arithmetic difference in this problem.
# How to keep track of the length as well as the difference? We can use a hashmap, 
# whose key is the (index, differenc) and value is the length.

# for two elements A[i] and A[j] where j < i, 
# the difference between A[i] and A[j] (name it diff) is a critical condition. 
# If the hashmap at position j has the key diff, it means that there is 
# an arithmetic subsequence ending at index j, with arithmetic difference diff and length dp[j][diff]. 
# And we just add the length by 1. If hashmap does not have the key diff, then those two elements can form a 2-length arithmetic subsequence.


# here dp[(i, diff)]= gives the sequence length of possible diff ending at index 'i'.

# time: O(n^2)

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n= len(nums)
        dp = collections.defaultdict()
        for i in range(n):
            for j in range(i):
                diff= nums[i] - nums[j]
                # Agar is diff ka koi sequence index 'j' pe h tb uska length add kar do '+1'
                # Nhi to ye dono dono ko mila ke ek nya sequence bna ko at index 'i' having length= 2
                dp[(i, diff)] = dp.get((j, diff), 1) + 1
        return max(dp.values())
    
