# Time: O(n), space : O(1)

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        i , j = 0, 0
        ans = 0
        curCost = 0
        while j < n:
            curCost += abs(ord(s[j]) - ord(t[j]))
            # reomev from left till curCost > maxCost
            while curCost > maxCost:
                curCost -= abs(ord(s[i]) - ord(t[i]))
                i += 1
            ans = max(ans, j - i + 1)
            j += 1
        return ans


# Java
"""
class Solution {
    public int equalSubstring(String s, String t, int maxCost) {
        int n = s.length() ;
        int i = 0 , j = 0;
        int curCost = 0 ;
        int ans = 0 ;
        while(j < n) {
            curCost += Math.abs((int)s.charAt(j) - (int)t.charAt(j)) ;
            while(curCost > maxCost){
                curCost -= Math.abs((int)s.charAt(i) - (int)t.charAt(i)) ;
                i += 1 ;
            }
            ans = Math.max(ans, j - i + 1) ;
            j += 1 ;
        }
        return ans;
    }
}
"""