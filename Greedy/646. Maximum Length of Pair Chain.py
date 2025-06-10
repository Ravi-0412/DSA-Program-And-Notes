# method 1: using DP

# Recursion + memoisation

# Time: O(n^2)

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        @lru_cache(None)
        def solve(pre, cur):
            if cur == len(pairs):
                return 0
            ans = solve(pre, cur + 1) 
            if pre == -1 or  pairs[cur][0] > pairs[pre][1]:
                ans = max(ans, 1 + solve(cur, cur + 1))
            return ans

        pairs.sort()  # sorting based on starting time
        return solve(-1, 0)


# Method 2:
# just think 'pairs' as intervals.

# This Q is exactly same as " Find max no of non-overlapping intervals"
# And this we did in "435. Non-overlapping Intervals".

# Time : O(n*logn)

class Solution:
    def findLongestChain(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x : x[1])   
        preEnd= intervals[0][1]  # will keep track of last added inetrval.
        count = 1  # will count the max no of non-overlapping intervals. 
        # Starting from '1 because if not overlap then at 1st time we will have to add both the intervals.
        # Also 1st will be always included.
        for start, end in intervals[1:]:
            # if they are not overlapping
            if start > preEnd: 
                preEnd= end
                count += 1
            # if overlapping,  skip the cur one since pre ending interval will be before only and we already taken that.
        return count

# Java Code 
"""
//Method 1: Recursive DP with Memoization
import java.util.*;

class Solution {
    int[][] pairs;
    int[][] memo;

    public int findLongestChain(int[][] pairs) {
        Arrays.sort(pairs, (a, b) -> Integer.compare(a[0], b[0]));  // sorting based on starting time
        this.pairs = pairs;
        int n = pairs.length;
        memo = new int[n + 1][n + 1];
        for (int[] row : memo)
            Arrays.fill(row, -1);
        return solve(-1, 0);
    }

    private int solve(int pre, int cur) {
        if (cur == pairs.length) return 0;
        if (memo[pre + 1][cur] != -1) return memo[pre + 1][cur];

        int ans = solve(pre, cur + 1);
        if (pre == -1 || pairs[cur][0] > pairs[pre][1]) {
            ans = Math.max(ans, 1 + solve(cur, cur + 1));
        }
        return memo[pre + 1][cur] = ans;
    }
}

// Method 2: Greedy (same as max non-overlapping intervals)
import java.util.*;

class Solution {
    public int findLongestChain(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));

        int preEnd = intervals[0][1];  // will keep track of last added inetrval.
        int count = 1;  // will count the max no of non-overlapping intervals. 
        // Starting from 1 because if not overlap then at 1st time we will have to add both the intervals.
        // Also 1st will be always included.

        for (int i = 1; i < intervals.length; i++) {
            int start = intervals[i][0];
            int end = intervals[i][1];

            // if they are not overlapping
            if (start > preEnd) {
                preEnd = end;
                count++;
            }
            // if overlapping, skip the cur one since pre ending interval will be before only and we already taken that.
        }

        return count;
    }
}

"""

# C++ Code 
"""
//Method 1: Recursive DP with Memoization
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> pairs;
    vector<vector<int>> memo;

    int findLongestChain(vector<vector<int>>& pairs) {
        sort(pairs.begin(), pairs.end());  // sorting based on starting time
        this->pairs = pairs;
        int n = pairs.size();
        memo = vector<vector<int>>(n + 1, vector<int>(n + 1, -1));
        return solve(-1, 0);
    }

    int solve(int pre, int cur) {
        if (cur == pairs.size()) return 0;
        if (memo[pre + 1][cur] != -1) return memo[pre + 1][cur];

        int ans = solve(pre, cur + 1);
        if (pre == -1 || pairs[cur][0] > pairs[pre][1]) {
            ans = max(ans, 1 + solve(cur, cur + 1));
        }
        return memo[pre + 1][cur] = ans;
    }
};
//Method 2: Greedy (same as max non-overlapping intervals)
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int findLongestChain(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });

        int preEnd = intervals[0][1];  // will keep track of last added inetrval.
        int count = 1;  // will count the max no of non-overlapping intervals. 
        // Starting from 1 because if not overlap then at 1st time we will have to add both the intervals.
        // Also 1st will be always included.

        for (int i = 1; i < intervals.size(); i++) {
            int start = intervals[i][0];
            int end = intervals[i][1];

            // if they are not overlapping
            if (start > preEnd) {
                preEnd = end;
                count++;
            }
            // if overlapping, skip the cur one since pre ending interval will be before only and we already taken that.
        }

        return count;
    }
};

"""