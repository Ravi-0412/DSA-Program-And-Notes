# Logic: Value in cur row will depend on pre row values.
# juist similar as "pascal's triangle".

# Do on paper then you will find a pattern.

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if query_row == 0 and query_glass == 0:
            return poured if poured <= 1 else 1
        pre = [poured]     # 0th glass in 0th row will have this much quantity before releasing excess liquid.
        # starting from 1st row
        for row in range(1, query_row + 1):
            cur = [0]* (row + 1)  # 1th row will have 2 glass and so on.
            for glass in range(row + 1):
                if glass == 0:
                    # Taking max so avoid negative values.
                    # subracting '1' because it will get only the half of excess quantity.
                    cur[glass] = max(0, (pre[glass] - 1) /2)   
                elif glass == row:
                    cur[glass] = max(0, (pre[glass -1] - 1) /2)
                else:
                    cur[glass] = max(0, (pre[glass] - 1) /2) +  max(0, (pre[glass -1] - 1) /2)
                if query_row == row and query_glass == glass:
                    return cur[glass] if cur[glass] <= 1 else 1
            pre = cur.copy()