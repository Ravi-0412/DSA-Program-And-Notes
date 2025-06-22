# Method 1: 
# Recursion + Memoisation

# Totally same as "1140. stone game 2".
# just pass m= 3 and don't change 'm' in cal;ling funtion and also in for loop run till 'm+1' that's it.

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        total = sum(stoneValue)

        # Create 3D DP array: dp[i][turn] where turn = 0 (Bob), 1 (Alice)
        dp = [[-1] * 2 for _ in range(n + 1)]

        def FindScore(i, m, turn):
            if i >= n:
                return 0
            if dp[i][turn] != -1:
                return dp[i][turn]

            if turn:  # means player1 turn (Alice)
                ans = float('-inf')
                for k in range(1, m + 1):
                    if i + k <= n:
                        tempAns = sum(stoneValue[i: i + k]) + FindScore(i + k, m, 0)
                        ans = max(ans, tempAns)
                dp[i][turn] = ans
            else:  # Bob's turn
                ans = float('inf')
                for k in range(1, m + 1):
                    if i + k <= n:
                        tempAns = FindScore(i + k, m, 1)
                        ans = min(ans, tempAns)
                dp[i][turn] = ans

            return dp[i][turn]

        AliceScore = FindScore(0, 3, 1)  # initially pass m = 3, turn = 1 (Alice)
        BobScore = total - AliceScore

        if AliceScore == BobScore:
            return "Tie"
        elif AliceScore > BobScore:
            return "Alice"
        else:
            return "Bob"

# Java Code 
"""
import java.util.*;

class Solution {
    int[][][] dp;
    int n;

    public String stoneGameIII(int[] stoneValue) {
        n = stoneValue.length;
        dp = new int[n + 1][4][2];  // 3D DP: [index][m][turn]
        for (int i = 0; i <= n; i++)
            for (int j = 0; j <= 3; j++)
                Arrays.fill(dp[i][j], Integer.MIN_VALUE);

        int aliceScore = findScore(0, 3, 1, stoneValue);  // initially pass m = 3
        int total = Arrays.stream(stoneValue).sum();
        int bobScore = total - aliceScore;

        if (aliceScore == bobScore) return "Tie";
        else if (aliceScore > bobScore) return "Alice";
        else return "Bob";
    }

    private int findScore(int i, int m, int turn, int[] stoneValue) {
        if (i >= n) return 0;
        if (dp[i][m][turn] != Integer.MIN_VALUE) return dp[i][m][turn];

        if (turn == 1) {  // player1 (Alice) turn
            int ans = Integer.MIN_VALUE;
            int sum = 0;
            for (int k = 1; k <= m && i + k <= n; k++) {
                sum += stoneValue[i + k - 1];
                int temp = sum + findScore(i + k, m, 0, stoneValue);
                ans = Math.max(ans, temp);  // take max of all possible chance
            }
            return dp[i][m][turn] = ans;
        } else {
            int ans = Integer.MAX_VALUE;
            for (int k = 1; k <= m && i + k <= n; k++) {
                int temp = findScore(i + k, m, 1, stoneValue);
                ans = Math.min(ans, temp);  // take minimum of all possible chance
            }
            return dp[i][m][turn] = ans;
        }
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>
#include <climits>
using namespace std;

class Solution {
public:
    int dp[50001][4][2];
    int n;

    string stoneGameIII(vector<int>& stoneValue) {
        n = stoneValue.size();
        for (int i = 0; i <= n; ++i)
            for (int m = 0; m <= 3; ++m)
                for (int t = 0; t < 2; ++t)
                    dp[i][m][t] = INT_MIN;

        int aliceScore = findScore(0, 3, 1, stoneValue);  // initially pass m = 3
        int total = accumulate(stoneValue.begin(), stoneValue.end(), 0);
        int bobScore = total - aliceScore;

        if (aliceScore == bobScore) return "Tie";
        else if (aliceScore > bobScore) return "Alice";
        else return "Bob";
    }

    int findScore(int i, int m, int turn, const vector<int>& stoneValue) {
        if (i >= n) return 0;
        if (dp[i][m][turn] != INT_MIN) return dp[i][m][turn];

        if (turn == 1) {  // player1 (Alice) turn
            int ans = INT_MIN, sum = 0;
            for (int k = 1; k <= m && i + k <= n; ++k) {
                sum += stoneValue[i + k - 1];
                int temp = sum + findScore(i + k, m, 0, stoneValue);
                ans = max(ans, temp);  // take max of all possible chance
            }
            return dp[i][m][turn] = ans;
        } else {
            int ans = INT_MAX;
            for (int k = 1; k <= m && i + k <= n; ++k) {
                int temp = findScore(i + k, m, 1, stoneValue);
                ans = min(ans, temp);  // take minimum of all possible chance
            }
            return dp[i][m][turn] = ans;
        }
    }
};
"""


# Method 2:
# Tabulation

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        # dp[i][turn]: max score Alice can get starting from index i
        # turn = 1 (Alice), turn = 0 (Bob)
        dp = [[0] * 2 for _ in range(n + 1)]  # base case: when i == n, score is 0

        for i in range(n - 1, -1, -1):
            for turn in [0, 1]:  # 1 means Alice's turn, 0 means Bob's turn
                if turn:  # means player1 turn (Alice)
                    ans = float('-inf')
                    total = 0
                    for k in range(1, 4):  # m = 3
                        if i + k <= n:
                            total += stoneValue[i + k - 1]
                            tempAns = total + dp[i + k][0]  # Bob's turn next
                            ans = max(ans, tempAns)  # take max of all possible choices
                    dp[i][turn] = ans
                else:  # Bob's turn
                    ans = float('inf')
                    for k in range(1, 4):  # m = 3
                        if i + k <= n:
                            tempAns = dp[i + k][1]  # Alice's turn next
                            ans = min(ans, tempAns)  # take min of all possible choices
                    dp[i][turn] = ans

        AliceScore = dp[0][1]  # starting from index 0, Alice's turn
        BobScore = sum(stoneValue) - AliceScore

        if AliceScore == BobScore:
            return "Tie"
        elif AliceScore > BobScore:
            return "Alice"
        else:
            return "Bob"



