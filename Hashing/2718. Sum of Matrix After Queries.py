# Time : O(N) where N = q.size()
# Space : O(N) where N = n

# logic: queries on same row/col for multiple time will get overritten by last one
# i.e only last query on each row and col will affect the sum.
# so start from last queries.

# We start with the last query and go backwards.
# We track id of rows and columns we have seen ,  so we can ignore earlier queries that will be overwritten.
# We also track how many rows and columns are still not covered by any query.

# v * remaining_cols_cnt for a row,
# v * remaining_rows_cnt for a column.

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        rowUsed, colUsed= [0]*n, [0]*n  # will tell whether any row/col has been already updated or not.
        ans= 0
        rowRemain, colRemain= n, n  # queries will only impact the rows and cols not used
        m= len(queries)
        for i in range(m-1, -1, -1):
            type, ind, val= queries[i]
            if type== 0 and not rowUsed[ind]:
                ans += colRemain * val
                rowUsed[ind]= 1   # marking that we have formed operation on this row
                rowRemain -= 1
            if type== 1 and not colUsed[ind]:
                ans += rowRemain * val
                colUsed[ind]= 1   # marking that we have formed operation on this row
                colRemain -= 1
        return ans

# Java Code
"""
import java.util.List;

class Solution {
    public int matrixSumQueries(int n, List<List<Integer>> queries) {
        int[] rowUsed = new int[n], colUsed = new int[n]; // Tracks if a row/column has been updated
        int ans = 0, rowRemain = n, colRemain = n; // Only affect unused rows/columns
        int m = queries.size();

        for (int i = m - 1; i >= 0; i--) {
            int type = queries.get(i).get(0), ind = queries.get(i).get(1), val = queries.get(i).get(2);

            if (type == 0 && rowUsed[ind] == 0) {
                ans += colRemain * val;
                rowUsed[ind] = 1; // Mark row as updated
                rowRemain--;
            }
            if (type == 1 && colUsed[ind] == 0) {
                ans += rowRemain * val;
                colUsed[ind] = 1; // Mark column as updated
                colRemain--;
            }
        }
        return ans;
    }
}
"""

# C++ Code 
"""
#include <vector>
using namespace std;

class Solution {
public:
    int matrixSumQueries(int n, vector<vector<int>>& queries) {
        vector<int> rowUsed(n, 0), colUsed(n, 0); // Tracks if a row/column has been updated
        int ans = 0, rowRemain = n, colRemain = n; // Only affect unused rows/columns
        int m = queries.size();

        for (int i = m - 1; i >= 0; i--) {
            int type = queries[i][0], ind = queries[i][1], val = queries[i][2];

            if (type == 0 && !rowUsed[ind]) {
                ans += colRemain * val;
                rowUsed[ind] = 1; // Mark row as updated
                rowRemain--;
            }
            if (type == 1 && !colUsed[ind]) {
                ans += rowRemain * val;
                colUsed[ind] = 1; // Mark column as updated
                colRemain--;
            }
        }
        return ans;
    }
};
"""