# logic: All elements must lie between [min(nums), max(nums)] when all will be equal.

# Note: the goal of this problem is to "find a num that makes the sum of moves minimum".

# Note vvi: 'target' ele must be from one of the given nums only.
# e.g: Well, you say, if our array is [2, 5], what if we can achieve min cost by making them 3 or 4?
# For this to be the case, the cost for both 2 and 5 must be the same. 
# But if the cost is same, we can achieve the same min cost if we pick 2 or 5.

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


# method 3: Weighted median

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

# java
"""
import java.util.Arrays;

class Solution {
    public long minCost(int[] nums, int[] cost) {
        // Create an array of pairs (num, cost)
        int n = nums.length;
        long[][] arr = new long[n][2];
        for (int i = 0; i < n; i++) {
            arr[i][0] = nums[i];
            arr[i][1] = cost[i];
        }

        // Sort the array based on the nums
        Arrays.sort(arr, (a, b) -> Long.compare(a[0], b[0]));

        // Calculate the total cost
        long totalCost = 0;
        for (long c : cost) {
            totalCost += c;
        }

        // Find the target element
        long curSum = 0;
        long target = 0;
        for (long[] pair : arr) {
            curSum += pair[1];
            if (curSum > totalCost / 2) {
                target = pair[0];
                break;
            }
        }

        // Calculate the minimum cost to make all elements equal to the target
        long minCost = 0;
        for (long[] pair : arr) {
            minCost += Math.abs(pair[0] - target) * pair[1];
        }

        return minCost;
    }
}
"""

# Related Q: 
"462. Minimum Moves to Equal Array Elements II", 
