# Logic: Similar to "2013. Detect Squares"
"""
# In case of rectangle any two points can be diagonal, won't follow property like square 'abs(x1 - x2) == abs(y1 - y2)'.
# So consider each possible diagonal pair then other two points will be same as square i.e '(x1, y2)' and '(x2, y1)'.
and one side length = abs(x1 - x2) and other side length = abs(y1 - y2)
"""

# Time: O(n^2)

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        pointsMap = {(points[i][0], points[i][1]): i for i in range(n)}   # for checking points in O(1)
        ans = float('inf')
        for i in range(n):
            x1, y1 = points[i][0], points[i][1]
            for j in range(n):
                x2, y2 = points[j][0], points[j][1]
              # x1 != x2 and y1 != y2 : for parallel axis
                if x1 != x2 and y1 != y2 and (x1, y2) in pointsMap and (x2, y1) in pointsMap:
                    ans = min(ans, abs(x1 - x2) * abs(y1 - y2))
        return ans if ans != float('inf') else 0

# Java Code
"""
import java.util.*;

class Solution {
    public int minAreaRect(int[][] points) {
        int n = points.length;
        Map<Integer, Set<Integer>> pointsMap = new HashMap<>(); // For checking points in O(1)

        for (int[] point : points) {
            pointsMap.putIfAbsent(point[0], new HashSet<>());
            pointsMap.get(point[0]).add(point[1]);
        }

        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            int x1 = points[i][0], y1 = points[i][1];
            for (int j = 0; j < n; j++) {
                int x2 = points[j][0], y2 = points[j][1];

                // x1 != x2 and y1 != y2 : for parallel axis
                if (x1 != x2 && y1 != y2 && pointsMap.get(x1).contains(y2) && pointsMap.get(x2).contains(y1)) {
                    ans = Math.min(ans, Math.abs(x1 - x2) * Math.abs(y1 - y2));
                }
            }
        }

        return (ans == Integer.MAX_VALUE) ? 0 : ans;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <unordered_map>
#include <limits>

using namespace std;

class Solution {
public:
    int minAreaRect(vector<vector<int>>& points) {
        int n = points.size();
        unordered_map<int, unordered_map<int, int>> pointsMap; // For checking points in O(1)

        for (int i = 0; i < n; i++) {
            pointsMap[points[i][0]][points[i][1]] = i;
        }

        int ans = numeric_limits<int>::max();
        for (int i = 0; i < n; i++) {
            int x1 = points[i][0], y1 = points[i][1];
            for (int j = 0; j < n; j++) {
                int x2 = points[j][0], y2 = points[j][1];

                // x1 != x2 and y1 != y2 : for parallel axis
                if (x1 != x2 && y1 != y2 && pointsMap[x1].count(y2) && pointsMap[x2].count(y1)) {
                    ans = min(ans, abs(x1 - x2) * abs(y1 - y2));
                }
            }
        }

        return (ans == numeric_limits<int>::max()) ? 0 : ans;
    }
};
"""