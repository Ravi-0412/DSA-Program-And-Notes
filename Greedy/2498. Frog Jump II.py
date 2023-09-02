# Note: for minimum lenth we will take as max jump as possible.
# suppose given: "we need to go from 1st stone to last stone" no back trip.
# Then ans in this case = min(difference among consecutive pairs) 
# Raeson: if we skip any stone then length may increase. so jump on all stones.

# Now come to this Q:
# We have to come back also and we also know for min cost ' we need to take as max jump as possible".
# But we can use any stone once. 
# So in this case we wil take alternate jump.

# Therefore, in this case ans = min(difference betwen each alternate pairs.)

# Alternate stones not used while going forward, will taken while coming backward.

# First going forward and coming back is same this as going twice.  

# Note: you can apply this logic only if array is sorted .

# time= O(n), space= O(1)


# More explanation:
# 1) On its way to the right, the frog should make at least one jump of length greater than 1. 
# If all jumps were of length 1 (let's call them 1-jumps), there will remain no stones to return to the origin.

# 2) There is no point in making jumps of length greater than 2 (let's call them 2-jumps) becuase all of 
# them can be optimized to a combination of 1-jumps and 2-jumps.

# 3) So the question is, which 2-jumps should the frog make? Can it skip the most longest one? 
# The answer is no. Let's consider a triple of stones [..., x, A, B, C, y, ...] 
# where C-A is the longest possible 2-jump. If the frog decides not to jump directly from A to C, 
# but rather to use an intermediate stone B, then on its way back it would have to take an even longer jump from y to x. 
# Thus, the frog should always make the longest 2-jump.

# 4) Considering all these observations, the optimal strategy would be to take a 1-stone-separated path 
# (with the longest 2-jump included) on the way right and use the remaining stones on the way back to the origin. 
# On the boundaries, we might have to make 1-jumps to correctly align ourselves to the path with the longest 2-jump.

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