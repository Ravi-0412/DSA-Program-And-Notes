# Logic: Find the xor of whole 'xorr' and then compare bit of 'xorr' with 'k'.
# If bit is different then increment by ans by '1'.

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xorr = 0
        for num in nums:
            xorr ^= num
        ans = 0
        for i in range(32):
            bit1 = (k >> i) & 1
            bit2 = (xorr >> i) & 1
            if bit1 != bit2:
                ans += 1
        return ans
