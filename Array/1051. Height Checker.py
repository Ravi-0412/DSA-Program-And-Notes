# method 1:
# Time = O(n*logn)

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

# Method 2:
# logic: 
"""
Just count the frequency of each height (using HashMap or int[] as the height is promised to be within range[1, 100]) and 
then compares them in order to the heights in the input array.

# Time = space = O(n)
"""

class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        # Frequency array to count occurrences of each height (range 0-100)
        height_to_freq = [0] * 101  

        # Populate frequency array
        for height in heights:
            height_to_freq[height] += 1

        result = 0  # Counter for mismatches
        cur_height = 0  # Pointer to track the expected height in sorted order

        # Iterate through the original heights array
        for height in heights:
            # Move to the next non-zero frequency height
            while height_to_freq[cur_height] == 0:
                cur_height += 1

            # If the expected height doesn't match the original, count it as a mismatch
            if cur_height != height:
                result += 1

            # Reduce the frequency of the used height
            height_to_freq[cur_height] -= 1

        return result  # Return the number of mismatches
# Java
"""
class Solution {
    public int heightChecker(int[] heights) {
        int[] heightToFreq = new int[101];
        
        for (int height : heights) {
            heightToFreq[height]++;
        }
        
        int result = 0;
        int curHeight = 0;
        
        for (int i = 0; i < heights.length; i++) {
            while (heightToFreq[curHeight] == 0) {
                curHeight++;
            }
            
            if (curHeight != heights[i]) {
                result++;
            }
            heightToFreq[curHeight]--;
        }
        
        return result;
    }
}
"""
