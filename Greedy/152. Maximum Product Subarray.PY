
# logic: negative no is making problem like if product till now is min but next time it can become the ans if next ele will be negative.
# that's why maintaining two varaibel to store the curr_max and curr_min till now.
# here we are becoming greedy as we can get our ans from both like curr_min and curr_max.
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans= nums[0]
        curr_max, curr_min= 1, 1  # for multiplication '1' won't effect the ans
        for n in nums:
            temp= curr_max*n  # have to update curr_min acc to prev value only
            # for curr_max: 1) n is +ve and curr_max is +ve 2) n is -ve and curr_min is -ve 3) if for input like: [-1, 8]
            curr_max= max(n* curr_max, n*curr_min, n)
            # for curr_min: 1) n is -ve and curr_max is +ve 2) n is +ve and curr_min is -ve 3) if for input like: [-1, -8]
            curr_min= min(temp, n*curr_min, n)
            ans= max(ans, curr_max)
        return ans

