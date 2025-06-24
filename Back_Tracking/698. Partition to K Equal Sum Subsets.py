# method 1: vvi
"""
logic: every element can go into any of the 'k' buckets.
so just start putting each ele into each bucket one by one.

Two game changer:
1. if sums[j] == 0: return False

The key is, sums[j] == 0 means for all k > j, sums[k] == 0; 
because this algorithm always fill the previous buckets before trying the next.
So if by putting nums[i] in this empty bucket can't solve the game, 
putting nums[i] on other empty buckets can't solve the game either. So simply return False

Kyonki agar dusre next partition me rakh denge nums[i] ko , then again hmko yahi milega.

If subsets[j] = 0, it means this is the first time adding values to that subset.
If the backtrack search fails when adding the values to subSets[j] and subSets[j] remains 0, 
it will also fail for all subSets from subSets[j+1:].
Because we are simply going through the previous recursive tree again for a different j+1 position.
So we can effectively break from the for loop or directly return False.

In the same level of DFS, if a bucket failed, then all other buckets of the same value should also fail.

time: O(k^n). (will be less than this only for all similar Q like this)

2. nums.sort(reverse=True)
Always start from big numbers for this kind of problem, 
just by doing it yourself for a few times you will find out that the big numbers are the easiest to place.

Note vvi: if we will do by sorting in ascending order then above method will give TLE.
Reason: when we sort in descending order then we will reach the base case inside the loop faster.
Due to less no of function call.
But in case if we sort in ascending order, we will reach the base case later because of more recursion call.
"""

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        if sum(nums) % k:
            return False
        sums = [0]*k  # will store the partition of each sum.
        subsetSum = sum(nums) // k
        nums.sort(reverse=True)
        n = len(nums)
        
        # function determines which bucket to put the 'current element' (nums[id] ) into
        def canPartition(i):
            # If we've placed all of the items, we're done;
            # check if we correctly made k equal subsets of 
            # size sum(nums) // k
            if i == n:
                return len(set(sums)) == 1
            # cur ele can go to any of the subset
            for j in range(k):
                # Try adding the current element to it
                sums[j] += nums[i]
                # If it's a valid placement and we correctly placed the next element, we're
                # done placing the current element.
                if sums[j] <= subsetSum and canPartition(i+1):  # optimisation
                    return True
                sums[j] -= nums[i]
                """
		This is an optimization that is not strictly necessary. 
                If buckets[j] == 0, it means:
                  - We put nums[i] into an empty bucket
                  - We tried placing every other element after and failed.
                  - We took nums[i] out of the bucket, making it empty again. 
                So trying to put nums[i] into a _different_ empty bucket as 1st ele will not produce
                a correct solution; we will just waste time (we place elements left to right,
                so if this bucket is now empty, every one after it is too).
		
                Otherwise (sums[j] > 0), we just go to the next bucket and 
                try placing nums[i] there. If none of them work out, we wind up returning False.
		"""
                if sums[j] == 0:  # optimisation, no need to try other empty bucket
                    return False
            # We couldn't place the current element anywhere that 
            # leads to a invalid solution, so we will need to backtrack
            # and try something else.
            return False        
        
        # Start by trying to place nums[0]
        return canPartition(0)

# Java Code 
"""
public class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int total = 0;
        for (int num : nums) total += num;
        if (total % k != 0) return false;

        int subsetSum = total / k;
        int[] sums = new int[k];  // will store the partition of each sum.
        Arrays.sort(nums);
        int n = nums.length;

        // reverse to match reverse sorting in Python
        for (int i = 0; i < n / 2; i++) {
            int temp = nums[i];
            nums[i] = nums[n - 1 - i];
            nums[n - 1 - i] = temp;
        }

        return canPartition(0, nums, sums, k, subsetSum);
    }

    // function determines which bucket to put the 'current element' (nums[i]) into
    private boolean canPartition(int i, int[] nums, int[] sums, int k, int subsetSum) {
        // If we've placed all of the items, we're done;
        // check if we correctly made k equal subsets of size total / k
        if (i == nums.length) {
            for (int j = 1; j < k; j++) {
                if (sums[j] != sums[0]) return false;
            }
            return true;
        }

        // cur ele can go to any of the subset
        for (int j = 0; j < k; j++) {
            sums[j] += nums[i];  // Try adding the current element to it
            // If it's a valid placement and we correctly placed the next element, we're done
            if (sums[j] <= subsetSum && canPartition(i + 1, nums, sums, k, subsetSum))
                return true;
            sums[j] -= nums[i];

            /*
              Optimization that is not strictly necessary:
              If sums[j] == 0, it means:
                - We put nums[i] into an empty bucket
                - We tried placing every other element after and failed.
                - We took nums[i] out of the bucket, making it empty again.
              So trying to put nums[i] into a _different_ empty bucket will not produce a correct solution;
              we will just waste time.
            */
            if (sums[j] == 0) return false;
        }

        // We couldn't place the current element anywhere, so we backtrack
        return false;
    }
}
"""

# C++ Code 
"""
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int total = 0;
        for (int num : nums) total += num;
        if (total % k != 0) return false;

        int subsetSum = total / k;
        vector<int> sums(k, 0);  // will store the partition of each sum
        sort(nums.rbegin(), nums.rend());  // reverse sort to optimize
        return canPartition(0, nums, sums, k, subsetSum);
    }

    // function determines which bucket to put the 'current element' (nums[i]) into
    bool canPartition(int i, vector<int>& nums, vector<int>& sums, int k, int subsetSum) {
        // If we've placed all of the items, we're done;
        // check if we correctly made k equal subsets
        if (i == nums.size()) {
            for (int j = 1; j < k; ++j) {
                if (sums[j] != sums[0]) return false;
            }
            return true;
        }

        // cur ele can go to any of the subset
        for (int j = 0; j < k; ++j) {
            sums[j] += nums[i];  // Try adding the current element to it
            // If it's a valid placement and we correctly placed the next element, we're done
            if (sums[j] <= subsetSum && canPartition(i + 1, nums, sums, k, subsetSum))
                return true;
            sums[j] -= nums[i];

            /*
              Optimization: no need to try other empty buckets
              If sums[j] == 0, trying to place in other empty buckets is redundant
            */
            if (sums[j] == 0) return false;
        }

        // Couldn't place the current element anywhere
        return false;
    }
};
"""

# Note vvi: whenever you are asked to operate on the sum on a set of objects, just make a list sum and store sum of a set at an index.
# Note: if number is negative also then do by this logic
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/solutions/108730/java-c-straightforward-dfs-solution/
    
    
# Method 2: 
# Better one : using Bit Masking

# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/solutions/1494999/c-java-python-top-down-dp-bitmask-clean-concise/
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/solutions/905981/iterative-dp-deep-analysis-4-solutions-2-ways-of-bit-masking-1-backtracking-1-knapsack/
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/solutions/867956/python3-two-solutions-dp-with-bit-mask-48ms-dfs-backtracking-with-detailed-explanations/

# Related Questions:
"""
1) 473. Matchsticks to Square
2) 2305. Fair Distribution of Cookies
3) 1723. Find Minimum Time to Finish All Jobs
4) 1601. Maximum Number of Achievable Transfer Requests
"""

