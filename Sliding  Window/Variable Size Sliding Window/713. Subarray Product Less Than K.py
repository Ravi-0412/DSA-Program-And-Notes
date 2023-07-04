# logic: Traverse the array and keep adding the cur number to window i.e product
# if the product is greater than k, then try to reduce numbers on the left(i),
#  until the subarray product fit less than k again, (subarray could be empty).

# vvi: After inserting each num , first find the length of valid subarray by doing above thing.

# 2) After getting the length of valid subarray after inserting then number of new subarray after inserting the curr ele= length only.
# Reason: Curr ele can form a subarray with itself of size 1, subarray of size 2 with its adjacent left ele, 
# subarray of size 3 including two ele from left and so on until we reach the last index on left.
# so we will get one subarray of each size from '1' to length of subarray at that point, total subarray= length only.

# In other words , cur number will get added to each of the subarray formed before say 'k' then adding humself it will be 'k+1' = length of valid subarray.

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
            # just shrinking the subarray.
            while product >= k: 
                product//= nums[i]
                i+= 1
            count+= j - i + 1  # length of subarray. this no of subarray we can form after inserting this num.
            j+= 1
        return count


# Note vvvvi: use this logic only whenever you are asked to find the total number of subarray and you have include each pair of that subarray in the ans.

# Note: This is a very good and useful template, can be applied to many Q like: "209. Minimum Size Subarray Sum",
#  "Longest Subarray having sum of elements atmost ‘k’", 2762. Continuous Subarrays, 

# Just find
