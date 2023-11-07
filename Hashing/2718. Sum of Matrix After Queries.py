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
