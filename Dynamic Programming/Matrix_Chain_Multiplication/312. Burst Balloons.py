# method 1: 

# vvi: my mistake and analysation of mistake.
# i was trying do bring into same format as MCM but it will give error.
# reason: [1,5,8,1]  # after adding '1' at first and last. suppose we divide at k= 2 then in left part (1,1) and right (3,3).
# and left part will return here '0' but in actual '5' should have multiplied with '8'. sinc '8' will burst afetr '5' only.
# That's why got error.

# when we have include the ele like this which are not in the curr index then start from last valid index (for j) and in base case i>j.
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0,1)  # to get the left of  first balloons
        nums.append(1)    # to get the right of last  balloons
        n= len(nums)
        i, j= 1, n-1  # j is passed as last valid so if i==j then still we have to call the rec fn. now both the end is valid
        return self.helper(nums, i, j)
    
    def helper(self, nums, i , j):
        if i >= j:  # since 'j' was last valid instead of first invalid so base case will change like this(go one step further)
            return 0
        mx= -9999999999
        for k in range(i, j):  # 'j' in inclusive now(last valid)
            tempAns= self.helper(nums, i, k-1) + self.helper(nums, k+1, j) + nums[i-1]*nums[k]*nums[j]
            mx= max(mx, tempAns)
        return mx

<<<<<<< HEAD
# Java Code 
"""
class Solution {
    public int maxCoins(int[] nums) {
        List<Integer> list = new ArrayList<>();
        list.add(1);  // to get the left of first balloons
        for (int num : nums) list.add(num);
        list.add(1);  // to get the right of last balloons
        int n = list.size();
        int i = 1, j = n - 1;
        return helper(list, i, j);
    }

    private int helper(List<Integer> nums, int i, int j) {
        if (i == j)
            return 0;
        int mn = Integer.MIN_VALUE;
        for (int k = i; k < j; k++) {
            int tempAns = helper(nums, i, k) + helper(nums, k + 1, j) + nums.get(i - 1) * nums.get(k) * nums.get(j);
            mn = Math.max(mn, tempAns);
        }
        return mn;
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
    int maxCoins(vector<int>& nums) {
        nums.insert(nums.begin(), 1);  // to get the left of first balloons
        nums.push_back(1);            // to get the right of last balloons
        int n = nums.size();
        int i = 1, j = n - 1;
        return helper(nums, i, j);
    }

    int helper(vector<int>& nums, int i, int j) {
        if (i == j)
            return 0;
        int mn = INT_MIN;
        for (int k = i; k < j; ++k) {
            int tempAns = helper(nums, i, k) + helper(nums, k + 1, j) + nums[i - 1] * nums[k] * nums[j];
            mn = max(mn, tempAns);
        }
        return mn;
    }
};
"""

# method 1: 
=======

# Correct way 
>>>>>>> a40de18 (verified Binary Search and DP)
# logic: we have to divide the subproblem in such a way that both are independent to each other.
# by dividing like above, subproblem becomes dependent on each other to find the next left and right balloons which has not been burst yet.
# so to aolve that we will do by Bottom Up Approach. 

# main part: the kth picked balloon we will burst at last so that it's left and right balloons can get this 'k' easily.
# so when they will return the value, the next uburst left and right of 'kth' balloon will be 'i-1' and 'j+1' as all from 'i' to 'j' will get burst except 'k' in bottom up.
# so cost of bursting kth balloon will be : nums[i-1]*nums[k]*nums[j+1].
# vvi: After dividing the problem at 'k', nums[k] will get multiplied in both the parts i.e for left one  as 'j+1' and for right one 'i-1' .
# Do this on pen and paper or read the explanation in the link(sheet). 
# logically also it shoule be get multiplied to both onl;y since it is adjacent to both and we are bursting this at last only.

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0,1)  # to get the left of  first balloons
        nums.append(1)    # to get the right of last  balloons
        n= len(nums)
        i, j= 1, n-2  # j is passed as last valid so if i==j then still we have to call the rec fn. now both the end is valid
        return self.helper(nums, i, j)
    
    def helper(self, nums, i , j):
        if i> j:  # since 'j' was last valid instead of first invalid so base case will change like this(go one step further)
            return 0
        mx= -9999999999
        for k in range(i, j+1):  # 'j' in inclusive now(last valid)
            tempAns= self.helper(nums, i, k-1) + self.helper(nums, k+1, j) + nums[i-1]*nums[k]*nums[j+1]
            mx= max(mx, tempAns)
        return mx

