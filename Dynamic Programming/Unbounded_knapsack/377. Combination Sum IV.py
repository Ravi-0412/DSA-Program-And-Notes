# method 1: 

"""
Recursion + memoisation

Note: Same Q as "518. Coin Change II" but here order also matter.

Logic vvi: Kisi bhi element ke bad koi bhi ele aa sakta h kabhi bhi.
i.e since asking for combination so pre index ele can also come again because here 
different order of same sets of element is also calculated as ans.

e.g: nums = [1,2,3], target = 4
possible ans = (1, 1, 1, 1), (1, 1, 2), (1, 2, 1), (1, 3), (2, 1, 1), (2, 2), (3, 1)

Take : (1, 2, 1) & (2, 1, 1)
element at index '0' i.e '1' is coming after ele at index 1' i.e 2.

So in this we take index as parameter like 'coin change' then we won't be able to consider 
pre index element again but we have to consider that again.

Note vvi: In this type of question always use for loop and don't take index as parameter in function call.
using for loop an element can come after any element. 
And only call next function checking the condition, this will take us to the proper base case a/c to the q.

vvi: for base case -> we have to avoid function call while taking any number only.
So before taking any number just check 'if nums[i] <= target'.
And for base check if target == 0.

Time : O(target * N)

"""

class Solution: 
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1] * (target + 1)

        def solve(target):
            if target == 0:
                return 1
            if dp[target] != -1:
                return dp[target]

            ans = 0
            for i in range(len(nums)):
                if nums[i] <= target:
                    ans += solve(target - nums[i])   # sb possibility ko add karna h.
            dp[target] = ans
            return ans

        return solve(target)

# Java Code 
"""
import java.util.*;

public class Solution {
    public int combinationSum4(int[] nums, int target) {
        Map<Integer, Integer> memo = new HashMap<>();
        return solve(target, nums, memo);
    }

    private int solve(int target, int[] nums, Map<Integer, Integer> memo) {
        if (target == 0)
            return 1;

        if (memo.containsKey(target))
            return memo.get(target);

        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] <= target) {
                ans += solve(target - nums[i], nums, memo);  // sb possibility ko add karna h.
            }
        }

        memo.put(target, ans);
        return ans;
    }
}
"""

# C++ Code 
"""
class Solution {
public:
    int combinationSum4(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> memo;
        return solve(target, nums, memo);
    }

private:
    int solve(int target, const std::vector<int>& nums, std::unordered_map<int, int>& memo) {
        if (target == 0)
            return 1;

        if (memo.count(target))
            return memo[target];

        int ans = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] <= target) {
                ans += solve(target - nums[i], nums, memo);  // sb possibility ko add karna h.
            }
        }

        return memo[target] = ans;
    }
};
"""

"""
Follow ups:
Q) What if negative numbers are allowed in the given array? How does it change the problem? 
What limitation we need to add to the question to allow negative numbers?

--> If you introduce negative numbers, you can create a cycle that sums to zero.
This means there are infinitely many combinations that result in the target. The answer effectively becomes "Infinity."

What limitation must be added?
1. You could restrict the sequence length: "Find the number of combinations that sum to target using exactly $K$ integers."
2. Forbid Zero-Sum Subsequences
You could explicitly state: "You cannot use any subsequence of numbers that sums to zero."
"""

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[i] will store the number of ways to reach amount 'i'
        dp = [0] * (target + 1)
        
        # Base case: There is 1 way to reach amount 0 (by choosing nothing)
        dp[0] = 1
        
        # Build the table from 1 up to target
        for amount in range(1, target + 1):
            for num in nums:
                # If the coin can fit into the current amount
                if amount >= num:
                    # Add the ways we found for the remainder
                    dp[amount] += dp[amount - num]
                    
        return dp[target]
