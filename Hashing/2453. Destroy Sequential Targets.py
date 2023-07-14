# Method 1: Brute force
# Any number say 'y' if can be expressed as : y = x + c*space (where x= nums[i])
# Then, 'y-x' must be divisible by 'space'.

# Checking from start how many number we can include starting from that number.
# time: O(n^2)

class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:

        def maxTargets(num):
            count = 0
            for i in range(len(nums)):
                if nums[i] not in visited:
                    if (nums[i] - num) % space == 0:
                        count += 1
            return count

        nums.sort()
        max_target, ans = 0, None
        visited = set()  # No need to start from same number again
        for i in range(len(nums)):
            if nums[i] not in visited:
                
                targets = maxTargets(nums[i])
                print(i , targets, max_target)
                if targets > max_target:
                    ans = nums[i]
                    max_target = targets
            visited.add(nums[i])
        return ans


# Method 2: Optimising the above one like : "1218. Longest Arithmetic Subsequence of Given Difference".

# Observation: The elements with same remainder module by space, can be destroyed together.
# Reason: When adding 'c*space' to a fix number, all of the number generated from this will be having same remainder. 

# So if we store the count of remainder value i.e [remainder : count] then, 
# our Q reduces to 'find the minimum no which contributed in maximum count'.

# Note: In this type of Q, try to find the common between each number that will be in same group or how we can tarck the other no using the cur one.
# Try to observe the things and find the relation.

# Steps: 

# 1. Count number of elements with same reminder, this can be achived by simple adding reminder to map & incrementing it.
# 2. Also keep track of the max count of remainder with same remainder value.
# 3. Scan the array again and find the smallest element with the max count reminder value, that we found in above step.

# Time: O(n)

class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        count = collections.defaultdict(int)  # [remainder, count_ele_we_can_destroy]
        maximum = 1   # will tell the maximum target we can destroy
        for num in nums:
            remainder = num % space
            count[remainder] = count.get(remainder, 0) + 1
            maximum = max(maximum, count[remainder])
        # Now we have to return the minimu num which is part of maximum length
        ans= max(nums)
        for num in nums:
            remainder = num % space
            if maximum == count[remainder]:
                # Means 'num' also contributed in maximum length.
                ans = min(ans, num)
        return ans