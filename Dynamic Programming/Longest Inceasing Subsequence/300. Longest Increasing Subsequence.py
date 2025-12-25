# Method 1: 

"""
If we closely observe the problem then we can convert this problem to longest Common Subsequence Problem.
Firstly we will create another array of unique elements of original array and sort it. 
Now the longest increasing subsequence of our array must be present as a subsequence in our sorted array. 
That’s why our problem is now reduced to finding the common subsequence between the two arrays.

Time and Space: O(n^2)

"""

class Solution:
    # Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        a1= sorted(list(set(a)))
        n1= len(a1)
        return self.lcs(a, a1, n, n1)
    def lcs(self, s1, s2, x, y):
        dp= [[0 for j in range(y+1)] for i in range(x+1)]
        for i in range(1,x+1):
            for j in range(1,y+1):
                if s1[i-1]== s2[j-1]:
                    dp[i][j]= 1+ dp[i-1][j-1]
                else:
                    dp[i][j]= max(dp[i-1][j], dp[i][j-1])
        return dp[x][y]

# Java Code 
"""
import java.util.*;

class Solution {
    // Function to find length of longest increasing subsequence
    public int longestSubsequence(int[] a, int n) {
        Set<Integer> set = new TreeSet<>();
        for (int val : a) set.add(val);
        int[] a1 = new int[set.size()];
        int idx = 0;
        for (int val : set) a1[idx++] = val;

        return lcs(a, a1, n, a1.length);
    }

    private int lcs(int[] s1, int[] s2, int x, int y) {
        int[][] dp = new int[x + 1][y + 1];
        for (int i = 1; i <= x; i++) {
            for (int j = 1; j <= y; j++) {
                if (s1[i - 1] == s2[j - 1]) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[x][y];
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

class Solution {
public:
    // Function to find length of longest increasing subsequence
    int longestSubsequence(int a[], int n) {
        set<int> s(a, a + n);
        vector<int> a1(s.begin(), s.end());

        return lcs(a, a1, n, a1.size());
    }

private:
    int lcs(int s1[], const vector<int>& s2, int x, int y) {
        vector<vector<int>> dp(x + 1, vector<int>(y + 1, 0));
        for (int i = 1; i <= x; ++i) {
            for (int j = 1; j <= y; ++j) {
                if (s1[i - 1] == s2[j - 1]) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[x][y];
    }
};
"""

# method 2: 
# Better one
"""
Note vvvi: This is better one template in case of 'take' and 'notTake'  which there is 'notTake' option always there.
So just find the condition for 'take' and return the max(take, notTake)

How?
There is no need to check the possibility of 'taking' and 'not taking' in possible case.
There is always one choice to 'not take' and we can only take if follows the sequence.

in case of pick and non_pick always write the pick case and non_pick case separately 
if there are some condition involved before including or not_including any ele.

time: O(2^n)
space: O(n)
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.helper(0, -1, nums)
    def helper(self, ind, pre_ind, arr):
        if ind== len(arr):
            return 0
        take= 0
        notTake= self.helper(ind +1, pre_ind, arr)  # if we not include
        # when we include but we can only include in following condition only.
        if pre_ind== -1 or arr[ind] > arr[pre_ind]:  # when can only include if strictly increasing
            take= 1+ self.helper(ind +1, ind, arr)
        return max(take, notTake)


# Java Code 
"""
class Solution {
    public int lengthOfLIS(int[] nums) {
        return helper(0, -1, nums);
    }

    private int helper(int ind, int preInd, int[] arr) {
        if (ind == arr.length)
            return 0;

        int take = 0;
        int notTake = helper(ind + 1, preInd, arr);  // if we not include

        // when we include but we can only include in following condition only
        if (preInd == -1 || arr[ind] > arr[preInd])  // can only include if strictly increasing
            take = 1 + helper(ind + 1, ind, arr);

        return Math.max(take, notTake);
    }
}
"""
# C++ Code 
"""
#include <vector>
using namespace std;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        return helper(0, -1, nums);
    }

