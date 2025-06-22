# method 1: Brute force
# check every pair
# Time : O(n^2)

# method 2: Optimising to O(n) 
# Using similar logic as : "121. Best Time to Buy and Sell Stock".

# Logic: 
"""
Maintain two variable that will store curMaxPoint and curMaxPointIndex .
At each index we can decide whether we to update our 'curMaxPoint and curMaxPointIndex' to 'values[j] and j'
or forward the same 'curMaxPoint and curMaxPointIndex' to next index.

For this we will check 'if values[j] > curMaxPoint - (j - curMaxPointIndex)' then we will update curMaxPointIndex' to 'values[j] and j'.
Why this because for next index curMaxPoint value will decrease by 'curMaxPoint - (j - curMaxPointIndex)'.
"""

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        curMaxPoint = values[0]
        curMaxPointIndex = 0
        ans = 0
        for j in range(1, n):
            ans = max(ans , curMaxPoint + values[j] - (j - curMaxPointIndex))
            if values[j] > curMaxPoint - (j - curMaxPointIndex):
                curMaxPoint = values[j]
                curMaxPointIndex = j
        return ans

# Java Code 
"""
class Solution {
    public int maxScoreSightseeingPair(int[] values) {
        int n = values.length;
        int curMaxPoint = values[0];
        int curMaxPointIndex = 0;
        int ans = 0;

        for (int j = 1; j < n; j++) {
            ans = Math.max(ans, curMaxPoint + values[j] - (j - curMaxPointIndex));
            if (values[j] > curMaxPoint - (j - curMaxPointIndex)) {
                curMaxPoint = values[j];
                curMaxPointIndex = j;
            }
        }

        return ans;
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        int n = values.size();
        int curMaxPoint = values[0];
        int curMaxPointIndex = 0;
        int ans = 0;

        for (int j = 1; j < n; ++j) {
            ans = max(ans, curMaxPoint + values[j] - (j - curMaxPointIndex));
            if (values[j] > curMaxPoint - (j - curMaxPointIndex)) {
                curMaxPoint = values[j];
                curMaxPointIndex = j;
            }
        }

        return ans;
    }
};
"""
