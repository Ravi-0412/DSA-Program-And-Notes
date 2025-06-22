# just same method we used to find the score of player1 in "486. predict winner". (method 2)

# why here only we need one index para?
# Ans: here we can pick only from start that's why.
# when the index goes out of bound tehn we can simply return '0'.

# Note: 
# piles[i: i+k]=  in case 'i+k' go out of bound then it will give the array from index 'i' to last index.
# And if 'i' goes out of bound then it will give empty array 

# So out of bound cases will get handled automatically, no need to handle separately.

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        def FindScore(i, m, turn):
            if i >= len(piles):
                return 0
            if turn: # means player1 turn.
                ans= float('-inf')
                for k in range(1, 2*m +1):
                    tempAns= sum(piles[i: i+k]) + FindScore(i +k, max(m, k), False)   # max(m, k) because: we must take max of already picked one . e.g: if m= 3 and k= 1 then can't be less than '3' for any further pick.
                    ans= max(ans, tempAns)   # take max of all possibile chance
                return ans
            else:
                ans= float('inf')
                for k in range(1, 2*m +1):
                    tempAns= FindScore(i +k, max(m, k), True)
                    ans= min(ans, tempAns)   # take minimum of all possible chance
                return ans

        return FindScore(0, 1, True)

# Java Code 
"""
class Solution {
    public int stoneGameII(int[] piles) {
        return findScore(0, 1, true, piles);
    }

    public int findScore(int i, int m, boolean turn, int[] piles) {
        if (i >= piles.length)
            return 0;

        if (turn) {  // means player1 turn
            int ans = Integer.MIN_VALUE;
            for (int k = 1; k <= 2 * m; k++) {
                int tempSum = 0;
                for (int x = i; x < Math.min(piles.length, i + k); x++)
                    tempSum += piles[x];

                int tempAns = tempSum + findScore(i + k, Math.max(m, k), false, piles);  // max(m, k) because: we must take max of already picked one
                ans = Math.max(ans, tempAns);  // take max of all possible chance
            }
            return ans;
        } else {
            int ans = Integer.MAX_VALUE;
            for (int k = 1; k <= 2 * m; k++) {
                int tempAns = findScore(i + k, Math.max(m, k), true, piles);
                ans = Math.min(ans, tempAns);  // take minimum of all possible chance
            }
            return ans;
        }
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int stoneGameII(vector<int>& piles) {
        return findScore(0, 1, true, piles);
    }

    int findScore(int i, int m, bool turn, const vector<int>& piles) {
        if (i >= piles.size())
            return 0;

        if (turn) {  // means player1 turn
            int ans = INT_MIN;
            for (int k = 1; k <= 2 * m; ++k) {
                int tempSum = 0;
                for (int x = i; x < min((int)piles.size(), i + k); ++x)
                    tempSum += piles[x];

                int tempAns = tempSum + findScore(i + k, max(m, k), false, piles);  // max(m, k) because: we must take max of already picked one
                ans = max(ans, tempAns);  // take max of all possible chance
            }
            return ans;
        } else {
            int ans = INT_MAX;
            for (int k = 1; k <= 2 * m; ++k) {
                int tempAns = findScore(i + k, max(m, k), true, piles);
                ans = min(ans, tempAns);  // take minimum of all possible chance
            }
            return ans;
        }
    }
};
"""


# memoisation
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        def FindScore(i, m, turn):
            if i >= len(piles):
                return 0
            if (i, m, turn) in cache:
                return cache[(i, m, turn)]
            if turn: # means player1 turn.
                ans= float('-inf')
                for k in range(1, 2*m +1):
                    tempAns= sum(piles[i: i+k]) + FindScore(i +k, max(m, k), False)
                    ans= max(ans, tempAns)   # take max of all possibile chance
                cache[(i, m, turn)]= ans
                return cache[(i, m, turn)]
            else:
                ans= float('inf')
                for k in range(1, 2*m +1):
                    tempAns= FindScore(i +k, max(m, k), True)
                    ans= min(ans, tempAns)   # take minimum of all possible chance
                cache[(i, m, turn)]= ans
                return cache[(i, m, turn)]
                
        cache= {}
        return FindScore(0, 1, True)
 
