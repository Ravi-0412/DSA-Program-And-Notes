# Real meaning of Q: How I read this problem is you have n kids, maxSum dollar, and index is your special or favourite child. 
# Need to distribute the max dollar b/w n kid with given condition. (Fav kid(index) should get max amount)?

# logic: 
# The minimum case would be nums[index] is a peak in nums.
# It's arithmetic sequence on the left of A[index] with difference is 1.
# It's also arithmetic sequence on the right of A[index] with difference is -1.

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        r = n - index -1   # no of ele on right side of 'index'
        l = index          # no of ele on left side of 'index'

        def isPossible(mid):
            m = mid - 1  # from this num i.e 'm' we will start placing in both left and right side to maintain diff of '1'.
            leftSum, rightSum = 0, 0
            # Calculating for right part
            if r <= m:
                # if no of ele on right is <= 'm'.
                # i.e sum_natural_no_till_m - sum_natural_no_till_(m-r).
                # (m -r) is the number we didn't use while filling. so we have to subtract sum from 1 to 'm-r'.
                rightSum = m*(m + 1)//2 - (m - r)*(m - r +1)//2
            else:
                # means we have to fill some index with '1' to maintain the diff <= 1.
                rightSum = m * (m + 1)// 2 + 1 * (r - m)   # after filling in decreasing order, fill the remaining with '1'.
            # Calculating for left part in same way. justreplace 'r' -> 'l'.
            if l <= m:
                leftSum = m*(m + 1)//2 - (m - l)*(m - l + 1)//2
            else:
                leftSum = m * (m + 1)// 2 + 1 * (l - m)
            return (leftSum + mid + rightSum) <= maxSum   # checking total_sum <= maxSum

        # Possible value at index. end= 'maxSum -n + 1' because we have to give at least '1' at every index because given nums[i] >0.
        start , end = 1, maxSum - (n -1)
        # Just we used to find the last index of an ele.
        while start <= end:
            mid = start + (end - start)//2
            # check we put nums[index] = mid then we can make whole sum <= maxSum following the property.
            if isPossible(mid):
                # means we can try for greater number
                start = mid + 1
            else:
                end = mid -1
        return end