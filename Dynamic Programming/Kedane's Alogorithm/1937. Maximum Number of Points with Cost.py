# Method 1: 

# Logic : 
# Similar to "1014. Best Sightseeing Pair"
"""
for 'X+1'th row (points[X + 1]) to pick say 'curr'
for the index i in curr, we have:
curr[i] = max(prev[j] - abs(j - i) for j in range(n)) + points[X+1][i],

compare every index in prev with every index i in points[X+1], which brings O(N ^ 2) time for a single row and O(N ^ 3) for the whole grids.

Note: for a certain index i, the maximum value for i is a index that could either come from its left, or its right(inclusive).

we can build two arrays, lft and rgt, and focus on the maximum value only coming from its left or right. 
Finding the best fit for a single index i could just cost O(1) time from then on.

for lft[0] is just prev[0], since there is no other values coming from its left.

lft[1], we need to make a choice, the value is the larger one between prev[1] or lft[0] - 1, 
(considering the index shift so we need to substract 1 from lft[0]).
For lft[2], the value is the larger one between prev[2] or lft[1] - 1, so on so forth.

Build right(rgt) using the same method.
# Time: O(n^2)
"""

class Solution:
    def maxPoints(self, P: List[List[int]]) -> int:
        m, n = len(P), len(P[0])
        if m == 1: return max(P[0])
        if n == 1: return sum(sum(x) for x in P)
        
        def left(arr):
            lft = [arr[0]] + [0] * (n - 1)
            for i in range(1, n): lft[i] = max(lft[i - 1] - 1, arr[i])
            return lft
        
        def right(arr):
            rgt = [0] * (n - 1) + [arr[-1]]
            for i in range(n - 2, -1, -1): rgt[i] = max(rgt[i + 1] - 1, arr[i])
            return rgt
        
        pre = P[0]
        for i in range(m - 1):
            lft, rgt, cur = left(pre), right(pre), [0] * n
            for j in range(n):
                cur[j] = P[i + 1][j] + max(lft[j], rgt[j])
            pre = cur[:]

        return max(pre)

