# Logic: The elements with same remainder module by space, can be destroied together.
# Reason: When adding c*space to a fix number, all of the number generated from this will be having same reminder. 

# Then take the smallest element with having reminder same as that of maximum elements with same reminder.

# Steps: 

# 1. Count number of elements with same reminder, this can be achived by simple adding reminder to map & increamenting it.
# 2. Also keep track of the max count of reminder with same reminder value.
# 3. Scan the array again and find the smallest element with the max count reminder value, that we found in above step.

# Time: O(n)

class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        count = collections.defaultdict(int)  # [remainder, ele_we_can_destroy]
        ans= max(nums)
        maximum = 1   # will tell the maximum target we can destroy
        for num in nums:
            remainder = num % space
            count[remainder] = count.get(remainder, 0) + 1
            maximum = max(maximum, count[remainder])
        # Now we have to return the num which is part of maximum length
        for num in nums:
            remainder = num % space
            if maximum == count[remainder]:
                # Means 'num' is also part in maximum length
                ans = min(ans, num)
        return ans