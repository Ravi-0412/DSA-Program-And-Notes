# Logic:
"""
Note: Think the opposite direction instead of minimum elements to remove the maximum mountain subsequence.
Use LIS logic for this.

The idea is the following: split our list into two parts, and find LIS for left part and 
also Longest Decreasing Subsequence for the second part. 
find LIS for these parts and if lengths of both parts 2 or more, 
it means we can construct Mountain Array, so we update our max_found.
"""
# Time : O(n^2) , space : O(n)
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: Calculate LIS (Longest Increasing Subsequence) from the left for each element
        lis = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis[i] = max(lis[i], lis[j] + 1)
        
        # Step 2: Calculate LDS (Longest Decreasing Subsequence) from the right for each element
        lds = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    lds[i] = max(lds[i], lds[j] + 1)
        
        # Step 3: Find the maximum length of a mountain array
        max_mountain_length = 0
        for i in range(1, n - 1):
            if lis[i] > 1 and lds[i] > 1:  # To ensure it's a valid peak
                max_mountain_length = max(max_mountain_length, lis[i] + lds[i] - 1)
        
        # Step 4: Calculate the minimum number of removals
        return n - max_mountain_length

# Java
"""
import java.util.List;

public class Solution {
    public int minimumMountainRemovals(int[] nums) {
        int n = nums.length;

        // Step 1: Calculate LIS (Longest Increasing Subsequence) from the left for each element
        int[] lis = new int[n];
        for (int i = 0; i < n; i++) {
            lis[i] = 1;
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    lis[i] = Math.max(lis[i], lis[j] + 1);
                }
            }
        }

        // Step 2: Calculate LDS (Longest Decreasing Subsequence) from the right for each element
        int[] lds = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            lds[i] = 1;
            for (int j = i + 1; j < n; j++) {
                if (nums[j] < nums[i]) {
                    lds[i] = Math.max(lds[i], lds[j] + 1);
                }
            }
        }

        // Step 3: Find the maximum length of a mountain array
        int maxMountainLength = 0;
        for (int i = 1; i < n - 1; i++) {
            if (lis[i] > 1 && lds[i] > 1) { // Ensure it's a valid peak
                maxMountainLength = Math.max(maxMountainLength, lis[i] + lds[i] - 1);
            }
        }

        // Step 4: Calculate the minimum number of removals
        return n - maxMountainLength;
    }
}
"""

# Note: use binary search to find LIS and LDS
# Time: O(n*logn)

from typing import List
import bisect

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Calculate LIS from the left for each element using binary search
        def calculateLIS(nums):
            lis = [0] * n
            seq = []
            for i in range(n):
                pos = bisect.bisect_left(seq, nums[i])
                if pos == len(seq):
                    seq.append(nums[i])
                else:
                    seq[pos] = nums[i]
                lis[i] = pos + 1  # Length of LIS up to index i
            return lis

        # Calculate LIS for the original array
        lis = calculateLIS(nums)
        
        # Step 2: Calculate LDS from the right using the same binary search approach
        nums_reversed = nums[::-1]
        lds_reversed = calculateLIS(nums_reversed)
        lds = lds_reversed[::-1]  # Reverse it back to original indexing

        # Step 3: Find the maximum mountain length
        max_mountain_length = 0
        for i in range(1, n - 1):
            if lis[i] > 1 and lds[i] > 1:  # Valid peak
                max_mountain_length = max(max_mountain_length, lis[i] + lds[i] - 1)

        # Step 4: Calculate minimum removals
        return n - max_mountain_length

# Java
"""
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public int minimumMountainRemovals(int[] nums) {
        int n = nums.length;
        
        // Step 1: Calculate LIS for each element using binary search
        int[] lis = calculateLIS(nums);
        
        // Step 2: Calculate LDS by reversing the array and using the same LIS logic
        int[] numsReversed = new int[n];
        for (int i = 0; i < n; i++) {
            numsReversed[i] = nums[n - i - 1];
        }
        int[] ldsReversed = calculateLIS(numsReversed);
        
        // Reverse the LDS result back to match the original array's indexing
        int[] lds = new int[n];
        for (int i = 0; i < n; i++) {
            lds[i] = ldsReversed[n - i - 1];
        }

        // Step 3: Find the maximum mountain length
        int maxMountainLength = 0;
        for (int i = 1; i < n - 1; i++) {
            if (lis[i] > 1 && lds[i] > 1) { // Valid peak
                maxMountainLength = Math.max(maxMountainLength, lis[i] + lds[i] - 1);
            }
        }

        // Step 4: Calculate minimum removals
        return n - maxMountainLength;
    }

    private int[] calculateLIS(int[] nums) {
        int n = nums.length;
        int[] lis = new int[n];
        List<Integer> seq = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int pos = binarySearch(seq, nums[i]);
            if (pos == seq.size()) {
                seq.add(nums[i]);
            } else {
                seq.set(pos, nums[i]);
            }
            lis[i] = pos + 1; // Length of LIS up to index i
        }
        
        return lis;
    }

    private int binarySearch(List<Integer> seq, int key) {
        int left = 0, right = seq.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (seq.get(mid) < key) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
}
"""
