# Note:
# Score : means cost of all k bags after distributing the marbles.
# Means first we have to minimum and maximum score we can get after distribution then just subatrct both to get the ans.

# Observation: 1st and last ele will always get included in any of the distribution.
# so what will be matter is the middle element.

# Explanation:

# First for any of distributions,
# we will sum up A[0] and A[n - 1] in the total socre,
# so this won't make any difference between max and min.

# To split into k bags 
# we actually choose k-1 cut points because 1st and last ele will get included automatically.

# Note vvvi: Ans for min and max will depend on where we are making the cuts.
# And value of each partition depend on 1st and last ele of that partition only.
# So q reduces to 'k-1' min/max pair wise sum .

# More explanation

# A[0]...A[i1]
# A[i1+1]....A[i2]
# A[i2+1]....A[i3]
# ....
# A[ik+1]....A[n-1]

# The result score is:
# (A[0] + A[i1]) + (A[i2] + A[i3]) +..... + (A[ik+1] + A[n-1])
# equals to
# A[0] + (A[i1] + A[i1+1]) + (A[i2] + A[i2+1]) + ....

# So the problem turns out to be,
# calculate the max/min sum of k - 1 numbers in
# A[0] + A[1], A[1] + A[2],..., A[n-1] + A[n].

# Read this link also for clarity:
# https://leetcode.com/problems/put-marbles-in-bags/solutions/3735251/intution-building-explanation-c/

# Time : O(n*logn)

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        possibleCuts = []   # will store the pair wise sum so it's length = n -1
        for i in range(n - 1):
            # if we make cut at 'i' then weights[i] will be last ele of pre partitions and
            # weights[i + 1] will be 1st ele of previous partition
            sumPair = weights[i] + weights[i + 1]
            possibleCuts.append(sumPair)
        
        # Now sort to get the 'k-1' minimum and maximum
        possibleCuts.sort()

        # Getting the 'k-1' minimum and maximum
        minimum , maximum= 0, 0
        for i in range(k -1):
            minimum += possibleCuts[i]
            maximum += possibleCuts[n - 2 - i]  # 'n-1' length so last index will be 'n-2'.
        return maximum - minimum
    
# Note: it needs a lot of visualisation to find the pattern.
# I was thinking of DP.