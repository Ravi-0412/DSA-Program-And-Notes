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

# Java Code
"""
import java.util.*;

class Solution {
    public List<Integer> queryResults(int limit, List<List<Integer>> queries) {
        Map<Integer, Integer> ballsColored = new HashMap<>(); // Stores ball color mappings
        Map<Integer, Integer> coloredCount = new HashMap<>(); // Keeps track of color frequencies
        List<Integer> ans = new ArrayList<>();

        for (List<Integer> query : queries) {
            int ball = query.get(0), color = query.get(1);

            if (ballsColored.containsKey(ball)) {
                int prevColor = ballsColored.get(ball); // Get previous color
                coloredCount.put(prevColor, coloredCount.get(prevColor) - 1);
                if (coloredCount.get(prevColor) == 0) {
                    coloredCount.remove(prevColor);
                }
            }

            ballsColored.put(ball, color);
            coloredCount.put(color, coloredCount.getOrDefault(color, 0) + 1);

            ans.add(coloredCount.size());
        }

        return ans;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> queryResults(int limit, vector<vector<int>>& queries) {
        unordered_map<int, int> balls_colored; // Stores ball color mappings
        unordered_map<int, int> coloredCount; // Keeps track of color frequencies
        vector<int> ans;

        for (const auto& query : queries) {
            int ball = query[0], color = query[1];

            if (balls_colored.count(ball)) {
                int prev_color = balls_colored[ball]; // Get previous color
                coloredCount[prev_color]--;
                if (coloredCount[prev_color] == 0) {
                    coloredCount.erase(prev_color);
                }
            }

            balls_colored[ball] = color;
            coloredCount[color]++;

            ans.push_back(coloredCount.size());
        }

        return ans;
    }
};
"""