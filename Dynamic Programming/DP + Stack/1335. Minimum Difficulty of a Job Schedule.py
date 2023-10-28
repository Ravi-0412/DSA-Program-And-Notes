# Method 1: Recursion + memoisation

# dfs(i, d): find the the minimum difficulty if start work at 'i'th job with d days left.
# If d = 1, only one day left, we have to do all jobs, return the maximum difficulty of remaining jobs.

# Time : O(n*n*d)

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        @lru_cache(None)
        def dfs(i , d):
            if d == 1:
                # we will have to do all remaining work on this single day only
                return max(jobDifficulty[i :])  # maximum of all remaining jobs.
            # Each day at least ek kam karna hi h,
            # isliye hm pura job next coming single day me nhi kar sakte
            # remaining day ke liye bhi at least ek kam leave karna hoga.
            # so 'n - d + 1'.

            ans = float('inf')
            maxDiff = 0   # maximum difficulty
            for j in range(i , n - d + 1):
                # means taken 'j -i + 1' consecutive work on next single day
                maxDiff = max(maxDiff , jobDifficulty[j])  # taking maximum of job we are including
                ans = min(ans, maxDiff + dfs(j + 1, d - 1))
            return ans  

        return dfs(0, d)

# Do tabulation and try by stack also
# Solution in sheet(Lee solution).


# Method 2:
# Note vvi: we can reduce this problem into 
# "break up a list into 'd' consecutive segments such that the sum of the max number in each segment is minimized."

# See this logic and do by recursion and memoisation also.
# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/solutions/924611/dfs-dp-progression-with-explanation-o-n-3d-o-nd/
