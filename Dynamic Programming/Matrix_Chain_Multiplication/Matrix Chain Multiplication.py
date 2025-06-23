# Method 1: 

# Recursive approach 
# correct only but give TLE

class Solution:
    def matrixMultiplication(self, N, arr):
        i,j = 1, N-1  # we can only subdivide before 'n-1' so took j= 'n-1'. can put braces from first matrix to 'one before last matrix)
        return self.MCM(arr,i,j)  # calculating the minimum multiplication from 'i'th matrix to 'j'th matrix.
    def MCM(self,arr,start,end):
        if start >= end:  # only one matrix remaining. "==" will also work.
            return 0
        mn= 99999999999
        for k in range(start,end):
            """
            start matrix se leke 'k' matrix tak + (k + 1) se leke 'j-1' tak
            (start , k) matrix tak jo result matrix milega uska dimension hoga: arr[start-1]*arr[k]
            (k + 1, end) matrix tak jo result matrix milega uska dimension hoga: arr[k] * arr[end]
            no of multiplication hoga dono ka: arr[start-1]*arr[k] * arr[end] i.e just conside above sub-matrix as separate matrix .
            And is dono ka resultant matrix ka jo dimension hoga: arr[start-1] * arr[end] .
            """
            tempAns = self.MCM(arr,start,k) + self.MCM(arr,k+1,end) + arr[start-1]*arr[k]*arr[end]   # will store all possible ans
            mn= min(mn,tempAns)   # take minimum of all ans.
        return mn

# Java Code 
"""
class Solution {
    public int matrixMultiplication(int N, int[] arr) {
        int i = 1, j = N - 1;  // we can only subdivide before 'n-1' so took j= 'n-1'. can put braces from first matrix to 'one before last matrix)
        return MCM(arr, i, j);  // calculating the minimum multiplication from 'i'th matrix to 'j'th matrix.
    }

    public int MCM(int[] arr, int start, int end) {
        if (start >= end)  // only one matrix remaining. "==" will also work.
            return 0;

        int mn = Integer.MAX_VALUE;
        for (int k = start; k < end; k++) {
            /*
            start matrix se leke 'k' matrix tak + (k + 1) se leke 'j-1' tak
            (start , k) matrix tak jo result matrix milega uska dimension hoga: arr[start-1]*arr[k]
            (k + 1, end) matrix tak jo result matrix milega uska dimension hoga: arr[k] * arr[end]
            no of multiplication hoga dono ka: arr[start-1]*arr[k] * arr[end] i.e just consider above sub-matrix as separate matrix .
            And is dono ka resultant matrix ka jo dimension hoga: arr[start-1] * arr[end] .
            */
            int tempAns = MCM(arr, start, k) + MCM(arr, k + 1, end) + arr[start - 1] * arr[k] * arr[end];  // will store all possible ans
            mn = Math.min(mn, tempAns);  // take minimum of all ans.
        }

        return mn;
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
    int matrixMultiplication(int N, vector<int>& arr) {
        int i = 1, j = N - 1;  // we can only subdivide before 'n-1' so took j= 'n-1'. can put braces from first matrix to 'one before last matrix)
        return MCM(arr, i, j);  // calculating the minimum multiplication from 'i'th matrix to 'j'th matrix.
    }

    int MCM(vector<int>& arr, int start, int end) {
        if (start >= end)  // only one matrix remaining. "==" will also work.
            return 0;

        int mn = INT_MAX;
        for (int k = start; k < end; ++k) {
            /*
            start matrix se leke 'k' matrix tak + (k + 1) se leke 'j-1' tak
            (start , k) matrix tak jo result matrix milega uska dimension hoga: arr[start-1]*arr[k]
            (k + 1, end) matrix tak jo result matrix milega uska dimension hoga: arr[k] * arr[end]
            no of multiplication hoga dono ka: arr[start-1]*arr[k] * arr[end] i.e just consider above sub-matrix as separate matrix .
            And is dono ka resultant matrix ka jo dimension hoga: arr[start-1] * arr[end] .
            */
            int tempAns = MCM(arr, start, k) + MCM(arr, k + 1, end) + arr[start - 1] * arr[k] * arr[end];  // will store all possible ans
            mn = min(mn, tempAns);  // take minimum of all ans.
        }

        return mn;
    }
};
"""


# method 2:
# memoization
# time: O(n^3)
class Solution:
    def matrixMultiplication(self, N, arr):
        i,j= 1, N-1
        dp= [[-1 for j in range(N)] for i in range(N)]  # range of 'i' and 'j' is 'n' i.e from '1' to 'n-1' but indexing will start from '0' only so took size= n
        return self.MCM(arr,i,j,dp)
    def MCM(self,arr,start,end,dp):
        if start>= end:
            # dp[start][end]= 0
            # return dp[start][end]
            return 0  # or simply this only
        if dp[start][end]!= -1:
            return dp[start][end]
        mn= 99999999999
        for k in range(start,end):
            tempAns= self.MCM(arr,start,k,dp) + self.MCM(arr,k+1,end,dp) + arr[start-1]*arr[k]*arr[end]
            mn= min(mn,tempAns)
        dp[start][end]= mn
        return dp[start][end]

