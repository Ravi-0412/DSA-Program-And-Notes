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

# Java Code 
"""
import java.util.*;

public class Solution {
    int[][] mat;
    int m, n;
    Map<String, Integer> dp;

    public int maxIncreasingCells(int[][] matrix) {
        this.mat = matrix;
        m = mat.length;
        n = mat[0].length;
        dp = new HashMap<>();

        int ans = 1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                ans = Math.max(ans, dfs(i, j));
            }
        }
        return ans;
    }

    private int dfs(int i, int j) {
        String key = i + "," + j;
        if (dp.containsKey(key))
            return dp.get(key);
        int ans = 1;

        // go in col
        for (int c = 0; c < n; c++) {
            if (mat[i][c] > mat[i][j]) {
                int colAns = 1 + dfs(i, c);
                ans = Math.max(ans, colAns);
            }
        }
        // Go in row
        for (int r = 0; r < m; r++) {
            if (mat[r][j] > mat[i][j]) {
                int rowAns = 1 + dfs(r, j);
                ans = Math.max(ans, rowAns);
            }
        }

        dp.put(key, ans);
        return ans;
    }
}
"""
# C++ Code 
"""
class Solution {
    std::vector<std::vector<int>> mat;
    int m, n;
    std::unordered_map<std::string, int> dp;

public:
    int maxIncreasingCells(std::vector<std::vector<int>>& matrix) {
        mat = matrix;
        m = mat.size();
        n = mat[0].size();
        int ans = 1;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                ans = std::max(ans, dfs(i, j));
            }
        }
        return ans;
    }

private:
    int dfs(int i, int j) {
        std::string key = std::to_string(i) + "," + std::to_string(j);
        if (dp.count(key)) return dp[key];
        int ans = 1;

        // go in col
        for (int c = 0; c < n; ++c) {
            if (mat[i][c] > mat[i][j]) {
                int colAns = 1 + dfs(i, c);
                ans = std::max(ans, colAns);
            }
        }
        // Go in row
        for (int r = 0; r < m; ++r) {
            if (mat[r][j] > mat[i][j]) {
                int rowAns = 1 + dfs(r, j);
                ans = std::max(ans, rowAns);
            }
        }

        return dp[key] = ans;
    }
};
"""

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


# Java Code 
"""
import java.util.*;

public class Solution {
    public int maxIncreasingCells(int[][] mat) {
        int m = mat.length, n = mat[0].length;

        // first store the all (r,c) of an ele, since that ele can occur many times.
        Map<Integer, List<int[]>> valToIndices = new TreeMap<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                valToIndices.computeIfAbsent(mat[i][j], k -> new ArrayList<>()).add(new int[]{i, j});
            }
        }

        int[][] dp = new int[m][n];  // dp[i][j]: will tell the longest path from (i, j)
        int[] rows = new int[m];     // rows[i]: tell the longest path in ith row.
        int[] cols = new int[n];     // cols[i]: tell the longest path in ith col.
        int ans = 1;                 // minimum must be this only

        // Traversing in sorted order according to values.
        for (int num : valToIndices.keySet()) {
            List<int[]> positions = valToIndices.get(num);
            Map<String, Integer> updates = new HashMap<>();

            for (int[] pos : positions) {
                int i = pos[0], j = pos[1];
                // max we can go from (i, j) is max(row[i], col[j]) + 1
                // for smaller value we already calculated so for cur value max we can go is this only.
                // Num can take all cell traversed by element smaller than 'num'.
                // Here taking the decreasing order values
                dp[i][j] = 1 + Math.max(rows[i], cols[j]);
                ans = Math.max(ans, dp[i][j]);
                updates.put(i + "," + j, dp[i][j]);
            }

            // now update the value of rows and cols array.
            for (int[] pos : positions) {
                int i = pos[0], j = pos[1];
                rows[i] = Math.max(rows[i], dp[i][j]);
                cols[j] = Math.max(cols[j], dp[i][j]);
            }
        }

        return ans;
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxIncreasingCells(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();

        // first store the all (r,c) of an ele, since that ele can occur many times.
        map<int, vector<pair<int, int>>> valToIndices;
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                valToIndices[mat[i][j]].emplace_back(i, j);

        vector<vector<int>> dp(m, vector<int>(n, 0));  // dp[i][j]: will tell the longest path from (i, j)
        vector<int> rows(m, 0);  // rows[i]: tell the longest path in ith row.
        vector<int> cols(n, 0);  // cols[i]: tell the longest path in ith col.
        int ans = 1;             // minimum must be this only

        // Traversing in sorted order according to values.
        for (auto& [num, positions] : valToIndices) {
            vector<tuple<int, int, int>> updates;
            for (auto& [i, j] : positions) {
                // max we can go from (i, j) is max(row[i], col[j]) + 1
                // for smaller value we already calculated so for cur value max we can go is this only.
                // Num can take all cell traversed by element smaller than 'num'.
                // Here taking the decreasing order values
                dp[i][j] = 1 + max(rows[i], cols[j]);
                ans = max(ans, dp[i][j]);
                updates.emplace_back(i, j, dp[i][j]);
            }

            // now update the value of rows and cols array.
            for (auto& [i, j, val] : updates) {
                rows[i] = max(rows[i], val);
                cols[j] = max(cols[j], val);
            }
        }

        return ans;
    }
};
"""
