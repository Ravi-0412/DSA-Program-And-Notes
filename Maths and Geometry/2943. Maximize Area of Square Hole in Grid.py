# Logic: For max , we will have to find max side we can get after removing bars in both horizontal and vertical.
# FOr this we have to find the max consecutive bars we can  remove.
# if we can remove 'n' bars then , it will contribute to side 'n+1' combining with adjacent bars.

# Actual side of square = min(max_hori_side , max_ver_side)

# tIme: O(n)

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        
        def getMaxSide(bars):
            ans = 2   # minimum side must be '2'
            bars.sort()
            cnt = 1
            for i in range(1, len(bars)):
                if bars[i] != bars[i -1] + 1:
                    cnt = 1
                else:
                    cnt += 1
                    ans = max(ans, cnt + 1)
            return ans
                
        max_hori_side = getMaxSide(hBars)
        max_ver_side =  getMaxSide(vBars)
        side = min(max_hori_side , max_ver_side)
        return side * side