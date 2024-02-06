# Note: Given: All alloys must be created with the same machine.

# Logic: check for given mid, if possible then try to find the more bigger value.
# Just like we 'find the last index in sorted array'.

#  time complexity : O(log(1e9) * n * k)

# Note: Not always try to guess the correct range, if not able to guess then take minimum possible value for 'start'
# any very big value for 'end'.

class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:

        # is it possible to make 'mid' no of alloys with any of the machine in given budget?
        def isPossible(mid):
            minCost = float('inf')  # to take min cost of all machine
            for i in range(k):
                curCost = 0   # cost if we make all alloys by machine 'i'.
                for j in range(n):
                    unit = composition[i][j]  # for making one alloy, machine[i] will need this much unit of metal[j]
                    curUnit = mid * unit   # to create 'mid' no of alloys, total required unit
                    if stock[j] >= curUnit:
                        # then we make 'mid' no of alloys of metal[j] from machine[i]
                        continue
                    else:
                        # we need to purchase some unit of alloys
                        extraUnit = curUnit - stock[j]
                        extraCost = extraUnit * cost[j]
                        curCost += extraCost
                minCost = min(minCost, curCost)
            return minCost <= budget

        # Just we find the last index in sorted array
        start = 0
        end =  10**9   # any very big value
        while start <= end:
            mid = start + (end - start) //2
            if isPossible(mid):
                start = mid + 1
            else:
                end = mid - 1
        return end