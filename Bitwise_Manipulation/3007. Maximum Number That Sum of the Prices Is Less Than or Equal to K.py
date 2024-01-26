# For explanation and pattern finding
# Go through link: 
# https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/solutions/4569799/pattern-observation-and-binary-search-easy-to-understand-beginner-friendly-full-explanation/

# Time complexity:
# LOG(N): for binary searching over the solution space
# LOG(N): for computing price of a given range
# fianlly : O(LOGN * (LOG(N)))


class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:

        def isValid(num):
            sum = 0

            # calculate bit by bit
            for i in range(x, 65, x):
                no_block = (num + 1) // (2 ** i)   # sequence we are getting including number '0' so adding '1' i.e (num + 1)
                remainder = (num + 1) % (2 ** i)   # partial block
                block_sum = no_block * (2 **(i - 1)) # in each block no of 'i'th bit set = 2 **(i - 1) i.e last '2 **(i - 1)' bit
                remainder_sum = max(0, remainder - (2 **(i - 1)) )  # remaining number from last '2 **(i - 1)' which are set.
                sum += block_sum + remainder_sum

            return sum <= k

        start = 1
        end = 10 ** 15
        # Just we find the last index of an element in an array.
        while start <= end:
            mid = start + (end - start) // 2
            if isValid(mid):
                start = mid + 1
            else:
                end = mid - 1
        return end
        
    