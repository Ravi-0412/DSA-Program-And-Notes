# Method 1: 

# just exactly same as "523. Continuous Subarray Sum".
# in that Q we have to keep track of length also in case we see any duplicates, so we were storing {modulus: index}

# Here we have to find no of subarray, so we are storing {modulus: count}.

# Note: python '%' operator behave very differently if numerator is negative.
# But still it will work because ans will depend on dulicates so it won't create any problem.

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans= 0
        modulusCount= {0: 1}   # {modulo_sum: count}
        curSum= 0
        for i in range(len(nums)):
            curSum += nums[i]
            curSum = curSum % k
            if curSum in modulusCount:
                count= modulusCount[curSum]
                ans += count
                modulusCount[curSum] += 1
            else:
                modulusCount[curSum] = 1
        return ans
    

# Java Code 
"""
import java.util.*;

class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        int ans = 0;
        Map<Integer, Integer> modulusCount = new HashMap<>();
        modulusCount.put(0, 1);  // {modulo_sum: count}
        int curSum = 0;

        for (int i = 0; i < nums.length; i++) {
            curSum += nums[i];
            curSum = curSum % k;

            if (modulusCount.containsKey(curSum)) {  
                int count = modulusCount.get(curSum);
                ans += count;
                modulusCount.put(curSum, count + 1);
            } else {
                modulusCount.put(curSum, 1);
            }
        }

        return ans;
    }
}
"""

# C++ Code 
"""
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        int ans = 0;
        unordered_map<int, int> modulusCount = {{0, 1}};  // {modulo_sum: count}
        int curSum = 0;

        for (int i = 0; i < nums.size(); i++) {
            curSum += nums[i];
            curSum = curSum % k;

            if (modulusCount.find(curSum) != modulusCount.end()) {  
                int count = modulusCount[curSum];
                ans += count;
                modulusCount[curSum]++;
            } else {
                modulusCount[curSum] = 1;
            }
        }

        return ans;
    }
};
"""