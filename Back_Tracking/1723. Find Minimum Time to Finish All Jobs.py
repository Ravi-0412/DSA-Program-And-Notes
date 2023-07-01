# Exacly same as "2305. Fair Distribution of Cookies".

# Logic: Cur job can be assigned to any worker.

# Time: O(n^k)

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        self.ans = float('inf')
        # jobs.sort(reverse = True)
        sums = [0]*k

        def backtrack(i):
            if i == n:
                # we have to update ans
                # first find the max sum of all partition and then update the ans.
                maxSum = max(sums)
                self.ans = min(self.ans, maxSum)
                return 
            for j in range(k):
                if sums[j] + jobs[i] < self.ans:   # optimisation
                    sums[j] += jobs[i]
                    backtrack(i + 1)
                    sums[j] -= jobs[i]
                    if sums[j] == 0:   # optimisation
                        return
        
        backtrack(0)
        return self.ans