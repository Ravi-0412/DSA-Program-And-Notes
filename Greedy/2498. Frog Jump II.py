# write the logic in notes.

# logic: To minimise the maximum distance between jumps, there will be jumps from each pair of alternate stones.
# And for ans we have to take maximum of those jumps.

# if we skip more stones then the distance will increase and alternate stones not used while going forward,
# will taken while coming backward.

# First going and coming back is same this as going twice. 

# time= O(n), space= O(1)

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n= len(stones)
        if n== 2:
            return stones[1] - stones[0]
        ans= 0
        # same num is used twice, one for going forward one for going backward.
        for i in range(2, n):  
            ans= max(ans, stones[i] - stones[i-2])
        return ans