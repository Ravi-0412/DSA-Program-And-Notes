# Method 1: 

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
            ans += hashmap.get(positive_case_prev_sum, 0)
            negative_case_prev_sum = nums[j] - k   # checking if we have seen this num when we will open the modulus with -ve sign.
            ans+= hashmap.get(negative_case_prev_sum, 0)
            # update the frequency of nums[i] in hashmap.
            hashmap[nums[j]]= 1 + hashmap.get(nums[j], 0)
        return ans


# method 2: 
# Counting sort
# Can utilise the lesser constraint of 'nums[i]'.

# Note: Here storing the frequency first then finding the ans.
# But still it won't give duplicates or unnecessary ans because while finding ans
# we are checking for values at different index.

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count= [0]*101 # count[i]: frequency of 'i' for i > 0. max values of nums[i]= 100
        for n in nums: # calculate the frequency of each num 'n'
            count[n]+= 1
        ans= 0
        # starting from 'k+1' because of number will start from index '1'.
        # We get get abs diff = k only when there exist ele at 'i' and 'i-k' 
        # just checking at i == j and i == j - k
        for i in range(k+1, 101):  
            ans+= count[i] * count[i-k]   # all possible pair will contribute to ans. 
        return ans


# Related q: 
# 1) 532. K-diff Pairs in an Array
# just extension of this