<<<<<<< HEAD
# Java Code 
"""
class Solution {
    public int maxCoins(int[] arr) {
        List<Integer> nums = new ArrayList<>();
        nums.add(1);  // to get the left of first balloons
        for (int val : arr) nums.add(val);
        nums.add(1);  // to get the right of last balloons

        int n = nums.size();
        int i = 1, j = n - 2;  // j is passed as last valid so if i==j then still we have to call the rec fn. now both the end is valid
        return helper(nums, i, j);
    }

    public int helper(List<Integer> nums, int i, int j) {
        if (i > j)  // since 'j' was last valid instead of first invalid so base case will change like this(go one step further)
            return 0;
        int mx = Integer.MIN_VALUE;
        for (int k = i; k <= j; ++k) {  // 'j' is inclusive now (last valid)
            int tempAns = helper(nums, i, k - 1) + helper(nums, k + 1, j) + nums.get(i - 1) * nums.get(k) * nums.get(j + 1);
            mx = Math.max(mx, tempAns);
        }
        return mx;
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
    int maxCoins(vector<int>& arr) {
        vector<int> nums;
        nums.push_back(1);  // to get the left of first balloons
        nums.insert(nums.end(), arr.begin(), arr.end());
        nums.push_back(1);  // to get the right of last balloons

        int n = nums.size();
        int i = 1, j = n - 2;  // j is passed as last valid so if i==j then still we have to call the rec fn. now both the end is valid
        return helper(nums, i, j);
    }

    int helper(vector<int>& nums, int i, int j) {
        if (i > j)  // since 'j' was last valid instead of first invalid so base case will change like this(go one step further)
            return 0;

        int mx = INT_MIN;
        for (int k = i; k <= j; ++k) {  // 'j' is inclusive now (last valid)
            int tempAns = helper(nums, i, k - 1) + helper(nums, k + 1, j) + nums[i - 1] * nums[k] * nums[j + 1];
            mx = max(mx, tempAns);
        }
        return mx;
    }
};
"""
=======

# Method 2: 
>>>>>>> a40de18 (verified Binary Search and DP)
# memoization:
# for dp size: 1) range of i: 'i' can go from 1 to 'n-1'(invalid one. jb 'i' , 'j' se bda hoga: base case). size= 'n-1'
# but 'k' is going till 'i+1'(till n). so finally size of 'i' should be 'n'(1 to n).
 
# 2) range of 'j': 'j' can go from 'n-2' to '0'(invalid one. jb 'j' , 'i' se chota hoga: base case), so size= 'n-1'.
# but 'k' is going to 'j-1'(to n-1 also). so finally size of 'j' should be 'n'(n-1 to 0).

# for memoization: 'n-1'*'n-1' will also work but will give error(out of index) in Tabulation.

# for bda and chota value of 'i' and 'j' (invalid one), see the value by which we made the first function call.
# time: O(n^3)

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0,1)  # to get the left of  first balloons
        nums.append(1)    # to get the right of last  balloons
        n= len(nums)
        dp= [[-1 for j in range(n-1)] for i in range(n-1)]
        i, j= 1, n-2  # j is passed as last valid so if i==j then still we have to call the rec fn. now both the end is valid
        return self.helper(nums, i, j, dp)
    
    def helper(self, nums, i , j, dp):
        if i> j:  # since 'j' was last valid instead of first invalid so base case will change like this(go one step further)
            return 0
        if dp[i][j]!= -1:
            return dp[i][j]
        mx= -9999999999
        for k in range(i, j+1):  # 'j' in inclusive now(last valid)
            tempAns= self.helper(nums, i, k-1, dp) + self.helper(nums, k+1, j, dp) + nums[i-1]*nums[k]*nums[j+1]
            mx= max(mx, tempAns)
            dp[i][j]= mx
        return dp[i][j]

<<<<<<< HEAD
# Java Code 
"""
class Solution {
    public int maxCoins(int[] arr) {
        int n = arr.length + 2;
        int[] nums = new int[n];
        nums[0] = 1;  // to get the left of first balloons
        nums[n - 1] = 1;  // to get the right of last balloons
        for (int i = 0; i < arr.length; i++) {
            nums[i + 1] = arr[i];
        }

        int[][] dp = new int[n - 1][n - 1];
        for (int i = 0; i < n - 1; i++)
            for (int j = 0; j < n - 1; j++)
                dp[i][j] = -1;

        return helper(nums, 1, n - 2, dp);  // j is passed as last valid so if i==j then still we have to call the rec fn. now both the end is valid
    }

    private int helper(int[] nums, int i, int j, int[][] dp) {
        if (i > j)  // since 'j' was last valid instead of first invalid so base case will change like this(go one step further)
            return 0;
        if (dp[i][j] != -1)
            return dp[i][j];
        int mx = Integer.MIN_VALUE;
        for (int k = i; k <= j; k++) {  // 'j' is inclusive now(last valid)
            int temp = helper(nums, i, k - 1, dp) + helper(nums, k + 1, j, dp) + nums[i - 1] * nums[k] * nums[j + 1];
            mx = Math.max(mx, temp);
            dp[i][j] = mx;
        }
        return dp[i][j];
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
    int maxCoins(vector<int>& arr) {
        int n = arr.size() + 2;
        vector<int> nums(n);
        nums[0] = 1;  // to get the left of first balloons
        nums[n - 1] = 1;  // to get the right of last balloons
        for (int i = 0; i < arr.size(); ++i) {
            nums[i + 1] = arr[i];
        }

        vector<vector<int>> dp(n - 1, vector<int>(n - 1, -1));
        return helper(nums, 1, n - 2, dp);  // j is passed as last valid so if i==j then still we have to call the rec fn. now both the end is valid
    }

private:
    int helper(vector<int>& nums, int i, int j, vector<vector<int>>& dp) {
        if (i > j)  // since 'j' was last valid instead of first invalid so base case will change like this(go one step further)
            return 0;
        if (dp[i][j] != -1)
            return dp[i][j];
        int mx = INT_MIN;
        for (int k = i; k <= j; ++k) {  // 'j' is inclusive now(last valid)
            int temp = helper(nums, i, k - 1, dp) + helper(nums, k + 1, j, dp) + nums[i - 1] * nums[k] * nums[j + 1];
            mx = max(mx, temp);
            dp[i][j] = mx;
        }
        return dp[i][j];
    }
};
"""
# Tabulation: Analyse properly
=======


