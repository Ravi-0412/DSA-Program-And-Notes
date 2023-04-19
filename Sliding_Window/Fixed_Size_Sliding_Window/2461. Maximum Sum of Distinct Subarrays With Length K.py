# just like "max sum subarray of size k"
# Here when we find any subarray of size= 'k' then first we will check if all elements are distinct or not.
# For this we will store the frequency count in hashmap.
# if len(hashmap)== k in window then update the ans.

# after reaching any window we will subtract the frequency count of 'nums[i]' also like we used to subtract 'nums[i]' from curSum.
# and if frequency becomes '0' after subtarcting then delete 'nums[i]' from hashmap.

# time= space= O(n)

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        frequency= collections.defaultdict(int)
        i, j= 0, 0
        curSum= 0
        maxSum= 0  # all number is +ve only
        while j < len(nums):
            n= nums[j]
            curSum+= n
            frequency[n]= 1+ frequency.get(n, 0)
            if j - i + 1 >= k:
                if len(frequency)== k :
                    maxSum= max(maxSum, curSum)

                curSum-= nums[i]
                frequency[nums[i]]-= 1
                if frequency[nums[i]]== 0:
                    del frequency[nums[i]]
                    
                i+= 1
            j+= 1
        return maxSum

