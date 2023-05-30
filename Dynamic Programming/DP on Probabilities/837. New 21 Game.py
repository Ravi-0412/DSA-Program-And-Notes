# time: O(k*n). 
# TLE

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:

        cache= {}
        # when we will start with this score, return the probability
        def dfs(score):
            if score >= k:
                return 1 if score <= n  else 0
            prob= 0
            for i in range(1, maxPts + 1):
                # Add all the probabilities
                prob += dfs(score + i)
            # Now take average. Every time we branch 'maxPts' no of times
            cache[score]= prob / maxPts
            return cache[score]
      
        return dfs(0)

# optimised one
# time: O(k)

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # no need to remove any card(we got ans without picking any card) or whatever card we will take all will give the prob= 1
        if k== 0 or k + maxPts <= n:
            return 1
        # calculate the windowSum (probability only) from 'k' to 'k + maxPts' i.e after base case
        # just like filling the base case 
        # if it is less than 'n' then prob= 1 else 0
        windowSum= 0
        for i in range(k, k + maxPts):
            windowSum+= 1 if i <= n else 0
        dp = {}  # will store the score at which start : probability.
        # Now calculate the prob for normal score i..e till 'k-1' with the help of base case
        # Just like we calculate the value of dp array with the help of base case.
        for i in range(k-1, -1, -1):
            dp[i]= windowSum /maxPts   # for calculating prob divide the sum of prob by 'maxPts'.
            # Now remove the farthest right value as we are traversing from right to left.
            remove= 0
            if i + maxPts <= n:
                remove= dp.get(i + maxPts, 1)
            # else: remove= 0
            windowSum+= dp[i] - remove   

        return dp[0]   # we had called the recursive function for score= 0
