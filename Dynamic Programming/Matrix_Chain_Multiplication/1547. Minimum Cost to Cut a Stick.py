# 1st method: 

# Recursive
# logic in notes: 123,124

# lOgic: # we can cur at any of the given position in cuts so there must be something on leftmost and rightmost side 
# to calculate the length that's why appedning these number.
# so first insert '0' and 'n' and then sort. Then automatically '0' will come at furst and 'n' at last.
# why sorting?
# agla kon sa length pe cut karna h har part me, usko pta karne ke liye sort karna hoga

# After that apply same logic as 'MCM'.

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        l= len(cuts)
        return self.helper(cuts, 1, l-1)   # first valied -> 1 and first invalid -> l - 1
                                           # first_invalid - (1st_valid - 1)  will give length after each cut.
    
    def helper(self, cuts, i, j):
        if i==j:
            return 0
        mn= 9999999999
        for k in range(i, j):
            tempAns= self.helper(cuts, i, k) + self.helper(cuts, k+1, j) + cuts[j]- cuts[i-1]
            # tempAns= self.helper(cuts, i, k-1) + self.helper(cuts, k+1, j) + cuts[j]- cuts[i-1]   # i was writing this. last range should be invalid only and writing 'k-1' will make valid
            mn = min(mn, tempAns)
        return mn

<<<<<<< HEAD
# Java Code 
"""
import java.util.*;

class Solution {
    public int minCost(int n, int[] cuts) {
        List<Integer> list = new ArrayList<>();
        for (int cut : cuts) list.add(cut);
        list.add(0);
        list.add(n);
        Collections.sort(list);
        int l = list.size();
        return helper(list, 1, l - 1);  // first valied -> 1 and first invalid -> l - 1
                                        // first_invalid - (1st_valid - 1)  will give length after each cut.
    }

    public int helper(List<Integer> cuts, int i, int j) {
        if (i == j)
            return 0;
        int mn = Integer.MAX_VALUE;
        for (int k = i; k < j; k++) {
            int tempAns = helper(cuts, i, k) + helper(cuts, k + 1, j) + cuts.get(j) - cuts.get(i - 1);
            // int tempAns = helper(cuts, i, k - 1) + helper(cuts, k + 1, j) + cuts[j] - cuts[i - 1];
            // i was writing this. last range should be invalid only and writing 'k-1' will make valid
            mn = Math.min(mn, tempAns);
        }
        return mn;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    int minCost(int n, vector<int>& cuts) {
        cuts.push_back(0);
        cuts.push_back(n);
        sort(cuts.begin(), cuts.end());
        int l = cuts.size();
        return helper(cuts, 1, l - 1);  // first valied -> 1 and first invalid -> l - 1
                                       // first_invalid - (1st_valid - 1)  will give length after each cut.
    }

    int helper(vector<int>& cuts, int i, int j) {
        if (i == j)
            return 0;
        int mn = INT_MAX;
        for (int k = i; k < j; ++k) {
            int tempAns = helper(cuts, i, k) + helper(cuts, k + 1, j) + cuts[j] - cuts[i - 1];
            // int tempAns = helper(cuts, i, k - 1) + helper(cuts, k + 1, j) + cuts[j] - cuts[i - 1];
            // i was writing this. last range should be invalid only and writing 'k-1' will make valid
            mn = min(mn, tempAns);
        }
        return mn;
    }
};
"""

# method 2: memoization
=======
# method 2: 
# memoization
>>>>>>> a40de18 (verified Binary Search and DP)
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        l= len(cuts)
        dp= [[-1 for j in range(l)] for i in range(l)]
        return self.helper(cuts, 1, l-1, dp)
    
    def helper(self, cuts, i, j, dp):
        if i==j:
            return 0
        if dp[i][j]!= -1:
            return dp[i][j]
        mn= 9999999999
        for k in range(i, j):
            tempAns= self.helper(cuts, i, k, dp) + self.helper(cuts, k+1, j, dp) + cuts[j]- cuts[i-1]
            mn= min(mn, tempAns)
        dp[i][j]= mn
        return dp[i][j]
<<<<<<< HEAD

