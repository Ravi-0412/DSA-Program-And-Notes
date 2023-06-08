# Time : O(N) where N = q.size()
# Space : O(N) where N = n

# logic: queries on same row/col for multiple time will get overritten by last one.
# so start from last queries.

# We start with the last query and go backwards.
# We track id if rows and columns we have seen - so we can ignore earlier queries that will be overwritten.
# We also track how many rows and columns are still not covered by any query. That way, each query adds:
# v * cols_cnt for a row,
# v * rows_cnt for a column.
class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        rowUsed, colUsed= [0]*n, [0]*n
        ans= 0
        rowRemain, colRemain= n, n
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
