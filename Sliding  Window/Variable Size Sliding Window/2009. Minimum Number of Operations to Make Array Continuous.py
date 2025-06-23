# Method 1: 

# Logic: we if we consider any ele say 'nums[i]' as starting ele then max number we can include in 
# arr say nums[j] = nums[i] + (n - 1)

# Since we want only unique values so store in set to get unique values 
# And after that sort to find the max number we can include.

# Observation: more the length of arr, less we will need to replace.
# So Q reduces to "get the length of the longest subarray whose difference between min and max elements is N - 1".

# Note: The brute force way is to pick each A[i] as the start of the subarray and 
# count the number of elements that are <= A[i] + N - 1, which takes O(N^2) time.

# Since the array is already sorted, we can use sliding window so that we only traverse the entire array once.

# suppose we are able to include ele before index 'j' consider starting number as 'nums[i]' then,
# 'no of unique ele considering 'i' as starting ele = 'j - i'.
# So total replacement = n - no_unique_ele = n - (j - i).

# Time : O(n*logn)

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)  # initial length
        nums = sorted(set(nums))
        m = len(nums)  # length after sorting unique values
        j = 0
        ans = n  # any big not possible ans
        for i in range(m):
            start, end = nums[i] , nums[i] + (n - 1)
            while j < m and nums[j] <= end:
                j += 1
            uniqueEle = j- i
            ans = min(ans , n - uniqueEle)  
        return ans

# Java Code 
"""
class Solution {
    public int minOperations(int[] nums) {
        int n = nums.length;  // initial length
        Set<Integer> set = new HashSet<>();
        for (int num : nums) set.add(num);
        List<Integer> list = new ArrayList<>(set);
        Collections.sort(list);
        int m = list.size();  // length after sorting unique values
        int j = 0;
        int ans = n;  // any big not possible ans
        for (int i = 0; i < m; i++) {
            int start = list.get(i), end = start + (n - 1);
            while (j < m && list.get(j) <= end) {
                j++;
            }
            int uniqueEle = j - i;
            ans = Math.min(ans, n - uniqueEle);
        }
        return ans;
    }
}
"""

# C++ Code 
"""
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();  // initial length
        unordered_set<int> s(nums.begin(), nums.end());
        vector<int> v(s.begin(), s.end());
        sort(v.begin(), v.end());
        int m = v.size();  // length after sorting unique values
        int j = 0;
        int ans = n;  // any big not possible ans
        for (int i = 0; i < m; i++) {
            int start = v[i], end = start + (n - 1);
            while (j < m && v[j] <= end) {
                j++;
            }
            int uniqueEle = j - i;
            ans = min(ans, n - uniqueEle);
        }
        return ans;
    }
};
"""

# Method 2: 
# Using Binary search
# Since we are finding the last ele nums[j] for each nums[i] in sorted array(after getting unique ele)

# For finding the index 'j' we can use binary search
# Because we have to find 1st index such that nums[j] > nums[i] + (n-1).

import bisect
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)  # initial length
        nums = sorted(set(nums))
        m = len(nums)  # length after sorting unique values
        ans = n  # any big not possible ans
        for i in range(m):
            start, end = nums[i] , nums[i] + (n - 1)
            j = bisect.bisect_right(nums, end)   
            uniqueEle = j- i
            ans = min(ans , n - uniqueEle)  
        return ans

# Java Code 
"""
import java.util.*;

class Solution {
    public int minOperations(int[] nums) {
        int n = nums.length;  // initial length
        Set<Integer> set = new HashSet<>();
        for (int num : nums) set.add(num);
        List<Integer> sorted = new ArrayList<>(set);
        Collections.sort(sorted);
        int m = sorted.size();  // length after sorting unique values
        int ans = n;  // any big not possible ans
        for (int i = 0; i < m; i++) {
            int start = sorted.get(i), end = start + (n - 1);
            int j = upperBound(sorted, end);   
            int uniqueEle = j - i;
            ans = Math.min(ans, n - uniqueEle);
        }
        return ans;
    }

    private int upperBound(List<Integer> list, int target) {
        int left = 0, right = list.size();
        while (left < right) {
            int mid = (left + right) / 2;
            if (list.get(mid) <= target) left = mid + 1;
            else right = mid;
        }
        return left;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();  // initial length
        unordered_set<int> s(nums.begin(), nums.end());
        vector<int> sorted(s.begin(), s.end());
        sort(sorted.begin(), sorted.end());
        int m = sorted.size();  // length after sorting unique values
        int ans = n;  // any big not possible ans
        for (int i = 0; i < m; i++) {
            int start = sorted[i], end = start + (n - 1);
            int j = upper_bound(sorted.begin(), sorted.end(), end) - sorted.begin();
            int uniqueEle = j - i;
            ans = min(ans, n - uniqueEle);
        }
        return ans;
    }
};
"""