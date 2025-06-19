# Method 1 : 

# Logic: We don't need to take space of size '2050' because year is varying from 1950 to 2050.
# So space of size '101' will be fine.


from typing import List
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        year = [0] * 101  # Covers years from 1950 to 2050 (inclusive)

        # O(n) time to build population delta
        for log in logs:
            year[log[0] - 1950] += 1
            year[log[1] - 1950] -= 1

        max_num = year[0]
        max_year = 1950

        for i in range(1, 101):
            year[i] += year[i - 1]  # Prefix sum to get actual population
            if year[i] > max_num:
                max_num = year[i]
                max_year = i + 1950

        return max_year

# Java Code 
"""
class Solution {
    public int maximumPopulation(int[][] logs) {
        int[] year = new int[101];  // Covers years from 1950 to 2050 (inclusive)

        // O(n) time to build population delta
        for (int[] log : logs) {
            year[log[0] - 1950] += 1;
            year[log[1] - 1950] -= 1;
        }

        int maxNum = year[0];
        int maxYear = 1950;

        for (int i = 1; i < 101; i++) {
            year[i] += year[i - 1];  // Prefix sum to get actual population
            if (year[i] > maxNum) {
                maxNum = year[i];
                maxYear = i + 1950;
            }
        }

        return maxYear;
    }
}
"""

# C++ Code 
"""
#include <vector>
using namespace std;

class Solution {
public:
    int maximumPopulation(vector<vector<int>>& logs) {
        int year[101] = {0};  // Covers years from 1950 to 2050 (inclusive)

        // O(n) time to build population delta
        for (auto& log : logs) {
            year[log[0] - 1950] += 1;
            year[log[1] - 1950] -= 1;
        }

        int maxNum = year[0];
        int maxYear = 1950;

        for (int i = 1; i < 101; i++) {
            year[i] += year[i - 1];  // Prefix sum to get actual population
            if (year[i] > maxNum) {
                maxNum = year[i];
                maxYear = i + 1950;
            }
        }

        return maxYear;
    }
};
"""

# Related Q:
# 1) 2848. Points That Intersect With Cars
# just apply same logic and add count of point whose value > 0.