private:
    int helper(int ind, int preInd, const vector<int>& arr) {
        if (ind == arr.size())
            return 0;

        int take = 0;
        int notTake = helper(ind + 1, preInd, arr);  // if we not include

        // when we include but we can only include in following condition only
        if (preInd == -1 || arr[ind] > arr[preInd])  // can only include if strictly increasing
            take = 1 + helper(ind + 1, ind, arr);

        return max(take, notTake);
    }
};
"""
# Method 3:
# memoizing the above method
# for matrix: we can't store -1 as pre_ind so we will do co-ordinate shift by +1 for pre_ind i.e for -1 we will write 0 and so on
# so in this range of pre_ind will be from [0, n] instead of '-1' to   and range of 'ind' from '0' to 'n-1'

# submitted on gfg but giving TLE on leetcode. have to ask someone
class Solution:
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        dp= [[-1 for j in range(n+1)] for i in range(n +1)]   # dp[i][j] denotes max LIS starting from i when 'j' is the index of previous picked element.
        return self.helper(0, -1, a, dp)
    def helper(self, ind, pre_ind, arr, dp):
        if ind== len(arr):
            return 0
        if dp[ind][pre_ind +1]!= -1:
            return dp[ind][pre_ind+1]
        take= 0
        notTake= self.helper(ind +1, pre_ind, arr, dp)
        if pre_ind== -1 or arr[ind] > arr[pre_ind]:
            take= 1+ self.helper(ind +1, ind, arr, dp)
        dp[ind][pre_ind+1]= max(take, notTake)
        return dp[ind][pre_ind+1]

# Java Code 
"""
class Solution {
    // Function to find length of longest increasing subsequence
    public int longestSubsequence(int n, int[] a) {
        int[][] dp = new int[n + 1][n + 1]; // dp[i][j] denotes max LIS starting from i when 'j-1' is the index of previous picked element
        for (int i = 0; i <= n; i++) {
            java.util.Arrays.fill(dp[i], -1);
        }
        return helper(0, -1, a, dp);
    }

    private int helper(int ind, int preInd, int[] arr, int[][] dp) {
        if (ind == arr.length) return 0;

        if (dp[ind][preInd + 1] != -1) return dp[ind][preInd + 1];

        int notTake = helper(ind + 1, preInd, arr, dp);
        int take = 0;

        if (preInd == -1 || arr[ind] > arr[preInd]) {
            take = 1 + helper(ind + 1, ind, arr, dp);
        }

        dp[ind][preInd + 1] = Math.max(take, notTake);
        return dp[ind][preInd + 1];
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
    // Function to find length of longest increasing subsequence
    int longestSubsequence(int n, int a[]) {
        vector<vector<int>> dp(n + 1, vector<int>(n + 1, -1)); // dp[i][j] denotes max LIS starting from i when 'j-1' is the index of previous picked element
        return helper(0, -1, a, n, dp);
    }

private:
    int helper(int ind, int preInd, int a[], int n, vector<vector<int>>& dp) {
        if (ind == n) return 0;

        if (dp[ind][preInd + 1] != -1) return dp[ind][preInd + 1];

        int notTake = helper(ind + 1, preInd, a, n, dp);
        int take = 0;

        if (preInd == -1 || a[ind] > a[preInd]) {
            take = 1 + helper(ind + 1, ind, a, n, dp);
        }

        return dp[ind][preInd + 1] = max(take, notTake);
    }
};
"""

# Method 4: 
"""
converting to Tabulation VVI: Top down 
little twist here: different from general pattern.
Rules: 1) write the base case
2) convert the indices into for loop by seeing the starting and ending point of indices.
Here 'ind' will go from 'n-1' to '0'. 
And 'pre_ind' will go from 'n-1' to '-1' but it can't be equal to ind , it will be always less than the 'ind'..So it will from 'ind-1' to '-1'.
3) copy paste the recurrence do coordinate shift of '1' in case of 'pre_ind'. That's it.
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n= len(nums)
        dp= [[0 for j in range(n+1)] for i in range(n +1)]   
        for ind in range(n-1, -1, -1):
            for pre_ind in range(ind -1, -2, -1):
                take= 0
                notTake= dp[ind +1][pre_ind +1]
                if pre_ind== -1 or nums[ind] > nums[pre_ind]:
                    take= 1+ dp[ind+ 1][ind +1]
                dp[ind][pre_ind +1]= max(take, notTake)
        return dp[0][0]   # return the dp for which you had called the recursive function. 
    

# Java Code 
"""
class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int[][] dp = new int[n + 1][n + 1]; 

        for (int ind = n - 1; ind >= 0; ind--) {
            for (int preInd = ind - 1; preInd >= -1; preInd--) {
                int take = 0;
                int notTake = dp[ind + 1][preInd + 1];

                if (preInd == -1 || nums[ind] > nums[preInd]) {
                    take = 1 + dp[ind + 1][ind + 1];
                }

                dp[ind][preInd + 1] = Math.max(take, notTake);
            }
        }

        return dp[0][0];  // return the dp for which you had called the recursive function
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
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));

        for (int ind = n - 1; ind >= 0; --ind) {
            for (int preInd = ind - 1; preInd >= -1; --preInd) {
                int take = 0;
                int notTake = dp[ind + 1][preInd + 1];

                if (preInd == -1 || nums[ind] > nums[preInd]) {
                    take = 1 + dp[ind + 1][ind + 1];
                }

                dp[ind][preInd + 1] = max(take, notTake);
            }
        }

        return dp[0][0];  // return the dp for which you had called the recursive function
    }
};
"""


