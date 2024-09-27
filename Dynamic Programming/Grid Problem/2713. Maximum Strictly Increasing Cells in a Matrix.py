# method 1: Brute force
# logic: for (i,j), longest path= max(longest path in  row i, longest path in col j) + 1.

# For row and col, we need to check every ele as for cur cell either ele on left or right may be greater.

# Time: O(m*n*(m+n))


class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n= len(mat), len(mat[0])
        dp= {}

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            ans= 1
            # go in col
            for c in range(n):
                if mat[i][c] > mat[i][j]:
                    colAns= 1 + dfs(i, c)
                    ans=  max(ans, colAns)
            # Go in row
            for r in range(m):
                if mat[r][j] > mat[i][j]:
                    rowAns= 1 + dfs(r, j)
                    ans= max(ans, rowAns)
            dp[(i, j)]= ans
            return ans

        ans= 1
        for i in range(m):
            for j in range(n):
                ans= max(ans, dfs(i, j))
        return ans

# method 2:
# optimising the above 
# A single ele can repeat many times and we are again and again calling function for those indices.

# Intitution: 
# we find the longest increasing paths starting from each value(not cell) in the matrix. 
# By keeping track of the longest paths for rows and columns, we determine the maximum number of cells we can visit. 
# The final result is the maximum path length among all rows and columns

# note: we have to traverse either in ascending or descendimg order of values.
# So 1st we need to store the cells wrt to a value.

# A single ele can repeat many times so first we have to store all its indices .{val: indices}

# Read the solution for calrity.
# time: O(m*n*log(m*n))


class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n= len(mat), len(mat[0])
        # first store the all (r,c) of an ele, since that ele can occur many times.
        valToIndices= collections.defaultdict(list)  # {value: indices}
        for i in range(m):
            for j in range(n):
                valToIndices[mat[i][j]].append((i, j))
        dp= [[0 for j in range(n)] for i in range(m)]
        # dp[i][j]: will tell the longest path from (i, j)
        rows= [0]*m  # rows[i]: tell the longest path in ith row.
        cols= [0]*n  # cols[i]: tell the longest path in ith col.
        ans= 1  # minimum must be this only

        # Traversing in sorted order according to values.
        for num in sorted(valToIndices):
            for (i, j) in valToIndices[num]:
                # max we can go from (i, j) is max(row[i], col[j]) + 1
                # for smaller value we already calculated so for cur value max we can go is this only.
                # Num can take all cell traversed by element smaller than 'num' .
                # Here taking the decreasing order values
                dp[i][j]= 1 + max(rows[i], cols[j]) 
                ans= max(ans, dp[i][j])
            # now update the value of rows and cols array.
            for (i, j) in valToIndices[num]:
                rows[i]= max(dp[i][j], rows[i])
                cols[j]= max(dp[i][j], cols[j])
        return ans

# java
"""
import java.util.*;

class Solution {
    public int maxIncreasingCells(int[][] mat) {
        int m = mat.length, n = mat[0].length;
        
        // Create a map to store the positions of each value in the matrix
        Map<Integer, List<int[]>> valToIndices = new HashMap<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                valToIndices.computeIfAbsent(mat[i][j], k -> new ArrayList<>()).add(new int[]{i, j});
            }
        }

        int[][] dp = new int[m][n];  // dp[i][j]: longest path starting from (i, j)
        int[] rows = new int[m];  // rows[i]: longest path in ith row
        int[] cols = new int[n];  // cols[j]: longest path in jth column
        int ans = 1;  // minimum path is 1

        // Traverse values in sorted order
        List<Integer> sortedValues = new ArrayList<>(valToIndices.keySet());
        Collections.sort(sortedValues);

        for (int num : sortedValues) {
            // Process all cells with the current value
            List<int[]> indices = valToIndices.get(num);
            for (int[] index : indices) {
                int i = index[0], j = index[1];
                // Update dp[i][j] with the max path length from rows[i] or cols[j]
                dp[i][j] = 1 + Math.max(rows[i], cols[j]);
                ans = Math.max(ans, dp[i][j]);
            }
            
            // Update rows and cols based on the dp values calculated for this value
            for (int[] index : indices) {
                int i = index[0], j = index[1];
                rows[i] = Math.max(dp[i][j], rows[i]);
                cols[j] = Math.max(dp[i][j], cols[j]);
            }
        }

        return ans;
    }
}
"""