# Java Code 
"""
import java.util.*;

class Solution {
    Map<String, Integer> cache = new HashMap<>();

    public int stoneGameII(int[] piles) {
        return findScore(0, 1, true, piles);
    }

    private int findScore(int i, int m, boolean turn, int[] piles) {
        if (i >= piles.length)
            return 0;

        String key = i + "," + m + "," + turn;
        if (cache.containsKey(key))
            return cache.get(key);

        if (turn) { // means player1 turn
            int ans = Integer.MIN_VALUE;
            int sum = 0;
            for (int k = 1; k <= 2 * m && i + k <= piles.length; k++) {
                for (int j = i; j < i + k; j++) sum += piles[j];
                int tempAns = sum + findScore(i + k, Math.max(m, k), false, piles);
                ans = Math.max(ans, tempAns); // take max of all possible chance
                sum = 0; // reset for next k
            }
            cache.put(key, ans);
            return ans;
        } else {
            int ans = Integer.MAX_VALUE;
            for (int k = 1; k <= 2 * m && i + k <= piles.length; k++) {
                int tempAns = findScore(i + k, Math.max(m, k), true, piles);
                ans = Math.min(ans, tempAns); // take minimum of all possible chance
            }
            cache.put(key, ans);
            return ans;
        }
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <unordered_map>
#include <string>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    unordered_map<string, int> cache;

    int stoneGameII(vector<int>& piles) {
        return findScore(0, 1, true, piles);
    }

    int findScore(int i, int m, bool turn, const vector<int>& piles) {
        if (i >= piles.size()) return 0;

        string key = to_string(i) + "," + to_string(m) + "," + to_string(turn);
        if (cache.count(key))
            return cache[key];

        if (turn) {  // means player1 turn
            int ans = INT_MIN;
            int sum = 0;
            for (int k = 1; k <= 2 * m && i + k <= piles.size(); ++k) {
                for (int j = i; j < i + k; ++j) sum += piles[j];
                int tempAns = sum + findScore(i + k, max(m, k), false, piles);
                ans = max(ans, tempAns);  // take max of all possible chance
                sum = 0;
            }
            return cache[key] = ans;
        } else {
            int ans = INT_MAX;
            for (int k = 1; k <= 2 * m && i + k <= piles.size(); ++k) {
                int tempAns = findScore(i + k, max(m, k), true, piles);
                ans = min(ans, tempAns);  // take minimum of all possible chance
            }
            return cache[key] = ans;
        }
    }
};
"""   
# memoisation using 3d array.

# range of 'i': 0 to n  , size: n+1
# range of 'm': if m= n then it can go till 2*n. But weit will get retured automatically when i will go beyond 'n' .so will also work for size 'n+1'
# range of turn: 2(True/false)
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        def FindScore(i, m, turn):
            if i >= n:
                return 0
            if dp[i][m][turn]!= -1:
                return dp[i][m][turn]
            if turn: # means player1 turn.
                ans= float('-inf')
                for k in range(1, 2*m +1):
                    tempAns= sum(piles[i: i+k]) + FindScore(i +k, max(m, k), False)
                    ans= max(ans, tempAns)   # take max of all possibile chance
                dp[i][m][turn]= ans
                return dp[i][m][turn]
            else:
                ans= float('inf')
                for k in range(1, 2*m +1):
                    tempAns= FindScore(i +k, max(m, k), True)
                    ans= min(ans, tempAns)   # take minimum of all possible chance
                dp[i][m][turn]= ans
                return dp[i][m][turn]
                
        n= len(piles)
        dp= [[[-1 for t in range(2)] for j in range(2*n + 1)] for i in range(n+1)]
        return FindScore(0, 1, True)

# Java Code 
"""
class Solution {
    public int stoneGameII(int[] piles) {
        int n = piles.length;
        int[][][] dp = new int[n + 1][2 * n + 1][2];  // dp[i][m][turn]
        for (int i = 0; i <= n; i++)
            for (int j = 0; j <= 2 * n; j++)
                for (int t = 0; t < 2; t++)
                    dp[i][j][t] = -1;

        return findScore(0, 1, 1, piles, dp);  // turn: 1 for player1
    }

    private int findScore(int i, int m, int turn, int[] piles, int[][][] dp) {
        int n = piles.length;
        if (i >= n)
            return 0;
        if (dp[i][m][turn] != -1)
            return dp[i][m][turn];

        if (turn == 1) {  // means player1 turn
            int ans = Integer.MIN_VALUE;
            int total = 0;
            for (int k = 1; k <= 2 * m && i + k <= n; k++) {
                total += piles[i + k - 1];
                int tempAns = total + findScore(i + k, Math.max(m, k), 0, piles, dp);
                ans = Math.max(ans, tempAns);  // take max of all possible chance
            }
            dp[i][m][turn] = ans;
        } else {
            int ans = Integer.MAX_VALUE;
            for (int k = 1; k <= 2 * m && i + k <= n; k++) {
                int tempAns = findScore(i + k, Math.max(m, k), 1, piles, dp);
                ans = Math.min(ans, tempAns);  // take minimum of all possible chance
            }
            dp[i][m][turn] = ans;
        }

        return dp[i][m][turn];
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <climits>
#include <algorithm>
using namespace std;

class Solution {
public:
    int stoneGameII(vector<int>& piles) {
        int n = piles.size();
        vector<vector<vector<int>>> dp(n + 1, vector<vector<int>>(2 * n + 1, vector<int>(2, -1)));
        return findScore(0, 1, 1, piles, dp);  // turn: 1 for player1
    }

    int findScore(int i, int m, int turn, const vector<int>& piles, vector<vector<vector<int>>>& dp) {
        int n = piles.size();
        if (i >= n)
            return 0;
        if (dp[i][m][turn] != -1)
            return dp[i][m][turn];

        if (turn == 1) {  // means player1 turn
            int ans = INT_MIN;
            int total = 0;
            for (int k = 1; k <= 2 * m && i + k <= n; ++k) {
                total += piles[i + k - 1];
                int tempAns = total + findScore(i + k, max(m, k), 0, piles, dp);
                ans = max(ans, tempAns);  // take max of all possible chance
            }
            dp[i][m][turn] = ans;
        } else {
            int ans = INT_MAX;
            for (int k = 1; k <= 2 * m && i + k <= n; ++k) {
                int tempAns = findScore(i + k, max(m, k), 1, piles, dp);
                ans = min(ans, tempAns);  // take minimum of all possible chance
            }
            dp[i][m][turn] = ans;
        }

        return dp[i][m][turn];
    }
};
"""