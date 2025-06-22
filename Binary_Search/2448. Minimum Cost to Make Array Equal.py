# Basic: 

# logic: All elements must lie between [min(nums), max(nums)] when all will be equal.

# Note: the goal of this problem is to "find a num that makes the sum of moves minimum".

# Note vvi: 'target' ele must be from one of the given nums only.
# e.g: Well, you say, if our array is [2, 5], what if we can achieve min cost by making them 3 or 4?
# For this to be the case, the cost for both 2 and 5 must be the same. 
# But if the cost is same, we can achieve the same min cost if we pick 2 or 5.

# Method 1: 

# Brute force: Just caculating the cost of making all ele equal in above range.
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        mn, mx= min(nums), max(nums)
        ans= float('inf')
        for i in range(mn, mx + 1):
            curCost= 0
            for j in range(len(nums)):
                curCost += abs(nums[j] - i) * cost[j]
            ans= min(ans, curCost)
        return ans


# Method 2: 
# Little bit optimising the above solution.
# Taking only element of same array and making them equal.

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        ans= float('inf')
        for num in set(nums):
            curCost= 0
            for j in range(len(nums)):
                curCost += abs(nums[j] - num) * cost[j]
            ans= min(ans, curCost)
        return ans


# Method 3: 
# Optimising using binary Search

# Assume the final equal values are x
# the total cost function y = f(x) is a convex function(upward parabola) i.e 
# there will be only one value for which this will be minimum on the range of [min(A), max(A)].

# To find the minimum value of f(x),
# we can binary search x by comparing f(mid) and f(mid + 1).  (adjacent value)

# If f(mid) >= f(mid + 1),
# the minimum f(x) is on the right of 'mid' so make start = mid + 1
# where x >= mid + 1

# If f(mid) < f(mid + 1),
# the minimum f(x) is on left of mid including 'mid',
# where x <= mid.

# Repeatly doing this while left < right,
# until we find the minimum value and return it.

# Note vvi: This method is known as ternary search, if we check f(mid1) and f(mid2).


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:

        # Cost of making all element equal to 'x'.
        def f(x) :
            curCost= 0
            for a, c in zip(nums, cost):
                curCost += abs(a - x) * c
            return curCost
        
        start, end = min(nums) , max(nums)
        ans = f(start)
        while start < end:
            x = (start + end) //2  # just mid only
            y1, y2 = f(x), f(x + 1)
            ans = min(y1, y2)
            if y1 >= y2 :
                start = x + 1
            else:
                end = x
        return ans


# method 4: 
# Weighted median

# logic: Think of the cost array as the weight of the corresponding num in the nums array. 
# For example when nums = [1, 3, 5, 2] and cost = [2, 3, 1, 14], suppose we want to increase 1 in nums to 2, 
# we know that the cost for this operation is 2. However, this is equivalent as 
# if there are two 1’s in nums and we increase both of them to 2 with cost of '1'. 
# Therefore, the minimum total cost such that all the elements of the array nums become equal is equivalent 
# to the minimum total cost such that all the elements of the array 
# nums = [1, 1, 3, 3, 3, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] become equal, 
# with the cost of doing one operation on each element being 1.

# Note : so As such, the answer to this question is the :
# total cost for moving all elements to the (unweighted) median in the new (collapsed) array.

# Note vvvvi: If the cost for all element is the same, then the minimum cost is when all numbers converge at the median.
# Since the cost is not the same, we need to find a weighted median.

# How will find the 'weighted median'?
# To find a weighted median(target), we sort elements, "repeating" each element based on its weight.
# For nums: [1,3,5,2], cost:  [2,3,1,4] case, the repeated array looks like this: [1,1,2,2,2,2,3,3,3,5].

# Note: Now aggregate the current weight going from one side, and stop when current > total // 2.

# After that calculate the cost of making all ele equal to this 'target'.

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        arr = sorted(zip(nums, cost))
        total= sum(cost)
        curSum = 0
        target = None
        for num, c in arr:
            curSum += c
            if curSum > total //2:
                target = num
                break
        # Now find the cost of making all ele equal to 'target'.
        return sum(abs(num - target) * c for num, c in arr)

