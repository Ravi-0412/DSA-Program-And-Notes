# method 1: 
# Recursion
# just extension of q: "740. Delete and Earn".
# Here you need to skip 'i+1' or 'i + 2' based on condition.
# Time : O(n^3) , space: O(n)


from collections import Counter
from typing import List

class Solution:
    def maximumTotalDamage(self, nums: List[int]) -> int:
        freq = Counter(nums)
        nums = sorted(list(set(nums)))
        n = len(nums)

        def solve(i):
            if i >= n:
                return 0
            notTake = solve(i + 1)
            take = freq[nums[i]] * nums[i]
            if (i + 1 < n and nums[i + 1] != nums[i] + 1 and nums[i + 1] != nums[i] + 2):
                take += solve(i + 1)
            elif i + 2 < n and nums[i + 2] != nums[i] + 2:
                take += solve(i + 2)
            else:
                take += solve(i + 3)
            return max(take, notTake)

        return solve(0)

# Java Code 
"""
import java.util.*;

public class Solution {
    public int maximumTotalDamage(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums)
            freq.put(num, freq.getOrDefault(num, 0) + 1);

        Set<Integer> uniqueSet = new HashSet<>();
        for (int num : nums)
            uniqueSet.add(num);

        List<Integer> sortedNums = new ArrayList<>(uniqueSet);
        Collections.sort(sortedNums);
        int n = sortedNums.size();

        return solve(0, sortedNums, freq);
    }

    private int solve(int i, List<Integer> nums, Map<Integer, Integer> freq) {
        int n = nums.size();
        if (i >= n)
            return 0;

        int notTake = solve(i + 1, nums, freq);
        int take = freq.get(nums.get(i)) * nums.get(i);

        if (i + 1 < n && nums.get(i + 1) != nums.get(i) + 1 && nums.get(i + 1) != nums.get(i) + 2)
            take += solve(i + 1, nums, freq);
        else if (i + 2 < n && nums.get(i + 2) != nums.get(i) + 2)
            take += solve(i + 2, nums, freq);
        else
            take += solve(i + 3, nums, freq);

        return Math.max(take, notTake);
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <unordered_map>
#include <set>
#include <algorithm>

class Solution {
public:
    int maximumTotalDamage(std::vector<int>& nums) {
        std::unordered_map<int, int> freq;
        for (int num : nums)
            freq[num]++;

        std::set<int> uniqueSet(nums.begin(), nums.end());
        std::vector<int> sortedNums(uniqueSet.begin(), uniqueSet.end());
        int n = sortedNums.size();

        return solve(0, sortedNums, freq);
    }

private:
    int solve(int i, const std::vector<int>& nums, std::unordered_map<int, int>& freq) {
        int n = nums.size();
        if (i >= n)
            return 0;

        int notTake = solve(i + 1, nums, freq);
        int take = freq[nums[i]] * nums[i];

        if (i + 1 < n && nums[i + 1] != nums[i] + 1 && nums[i + 1] != nums[i] + 2)
            take += solve(i + 1, nums, freq);
        else if (i + 2 < n && nums[i + 2] != nums[i] + 2)
            take += solve(i + 2, nums, freq);
        else
            take += solve(i + 3, nums, freq);

        return std::max(take, notTake);
    }
};
"""

# Method 2 : 
# Recursion with memoization
# Time = O(n*logn) 
# Space = O(n)


from collections import Counter
from typing import List