# Method 5:
# very better one    
"""
logic: traverse the array from right to left . just the conversion of above logic and optimising the space to O(n).
e.g: LIS[2] means nums[2] will get appened(+1) to any of the LIS ahead of it,
(i.e if all the ele of of any of the LIS will be grater than nums[2] then we will add +1).     
time: O(n^2)    
"""                                               
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS= [1]* len(nums)   # LIS[i] indicates that LIS that end at index 'i' from last
                                #  for each index at least ele at curr index will be get included so initialised with '1'
        for i in range(len(nums)-1, -1, -1):
            # for 'i'th index we have to merge this ele with any of the ans(LIS) after it. so we will check for all ele after this.
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]: # checking whether this ele at 'j' can get added to LIS at 'i'.
                    LIS[i]= max(LIS[i], 1+ LIS[j])  # Have to take max of all LIS ahead of it.
        # at last return the maximum in LIS
        return max(LIS)

# Java Code 
"""
class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] LIS = new int[nums.length];  // LIS[i] indicates that LIS that end at index 'i' from last
                                           // for each index at least ele at curr index will be get included so initialised with '1'
        Arrays.fill(LIS, 1);

        for (int i = nums.length - 1; i >= 0; i--) {
            // for 'i'th index we have to merge this ele with any of the ans(LIS) after it. so we will check for all ele after this.
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[j] > nums[i]) { // checking whether this ele at 'j' can get added to LIS at 'i'.
                    LIS[i] = Math.max(LIS[i], 1 + LIS[j]);  // Have to take max of all LIS ahead of it.
                }
            }
        }

        // at last return the maximum in LIS
        int max = 0;
        for (int len : LIS) {
            max = Math.max(max, len);
        }
        return max;
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
    int lengthOfLIS(vector<int>& nums) {
        vector<int> LIS(nums.size(), 1);  // LIS[i] indicates that LIS that end at index 'i' from last
                                          // for each index at least ele at curr index will be get included so initialised with '1'
        
        for (int i = nums.size() - 1; i >= 0; i--) {
            // for 'i'th index we have to merge this ele with any of the ans(LIS) after it. so we will check for all ele after this.
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[j] > nums[i]) { // checking whether this ele at 'j' can get added to LIS at 'i'.
                    LIS[i] = max(LIS[i], 1 + LIS[j]);  // Have to take max of all LIS ahead of it.
                }
            }
        }

        // at last return the maximum in LIS
        return *max_element(LIS.begin(), LIS.end());
    }
};
"""

# Method 6: 
"""
if you traverse from starting left to right
write this logic in notes with printing the LIS, counting the number of LIS in detail
for every ele, we have two choices either include that into 'subse' or not include to the pre_answers.
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS= [1]* len(nums)   # LIS[i] indicates that LIS that end at index 'i' from start. 
        for i in range(len(nums)):  # calculating for each index one by one
            for j in range(i):     # take the values from all the pre index till now 
                if nums[j] < nums[i]: # include the element. # checking whether this ele at 'j' can get added to LIS at 'i'.
                    LIS[i]= max(LIS[i], 1+ LIS[j])   # if follows the rule then incr the LIS by one 
        return max(LIS)
# Java Code 
"""
class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] LIS = new int[nums.length];  // LIS[i] indicates that LIS that end at index 'i' from start.
                                           // for each index at least ele at curr index will be get included so initialised with '1'
        Arrays.fill(LIS, 1);

        for (int i = 0; i < nums.length; i++) {  // calculating for each index one by one
            for (int j = 0; j < i; j++) {        // take the values from all the pre index till now
                if (nums[j] < nums[i]) {         // include the element. # checking whether this ele at 'j' can get added to LIS at 'i'.
                    LIS[i] = Math.max(LIS[i], 1 + LIS[j]);  // if follows the rule then incr the LIS by one
                }
            }
        }

        int max = 0;
        for (int len : LIS) {
            max = Math.max(max, len);
        }
        return max;
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
    int lengthOfLIS(vector<int>& nums) {
        vector<int> LIS(nums.size(), 1);  // LIS[i] indicates that LIS that end at index 'i' from start.
                                          // for each index at least ele at curr index will be get included so initialised with '1'

        for (int i = 0; i < nums.size(); i++) {  // calculating for each index one by one
            for (int j = 0; j < i; j++) {        // take the values from all the pre index till now
                if (nums[j] < nums[i]) {         // include the element. # checking whether this ele at 'j' can get added to LIS at 'i'.
                    LIS[i] = max(LIS[i], 1 + LIS[j]);  // if follows the rule then incr the LIS by one
                }
            }
        }

        return *max_element(LIS.begin(), LIS.end());
    }
};
"""

# method 7:

"""
best one: using binary search to find the proper position of curr index in case not follows the pattern 
and removing the curr ele at that index in 'subsequence'.

