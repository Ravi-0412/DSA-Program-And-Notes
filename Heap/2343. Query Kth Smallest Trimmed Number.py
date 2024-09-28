# Time: O(n * (n*n) + n*logn)

class Solution:
    def smallestTrimmedNumbers(self, nums, queries):
        res = []
        n = len(nums)
        
        for q in queries:
            k, trimLength = q[0] , q[1]
            pq = []
            for i in range(n):
                trimmed_num = nums[i][-trimLength :]  # Get the last q[1] characters
                pq.append((trimmed_num, i))
            
            pq.sort()  # Sort primarily by the trimmed number, and secondarily by index
            res.append(pq[k - 1][1])  # Get the index of the k-th smallest trimmed number
            
        return res


# java
"""
import java.util.*;

class Solution {
    public int[] smallestTrimmedNumbers(String[] nums, int[][] queries) {
        int[] res = new int[queries.length];
        int n = nums.length;

        for (int qi = 0; qi < queries.length; qi++) {
            int k = queries[qi][0];
            int trimLength = queries[qi][1];

            List<int[]> pq = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                String trimmedNum = nums[i].substring(nums[i].length() - trimLength);
                pq.add(new int[]{Integer.parseInt(trimmedNum), i});
            }

            pq.sort((a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);
            res[qi] = pq.get(k - 1)[1];
        }

        return res;
    }
}

"""


# Note: later learn and try by radix sort
