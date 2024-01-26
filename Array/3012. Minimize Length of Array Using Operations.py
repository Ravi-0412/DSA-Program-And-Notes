# Logic: For sure a smaller number can "kill" a bigger number because x % y = x if x < y.

# Let's say the smallest number in the array is m.

# If every number in the array is a multiply of m, then you can never produce a number smaller than m. 
# In this case answer is just (count(m) + 1) / 2.  # adding '+1' for handing when count is odd.

# If there exists a number N where N % m != 0, you can generate N % m who is smaller than everyone,
# then kill all the numbers. Answer is 1 in this case.

# Time : O(n)

class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        minimum = min(nums)
        for num in nums:
            if num % minimum:
                return 1
        return (nums.count(minimum) + 1) // 2  