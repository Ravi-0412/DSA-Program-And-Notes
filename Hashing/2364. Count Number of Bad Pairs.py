# Logic:
"""
Trick to this problem:
Total= Valid + Invalid
Invalid = Total- Valid

The real Equation: ( j - i ) != ( A[j] - A[i] )
The simple and more intuitive form of above equation: ( j - A[j] ) != ( i - A[i] ) OR => A[i] - i != A[j] - j

How to find total_valid one?
So first find the value of 'A[i] - i' for each index .
Then if we see any same value later nums[j] (i < j)  then, no of newly pair we can from this nums[j]
using all the same values we have seen = count[nums[i]], we take this nums[j] with any nums[i] we have seen before.

Note: for an array of size n, there are exactly n * (n - 1) / 2 unique pairs (i, j) where i < j. 
How? 
for i = 0 => n- 1
    i = 1 => n - 2
    ..
    i = n-1 => 1

Total unique pairs = 1 + 2 + .....+ (n-1) = n *(n-1)//2

Then, final ans = Total_unique_pairs - total_valid

Time = space = O(n)
"""
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n-1) // 2
        good_pair_count = 0
        seen_diff_count = {}
        for i in range(n):
            diff = nums[i] - i
            good_pair_count +=   seen_diff_count.get(diff, 0)
            seen_diff_count[diff] = seen_diff_count.get(diff, 0) + 1
        return total - good_pair_count

# Java
"""
import java.util.HashMap;
import java.util.Map;

class Solution {
    public long countBadPairs(int[] nums) {
        int n = nums.length;
        long total = (long) n * (n - 1) / 2; // Total possible pairs
        long goodPairCount = 0; // Count of good pairs
        Map<Integer, Integer> seenDiffCount = new HashMap<>(); // Map to store frequency of differences

        for (int i = 0; i < n; i++) {
            int diff = nums[i] - i; // Calculate the difference
            // Add the frequency of the current difference to goodPairCount
            goodPairCount += seenDiffCount.getOrDefault(diff, 0);
            // Update the frequency of the current difference
            seenDiffCount.put(diff, seenDiffCount.getOrDefault(diff, 0) + 1);
        }

        // Bad pairs = Total pairs - Good pairs
        return total - goodPairCount;
    }
}
  """
