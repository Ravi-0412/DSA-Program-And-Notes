# Just zip(difficulty, profit) for maintaining the index and sort.
# Now sort worker and check for each worker we can assign the maximum difficulty.
# Note: Worker having more value of worker[i] will surely can get >= difficulty than working having less 'worker[i]'.

# So we can use two pointer to find the maximum difficulty we can assign to each worker.
# sorted worker only to use this logic i.e two pointer.

# Time: O(n*logn)

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        ans = 0
        best = 0
        i , j = 0, 0
        while i < len(worker):
            while j < len(jobs) and worker[i] >= jobs[j][0]:
                best = max(best, jobs[j][1])
                j += 1
            ans += best
            i += 1
        return ans
