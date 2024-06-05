# Logic vvi: After inserting each num , first find the length of valid subarray.

# How to find valid subarray?
# Traverse the array and keep adding the cur number to window i.e product
# if the product is >= k, then try to reduce numbers on the left(i),
#  until the subarray product fit less than k again, (subarray could be empty).


# 2) After getting the length of valid subarray after inserting then number of new ans subarray after inserting the curr ele= length only.
# i.e kyonki har ek subarray ka combination mera ans ka part ho sakta because agar pura subarray ka product hi chota h then 
# uska koi bhi subarray combination ka chota to hoga hi.

# And no of subarray combination we can get from a subarray of length say 'n' = n
# Because cur ele jitna bhi subarray hoga sbke saath add ho sakta h i.e 'n-1' and '+1' for himself as single ele.

# More explanation: Curr ele can form a subarray with itself of size 1, subarray of size 2 with its adjacent left ele, 
# subarray of size 3 including two ele from left and so on until we reach the last index on left.
# so we will get one subarray of each size from '1' to length of subarray at that point, total subarray= length only.

# In other words , cur number will get added to each of the subarray formed before say 'k'
#  then adding humself it will be 'k+1' = length of valid subarray.

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

# Note: This is a very good and useful template. 
# Related Q: 
# 1) "Number of subarrays having sum less than K"
# 2)  "209. Minimum Size Subarray Sum",
# 3)  "Longest Subarray having sum of elements atmost ‘k’"
# 4)  2762. Continuous Subarrays
# 5) 2958. Length of Longest Subarray With at Most K Frequency
# 6) 2962. Count Subarrays Where Max Element Appears at Least K Times
# 7) 1208. Get Equal Substrings Within Budget

