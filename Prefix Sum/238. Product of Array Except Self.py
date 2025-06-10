# Brute force:
# Just calculate the 'prefix' and 'suffix' multiplication then, 
# ans[i] = prefix[i - 1] * suffix[i + 1]

# Method 2: 
# Optimising space

# we have to do in O(1) space complexity except ans array.
# means we will have to store prefix and suffix into a variable instead of array.

# 1) Traverse from left to right and store the 'prefix' for each ele.
# 2) for 'suffix' traverse right to left.
# time: O(n),space: O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans= [1]*(len(nums))
        # first storing the prefix mutliply for each number in 'ans'
        prefix= 1
        for i in range(len(nums)):
            ans[i]= prefix
            prefix= prefix* nums[i]
        # now calculate the postfix and store the final ans in the 'ans'.
        postfix= 1
        for i in range(len(nums) -1, -1, -1):
            ans[i]= ans[i] * postfix   # ans[i] store the prefix for that index and postfix is storing suffix.
            postfix= postfix * nums[i]
        return ans


# observation:
# 1) if count of '0' will be = 1 then all elements will have value= 0 excecpt the '0'th ele.
# 2) if count of '0' >= 2 then value= 0 for all elements.


# Link: https://leetcode.com/problems/product-of-array-except-self/solutions/1342916/3-minute-read-mimicking-an-interview/
# Java Code
"""
# Method 1:

class Solution {
    /*
    Brute force approach using prefix and suffix arrays:
    - Compute prefix product array storing products from start to `i-1`.
    - Compute suffix product array storing products from `i+1` to end.
    - Final answer is computed as `prefix[i - 1] * suffix[i + 1]`.
    - Time complexity: `O(n)`, Space complexity: `O(n)`.
    */
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] prefix = new int[n];
        int[] suffix = new int[n];
        int[] ans = new int[n];

        prefix[0] = 1;
        suffix[n - 1] = 1;

        // Compute prefix product
        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] * nums[i - 1];
        }

        // Compute suffix product
        for (int i = n - 2; i >= 0; i--) {
            suffix[i] = suffix[i + 1] * nums[i + 1];
        }

        // Compute final result using prefix and suffix arrays
        for (int i = 0; i < n; i++) {
            ans[i] = prefix[i] * suffix[i];
        }

        return ans;
    }
}

# method 2:

class Solution {
    /*
    Optimized approach:
    - Instead of maintaining separate arrays for prefix and suffix, use variables.
    - First pass: Calculate prefix products and store them in `ans`.
    - Second pass: Compute suffix products and update `ans` accordingly.
    - Time complexity: `O(n)`, Space complexity: `O(1)` (excluding output array).
    */
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];

        // Calculate prefix products
        int prefix = 1;
        for (int i = 0; i < n; i++) {
            ans[i] = prefix;
            prefix *= nums[i];
        }

        // Calculate postfix products and finalize the result
        int postfix = 1;
        for (int i = n - 1; i >= 0; i--) {
            ans[i] *= postfix; // `ans[i]` already holds the prefix product
            postfix *= nums[i];
        }

        return ans;
    }
}

"""

# C++ Code 
"""
//Method 1
#include <vector>

using namespace std;

class Solution {
public:
    /*
    Brute force approach using prefix and suffix arrays:
    - Compute prefix product array storing products from start to `i-1`.
    - Compute suffix product array storing products from `i+1` to end.
    - Final answer is computed as `prefix[i - 1] * suffix[i + 1]`.
    - Time complexity: `O(n)`, Space complexity: `O(n)`.
    */
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> prefix(n, 1), suffix(n, 1), ans(n, 1);

        // Compute prefix product
        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] * nums[i - 1];
        }

        // Compute suffix product
        for (int i = n - 2; i >= 0; i--) {
            suffix[i] = suffix[i + 1] * nums[i + 1];
        }

        // Compute final result using prefix and suffix arrays
        for (int i = 0; i < n; i++) {
            ans[i] = prefix[i] * suffix[i];
        }

        return ans;
    }
};
//Method 2
class Solution {
public:
    /*
    Optimized approach:
    - Instead of maintaining separate arrays for prefix and suffix, use variables.
    - First pass: Calculate prefix products and store them in `ans`.
    - Second pass: Compute suffix products and update `ans` accordingly.
    - Time complexity: `O(n)`, Space complexity: `O(1)` (excluding output array).
    */
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n, 1);

        // Calculate prefix products
        int prefix = 1;
        for (int i = 0; i < n; i++) {
            ans[i] = prefix;
            prefix *= nums[i];
        }

        // Calculate postfix products and finalize the result
        int postfix = 1;
        for (int i = n - 1; i >= 0; i--) {
            ans[i] *= postfix; // `ans[i]` already holds the prefix product
            postfix *= nums[i];
        }

        return ans;
    }
};
"""