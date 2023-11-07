# This problem is similar to Longest Increasing Subsequence problem.
# The difference is that we need to consider the arithmetic difference in this problem.

# LIS: me sirf bda dikha add kar diye but yahan difference bhi track karna hoga.
# we need to keep track of difference as well with length i.e
# Hmko har index pe, har possible difference ka AP ka length track karna hoga.

# How to keep track of the length as well as the difference? 
# We can use a hashmap, whose key is the (index, difference) and value is the length.

# for two elements A[i] and A[j] where i < j, 
# the difference between A[i] and A[j] (name it diff). 
# If the hashmap at position j has the key 'diff', it means that there is 
# an arithmetic subsequence ending at index j, with arithmetic difference 'diff' and length 'dp[j][diff]'. 
# And we just add the length by 1. If hashmap does not have the key diff, then those two elements can form a 2-length arithmetic subsequence.

# Note: LIS me bda dekh ke add kar rhe the '+1' usi 'j' wale ka length me, 
# Yahan diff dekh ke add karenge i.e agar same diff ka AP h tb add karenge.

# here dp[(i, diff)]= gives the sequence length of possible diff ending at index 'i'.

# time: O(n^2)

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n= len(nums)
        dp = collections.defaultdict()
        for i in range(n):
            for j in range(i):
                diff= nums[i] - nums[j]
                # Agar is diff ka koi sequence index 'j' pe h tb uska length me  add kar do '+1'
                # Nhi to ye dono dono ko mila ke ek nya sequence bna ko at index 'i' having length= 2
                dp[(i, diff)] = dp.get((j, diff), 1) + 1
        return max(dp.values())


# Note vvi: for  Q: "1218. Longest Arithmetic Subsequence of Given Difference" i.e 
# return the length of the longest subsequence in arr which is an arithmetic sequence 
# such that the difference between adjacent elements in the subsequence equals difference.

# I did like above but got TLE due to n= 10^5.

# Done optimisation of this q in hashing. See there 
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n= len(arr)
        dp = collections.defaultdict()
        for i in range(n):
            for j in range(i):
                diff= arr[i] - arr[j]
                if diff != difference:
                    continue
                # Agar is diff ka koi sequence index 'j' pe h tb uska length me  add kar do '+1'
                # Nhi to ye dono dono ko mila ke ek nya sequence bna ko at index 'i' having length= 2
                dp[(i, diff)] = dp.get((j, diff), 1) + 1
        # Ab give difference ka Ap ka max length return kar do.
        ans = 1
        for key, value in dp.items():
            if key[1] == difference:
                ans = max(ans, value)
        return ans

