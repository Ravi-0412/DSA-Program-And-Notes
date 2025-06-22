# Method 1: 

# Note : Similar to 'Maximum sum Rectangle' but here 
# If we find the sum after including each row using Kedane's algo then we won't get 
# correct ans because Kedane will give maximum sum and this maximum_sum can be < , =, or  > than 'k'.
# But we can get our optimal ans in between also.

# To solve this , we have to find the maximum sum possible <= k after each currrent sum 
# Is there any sum exist on left side such that 'right - left <= k  =>  left >= right - k'. (right -> curSum).
# Means we have to find the smallest value of sum of left side side say 'left' such that 'left >= right - k' for maximum sum.

# For finding left  we will have to apply binary search on all current sum.
# We can store all curSum into a 'sortedList'.

# After finding 'left' sum = 'right- left'. just same way as do in sliding window.

# How to think like this?
# if give to find sum == k like q: "560. Subarray Sum Equals K" then 
# At cur index 'j', we find the left such that left = curSum(right) - k
# If 'left' is present at some index 'i' then it means after index 'i' i.e from 'i+1' to 'j' sum == k.
# where sum = right - left (for generalization) which will be equal to 'k' only in this case.

# VVI: In similar way ,here telling to find the largest sum <= k
# so here we will find 'left' such that 'left >= right - k' then it means
# we can get sum = right - left <= k and for getting maximum sum we will find smallest 'left'.


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row, col = len(matrix), len(matrix[0])
        maxSum = float('-inf')

        for start in range(col):
            sum = [0 for _ in range(row)]
            for end in range(start, col):
                for r in range(row):
                    sum[r] += matrix[r][end]
                # now find the maximum sum for current joined rows rectangle like Kadane Algo
                currSum = self.MaximumSumSubArray(sum, k)
                maxSum = max(currSum, maxSum)
        return maxSum

    def MaximumSumSubArray(self, arr, k):
        right = 0  # will store the currsum for all index like 0,1,2...
        seen = [0]  # will store the curr sum i.e 'right' in sorted order
        ans = float('-inf')

        for i in range(len(arr)):
            right += arr[i]
            # After each curSum (right), find the smallest value of sum of left side say 'left' such that 'left >= right - k'.
            # Indirectly telling us to find the ceiling value of 'right - k'.
            left = self.Ceiling(seen, right - k)
            if left is not None:  # means if we have seen this difference then update the ans
                ans = max(ans, right - left)  # ans will be equal to 'right - left'

            # Insert 'right' into 'seen' in sorted order (like TreeSet or SortedList)
            self.insertSorted(seen, right)

        return ans

    # We have to find the smallest value >= than 'key'
    def Ceiling(self, arr, key):
        # Do binary search for key
        left, right = 0, len(arr) - 1
        res = None
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= key:
                res = arr[mid]
                right = mid - 1
            else:
                left = mid + 1
        return res

    # Insert value in sorted list using binary search
    def insertSorted(self, arr, val):
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < val:
                left = mid + 1
            else:
                right = mid
        arr.insert(left, val)


# Java Code
"""
import java.util.*;

class Solution {
    public int maxSumSubmatrix(int[][] matrix, int k) {
        int row = matrix.length, col = matrix[0].length;
        int maxSum = Integer.MIN_VALUE;

        for (int start = 0; start < col; start++) {
            int[] sum = new int[row];
            for (int end = start; end < col; end++) {
                for (int r = 0; r < row; r++) {
                    sum[r] += matrix[r][end];
                }
                // now find the maximum sum for current joined rows rectangle like Kadane Algo
                int currSum = MaximumSumSubArray(sum, k);
                maxSum = Math.max(currSum, maxSum);
            }
        }
        return maxSum;
    }

    public int MaximumSumSubArray(int[] arr, int k) {
        int right = 0;  // will store the currsum for all index like 0,1,2...
        List<Integer> seen = new ArrayList<>();
        seen.add(0);  // will store the curr sum i.e 'right' in sorted order
        int ans = Integer.MIN_VALUE;

        for (int i = 0; i < arr.length; i++) {
            right += arr[i];
            // After each curSum (right), find the smallest value of sum of left side say 'left' such that 'left >= right - k'.
            // Indirectly telling us to find the ceiling value of 'right - k'.
            Integer left = Ceiling(seen, right - k);
            if (left != null) {
                ans = Math.max(ans, right - left);  // ans will be equal to 'right - left'
            }
            // Insert 'right' into 'seen' in sorted order (like TreeSet or SortedList)
            insertSorted(seen, right);
        }

        return ans;
    }

    // We have to find the smallest value >= than 'key'
    public Integer Ceiling(List<Integer> arr, int key) {
        int left = 0, right = arr.size() - 1;
        Integer res = null;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (arr.get(mid) >= key) {
                res = arr.get(mid);
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return res;
    }

    // Insert value in sorted list using binary search
    public void insertSorted(List<Integer> arr, int val) {
        int left = 0, right = arr.size();
        while (left < right) {
            int mid = (left + right) / 2;
            if (arr.get(mid) < val)
                left = mid + 1;
            else
                right = mid;
        }
        arr.add(left, val);
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
        int row = matrix.size(), col = matrix[0].size();
        int maxSum = INT_MIN;

        for (int start = 0; start < col; ++start) {
            vector<int> sum(row, 0);
            for (int end = start; end < col; ++end) {
                for (int r = 0; r < row; ++r) {
                    sum[r] += matrix[r][end];
                }
                // now find the maximum sum for current joined rows rectangle like Kadane Algo
                int currSum = MaximumSumSubArray(sum, k);
                maxSum = max(maxSum, currSum);
            }
        }
        return maxSum;
    }

    int MaximumSumSubArray(vector<int>& arr, int k) {
        int right = 0;  // will store the currsum for all index like 0,1,2...
        vector<int> seen = {0};  // will store the curr sum i.e 'right' in sorted order
        int ans = INT_MIN;

        for (int i = 0; i < arr.size(); ++i) {
            right += arr[i];
            // After each curSum (right), find the smallest value of sum of left side say 'left' such that 'left >= right - k'.
            // Indirectly telling us to find the ceiling value of 'right - k'.
            auto it = Ceiling(seen, right - k);
            if (it != seen.end()) {  // means if we have seen this difference then update the ans
                ans = max(ans, right - *it);  // ans will be equal to 'right - left'
            }
            // Insert 'right' into 'seen' in sorted order (like TreeSet or SortedList)
            insertSorted(seen, right);
        }

        return ans;
    }

    // We have to find the smallest value >= than 'key'
    vector<int>::iterator Ceiling(vector<int>& arr, int key) {
        int left = 0, right = arr.size() - 1;
        int idx = arr.size();
        while (left <= right) {
            int mid = (left + right) / 2;
            if (arr[mid] >= key) {
                idx = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return arr.begin() + idx;
    }

    // Insert value in sorted list using binary search
    void insertSorted(vector<int>& arr, int val) {
        int left = 0, right = arr.size();
        while (left < right) {
            int mid = (left + right) / 2;
            if (arr[mid] < val)
                left = mid + 1;
            else
                right = mid;
        }
        arr.insert(arr.begin() + left, val);
    }
};
"""

# used python library
# https://www.geeksforgeeks.org/python-sorted-containers-an-introduction/
# https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
