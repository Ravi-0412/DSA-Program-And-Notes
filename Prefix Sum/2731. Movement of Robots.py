# logic: Exactly same as "1503. Last Moment Before All Ants Fall Out of a Plank" . just and extension

# Note: How to find sum of difference of all pairs in O(n*logn) than O(n^2).

# Now imagine finding distance of 'a4' with all elements before it:
# (a4-a1)+(a4-a2)+(a4-a3)---> (a4+a4+a4)-(a1+a2+3)---->i*a4-prefixsum[i-1], let index of a4= 'i'.
# vvi: this formula can be used only if the positions are sorted

# So sort the array and find the prefixSum where prefix[i]= sum till index 'i-1'.
# then fidn the total sum.

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
        prefixSum= [0] * n  # prefix[i]= sum till index 'i-1'.
        ans= 0
        for i in range(1, n):
            prefixSum[i]= nums[i-1] + prefixSum[i-1]
            ans += i* nums[i] - prefixSum[i]
        return ans % mod


