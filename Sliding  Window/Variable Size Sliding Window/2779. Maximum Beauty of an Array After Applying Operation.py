# Note: we don't have to care about order of elements because we are asked to find the length only.
# Also here not telling to replace any ele by other ele in range of indices.

# So we can sort the array.

# Note vvi: whenever you are asked to find the length of subsequenece or anything related to subsequence 
# where order of ele doesn't matter then , think about sorting once. 

# Logic: After sorting now q reduces to "find the maximum length of subarray having diff between max_ele and min_ele is <= 2*k ".
# How we came across this intuition?
#  Ans: for any two elements , say i and j where i < j ( sorted) , max possible value for 'i' is 'i + k'.. 
# and min possible value for j is j - k .. 
# These values will overlap if and only if j - k <= i + k i.e. j - i <= 2*k, where j is max and i is min..

# In short: we can only make any ele to in '2*k' range only.

# Time : O(n*logn)

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j= 0, 0
        ans = 1  # min we can get this 
        while j < len(nums):
            # (maxi - mini) <= 2*k for valid one
            while nums[j] - nums[i] > 2*k:
                i += 1
            ans= max(ans , j - i + 1)
            j += 1
        return ans



# Must try doing in O(n)
# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/solutions/3771403/line-sweep-approach-picture-explanation-study-guide/
# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/solutions/3771636/sweepline-algorithm-detailed-explanation-c-solution/