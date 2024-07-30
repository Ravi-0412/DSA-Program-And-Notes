# Note: we can say divisible by 'k' also.
# Observation vvi: '%' works as complement in subarray problem for 'division' or 'multiple'.

# Reason: if we are at index 'j' and remainder now is say 'x' then , 
# if we find any 'i' (i < j) having same remainder then, it means
# subarray from 'i + 1' to 'j' is divisible by 'k' i.e we remove the extra ele till 'i'.

# In mathematical way:
# if sum(nums[i:j]) % k == 0 for some i < j, then sum(nums[:j]) % k == sum(nums[:i]) % k. 
# So we just need to use a dictionary to keep track of sum(nums[:i]) % k and the corresponding index i. 
# Once some later sum(nums[:i']) % k == sum(nums[:i]) % k and i' - i > 1, we return True.

# So store 'remainder' as 'key' and 'index' as value.

# Note: Here we will only add in 'hashmap' if 'cursum' is not present because
# Here length is also mattering and we need bigger length.


# Time complexity: O(n), space complexity: O(min(k, n)) if k != 0, else O(n).
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sumTillIndex= {0: -1}   # {modulo_sum: index} # we will get this 'modulus' till index 'i' when we will divide by 'k'.
                               # we may get modulus= 0 later so to handle that initially we are mapping {0:-1}
        curSum= 0
        for i in range(len(nums)):
            curSum += nums[i]
            curSum = curSum % k
            if curSum in sumTillIndex:  # duplicate remainder
                pre = sumTillIndex[curSum]
                if i - pre >= 2:
                    return True
            else:
                sumTillIndex[curSum] = i 
        return False


# Related Q: 
# 1)  "974. Subarray Sums Divisible by K"
# 2) vvi: "2947. Count Beautiful Substrings I" , "2948. Count Beautiful Substrings II".

