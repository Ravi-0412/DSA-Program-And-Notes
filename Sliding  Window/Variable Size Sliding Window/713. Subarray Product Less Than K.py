# logic: 1) Every time shift window by adding a new number on the right(j), 
# if the product is greater than k, then try to reduce numbers on the left(i),
#  until the subarray product fit less than k again, (subarray could be empty).

# After inserting any num , first find the length of longest subarray now by doing above thing.

# 2) After getting the length of subarray after inserting then number of new subarray after inserting the curr ele= length only.
# Reason: Curr ele can form a subarray with itself of size 1, subarray of size 2 with its adjacent left ele, 
# subarray of size 3 including two ele from left and so on until we reach the last index on left.
# so we will get one subarray of each size from '1' to length of subarray at that point, total subarray= length only.

# time: O(n)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:  # all number is "+ve", so we can't get product less than '1'.
            return 0
        product= 1
        count= 0
        i, j= 0, 0
        while j < len(nums):
            product*= nums[j]
            # find the length of longest subarray having product < k after adding curr ele.
            while product >= k: 
                product//= nums[i]
                i+= 1
            count+= j - i + 1  # length of subarray. this no of subarray we can form after inserting this num.
            j+= 1
        return count
