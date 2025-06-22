# Method 1: 

# just same method we used to find the score of player1 in "486. predict winner".

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


# Method 2: 
# memoisation  

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


# Tabulation 
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # suffixSum[i]: total sum of stones from i to end
        suffixSum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffixSum[i] = suffixSum[i + 1] + piles[i]

        # dp[i][m]: max stones current player can get starting at i with M = m
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # Base case: If i >= n, return 0 (already filled with 0)

        # Bottom-up DP from i = n-1 to 0
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                ans = 0
                # simulate the turn where the current player is maximizing (Alice)
                # but we use total - opponent's score to simulate minimization
                for k in range(1, 2 * m + 1):
                    if i + k > n:
                        break
                    # current player picks sum(piles[i:i+k]) = suffixSum[i] - suffixSum[i+k]
                    # opponent gets dp[i + k][max(m, k)]
                    tempAns = suffixSum[i] - dp[i + k][max(m, k)]
                    ans = max(ans, tempAns)
                dp[i][m] = ans

        # First call: i = 0, m = 1
        return dp[0][1]

