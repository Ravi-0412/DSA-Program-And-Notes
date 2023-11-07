# Logic: for getting max(nums[i] - nums[j]) * nums[k]).
# For easier target 'j' then:
# 1) nums[i] should be max i.e we have to take max ele before index 'j' as our nums[i]
# 2) nums[k] should be max i.e we have to take max ele after index 'j' as our nums[k].

# So just calculate the max on left and right for each index.
# Then again traverse the list taking 'j' and find the ans.

# Time : O(2*n) = space

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_max = [0] * n     # prefix_max[j] = max from index '0' to index 'j'. 
                                 # max ele on left of 'j'(including)
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1] , nums[i])
        
        suffix_max = [0] * n     # suffix_max[j] = max from index 'j' to index 'n-1'.
                                # max ele on right of 'j'(including)
        suffix_max[n -1] = nums[-1]
        for k in range(n-2, -1, -1):
            suffix_max[k] = max(suffix_max[k + 1] , nums[k])

        ans = float('-inf')
        for j in range(1, n-1):
            ans = max(ans, (prefix_max[j - 1] - nums[j]) * suffix_max[j + 1])
        return ans if ans > 0 else 0
    
# We can reduce above solution into two pass,
# while find suffix_max calculate ans also.


# My mistake:
# for 'k' i was thinking same but for 'nums[i] - nums[j]' i was thinking from 'i' 
# And got stuck.


# Method 2:
# In one pass with O(1) space

# Logic: If somehow if we can keep track of max(nums[i] - nums[j]) for each index 'k'
# then, we can update our ans after each index 'k'.

# for keeping track of max(nums[i] - nums[j]) , we will need to keep track of 
# max element seen till now i.e nums[i]

# Very very nicce logic.

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        highest = 0  # to store highest number till now: nums[i]
        highest_diff = 0  # to store highest diff: nums[i] - nums[j] till now
        answer = 0  # to store current max value: (nums[i] - nums[j]) * nums[k]
        for num in nums:
            # this num will be same as 'nums[k]' while finding the ans.
            answer = max(answer, highest_diff * num) 
            # Now 'num' will become 'nums[j]' for calculating highest_diff
            highest_diff = max(highest_diff, highest - num)  # just we are doing prefix_max[i] - nums[j] where prefix_max[i] = highest_diff and nums[j] = num
            highest = max(highest, num)   #Just prefix_max[i]
        return answer