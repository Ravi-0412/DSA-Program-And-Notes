# logic: Exactly same as "1503. Last Moment Before All Ants Fall Out of a Plank" . just and extension

# Note: How to find sum of difference of all pairs in O(n*logn) than O(n^2).

# Now imagine finding distance of 'a4' with all elements before it:
# (a4-a1)+(a4-a2)+(a4-a3)---> (a4+a4+a4)-(a1+a2+3)---->i*a4-prefixsum[i-1], let index of a4= 'i'.

# No need to check for element on right side of it because 
# this will get automatically counted when we traverse further element on right.

# vvi: this formula can be used only if the positions are sorted.

# So sort the array and find the prefixSum where prefix[i]= sum till index 'i-1'.
# then find the total sum.

class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        mod= 10**9 + 7
        n= len(nums)
        for i in range(n):
            if s[i]== 'R':
                nums[i]= nums[i] + d 
            else:
                nums[i]= nums[i] - d
        # nums[i] won't give the actual position of ith Robots but last position of all robots must in nums at some position.
        # Now we have to find the sum of distances between all pairs
        nums.sort()  # to get in O(n*logn)
        prefixSum= 0  # will store the sum till index 'i-1'. No need to store in array
        ans= 0
        for i in range(1, n):
            prefixSum += nums[i-1]
            ans = (ans + i* nums[i] - prefixSum) % mod
        return ans % mod


# Extension of Q:
# 1) "2615. Sum of Distances"
# In this Q, we need to replace all values with pairwise sum.
# So in this we also need to do find sum from 'right' like 'left'.

# But in current Q, we need to find sum so no need to do from right.