# Java Code 
"""
import java.util.*;

class Solution {
    public int minCost(int n, int[] cutArray) {
        List<Integer> cuts = new ArrayList<>();
        for (int c : cutArray) cuts.add(c);
        cuts.add(0);
        cuts.add(n);
        Collections.sort(cuts);
        int l = cuts.size();

        int[][] dp = new int[l][l];
        for (int[] row : dp) Arrays.fill(row, -1);

        return helper(cuts, 1, l - 1, dp);
    }

    public int helper(List<Integer> cuts, int i, int j, int[][] dp) {
        if (i == j)
            return 0;
        if (dp[i][j] != -1)
            return dp[i][j];

        int mn = Integer.MAX_VALUE;
        for (int k = i; k < j; k++) {
            int tempAns = helper(cuts, i, k, dp) + helper(cuts, k + 1, j, dp) + cuts.get(j) - cuts.get(i - 1);
            mn = Math.min(mn, tempAns);
        }

        dp[i][j] = mn;
        return dp[i][j];
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    int minCost(int n, vector<int>& cuts) {
        cuts.push_back(0);
        cuts.push_back(n);
        sort(cuts.begin(), cuts.end());
        int l = cuts.size();
        vector<vector<int>> dp(l, vector<int>(l, -1));
        return helper(cuts, 1, l - 1, dp);
    }

    int helper(vector<int>& cuts, int i, int j, vector<vector<int>>& dp) {
        if (i == j)
            return 0;
        if (dp[i][j] != -1)
            return dp[i][j];

        int mn = INT_MAX;
        for (int k = i; k < j; ++k) {
            int tempAns = helper(cuts, i, k, dp) + helper(cuts, k + 1, j, dp) + cuts[j] - cuts[i - 1];
            mn = min(mn, tempAns);
        }

        dp[i][j] = mn;
        return dp[i][j];
    }
};
"""

=======


# Method 3: 
>>>>>>> a40de18 (verified Binary Search and DP)
# Tabulation
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        l= len(cuts)
        dp= [[0 for j in range(l)]for i in range(l)]  # already get initialised with base case 
        for i in range(l-2, 0, -1):   # from last valid one to first valid one
            for j in range(i+1, l):   # for valid one 'j' must be greater than 'i' i.e 'j' should go till 'l-1'
                mn= 9999999999
                for k in range(i, j):
                    tempAns= dp[i][k] + dp[k+1][j] + cuts[j]- cuts[i-1]
                    mn= min(mn, tempAns)
                dp[i][j]= mn
        return dp[1][l-1]

<<<<<<< HEAD

# Java Code 
"""
import java.util.*;

class Solution {
    public int minCost(int n, int[] cutArray) {
        List<Integer> cuts = new ArrayList<>();
        for (int c : cutArray) cuts.add(c);
        cuts.add(0);
        cuts.add(n);
        Collections.sort(cuts);

        int l = cuts.size();
        int[][] dp = new int[l][l];  // already get initialised with base case

        for (int i = l - 2; i > 0; --i) {  // from last valid one to first valid one
            for (int j = i + 1; j < l; ++j) {  // for valid one 'j' must be greater than 'i' i.e 'j' should go till 'l-1'
                int mn = Integer.MAX_VALUE;
                for (int k = i; k < j; ++k) {
                    int tempAns = dp[i][k] + dp[k + 1][j] + cuts.get(j) - cuts.get(i - 1);
                    mn = Math.min(mn, tempAns);
                }
                dp[i][j] = mn;
            }
        }

        return dp[1][l - 1];
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    int minCost(int n, vector<int>& cuts) {
        cuts.push_back(0);
        cuts.push_back(n);
        sort(cuts.begin(), cuts.end());

        int l = cuts.size();
        vector<vector<int>> dp(l, vector<int>(l, 0));  // already get initialised with base case

        for (int i = l - 2; i > 0; --i) {  // from last valid one to first valid one
            for (int j = i + 1; j < l; ++j) {  // for valid one 'j' must be greater than 'i' i.e 'j' should go till 'l-1'
                int mn = INT_MAX;
                for (int k = i; k < j; ++k) {
                    int tempAns = dp[i][k] + dp[k + 1][j] + cuts[j] - cuts[i - 1];
                    mn = min(mn, tempAns);
                }
                dp[i][j] = mn;
            }
        }

        return dp[1][l - 1];
    }
};
"""
=======

>>>>>>> a40de18 (verified Binary Search and DP)
