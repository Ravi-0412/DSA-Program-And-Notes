# was easy only but thought to the point
# logic: since first and last ele are neighbour so both can't be the part of ans simultaneously.
# i.e ans will be condition only one of them 
# so ans will equal to the max(when we don't rob the first house, when we don't rob the last house).

class Solution:
    def rob(self, nums: List[int]) -> int:
        n= len(nums)
        if n== 1:
            return nums[0]
        ans_excluding_last=  self.helper(nums[: n-1])
        ans_excluding_first= self.helper(nums[1: ])
        return max(ans_excluding_last, ans_excluding_first)
        
    def helper(self, nums):
        n= len(nums)
        non_adj= 0  # intially it will be zero. 
        adj= nums[0]  # initially it will be nums[0]. 
        ans= nums[0]  # in case only one ele is present and also this will be the minimum profit
        for i in range(2,n+1):
            ans= max(ans, nums[i-1]+ non_adj, adj)   # when you rob the current house or when you rob the next house
            # update adj and non_adj.
            adj, non_adj= ans, adj
        return ans

# Java Code 
"""
public class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1)
            return nums[0];

        int ansExcludingLast = helper(java.util.Arrays.copyOfRange(nums, 0, n - 1));
        int ansExcludingFirst = helper(java.util.Arrays.copyOfRange(nums, 1, n));
        return Math.max(ansExcludingLast, ansExcludingFirst);
    }

    private int helper(int[] nums) {
        int n = nums.length;
        int nonAdj = 0;       // initially it will be zero.
        int adj = nums[0];    // initially it will be nums[0].
        int ans = nums[0];    // in case only one ele is present and also this will be the minimum profit

        for (int i = 2; i <= n; i++) {
            ans = Math.max(ans, nums[i - 1] + nonAdj);  // when you rob the current house
            ans = Math.max(ans, adj);                   // or when you rob the next house

            // update adj and non_adj.
            int temp = adj;
            adj = ans;
            nonAdj = temp;
        }
        return ans;
    }
}
"""

# C++ Code 
"""
class Solution {
public:
    int rob(std::vector<int>& nums) {
        int n = nums.size();
        if (n == 1)
            return nums[0];

        std::vector<int> first(nums.begin(), nums.end() - 1);
        std::vector<int> second(nums.begin() + 1, nums.end());

        int ansExcludingLast = helper(first);
        int ansExcludingFirst = helper(second);
        return std::max(ansExcludingLast, ansExcludingFirst);
    }

private:
    int helper(const std::vector<int>& nums) {
        int n = nums.size();
        int nonAdj = 0;        // initially it will be zero.
        int adj = nums[0];     // initially it will be nums[0].
        int ans = nums[0];     // in case only one ele is present and also this will be the minimum profit

        for (int i = 2; i <= n; ++i) {
            ans = std::max(ans, nums[i - 1] + nonAdj);  // when you rob the current house
            ans = std::max(ans, adj);                   // or when you rob the next house

            // update adj and non_adj.
            int temp = adj;
            adj = ans;
            nonAdj = temp;
        }
        return ans;
    }
};
"""

# Method 3:
# logic : Just same approach as method 1, jst doing in single function call using Tabulation with space optimised to O(1)

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        # Case A: exclude last house
        prevA = currA = 0
        
        # Case B: exclude first house
        prevB = currB = 0

        for i in range(n):
            # Update Case A only if last house is excluded
            if i < n - 1:
                prevA, currA = currA, max(currA, prevA + nums[i])

            # Update Case B only if first house is excluded
            if i > 0:
                prevB, currB = currB, max(currB, prevB + nums[i])

        return max(currA, currB)

# Java 
"""
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];

        // Case A: exclude last house
        int prevA = 0, currA = 0;

        // Case B: exclude first house
        int prevB = 0, currB = 0;

        for (int i = 0; i < n; i++) {

            // Case A: consider houses [0 ... n-2]
            if (i < n - 1) {
                int temp = currA;
                currA = Math.max(currA, prevA + nums[i]);
                prevA = temp;
            }

            // Case B: consider houses [1 ... n-1]
            if (i > 0) {
                int temp = currB;
                currB = Math.max(currB, prevB + nums[i]);
                prevB = temp;
            }
        }

        return Math.max(currA, currB);
    }
}
"""


# C++
"""
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return nums[0];

        // Case A: exclude last house
        int prevA = 0, currA = 0;

        // Case B: exclude first house
        int prevB = 0, currB = 0;

        for (int i = 0; i < n; i++) {

            // Case A: houses [0 ... n-2]
            if (i < n - 1) {
                int temp = currA;
                currA = max(currA, prevA + nums[i]);
                prevA = temp;
            }

            // Case B: houses [1 ... n-1]
            if (i > 0) {
                int temp = currB;
                currB = max(currB, prevB + nums[i]);
                prevB = temp;
            }
        }

        return max(currA, currB);
    }
};
"""
