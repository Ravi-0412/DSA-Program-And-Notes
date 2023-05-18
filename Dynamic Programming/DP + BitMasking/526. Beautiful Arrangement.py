# mask will tell whether that number has been used in cur permutation or not.

# time complexity is O(N*2^N). Space complexity is O(2^N).

class Solution:
    def countArrangement(self, n: int) -> int:

        @lru_cache(None)
        def dp(mask, place):
            if place== 0:
                return 1
            ans= 0
            for num in range(1, n+ 1):
                # try to put each number from '1' to 'n' on this place if that number is not used at this place
                # and follow the property of beautiful arrangements.
                if mask & (1 << num) == 0 and ((num) % place== 0 or place % (num)==0 ):
                    # mark this num is used in the curent per
                    ans+= dp(mask | (1 << num), place -1)
            return ans
    
        return dp(0, n)
