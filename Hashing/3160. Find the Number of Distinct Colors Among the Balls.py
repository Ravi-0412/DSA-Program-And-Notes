# my mistake:
"""
if balls_colored[ball] != 0:
                coloredSet.remove(balls_colored[ball])
                
When a ball's color is removed, you only remove the color that was associated with that ball before, 
but you do not check if that color still exists on other balls. 
This could lead to incorrectly reducing the count of distinct colors.

For example, if one ball has color y, and you remove it from coloredSet, 
but another ball is also using the same color y, the count of distinct colors would be incorrectly decreased. 
This is because you are directly removing the color from the set without checking if it's still needed elsewhere.
"""
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls_colored = [0]* (limit + 1)
        coloredSet = set()
        ans = []
        for ball, color in queries:
            if balls_colored[ball] != 0:
                coloredSet.remove(balls_colored[ball])
            balls_colored[ball] = color
            coloredSet.add(color)
            ans.append(len(coloredSet))
        return ans

# Correct solution
"""
Instead of set, use hashmap to count the frequency of color to know whether that color has been used by other balls or not.

Note: This will give 'Memory Limit Exceeded' error because:
i) Range of limit is : 1 <= limit <= 10^9 which is greater than 10^8 and
ii) balls_colored = [0] * (limit + 1), so it's size can go beyond 10^8.

How to solve this ?
Instead of taking array to note the color of balls, use hashmap. see next solution.
"""
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls_colored = [0] * (limit + 1)  # default color is 0 (uncolored)
        coloredCount = {}  # map to keep track of color counts
        ans = []
        
        for ball, color in queries:
            prev_color = balls_colored[ball]  # get previous color of the ball
            
            # If the ball had a color, decrement its count in coloredCount
            if prev_color != 0:
                coloredCount[prev_color] -= 1
                if coloredCount[prev_color] == 0:
                    del coloredCount[prev_color]
            
            # Assign the new color to the ball
            balls_colored[ball] = color
            
            # Increment the count of the new color in coloredCount
            if color != 0:
                coloredCount[color] = coloredCount.get(color, 0) + 1
            
            # Append the number of distinct colors to the answer
            ans.append(len(coloredCount))
        
        return ans

# Fully correct one
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls_colored = {}  # default color is 0 (uncolored)
        coloredCount = {}  # map to keep track of color counts
        ans = []
        
        for ball, color in queries:
            if ball in balls_colored: 
                prev_color = balls_colored[ball]  # get previous color of the ball
                coloredCount[prev_color] -= 1
                if coloredCount[prev_color] == 0:
                    del coloredCount[prev_color]
            
            # Assign the new color to the ball
            balls_colored[ball] = color
            coloredCount[color] = coloredCount.get(color, 0) + 1
            
            # Append the number of distinct colors to the answer
            ans.append(len(coloredCount))
        
        return ans

# Java
"""
import java.util.*;

public class Solution {
    public int[] queryResults(int limit, int[][] queries) {
        // Map to store the color of each ball
        Map<Integer, Integer> ballsColored = new HashMap<>();
        // Map to track the count of each color
        Map<Integer, Integer> coloredCount = new HashMap<>();
        
        // Result array to store the number of distinct colors after each query
        int[] result = new int[queries.length];
        
        for (int i = 0; i < queries.length; i++) {
            int ball = queries[i][0];
            int color = queries[i][1];
            
            // If the ball has a previous color, decrement the count of that color
            if (ballsColored.containsKey(ball)) {
                int prevColor = ballsColored.get(ball);
                coloredCount.put(prevColor, coloredCount.get(prevColor) - 1);
                if (coloredCount.get(prevColor) == 0) {
                    coloredCount.remove(prevColor);
                }
            }
            
            // Assign the new color to the ball
            ballsColored.put(ball, color);
            
            // Increment the count of the new color
            coloredCount.put(color, coloredCount.getOrDefault(color, 0) + 1);
            
            // Store the number of distinct colors after this query
            result[i] = coloredCount.size();
        }
        
        return result;
    }
}
"""
