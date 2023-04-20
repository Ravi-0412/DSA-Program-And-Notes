# logic: open the modulus with positive and negative sign. just we used to do in maths.
# say: we are currently at index 'j', |nums[i] - nums[j]|= k (i <j), we must have seen nums[i] before to make pair with nums[j]

# 1) when we will open the 'modulus' by +ve sign then we have to check whether we have seen 'nums[i]= k+ nums[j]' before or not.
# 2) when we will open the 'modulus' by -ve sign then we have to check whether we have seen 'nums[i]= nums[j] -k' before or not.

# time= space= O(n)
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        hashmap= collections.defaultdict(int)
        ans= 0
        for j in range(len(nums)):
            positive_case_prev_sum= k + nums[j]   # checking if we have seen this num when we will open the modulus with +ve sign.
            ans+= hashmap.get(positive_case_prev_sum, 0)
            negative_case_prev_sum= nums[j] - k   # checking if we have seen this num when we will open the modulus with -ve sign.
            ans+= hashmap.get(negative_case_prev_sum, 0)
            # update the frequency of nums[i] in hashmap.
            hashmap[nums[j]]= 1 + hashmap.get(nums[j], 0)
        return ans
    
# method 2: Counting sort
# simple and logical only.
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count= [0]*101 # max values of nums[i]= 100
        for n in nums: # calucate the frequency of each num
            count[n]+= 1
        ans= 0
        for i in range(k+1, 101):  # starting from 'k+1' because of '0' based indexing.
            ans+= count[i] * count[i-k]   # see here sum= k of indices i.e i+ (i-k)= k. Indices here are number only.
        return ans
