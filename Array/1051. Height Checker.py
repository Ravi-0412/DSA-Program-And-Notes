
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = 0
        expected = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                ans += 1
        return ans

# If you will use 'sort() then it you have to do like this because 'sort()' modifies array internally in both python and java

# java
"""
class Solution {
    public int heightChecker(int[] heights) {
        int n = heights.length ;
        int[] expected = heights.clone();
        Arrays.sort(expected) ;
        int ans = 0;
        for(int i = 0; i < n; i ++) {
            if(expected[i] != heights[i]) {
                ans += 1 ;
            }
        }
        return ans; 
    }
}
"""