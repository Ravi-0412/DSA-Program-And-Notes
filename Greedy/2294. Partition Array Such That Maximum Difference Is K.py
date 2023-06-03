# logic: 
# Iterate each element A[i] in the input array,
# and we try to add it into the current subsequence.

# We need to check if the differnce is still good.
# So we firstly update the value of mn and mx
# mn = min(mn, a)
# mx = max(mx, a).

# If mx - mn > k,
# this means the difference between the maximum and minimum values,
# is bigger than k in current subsequence,

# A[i] cannot be added to the subsequence,
# so we start a new subsequence with A[i] as the first element,
# thus increment res and update mn = mx = a.

# Note: was asking for subsequence and only minimum and maximum will matter,
# so we can sort to check the difference easily.

# vvi: if asked for subarray then we can't sort because in subarray order matters.
# And in subsequence order doesn't matter so we can sort.

# time:O(n*logn)

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans= 1
        minNo = maxNo= nums[0]
        for num in nums:
            minNo= min(minNo, num)
            maxNo= max(maxNo, num)
            if maxNo - minNo > k:
                ans+= 1
                minNo= maxNo= num   # starting of new subsequence
        return ans
