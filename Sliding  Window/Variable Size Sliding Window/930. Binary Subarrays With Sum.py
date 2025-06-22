# method 1: 
# Exactly same as : "560. Subarray Sum Equals K"

# Time = space = o(n)

from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = {0: 1}
        curr_sum = 0
        count = 0
        
        for num in nums:
            curr_sum += num
            diff = curr_sum - goal
            count += prefix_sum.get(diff, 0)
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
        
        return count

# Java Code 
"""
import java.util.*;

class Solution {
    public int numSubarraysWithSum(int[] nums, int goal) {
        Map<Integer, Integer> prefix_sum = new HashMap<>();
        prefix_sum.put(0, 1);

        int curr_sum = 0;
        int count = 0;

        for (int num : nums) {
            curr_sum += num;

            int diff = curr_sum - goal;
            count += prefix_sum.getOrDefault(diff, 0);

            prefix_sum.put(curr_sum, prefix_sum.getOrDefault(curr_sum, 0) + 1);
        }

        return count;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        unordered_map<int, int> prefix_sum;
        prefix_sum[0] = 1;

        int curr_sum = 0;
        int count = 0;

        for (int num : nums) {
            curr_sum += num;

            int diff = curr_sum - goal;
            count += prefix_sum.count(diff) ? prefix_sum[diff] : 0;

            prefix_sum[curr_sum]++;
        }

        return count;
    }
};
"""

# method 2: 
# Since given value is only '0' and '1'.

# We can use obseravtion that ans = atMostSubarray(nums, goal) - atMostSubarray(nums, goal - 1)

# How ?
# a) atmostSubarray(nums,goal) will give you number of subarrays with sum <= goal
# i.e. goal, goal-1 , goal-2 , goal-3 ... 0

# b) atmostSubarray(nums,goal) will give you number of subarrays with sum <= goal -1
# i.e. goal-1 , goal-2 , goal-3 ... 0

# So we only need number of subarrays which having sum as goal ,

# atmostSubarray(nums,goal) having that , but additionally having other count too of subarrays having sum < goal.

# and we know atmostSubarray(nums,goal -1) having count of all subarrays having sum <= goal - 1 or
# we can say sum < goal too. So that means this contain that additional count which we want to remove
# from atmostSubarray(nums,goal) result.


# Note: This will only work for elements '0' and '1'.

# Time = O(n)
# space = O(1)

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def atMostSubarray(nums, goal):
            if goal < 0:
                return 0
            curSum = ans = 0
            i , j = 0, 0
            while j < len(nums):
                curSum += nums[j]
                while curSum > goal:
                    curSum -= nums[i]
                    i += 1
                ans += j - i + 1
                j += 1
            return ans

        return atMostSubarray(nums, goal) - atMostSubarray(nums, goal - 1)
    
# Java Code 
"""
class Solution {
    private int atMostSubarray(int[] nums, int goal) {
        if (goal < 0) return 0;
        int curSum = 0, ans = 0, i = 0, j = 0;
        while (j < nums.length) {
            curSum += nums[j];
            while (curSum > goal) {
                curSum -= nums[i];
                i++;
            }
            ans += j - i + 1;
            j++;
        }
        return ans;
    }

    public int numSubarraysWithSum(int[] nums, int goal) {
        return atMostSubarray(nums, goal) - atMostSubarray(nums, goal - 1);
    }
}
"""

# C++ Code 
"""
class Solution {
public:
    int atMostSubarray(const vector<int>& nums, int goal) {
        if (goal < 0) return 0;
        int curSum = 0, ans = 0, i = 0, j = 0;
        while (j < nums.size()) {
            curSum += nums[j];
            while (curSum > goal) {
                curSum -= nums[i];
                i++;
            }
            ans += j - i + 1;
            j++;
        }
        return ans;
    }

    int numSubarraysWithSum(vector<int>& nums, int goal) {
        return atMostSubarray(nums, goal) - atMostSubarray(nums, goal - 1);
    }
};
"""

# Extension: 

# Note: in these types of questions where you are told to find exactly 'k' 
# Then try to think like this only i.e AtMost(k) - AtMost(k - 1).

# Related Q: 
# 1) 992. Subarrays with K Different Integers
# 2) 1248. Count Number of Nice Subarrays