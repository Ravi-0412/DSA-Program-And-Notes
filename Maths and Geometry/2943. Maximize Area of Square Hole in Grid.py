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

# Java
"""
import java.util.*;

class Solution {
    public int maximizeSquareHoleArea(int n, int m, int[] hBars, int[] vBars) {
        return (int) Math.pow(Math.min(getMaxSide(hBars), getMaxSide(vBars)), 2);
    }

    private int getMaxSide(int[] bars) {
        if (bars.length == 0) return 2; // Minimum side length is 2
        Arrays.sort(bars);
        int ans = 2, count = 1;

        for (int i = 1; i < bars.length; i++) {
            if (bars[i] == bars[i - 1] + 1) {
                count++;
                ans = Math.max(ans, count + 1);
            } else {
                count = 1;
            }
        }
        return ans;
    }
}
"""