# Method 3:
# Tabulation
# time: O(n^3)
>>>>>>> a40de18 (verified Binary Search and DP)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)  # to get the left of first balloons
        nums.append(1)     # to get the right of last balloons
        n = len(nums)
        dp = [[0 for j in range(n)] for i in range(n)]  # n x n table, because we use i-1 and j+1
        
        for i in range(n-2, 0, -1):  # i starts from second last valid to 1
            for j in range(i, n-1):  # j is passed as last valid so j >= i
                mx = -9999999999
                for k in range(i, j+1):  # 'j' is inclusive now (last valid)
                    tempAns = dp[i][k-1] + dp[k+1][j] + nums[i-1] * nums[k] * nums[j+1]
                    mx = max(mx, tempAns)
                dp[i][j] = mx
        
        i, j = 1, n - 2  # 'i' is first valid, 'j' is last valid
        return dp[i][j]


<<<<<<< HEAD

# vvi: my mistake and analysation of mistake.
# i was trying do bring into same format as MCM but it will give error.
# reason: [1,5,8,1]  # after adding '1' at first and last. suppose we divide at k= 2 then in left part (1,1) and right (3,3).
# and left part will return here '0' but in actual '5' should have multiplied with '8'. sinc '8' will burst afetr '5' only.
# That's why got error.

# when we have include the ele like this which are not in the curr index then start from last valid index (for j) and in base case i>j.
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0,1)  # to get the left of  first balloons
        nums.append(1)    # to get the right of last  balloons
        n= len(nums)
        i, j= 1, n-1  # j is passed as last valid so if i==j then still we have to call the rec fn. now both the end is valid
        return self.helper(nums, i, j)
    
    def helper(self, nums, i , j):
        if i>=j:  # since 'j' was last valid instead of first invalid so base case will change like this(go one step further)
            return 0
        mx= -9999999999
        for k in range(i, j):  # 'j' in inclusive now(last valid)
            tempAns= self.helper(nums, i, k-1) + self.helper(nums, k+1, j) + nums[i-1]*nums[k]*nums[j]
            # print(tempAns, k, i, j)
            mx= max(mx, tempAns)
        return mx


# Java Code 
"""
class Solution {
    public int maxCoins(int[] arr) {
        int n = arr.length + 2;
        int[] nums = new int[n];
        nums[0] = 1;                       // to get the left of first balloon
        nums[n - 1] = 1;                   // to get the right of last balloon
        for (int i = 0; i < arr.length; i++) {
            nums[i + 1] = arr[i];
        }

        int[][] dp = new int[n][n];

        // from last valid one to first valid one
        for (int i = n - 2; i >= 1; i--) {
            // for valid one, 'j' should be >= 'i'
            for (int j = i; j <= n - 2; j++) {
                int max = Integer.MIN_VALUE;
                for (int k = i; k <= j; k++) {  // 'j' is inclusive now (last valid)
                    int temp = dp[i][k - 1] + dp[k + 1][j] + nums[i - 1] * nums[k] * nums[j + 1];
                    max = Math.max(max, temp);
                }
                dp[i][j] = max;
            }
        }

        return dp[1][n - 2];
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
    int maxCoins(vector<int>& arr) {
        int n = arr.size() + 2;
        vector<int> nums(n);
        nums[0] = 1;                  // to get the left of first balloon
        nums[n - 1] = 1;              // to get the right of last balloon
        for (int i = 0; i < arr.size(); ++i)
            nums[i + 1] = arr[i];

        vector<vector<int>> dp(n, vector<int>(n, 0));

        // from last valid one to first valid one
        for (int i = n - 2; i >= 1; --i) {
            // for valid one, 'j' should be >= 'i'
            for (int j = i; j <= n - 2; ++j) {
                int mx = INT_MIN;
                for (int k = i; k <= j; ++k) {  // 'j' is inclusive now (last valid)
                    int temp = dp[i][k - 1] + dp[k + 1][j] + nums[i - 1] * nums[k] * nums[j + 1];
                    mx = max(mx, temp);
                }
                dp[i][j] = mx;
            }
        }

        return dp[1][n - 2];
    }
};
"""
=======
>>>>>>> a40de18 (verified Binary Search and DP)
