# Logic: 'OR' will only set the bit.
# So once you find curOr >= k then you have to remove ele from left for minimum length.
# While removing you have to update your ans also.

# Note: But how will we remove 'OR' contribution of left element ??
# See the code

# Time = O(32 * n)
# Space = O(32)

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        setBit = [-1 for i in range(32)]   # it will tell if bit is set then it is set by element at that index 
                    # i.e setBit[i] = j then ith bit is set by set bit of element at j'th index.
                    # This will help when we will remove leftmost number from a window 
                    # We will only remove if that bit is set by leftmost element only.
        i, j = 0, 0
        ans = float('inf')
        curOr = 0
        while j < n:
            curOr |= nums[j]
            # set the bit in setBit
            for b in range(32):
                # if bth bit in nums is set.
                if nums[j] & (1 << b) :
                    # Note: Checking the bth bit is set or not from right(MSB) but setting bit from left.
                    # It won't matter because we are removing in similar way only
                    setBit[b] = j
            # shrink the window and update the ans
            while i <= j and curOr >= k:
                ans = min(ans, j - i + 1)
                # remove the leftmost ele from cur .
                # Only unset those bits that were set by nums[i] i.e after ith index there is no ele
                # till 'j' because of that bit was set.
                for b in range(32):
                    # setBit[b] == i means bth bit was set by nums[i] only
                    if nums[i] & (1 << b) and setBit[b] == i :
                        setBit[b] = -1
                        # Unset this bit in curOr
                        curOr ^= (1 << b)
                i += 1
            j += 1
        
        return ans if ans != float('inf') else -1