class Solution:
    def maximumTotalDamage(self, nums: List[int]) -> int:
        freq = Counter(nums)
        nums = sorted(list(set(nums)))
        n = len(nums)
        dp = [-1] * n  # for memoization

        def solve(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            
            notTake = solve(i + 1)
            take = freq[nums[i]] * nums[i]

            # first check if we can take 'i+1' as next or not.
            if i + 1 < n and nums[i + 1] != nums[i] + 1 and nums[i + 1] != nums[i] + 2:
                take += solve(i + 1)
            # if can't take 'i+1', check if we can take 'i+2'.
            elif i + 2 < n and nums[i + 2] != nums[i] + 2:
                take += solve(i + 2)
            # if can't take both 'i+1' or 'i +2' then, take 'i +3'
            else:
                take += solve(i + 3)

            dp[i] = max(take, notTake)
            return dp[i]

        return solve(0)

# Java Code 
"""
import java.util.*;

public class Solution {
    public int maximumTotalDamage(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums)
            freq.put(num, freq.getOrDefault(num, 0) + 1);

        Set<Integer> uniqueSet = new HashSet<>();
        for (int num : nums)
            uniqueSet.add(num);

        List<Integer> sortedNums = new ArrayList<>(uniqueSet);
        Collections.sort(sortedNums);
        int n = sortedNums.size();
        int[] dp = new int[n];  // for memoization
        Arrays.fill(dp, -1);

        return solve(0, sortedNums, freq, dp);
    }

    private int solve(int i, List<Integer> nums, Map<Integer, Integer> freq, int[] dp) {
        int n = nums.size();
        if (i >= n)
            return 0;
        if (dp[i] != -1)
            return dp[i];

        int notTake = solve(i + 1, nums, freq, dp);
        int take = freq.get(nums.get(i)) * nums.get(i);

        // first check if we can take 'i+1' as next or not.
        if (i + 1 < n && nums.get(i + 1) != nums.get(i) + 1 && nums.get(i + 1) != nums.get(i) + 2)
            take += solve(i + 1, nums, freq, dp);
        // if can't take 'i+1', check if we can take 'i+2'.
        else if (i + 2 < n && nums.get(i + 2) != nums.get(i) + 2)
            take += solve(i + 2, nums, freq, dp);
        // if can't take both 'i+1' or 'i +2' then, take 'i +3'
        else
            take += solve(i + 3, nums, freq, dp);

        return dp[i] = Math.max(take, notTake);
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <unordered_map>
#include <set>
#include <algorithm>

class Solution {
public:
    int maximumTotalDamage(std::vector<int>& nums) {
        std::unordered_map<int, int> freq;
        for (int num : nums)
            freq[num]++;

        std::set<int> uniqueSet(nums.begin(), nums.end());
        std::vector<int> sortedNums(uniqueSet.begin(), uniqueSet.end());
        int n = sortedNums.size();
        std::vector<int> dp(n, -1);  // for memoization

        return solve(0, sortedNums, freq, dp);
    }

private:
    int solve(int i, const std::vector<int>& nums,
              std::unordered_map<int, int>& freq, std::vector<int>& dp) {
        int n = nums.size();
        if (i >= n)
            return 0;
        if (dp[i] != -1)
            return dp[i];

        int notTake = solve(i + 1, nums, freq, dp);
        int take = freq[nums[i]] * nums[i];

        // first check if we can take 'i+1' as next or not.
        if (i + 1 < n && nums[i + 1] != nums[i] + 1 && nums[i + 1] != nums[i] + 2)
            take += solve(i + 1, nums, freq, dp);
        // if can't take 'i+1', check if we can take 'i+2'.
        else if (i + 2 < n && nums[i + 2] != nums[i] + 2)
            take += solve(i + 2, nums, freq, dp);
        // if can't take both 'i+1' or 'i +2' then, take 'i +3'
        else
            take += solve(i + 3, nums, freq, dp);

        return dp[i] = std::max(take, notTake);
    }
};
"""

# method 3:
# Tabulation
# Time: O(n*logn)
# Space: O(n) 

from collections import Counter
from typing import List

class Solution:
    def maximumTotalDamage(self, nums: List[int]) -> int:
        freq = Counter(nums)
        nums = sorted(list(set(nums)))
        n = len(nums)
        dp = [0] * (n + 3)  # To safely access i+3

        for i in range(n - 1, -1, -1):
            notTake = dp[i + 1]
            take = freq[nums[i]] * nums[i]
            
            if (i + 1 < n and nums[i + 1] != nums[i] + 1 and nums[i + 1] != nums[i] + 2):
                take += dp[i + 1]
            elif i + 2 < n and nums[i + 2] != nums[i] + 2:
                take += dp[i + 2]
            else:
                take += dp[i + 3]
                
            dp[i] = max(take, notTake)

        return dp[0]

# Java Code 
"""
import java.util.*;

public class Solution {
    public int maximumTotalDamage(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums)
            freq.put(num, freq.getOrDefault(num, 0) + 1);

        Set<Integer> uniqueSet = new HashSet<>();
        for (int num : nums)
            uniqueSet.add(num);

        List<Integer> sortedNums = new ArrayList<>(uniqueSet);
        Collections.sort(sortedNums);
        int n = sortedNums.size();

        int[] dp = new int[n + 3];  // To safely access i+3

        for (int i = n - 1; i >= 0; i--) {
            int notTake = dp[i + 1];
            int take = freq.get(sortedNums.get(i)) * sortedNums.get(i);

            if (i + 1 < n && sortedNums.get(i + 1) != sortedNums.get(i) + 1 &&
                sortedNums.get(i + 1) != sortedNums.get(i) + 2) {
                take += dp[i + 1];
            } else if (i + 2 < n && sortedNums.get(i + 2) != sortedNums.get(i) + 2) {
                take += dp[i + 2];
            } else {
                take += dp[i + 3];
            }

            dp[i] = Math.max(take, notTake);
        }

        return dp[0];
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <unordered_map>
#include <set>
#include <algorithm>

class Solution {
public:
    int maximumTotalDamage(std::vector<int>& nums) {
        std::unordered_map<int, int> freq;
        for (int num : nums)
            freq[num]++;

        std::set<int> uniqueSet(nums.begin(), nums.end());
        std::vector<int> sortedNums(uniqueSet.begin(), uniqueSet.end());
        int n = sortedNums.size();

        std::vector<int> dp(n + 3, 0);  // To safely access i+3

        for (int i = n - 1; i >= 0; --i) {
            int notTake = dp[i + 1];
            int take = freq[sortedNums[i]] * sortedNums[i];

            if (i + 1 < n && sortedNums[i + 1] != sortedNums[i] + 1 &&
                sortedNums[i + 1] != sortedNums[i] + 2) {
                take += dp[i + 1];
            } else if (i + 2 < n && sortedNums[i + 2] != sortedNums[i] + 2) {
                take += dp[i + 2];
            } else {
                take += dp[i + 3];
            }

            dp[i] = std::max(take, notTake);
        }

        return dp[0];
    }
};
"""