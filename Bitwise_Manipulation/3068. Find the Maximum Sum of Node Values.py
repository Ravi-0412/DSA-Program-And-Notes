# Logic: 1) For max we should take xor of any number at most once because doing xor 
# with same number again will bring to original number.
# e.g: n ^ x ^ x = n

# 2) For doing xor we have take any edge and xor two nodes associated with that edge.
# But we can take any two nodes and take xor.
# Reason: All internal nodes where we will take even times od xor will become same number only.
# e.g: 1 - 2- 3- 4 - 5 
# a) suppose we will get ans by taking xor with '1' and '5' then, 
# just take xor of '5' and '1' .
# How?
# take edge 1- 2 , 2- 3, 3- 4, 4 - 5.
# All nodes internally will be same number only , only '1' and '5' will get affected.
# b) suppose we want to take xor '2' and '5' only for maximum ans.
# then take edge 2-3, 3-4, 4- 5.

# VVi: from we get intution that take any two number that you want at a time.
# You can take single number because we have to take an edge.
# so in odd no of element we have to sacrifice one node.

# in similar way we can take as much nodes two at a time.

# 3) Whn we will take xor then that number may increase or decrease.
# so first find the difference either positive/negative by taking xor with each number.
# say 'delta' array.

# 4) To get maximum ans , sort the delta in reverse order and take 
# two element at a time and check if their delta sum value is > 0.
# if > 0 then, taking these nodes will increase our ans.
# so add their sum in ans.

# 5) return ans + sum(nums)

# Time: O(n* logn)

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        delta = [(num^k) - num for num in nums]
        delta.sort(reverse = True)
        ans = 0
        for i in range(0, n-1, 2):
            if delta[i] + delta[i + 1] > 0:
                ans += delta[i] + delta[i + 1]
        return ans + sum(nums)


# later do in O(n) and O(1) space using solution in sheet.


# Java
"""
// giving error in test case : 714. may be due to overflow. Have to check.

class Solution {
    public long maximumValueSum(int[] nums, int k, int[][] edges) {
        int n = nums.length;
        
        // Calculate delta array
        int[] delta = new int[n];
        for (int i = 0; i < n; i++) {
            delta[i] = (nums[i] ^ k) - nums[i];
        }
        
        // Sort the delta array in descending order
        Arrays.sort(delta);
        for (int i = 0; i < n / 2; i++) {
            int temp = delta[i];
            delta[i] = delta[n - i - 1];
            delta[n - i - 1] = temp;
        }
        long ans = 0;
        // Add pairs of deltas if their sum is positive
        for (int i = 0; i < n - 1; i += 2) {
            if (delta[i] + delta[i + 1] > 0) {
                ans += delta[i] + delta[i + 1];
            }
        }
        
        // Sum of original nums array
        long sumNums = Arrays.stream(nums).sum();
        ans = ans + sumNums;
        return ans;
    }
}
"""

# Why we can't sort in reverse order directly using below:
# 1) for list
# Collections.sort(list, Collections.reverseOrder());
# 2) Array
# Arrays.sort(array, Collections.reverseOrder());

# Note vvi:
# That will work fine with 'Array of Objects' such as Integer array 
# but will not work with a primitive array such as int array.

# The only way to sort a primitive array in descending order is, 
# first sort the array in ascending order and then reverse the array in place. 
# This is also true for two-dimensional primitive arrays.

# Link: https://stackoverflow.com/questions/1694751/java-array-sort-descending