How Binary search?
Since LIS will be in strictly sorted order only.
if cur ele follows the sequence i.e > pre added one then, we will add this directly i.e
If 'num' is bigger than last ele of sub, we just extend our list 
Otherwise, we will simply apply binary search to find the smallest element >= num and replace it.

why this logic is giving correct ans?
Ans: Replace karenge tb length to wahi rhega but smaller ele se replace karne pe next ele ka append hone ka chance increase kar jayega.
kyonki chota se replace kar rhe. e.g: [2, 8] next ele is '3'. 
after replacing => [2,3] ab agar next elements '3' se large hua to append kar denge directly,
 but agar [2,8] hota tb sirf '8' se bda wale ko hi append kar pate. 
Append kitna jayda ho rha last me wahi mera length ko increase karega..

Note: if we will use 'bisect_right' then we get duplicates also if 'num' is already  in 'sub' so using 'bisect_left'
 since we need to replace with smallest ele in sub >= num.
If we use 'bisect_right' then, it will replace with next greater ele than 'num', so we may get duplicate like pre and num will be same only.

Note vvi: 'sub' will give one of the 'LIS' .

time: O(n*logn)
space: O(n)

bisect function: https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
"""

import bisect
class Solution:  
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub= []  # will store the ele in strictly increasing order only.
        for num in nums:
            if not sub or sub[-1] < num:
                # if following the pattern.
                sub.append(num)
            else: # find the position of num in sub and replace that ind with num
                idx= bisect.bisect_left(sub, num)  # simply bisect_left(sub,num). 
                sub[idx]= num  # no need to check if idx >= len(sub) because if like this then must be greatest of all and this case is already covered above.
        return len(sub)
    

# Java Code 
"""
import java.util.*;

class Solution {
    public int lengthOfLIS(int[] nums) {
        List<Integer> sub = new ArrayList<>();  // will store the ele in strictly increasing order only

        for (int num : nums) {
            if (sub.isEmpty() || sub.get(sub.size() - 1) < num) {
                // if following the pattern
                sub.add(num);
            } else {
                // find the position of num in sub and replace that ind with num
                int idx = Collections.binarySearch(sub, num);
                if (idx < 0) idx = -idx - 1;  // equivalent to bisect_left
                sub.set(idx, num);  // no need to check if idx >= len(sub) because that case is already covered above
            }
        }

        return sub.size();
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
    int lengthOfLIS(vector<int>& nums) {
        vector<int> sub;  // will store the ele in strictly increasing order only

        for (int num : nums) {
            if (sub.empty() || sub.back() < num) {
                // if following the pattern
                sub.push_back(num);
            } else {
                // find the position of num in sub and replace that ind with num
                auto it = lower_bound(sub.begin(), sub.end(), num);  // equivalent to bisect_left
                *it = num;  // no need to check if it == sub.end() because that case is already covered above
            }
        }

        return sub.size();
    }
};
"""


# upload on website till method 7 only

# Note: when trying to do by "1235. Maximum Profit in Job Scheduling".
# And same q of this method is not working in '1235. Maximum Profit in Job Scheduling'.

# I am getting error . Have to ask someone
# nums = [4,10,4,3,8,9] , getting : 4 but exp = 3

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def solve(i):
            if i >= len(nums):
                return 0
            j = i + 1
            while j < len(nums):
                if nums[j] > nums[i]:
                    break
                j += 1
            return max(solve(i + 1), 1 + solve(j))
        
        return solve(0)


# Java Code 
"""
class Solution {
    public int lengthOfLIS(int[] nums) {
        return solve(0, nums);
    }

    private int solve(int i, int[] nums) {
        if (i >= nums.length)
            return 0;

        int j = i + 1;
        while (j < nums.length) {
            if (nums[j] > nums[i])
                break;
            j++;
        }

        return Math.max(solve(i + 1, nums), 1 + solve(j, nums));
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
    int lengthOfLIS(vector<int>& nums) {
        return solve(0, nums);
    }

private:
    int solve(int i, const vector<int>& nums) {
        if (i >= nums.size())
            return 0;

        int j = i + 1;
        while (j < nums.size()) {
            if (nums[j] > nums[i])
                break;
            j++;
        }

        return max(solve(i + 1, nums), 1 + solve(j, nums));
    }
};
"""

# Related QUestions:
"""
1) Printing LIS
2) 673. Number of Longest Increasing Subsequence
3) 1027. Longest Arithmetic Subsequence
4) 368. Largest Divisible Subset
5) 1048. Longest String Chain
6) Longest Bitonic Subsequence
"""
