# Exact same as: "373. Find K Pairs with Smallest Sums".

# Just sort both the arrays and apply same logic.

import heapq
class Solution:
    def solve(self, a, b, k):
        n = len(a)
        a.sort()
        b.sort()
        maxHeap = [(-1*(a[n-1] + b[n-1]), n-1, n-1)]
        cnt = 0
        ans = []
        visited = set()
        visited.add((n-1, n-1))
        while cnt < k :
            sum, i,  j = heapq.heappop(maxHeap)
            ans.append(-1*sum)
            cnt += 1
            # visited.add((i, j))   # Marking visited after poping will give duplicate ans.
            if j > 0 and (i, j-1) not in visited:
                heapq.heappush(maxHeap, (-1*(a[i] + b[j-1]), i, j-1))
                visited.add((i, j-1))
            if i > 0 and (i-1, j) not in visited:
                heapq.heappush(maxHeap, (-1*(a[i -1] + b[j]), i -1, j))
                visited.add((i-1, j))
        return ans
