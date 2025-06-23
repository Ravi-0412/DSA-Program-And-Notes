# Method 1: 

"""
Note: if we do like we do usually for simplicity i.e add elements from index '0' to 'n-1' to the last of given integer and 
apply same logic as normal array then, it won't work.
Reason: Elements from starting may get added twice. So we have to think some other way.
e.g: [5,-3,5]
if we do like this then ans = 12 but expected = 10.

Now come to solution: 
note => Ans for this will always >= ans of part 1:  "53. Maximum Subarray" since we can join ele in circular also here.

Explanation
There are two case.
Case 1. The first is that the subarray take only a middle part, and we know how to find the max subarray sum.
ans = "53. Maximum Subarray" 
Case2. The second is that the subarray take a part of head array and a part of tail array.
We can transfer this case to the part 1.
The maximum result equals to the total sum minus the minimum subarray sum.

For case 2: Find the minimum subarray sum and subtract from 'toal sum of array'.

So the max subarray circular sum equals to
ans = max( Non circular max sum + circular max sum ) i.e max(the max subarray sum, the total sum - the min subarray sum)

so we have to keep track of both 'minSum' and 'maxSum'.

Note: If we only consider case-2 , then why that is not enough?
There are may reason: if single element is minSum and maxSum then , it will give less ans. 
There are other reason as well think.

e.g : [1,-2,3,-2]
if we consider only case 2 then, ans = 2 but expected = 3.

Corner case in above one: 
Just one to pay attention:
If all numbers are negative, maxSum = max(A) and minSum = sum(A).
In this case, max(maxSum, total - minSum) = 0, which means the sum of an empty subarray.
According to the description, We need to return the max(A), instead of sum of am empty subarray.
So we return the maxSum to handle this corner case.

How we handle next and previous element in circular array?
Next: the next element of nums[i] is:  nums[(i + 1) % n] 
the previous element of nums[i] is:    nums[(i - 1 + n) % n].
"""

# time: O(n)
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total= sum(nums)
        curMin= minSum= nums[0]
        curMax= maxSum= nums[0]
        for i in range(1, len(nums)):
            curMin= min(curMin + nums[i], nums[i])
            minSum= min(minSum, curMin)
            curMax= max(curMax + nums[i], nums[i])
            maxSum= max(maxSum, curMax)
        if maxSum > 0:   # means all ele is not 'negative' or atleast one ele is 'positive'.
            return max(maxSum, total- minSum)
        return maxSum  # all ele is negative

# Java Code 
"""
class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        int total = 0;
        int curMin = nums[0], minSum = nums[0];
        int curMax = nums[0], maxSum = nums[0];

        for (int i = 0; i < nums.length; i++) {
            total += nums[i];

            if (i > 0) {
                curMin = Math.min(curMin + nums[i], nums[i]);
                minSum = Math.min(minSum, curMin);

                curMax = Math.max(curMax + nums[i], nums[i]);
                maxSum = Math.max(maxSum, curMax);
            }
        }

        if (maxSum > 0)  // means all ele is not 'negative' or at least one ele is 'positive'.
            return Math.max(maxSum, total - minSum);

        return maxSum;  // all ele is negative
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int total = 0;
        int curMin = nums[0], minSum = nums[0];
        int curMax = nums[0], maxSum = nums[0];

        for (int i = 0; i < nums.size(); ++i) {
            total += nums[i];

            if (i > 0) {
                curMin = min(curMin + nums[i], nums[i]);
                minSum = min(minSum, curMin);

                curMax = max(curMax + nums[i], nums[i]);
                maxSum = max(maxSum, curMax);
            }
        }

        if (maxSum > 0)  // means all ele is not 'negative' or at least one ele is 'positive'.
            return max(maxSum, total - minSum);

        return maxSum;  // all ele is negative
    }
};
"""