# Java Code 
"""
class Solution {
    public int matrixMultiplication(int N, int[] arr) {
        int i = 1, j = N - 1;
        int[][] dp = new int[N][N];  // range of 'i' and 'j' is 'n' i.e from '1' to 'n-1' but indexing will start from '0' only so took size= n
        for (int x = 0; x < N; x++) {
            for (int y = 0; y < N; y++) {
                dp[x][y] = -1;
            }
        }
        return MCM(arr, i, j, dp);
    }

    public int MCM(int[] arr, int start, int end, int[][] dp) {
        if (start >= end) {
            // dp[start][end]= 0
            // return dp[start][end]
            return 0;  // or simply this only
        }
        if (dp[start][end] != -1) {
            return dp[start][end];
        }
        int mn = Integer.MAX_VALUE;
        for (int k = start; k < end; k++) {
            int tempAns = MCM(arr, start, k, dp) + MCM(arr, k + 1, end, dp) + arr[start - 1] * arr[k] * arr[end];
            mn = Math.min(mn, tempAns);
        }
        dp[start][end] = mn;
        return dp[start][end];
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
    int matrixMultiplication(int N, vector<int>& arr) {
        int i = 1, j = N - 1;
        vector<vector<int>> dp(N, vector<int>(N, -1));  // range of 'i' and 'j' is 'n' i.e from '1' to 'n-1' but indexing will start from '0' only so took size= n
        return MCM(arr, i, j, dp);
    }

    int MCM(vector<int>& arr, int start, int end, vector<vector<int>>& dp) {
        if (start >= end) {
            // dp[start][end]= 0
            // return dp[start][end]
            return 0;  // or simply this only
        }
        if (dp[start][end] != -1) {
            return dp[start][end];
        }
        long long mn = LLONG_MAX;
        for (int k = start; k < end; ++k) {
            int tempAns = MCM(arr, start, k, dp) + MCM(arr, k + 1, end, dp) + arr[start - 1] * arr[k] * arr[end];
            mn = min(mn, (long long)tempAns);
        }
        dp[start][end] = mn;
        return dp[start][end];
    }
};
"""

# Method 3: 
# Tabulation:
# Note: In MCM type Q, go from first valid input to first invalid input (both inclusive) or vice versa.
# both looping variable should go till first function call after initialisng the base case.
class Solution:
    def matrixMultiplication(self, N, arr):
        dp= [[0 for j in range(N)] for i in range(N)]   # automatically get initialised with base for 'dp[i][i]= 0' 
                                                        # when both 'i' and 'j' will be equal
        for start in range(N-2,0,-1):  # from last valid one to first valid one. n-2 to '1'.
            for end in range(start+1,N):  # 'end' must be always right of 'start' so started with 'start+1'. as for valid one 'end' must be greater than 'start' and first invlaid one= 'n-1'.
                # now just copy paste the recurrence
                mn= 99999999999 
                for k in range(start,end):
                    tempAns= dp[start][k] + dp[k+1][end] + arr[start-1]*arr[k]*arr[end]
                    mn= min(mn,tempAns)
                dp[start][end]= mn
        return dp[1][N-1]   # we have called the recursive function for this variable value. so simply return that


# Java Code 
"""
class Solution {
    public int matrixMultiplication(int N, int[] arr) {
        int[][] dp = new int[N][N];  // automatically get initialised with base for 'dp[i][i]= 0' 
                                     // when both 'i' and 'j' will be equal

        for (int start = N - 2; start >= 1; --start) {  // from last valid one to first valid one. n-2 to '1'.
            for (int end = start + 1; end < N; ++end) {  // 'end' must be always right of 'start' so started with 'start+1'.
                                                          // as for valid one 'end' must be greater than 'start' and first invalid one= 'n-1'.
                // now just copy paste the recurrence
                int mn = Integer.MAX_VALUE;
                for (int k = start; k < end; ++k) {
                    int tempAns = dp[start][k] + dp[k + 1][end] + arr[start - 1] * arr[k] * arr[end];
                    mn = Math.min(mn, tempAns);
                }
                dp[start][end] = mn;
            }
        }

        return dp[1][N - 1];  // we have called the recursive function for this variable value. so simply return that
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
    int matrixMultiplication(int N, vector<int>& arr) {
        vector<vector<long long>> dp(N, vector<long long>(N, 0));  // automatically get initialised with base for 'dp[i][i]= 0' 
                                                                   // when both 'i' and 'j' will be equal

        for (int start = N - 2; start >= 1; --start) {  // from last valid one to first valid one. n-2 to '1'.
            for (int end = start + 1; end < N; ++end) {  // 'end' must be always right of 'start' so started with 'start+1'. 
                                                         // as for valid one 'end' must be greater than 'start' and first invalid one= 'n-1'.
                // now just copy paste the recurrence
                long long mn = LLONG_MAX;
                for (int k = start; k < end; ++k) {
                    long long tempAns = dp[start][k] + dp[k + 1][end] + (long long)arr[start - 1] * arr[k] * arr[end];
                    mn = min(mn, tempAns);
                }
                dp[start][end] = mn;
            }
        }

        return dp[1][N - 1];  // we have called the recursive function for this variable value. so simply return that
    }
};
"""