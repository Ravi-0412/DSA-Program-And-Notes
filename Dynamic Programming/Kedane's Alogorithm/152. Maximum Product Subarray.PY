# thought a lot but didn't come up by myself.


# Think: How you will tackle cases like: [1, -3, -6, -8], [1, -3, -6, -8 10], [-1, 8], [8, -1]

# logic: negative no is making problem like if product till now is min but 
# next time it can become the ans if next ele will be negative.
# that's why maintaining two variable to store the curr_max and curr_min till now.

# Logic: At every number ,update curMax and curMin a/c all possiblity we can have.
# Then update the ans a/c curMax.

# Time = O(n)
# space = O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans= float('-inf')
        curr_max, curr_min= 1, 1  # for multiplication '1' won't effect the ans
        # we will update ans a/c current maximum only
        for n in nums:
            temp= curr_max*n  # will use this to update cur_min.
            # for curr_max: 1) n is +ve and curr_max is +ve 2) n is -ve and curr_min is -ve 
            # 3) for input like: [-1, 8] => we have to take curNum = 8 only
            curr_max= max(n* curr_max, n*curr_min, n)
            # for curr_min: 1) n is -ve and curr_max is +ve 2) n is +ve and curr_min is -ve 3) for input like: [1, -8], we have to take '-8' only
            curr_min= min(temp, n*curr_min, n)   # just same as cur_max only
            ans= max(ans, curr_max)
        return ans

# Java Code 
"""
class Solution {
    public int maxProduct(int[] nums) {
        int ans = Integer.MIN_VALUE;
        int currMax = 1, currMin = 1;  // for multiplication '1' won't affect the ans

        // we will update ans a/c current maximum only
        for (int n : nums) {
            int temp = currMax * n;  // will use this to update curr_min

            // for currMax:
            // 1) n is +ve and currMax is +ve
            // 2) n is -ve and currMin is -ve
            // 3) for input like: [-1, 8] => we have to take curNum = 8 only
            currMax = Math.max(Math.max(n * currMax, n * currMin), n);

            // for currMin:
            // 1) n is -ve and currMax is +ve
            // 2) n is +ve and currMin is -ve
            // 3) for input like: [1, -8], we have to take '-8' only
            currMin = Math.min(Math.min(temp, n * currMin), n);  // just same as currMax only

            ans = Math.max(ans, currMax);
        }

        return ans;
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
    int maxProduct(vector<int>& nums) {
        int ans = INT_MIN;
        int currMax = 1, currMin = 1;  // for multiplication '1' won't affect the ans

        // we will update ans a/c current maximum only
        for (int n : nums) {
            int temp = currMax * n;  // will use this to update curr_min

            // for currMax:
            // 1) n is +ve and currMax is +ve
            // 2) n is -ve and currMin is -ve
            // 3) for input like: [-1, 8] => we have to take curNum = 8 only
            currMax = max({n * currMax, n * currMin, n});

            // for currMin:
            // 1) n is -ve and currMax is +ve
            // 2) n is +ve and currMin is -ve
            // 3) for input like: [1, -8], we have to take '-8' only
            currMin = min({temp, n * currMin, n});  // just same as currMax only

            ans = max(ans, currMax);
        }

        return ans;
    }
};
"""
