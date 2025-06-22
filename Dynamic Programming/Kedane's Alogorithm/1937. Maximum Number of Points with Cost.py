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


# Java Code 
"""
class Solution {
    public int maxPoints(int[][] P) {
        int m = P.length, n = P[0].length;
        if (m == 1) return maxInArray(P[0]);
        if (n == 1) return totalSum(P);

        int[] pre = P[0];

        for (int i = 0; i < m - 1; i++) {
            long[] left = new long[n];
            long[] right = new long[n];
            long[] cur = new long[n];

            // left sweep
            left[0] = pre[0];
            for (int j = 1; j < n; j++) {
                left[j] = Math.max(left[j - 1] - 1, pre[j]);
            }

            // right sweep
            right[n - 1] = pre[n - 1];
            for (int j = n - 2; j >= 0; j--) {
                right[j] = Math.max(right[j + 1] - 1, pre[j]);
            }

            for (int j = 0; j < n; j++) {
                cur[j] = P[i + 1][j] + Math.max(left[j], right[j]);
            }

            for (int j = 0; j < n; j++) pre[j] = (int) cur[j];
        }

        return maxInArray(pre);
    }

    private int maxInArray(int[] arr) {
        int max = arr[0];
        for (int a : arr) max = Math.max(max, a);
        return max;
    }

    private int totalSum(int[][] matrix) {
        int sum = 0;
        for (int[] row : matrix) {
            for (int v : row) sum += v;
        }
        return sum;
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxPoints(vector<vector<int>>& P) {
        int m = P.size(), n = P[0].size();
        if (m == 1) return *max_element(P[0].begin(), P[0].end());
        if (n == 1) {
            int total = 0;
            for (auto& row : P)
                for (int v : row) total += v;
            return total;
        }

        vector<long long> pre(P[0].begin(), P[0].end());

        for (int i = 0; i < m - 1; ++i) {
            vector<long long> left(n), right(n), cur(n);

            // left sweep
            left[0] = pre[0];
            for (int j = 1; j < n; ++j)
                left[j] = max(left[j - 1] - 1, pre[j]);

            // right sweep
            right[n - 1] = pre[n - 1];
            for (int j = n - 2; j >= 0; --j)
                right[j] = max(right[j + 1] - 1, pre[j]);

            for (int j = 0; j < n; ++j)
                cur[j] = P[i + 1][j] + max(left[j], right[j]);

            pre = cur;
        }

        return *max_element(pre.begin(), pre.end());
    }
};
"""
