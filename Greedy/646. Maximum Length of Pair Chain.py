# method 1: using DP

# Recursion + memoisation

# Time: O(n^2)

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        @lru_cache(None)
        def solve(pre, cur):
            if cur == len(pairs):
                return 0
            ans = solve(pre, cur + 1) 
            if pre == -1 or  pairs[cur][0] > pairs[pre][1]:
                ans = max(ans, 1 + solve(cur, cur + 1))
            return ans

        pairs.sort()  # sorting based on starting time
        return solve(-1, 0)


# Method 2:
# just think 'pairs' as intervals.

# This Q is exactly same as " Find max no of non-overlapping intervals"
# And this we did in "435. Non-overlapping Intervals".

# Time : O(n*logn)

class Solution:
    def findLongestChain(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x : x[1])   
        preEnd= intervals[0][1]  # will keep track of last added inetrval.
        count = 1  # will count the max no of non-overlapping intervals. 
        # Starting from '1 because if not overlap then at 1st time we will have to add both the intervals.
        # Also 1st will be always included.
        for start, end in intervals[1:]:
            # if they are not overlapping
            if start > preEnd: 
                preEnd= end
                count += 1
            # if overlapping,  skip the cur one since pre ending interval will be before only and we already taken that.
        return count