# Java Code 
"""
//Method 1
import java.util.*;

class Solution {
    public int minCost(int[] nums, int[] cost) {
        int mn = Arrays.stream(nums).min().getAsInt();
        int mx = Arrays.stream(nums).max().getAsInt();
        int ans = Integer.MAX_VALUE;

        for (int i = mn; i <= mx; i++) {
            int curCost = 0;
            for (int j = 0; j < nums.length; j++) {
                curCost += Math.abs(nums[j] - i) * cost[j];
            }
            ans = Math.min(ans, curCost);
        }
        return ans;
    }
}
//Method 2
class Solution {
    public int minCost(int[] nums, int[] cost) {
        int ans = Integer.MAX_VALUE;
        for (int num : nums) {
            int curCost = 0;
            for (int j = 0; j < nums.length; j++) {
                curCost += Math.abs(nums[j] - num) * cost[j];
            }
            ans = Math.min(ans, curCost);
        }
        return ans;
    }
}
//Method 3
class Solution {
    public int minCost(int[] nums, int[] cost) {
        int start = Arrays.stream(nums).min().getAsInt();
        int end = Arrays.stream(nums).max().getAsInt();
        int ans = f(nums, cost, start);

        while (start < end) {
            int mid = (start + end) / 2;
            int y1 = f(nums, cost, mid), y2 = f(nums, cost, mid + 1);
            ans = Math.min(y1, y2);

            if (y1 >= y2)
                start = mid + 1;
            else
                end = mid;
        }
        return ans;
    }

    private int f(int[] nums, int[] cost, int x) {
        int curCost = 0;
        for (int i = 0; i < nums.length; i++) {
            curCost += Math.abs(nums[i] - x) * cost[i];
        }
        return curCost;
    }
}
//Method 4
import java.util.*;

class Solution {
    public int minCost(int[] nums, int[] cost) {
        List<int[]> arr = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            arr.add(new int[]{nums[i], cost[i]});
        }
        arr.sort((a, b) -> Integer.compare(a[0], b[0]));

        int total = Arrays.stream(cost).sum();
        int curSum = 0, target = 0;

        for (int[] p : arr) {
            curSum += p[1];
            if (curSum > total / 2) {
                target = p[0];
                break;
            }
        }

        int result = 0;
        for (int[] p : arr) {
            result += Math.abs(p[0] - target) * p[1];
        }

        return result;
    }
}
"""

# C++ Code 
"""
//Method 1
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    int minCost(vector<int>& nums, vector<int>& cost) {
        int mn = *min_element(nums.begin(), nums.end());
        int mx = *max_element(nums.begin(), nums.end());
        int ans = INT_MAX;

        for (int i = mn; i <= mx; i++) {
            int curCost = 0;
            for (size_t j = 0; j < nums.size(); j++) {
                curCost += abs(nums[j] - i) * cost[j];
            }
            ans = min(ans, curCost);
        }
        return ans;
    }
};
//Method 2
class Solution {
public:
    int minCost(vector<int>& nums, vector<int>& cost) {
        int ans = INT_MAX;
        for (int num : nums) {
            int curCost = 0;
            for (size_t j = 0; j < nums.size(); j++) {
                curCost += abs(nums[j] - num) * cost[j];
            }
            ans = min(ans, curCost);
        }
        return ans;
    }
};
//Method 3
class Solution {
public:
    int minCost(vector<int>& nums, vector<int>& cost) {
        auto f = [&](int x) {
            int curCost = 0;
            for (size_t i = 0; i < nums.size(); i++) {
                curCost += abs(nums[i] - x) * cost[i];
            }
            return curCost;
        };

        int start = *min_element(nums.begin(), nums.end());
        int end = *max_element(nums.begin(), nums.end());
        int ans = f(start);

        while (start < end) {
            int mid = (start + end) / 2;
            int y1 = f(mid), y2 = f(mid + 1);
            ans = min(y1, y2);

            if (y1 >= y2)
                start = mid + 1;
            else
                end = mid;
        }
        return ans;
    }
};
//Method 4
class Solution {
public:
    int minCost(vector<int>& nums, vector<int>& cost) {
        vector<pair<int, int>> arr;
        for (size_t i = 0; i < nums.size(); i++) {
            arr.emplace_back(nums[i], cost[i]);
        }
        sort(arr.begin(), arr.end());

        int total = 0;
        for (const auto& p : arr) total += p.second;

        int curSum = 0;
        int target = 0;
        for (const auto& p : arr) {
            curSum += p.second;
            if (curSum > total / 2) {
                target = p.first;
                break;
            }
        }

        int result = 0;
        for (const auto& p : arr) {
            result += abs(p.first - target) * p.second;
        }

        return result;
    }
};
"""

